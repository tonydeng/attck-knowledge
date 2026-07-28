#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ATT&CK 知识库差异修复脚本

基于 _data/_fix_lists/ 下的 6 个修复清单，对本地知识库执行 6 类修复：
  1. missing_parents   — 创建缺失父技术占位文件
  2. extra_parents     — 标注已撤销父技术
  3. name_mismatch_parents — 重命名父技术文件 + 更新 attack_name_en
  4. missing_subs      — 创建缺失子技术占位文件
  5. extra_subs        — 标注已撤销子技术
  6. name_mismatch_subs — 重命名子技术文件 + 更新 attack_name_en（跳过 9 组重编号）

可选：若 _data/_fix_lists/_tid_remap.json 存在，则额外处理 9 组 TID 重编号。

默认 dry-run 模式，使用 --apply 实际执行。
仅依赖 Python 3.7+ 标准库（pathlib/json/re/argparse/sys/datetime）。

用法:
    python _tools/_apply_fixes.py                    # dry-run，仅预览
    python _tools/_apply_fixes.py --apply            # 实际执行修复
    python _tools/_apply_fixes.py --report report.md # 输出报告到文件
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

# ============================================================
# 路径与常量
# ============================================================
SCRIPT_DIR = Path(__file__).resolve().parent
KB_ROOT = SCRIPT_DIR.parent
DATA_DIR = KB_ROOT / "_data"
FIX_LIST_DIR = DATA_DIR / "_fix_lists"

# 战术清单（与 attack_mapping.py 保持一致）
TACTICS = [
    ("01-Reconnaissance",         "TA0043", "侦察",          "Reconnaissance"),
    ("02-Resource-Development",   "TA0042", "资源开发",      "Resource Development"),
    ("03-Initial-Access",         "TA0001", "初始访问",      "Initial Access"),
    ("04-Execution",              "TA0002", "执行",          "Execution"),
    ("05-Persistence",            "TA0003", "持久化",        "Persistence"),
    ("06-Privilege-Escalation",   "TA0004", "权限提升",      "Privilege Escalation"),
    ("07-Stealth",                "TA0005", "隐蔽",          "Stealth"),
    ("08-Defense-Impairment",     "TA0112", "防御损害",      "Defense Impairment"),
    ("09-Credential-Access",      "TA0006", "凭证访问",      "Credential Access"),
    ("10-Discovery",              "TA0007", "发现",          "Discovery"),
    ("11-Lateral-Movement",       "TA0008", "横向移动",      "Lateral Movement"),
    ("12-Collection",             "TA0009", "收集",          "Collection"),
    ("13-Command-and-Control",    "TA0011", "命令与控制",    "Command and Control"),
    ("14-Exfiltration",           "TA0010", "渗漏",          "Exfiltration"),
    ("15-Impact",                 "TA0040", "影响",          "Impact"),
]
TID_TO_DIR = {tid: d for d, tid, _, _ in TACTICS}
TID_TO_CN = {tid: cn for _, tid, cn, _ in TACTICS}

TODAY = date.today().isoformat()

# 9 组重编号 TID 前缀（在这些范围内的 name_mismatch_subs 条目跳过，等 _tid_remap.json 处理）
REMAP_SKIP_RANGES = [
    ("T1546", 9, 10),
    ("T1548", 1, 4),
    ("T1070", 1, 10),
    ("T1218", 1, 14),
    ("T1027", 8, 14),
    ("T1542", 3, 5),
    ("T1543", 1, 4),
    ("T1055", 7, 15),
    ("T1564", 1, 14),
]


# ============================================================
# 通用工具函数
# ============================================================

def slugify(name):
    """将英文名称转为文件名 slug。
    规则：
      - & → And
      - 空格 → 连字符
      - / → -（避免路径分隔符冲突）
      - 移除 () 内容和逗号
      - 每个空格分隔单词首字母大写，但保留全大写缩写（如 DLL, API, IDE）
      - 保留下划线（如 COR_PROFILER, LC_LOAD_DYLIB 中的下划线）
    """
    if not name:
        return ""
    # & → And
    s = name.replace("&", "And")
    # 移除括号内容（如 "At (Windows)" → "At Windows"）
    s = re.sub(r"\s*\([^)]*\)", "", s)
    # 移除逗号
    s = s.replace(",", "")
    # / → 连字符
    s = s.replace("/", "-")
    # 空格分割 → 处理每个单词 → 连字符连接
    parts = []
    for w in s.split():
        if not w:
            continue
        # 全大写且长度>=2 的缩写保留（DLL, API, IDE, TCC, SMB, VDSO, COR_PROFILER 等）
        if w.isupper() and len(w) >= 2:
            parts.append(w)
        # 含下划线的单词保留原样（COR_PROFILER, LC_LOAD_DYLIB）
        elif "_" in w:
            parts.append(w)
        else:
            parts.append(w.capitalize())
    return "-".join(parts)


def is_in_remap_range(tid):
    """判断 TID 是否属于 9 组重编号范围。"""
    m = re.match(r"^(T\d{4})\.(\d+)$", tid)
    if not m:
        return False
    parent, num = m.group(1), int(m.group(2))
    for p, lo, hi in REMAP_SKIP_RANGES:
        if parent == p and lo <= num <= hi:
            return True
    return False


def load_fix_list(name):
    """加载修复清单 JSON。"""
    path = FIX_LIST_DIR / f"{name}.json"
    if not path.exists():
        print(f"[WARN] 修复清单不存在: {path}")
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def parse_frontmatter_raw(text):
    """解析 YAML frontmatter，返回 (fm_dict, fm_text, body)。
    fm_text 是原始 frontmatter 文本（不含 --- 分隔符），用于精确替换。
    """
    if not text.startswith("---"):
        return {}, "", text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, "", text
    fm_text = text[3:end].lstrip("\n")
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in fm_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            fm[k] = v
    return fm, fm_text, body


def update_fm_field(fm_text, key, value):
    """在 frontmatter 文本中更新单个字段（保留其他字段原样）。
    若字段不存在则追加。"""
    lines = fm_text.splitlines()
    found = False
    new_lines = []
    for line in lines:
        # 匹配 "key:" 或 "key: value"
        m = re.match(r"^(\s*" + re.escape(key) + r"\s*):\s*(.*)$", line)
        if m and not found:
            new_lines.append(f'{key}: "{value}"' if isinstance(value, str) and value else f"{key}: {value}")
            found = True
        else:
            new_lines.append(line)
    if not found:
        new_lines.append(f'{key}: "{value}"' if isinstance(value, str) and value else f"{key}: {value}")
    return "\n".join(new_lines)


def rebuild_file(fm_text, body):
    """重组文件内容：---\n{fm_text}\n---\n\n{body}"""
    return f"---\n{fm_text}\n---\n\n{body}"


def read_file(path):
    """读取文件，返回 (text, fm, fm_text, body)。"""
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, fm_text, body = parse_frontmatter_raw(text)
    return text, fm, fm_text, body


def write_file(path, content):
    """写入文件。"""
    path.write_text(content, encoding="utf-8")


def find_parent_file(tid, tactic_dir):
    """在战术目录下查找父技术文件（按 TID 前缀匹配）。"""
    tactic_path = KB_ROOT / tactic_dir
    if not tactic_path.exists():
        return None
    for entry in tactic_path.iterdir():
        if entry.is_file() and entry.suffix == ".md" and entry.name.startswith(f"{tid}-"):
            return entry
    return None


def find_sub_file(tid, tactic_dir):
    """在战术目录/{parent}/ 下查找子技术文件。"""
    parent_tid = tid.split(".")[0]
    tactic_path = KB_ROOT / tactic_dir / parent_tid
    if not tactic_path.exists():
        return None
    for entry in tactic_path.iterdir():
        if entry.is_file() and entry.suffix == ".md" and entry.name.startswith(f"{tid}-"):
            return entry
    return None


# ============================================================
# 报告收集器
# ============================================================

class Report:
    def __init__(self):
        self.actions = []  # [(category, action_type, detail)]
        self.skipped = []  # [(category, reason, detail)]
        self.errors = []   # [(category, error, detail)]

    def add(self, category, action_type, detail):
        self.actions.append((category, action_type, detail))

    def skip(self, category, reason, detail):
        self.skipped.append((category, reason, detail))

    def error(self, category, err, detail):
        self.errors.append((category, err, detail))

    def summary(self):
        lines = []
        lines.append("=" * 70)
        lines.append("ATT&CK 知识库修复报告")
        lines.append("=" * 70)
        lines.append(f"日期: {TODAY}")
        lines.append(f"模式: {'APPLY' if APPLIED else 'DRY-RUN'}")
        lines.append("")

        # 按类别统计
        from collections import Counter
        action_counts = Counter(c for c, _, _ in self.actions)
        skip_counts = Counter(c for c, _, _ in self.skipped)
        error_counts = Counter(c for c, _, _ in self.errors)

        lines.append("[汇总]")
        lines.append(f"  执行操作: {len(self.actions)}")
        lines.append(f"  跳过: {len(self.skipped)}")
        lines.append(f"  错误: {len(self.errors)}")
        lines.append("")

        lines.append("[按类别统计]")
        all_cats = set(list(action_counts.keys()) + list(skip_counts.keys()) + list(error_counts.keys()))
        for cat in sorted(all_cats):
            a = action_counts.get(cat, 0)
            s = skip_counts.get(cat, 0)
            e = error_counts.get(cat, 0)
            lines.append(f"  {cat}: 执行={a}, 跳过={s}, 错误={e}")
        lines.append("")

        lines.append("[详细操作]")
        for cat, atype, detail in self.actions:
            tag = "[APPLIED]" if APPLIED else "[DRY-RUN]"
            lines.append(f"  {tag} [{cat}] {atype}: {detail}")
        lines.append("")

        if self.skipped:
            lines.append("[跳过项]")
            for cat, reason, detail in self.skipped:
                lines.append(f"  [SKIP] [{cat}] {reason}: {detail}")
            lines.append("")

        if self.errors:
            lines.append("[错误项]")
            for cat, err, detail in self.errors:
                lines.append(f"  [ERROR] [{cat}] {err}: {detail}")
            lines.append("")

        return "\n".join(lines)


REPORT = Report()
APPLIED = False  # 全局标志，由 main 设置


# ============================================================
# 修复 1: missing_parents — 创建缺失父技术占位文件
# ============================================================

def fix_missing_parents(items):
    """创建缺失父技术占位文件。"""
    cat = "missing_parents"
    for item in items:
        tid = item["tid"]
        official_name = item["official_name"]
        tactic_dir = item["_tactic_dir"]
        tactic_id = item["_tactic_id"]
        tactic_cn = TID_TO_CN.get(tactic_id, "")

        # 检查文件是否已存在
        existing = find_parent_file(tid, tactic_dir)
        if existing:
            REPORT.skip(cat, "文件已存在", f"{tid} in {tactic_dir}")
            continue

        slug = slugify(official_name)
        filename = f"{tid}-{slug}.md"
        filepath = KB_ROOT / tactic_dir / filename

        # 构建占位文件内容
        content = f"""---
status: 【待编写】
template_version: "3.1"
last_updated: "{TODAY}"
attack_id: "{tid}"
attack_name_en: "{official_name}"
attack_name_cn: ""
tactic_id: "{tactic_id}"
tactic_name: "{tactic_cn}"
difficulty: 0
sub_techniques_count: 0
aliases: []
platforms: []
detection: ""
permissions_required: ""
---

# {official_name} ({tid})

> 本文档为占位文件，待编写完整内容。

## 技术描述

（待编写）

## 检测建议

（待编写）

## 缓解措施

（待编写）

## 参考资料

- [MITRE ATT&CK 官方](https://attack.mitre.org/techniques/{tid}/)
"""

        if APPLIED:
            write_file(filepath, content)

        REPORT.add(cat, "CREATE", f"{tactic_dir}/{filename} ({official_name})")


# ============================================================
# 修复 2: extra_parents — 标注已撤销父技术
# ============================================================

def fix_extra_parents(items):
    """标注已撤销父技术（status:【已撤销】）。"""
    cat = "extra_parents"
    for item in items:
        tid = item["tid"]
        tactic_dir = item["_tactic_dir"]
        local_file = item["local_file"]

        filepath = KB_ROOT / tactic_dir / local_file
        if not filepath.exists():
            REPORT.error(cat, "文件不存在", str(filepath))
            continue

        text, fm, fm_text, body = read_file(filepath)

        # 检查是否已标注
        if fm.get("status") == "【已撤销】":
            REPORT.skip(cat, "已标注撤销", f"{tid} in {tactic_dir}")
            continue

        # 更新 frontmatter
        new_fm = update_fm_field(fm_text, "status", "【已撤销】")
        new_fm = update_fm_field(new_fm, "last_updated", TODAY)
        # 追加 revoked_note（若不存在）
        if "revoked_note" not in new_fm:
            new_fm = new_fm.rstrip() + f'\nrevoked_note: "该技术在 MITRE ATT&CK v19.1 中已被撤销"'

        new_content = rebuild_file(new_fm, body)

        if APPLIED:
            write_file(filepath, new_content)

        REPORT.add(cat, "REVOKE", f"{tactic_dir}/{local_file} ({tid})")


# ============================================================
# 修复 3: name_mismatch_parents — 重命名父技术文件 + 更新名称
# ============================================================

def fix_name_mismatch_parents(items):
    """重命名父技术文件 + 更新 attack_name_en。"""
    cat = "name_mismatch_parents"
    for item in items:
        tid = item["tid"]
        official_name = item["official_name"]
        tactic_dir = item["_tactic_dir"]
        local_file = item["local_file"]

        old_path = KB_ROOT / tactic_dir / local_file
        # 计算新文件名
        new_slug = slugify(official_name)
        new_filename = f"{tid}-{new_slug}.md"
        new_path = KB_ROOT / tactic_dir / new_filename

        # 幂等：old 不存在但 new 存在 → 已应用
        if not old_path.exists():
            if new_path.exists():
                # 检查 new_path 的 attack_name_en 是否已是 official_name
                _, fm2, _, _ = read_file(new_path)
                if fm2.get("attack_name_en") == official_name:
                    REPORT.skip(cat, "已应用（新文件已存在且名称正确）", f"{tid} in {tactic_dir}")
                    continue
            REPORT.error(cat, "文件不存在", str(old_path))
            continue

        # 幂等：old == new 且 attack_name_en 已正确 → 跳过
        if old_path == new_path:
            _, fm_chk, _, _ = read_file(old_path)
            if fm_chk.get("attack_name_en") == official_name:
                REPORT.skip(cat, "已应用（名称已正确）", f"{tid} in {tactic_dir}")
                continue

        # 读取并更新 frontmatter
        text, fm, fm_text, body = read_file(old_path)
        new_fm = update_fm_field(fm_text, "attack_name_en", official_name)
        new_fm = update_fm_field(new_fm, "last_updated", TODAY)
        new_content = rebuild_file(new_fm, body)

        if APPLIED:
            write_file(old_path, new_content)
            if old_path != new_path:
                # 目标已存在则覆盖（处理冲突）
                if new_path.exists():
                    new_path.unlink()
                old_path.rename(new_path)

        if old_path == new_path:
            REPORT.add(cat, "UPDATE_NAME", f"{tactic_dir}/{local_file} (仅更新 attack_name_en: {official_name})")
        else:
            REPORT.add(cat, "RENAME", f"{tactic_dir}/{local_file} → {tactic_dir}/{new_filename} ({official_name})")


# ============================================================
# 修复 4: missing_subs — 创建缺失子技术占位文件
# ============================================================

def fix_missing_subs(items):
    """创建缺失子技术占位文件。"""
    cat = "missing_subs"
    for item in items:
        tid = item["tid"]
        official_name = item["official_name"]
        parent_tid = item["parent"]
        tactic_dir = item["_tactic_dir"]
        tactic_id = item["_tactic_id"]
        tactic_cn = TID_TO_CN.get(tactic_id, "")

        # 检查文件是否已存在
        existing = find_sub_file(tid, tactic_dir)
        if existing:
            REPORT.skip(cat, "文件已存在", f"{tid} in {tactic_dir}")
            continue

        slug = slugify(official_name)
        filename = f"{tid}-{slug}.md"
        # 子目录：{tactic_dir}/{parent_tid}/
        subdir = KB_ROOT / tactic_dir / parent_tid
        filepath = subdir / filename

        # 父技术英文名（从修复清单或其他方式获取，这里留空让用户补充）
        parent_name_en = ""
        # 尝试从本地扫描数据获取父技术名
        local_scan = load_local_scan()
        if tactic_dir in local_scan:
            for p in local_scan[tactic_dir].get("parents", []):
                if p.get("attack_id") == parent_tid:
                    parent_name_en = p.get("attack_name_en", "")
                    break

        content = f"""---
status: 【待编写】
template_version: "3.1"
last_updated: "{TODAY}"
attack_id: "{tid}"
attack_name_en: "{official_name}"
attack_name_cn: ""
parent_technique: "{parent_tid}"
parent_name_en: "{parent_name_en}"
parent_name_cn: ""
tactic_id: "{tactic_id}"
tactic_name: "{tactic_cn}"
difficulty: 0
aliases: []
platforms: []
detection: ""
permissions_required: ""
---

# {official_name} ({tid})

> 本文档为占位文件，待编写完整内容。

## 技术描述

（待编写）

## 检测建议

（待编写）

## 缓解措施

（待编写）

## 参考资料

- [MITRE ATT&CK 官方](https://attack.mitre.org/techniques/{tid}/)
"""

        if APPLIED:
            subdir.mkdir(parents=True, exist_ok=True)
            write_file(filepath, content)

        REPORT.add(cat, "CREATE", f"{tactic_dir}/{parent_tid}/{filename} ({official_name})")


# ============================================================
# 修复 5: extra_subs — 标注已撤销子技术
# ============================================================

def fix_extra_subs(items):
    """标注已撤销子技术。"""
    cat = "extra_subs"
    for item in items:
        tid = item["tid"]
        tactic_dir = item["_tactic_dir"]
        local_file = item["local_file"]

        parent_tid = tid.split(".")[0]
        filepath = KB_ROOT / tactic_dir / parent_tid / local_file
        if not filepath.exists():
            REPORT.error(cat, "文件不存在", str(filepath))
            continue

        text, fm, fm_text, body = read_file(filepath)

        if fm.get("status") == "【已撤销】":
            REPORT.skip(cat, "已标注撤销", f"{tid} in {tactic_dir}")
            continue

        new_fm = update_fm_field(fm_text, "status", "【已撤销】")
        new_fm = update_fm_field(new_fm, "last_updated", TODAY)
        if "revoked_note" not in new_fm:
            new_fm = new_fm.rstrip() + f'\nrevoked_note: "该子技术在 MITRE ATT&CK v19.1 中已被撤销"'

        new_content = rebuild_file(new_fm, body)

        if APPLIED:
            write_file(filepath, new_content)

        REPORT.add(cat, "REVOKE", f"{tactic_dir}/{parent_tid}/{local_file} ({tid})")


# ============================================================
# 修复 6: name_mismatch_subs — 简单重命名（跳过 9 组重编号）
# ============================================================

def fix_name_mismatch_subs_simple(items):
    """重命名子技术文件 + 更新 attack_name_en（跳过 9 组重编号）。"""
    cat = "name_mismatch_subs"
    for item in items:
        tid = item["tid"]
        official_name = item["official_name"]
        tactic_dir = item["_tactic_dir"]
        local_file = item["local_file"]

        # 跳过 9 组重编号
        if is_in_remap_range(tid):
            REPORT.skip(cat, "9组重编号范围（待_tid_remap.json处理）", f"{tid} in {tactic_dir}")
            continue

        parent_tid = tid.split(".")[0]
        old_path = KB_ROOT / tactic_dir / parent_tid / local_file
        new_slug = slugify(official_name)
        new_filename = f"{tid}-{new_slug}.md"
        new_path = KB_ROOT / tactic_dir / parent_tid / new_filename

        # 幂等：old 不存在但 new 存在 → 已应用
        if not old_path.exists():
            if new_path.exists():
                _, fm2, _, _ = read_file(new_path)
                if fm2.get("attack_name_en") == official_name:
                    REPORT.skip(cat, "已应用（新文件已存在且名称正确）", f"{tid} in {tactic_dir}")
                    continue
            REPORT.error(cat, "文件不存在", str(old_path))
            continue

        # 幂等：old == new 且 attack_name_en 已正确 → 跳过
        if old_path == new_path:
            _, fm_chk, _, _ = read_file(old_path)
            if fm_chk.get("attack_name_en") == official_name:
                REPORT.skip(cat, "已应用（名称已正确）", f"{tid} in {tactic_dir}")
                continue

        text, fm, fm_text, body = read_file(old_path)
        new_fm = update_fm_field(fm_text, "attack_name_en", official_name)
        new_fm = update_fm_field(new_fm, "last_updated", TODAY)
        new_content = rebuild_file(new_fm, body)

        if APPLIED:
            write_file(old_path, new_content)
            if old_path != new_path:
                if new_path.exists():
                    new_path.unlink()
                old_path.rename(new_path)

        if old_path == new_path:
            REPORT.add(cat, "UPDATE_NAME", f"{tactic_dir}/{parent_tid}/{local_file} (仅更新 attack_name_en: {official_name})")
        else:
            REPORT.add(cat, "RENAME", f"{tactic_dir}/{parent_tid}/{local_file} → {parent_tid}/{new_filename} ({official_name})")


# ============================================================
# 修复 7（可选）: TID 重编号 — 基于 _tid_remap.json
# ============================================================

def fix_tid_remap(remap_data):
    """根据 _tid_remap.json 处理 TID 重编号/重分类/删除。

    JSON 实际结构（嵌套）:
      {
        metadata: {...},
        verified_correct: [...],     # 跳过
        fixes: [                      # 8 个修复组
          {group, group_desc, items: [...]}
        ]
      }

    每个 item 的 action:
      - rename_tid:    文件重命名（TID + 名称），可能存在交换/链式冲突
      - duplicate:     删除文件（内容由 keep_instead 覆盖）
      - reclassify:    删除子技术文件（父文件已在目标战术存在）
      - manual_review: 删除文件（官方已撤销）
    """
    cat = "tid_remap"

    # 处理嵌套结构
    if isinstance(remap_data, dict) and "fixes" in remap_data:
        groups = remap_data["fixes"]
    elif isinstance(remap_data, list):
        # 兼容旧的扁平结构（不应触发）
        groups = [{"group": "flat", "items": remap_data}]
    else:
        REPORT.error(cat, "remap_data 结构无法识别", str(type(remap_data)))
        return

    all_items = []
    for g in groups:
        all_items.extend(g.get("items", []))

    # ============================================================
    # 阶段 1：删除类操作（duplicate / reclassify / manual_review）
    # ============================================================
    for item in all_items:
        action = item.get("action")
        if action not in ("duplicate", "reclassify", "manual_review"):
            continue

        file_rel = item.get("file", "")
        if not file_rel:
            REPORT.error(cat, f"{action} 项缺 file 字段", str(item))
            continue

        old_path = KB_ROOT / file_rel
        if not old_path.exists():
            REPORT.skip(cat, f"{action} 已应用（文件不存在）", file_rel)
            continue

        if APPLIED:
            old_path.unlink()

        if action == "duplicate":
            keep = item.get("keep_instead", "")
            REPORT.add(cat, "DELETE_DUP", f"{file_rel} (重复，保留 {keep})")
        elif action == "reclassify":
            new_tid = item.get("new_tid", "")
            REPORT.add(cat, "DELETE_RECLASSIFY", f"{file_rel} (父文件 {new_tid} 已存在)")
        else:  # manual_review
            REPORT.add(cat, "DELETE_REVOKE", f"{file_rel} (官方已撤销)")

    # ============================================================
    # 阶段 2：rename_tid 操作
    # 两阶段处理避免交换/链式冲突：
    #   (a) 读取所有 rename 源文件到内存
    #   (b) 删除所有 rename 源文件
    #   (c) 写入新文件（更新 frontmatter）
    # ============================================================
    rename_items = [it for it in all_items if it.get("action") == "rename_tid"]

    # (a) 读取到内存
    in_memory = []
    for item in rename_items:
        file_rel = item.get("file", "")
        if not file_rel:
            REPORT.error(cat, "rename 项缺 file 字段", str(item))
            continue

        old_path = KB_ROOT / file_rel
        if not old_path.exists():
            REPORT.skip(cat, "rename 已应用（文件不存在）", file_rel)
            continue

        new_tid = item.get("new_tid", "")
        new_name_en = item.get("new_name_en", "")
        official_name_en = item.get("official_name_en", "") or new_name_en
        current_tid = item.get("current_tid", "")

        if not new_tid:
            REPORT.error(cat, "rename 项缺 new_tid", str(item))
            continue

        # 计算新路径
        # file_rel 格式: "05-Persistence/T1546/T1546.009-AppInit-DLLs.md"
        parts = file_rel.split("/")
        tactic_dir = parts[0]
        if "." in new_tid:
            new_parent = new_tid.split(".")[0]
            new_slug = slugify(new_name_en or official_name_en)
            new_filename = f"{new_tid}-{new_slug}.md"
            new_path = KB_ROOT / tactic_dir / new_parent / new_filename
        else:
            # 父技术级目标（不应在 rename_tid 中出现，但兜底处理）
            new_slug = slugify(new_name_en or official_name_en)
            new_filename = f"{new_tid}-{new_slug}.md"
            new_path = KB_ROOT / tactic_dir / new_filename

        text, fm, fm_text, body = read_file(old_path)
        in_memory.append({
            "item": item,
            "old_path": old_path,
            "new_path": new_path,
            "fm_text": fm_text,
            "body": body,
            "current_tid": current_tid,
            "new_tid": new_tid,
            "name_to_use": official_name_en,
            "file_rel": file_rel,
        })

    # (b) 删除原文件
    if APPLIED:
        for entry in in_memory:
            if entry["old_path"].exists():
                entry["old_path"].unlink()

    # (c) 写入新文件
    for entry in in_memory:
        new_path = entry["new_path"]
        new_tid = entry["new_tid"]
        current_tid = entry["current_tid"]
        name_to_use = entry["name_to_use"]
        file_rel = entry["file_rel"]

        new_fm = update_fm_field(entry["fm_text"], "attack_id", new_tid)
        if name_to_use:
            new_fm = update_fm_field(new_fm, "attack_name_en", name_to_use)
        if "." in new_tid:
            new_parent = new_tid.split(".")[0]
            # 仅当 frontmatter 已有 parent_technique 字段时更新
            if "parent_technique:" in new_fm:
                new_fm = update_fm_field(new_fm, "parent_technique", new_parent)
        new_fm = update_fm_field(new_fm, "last_updated", TODAY)
        new_content = rebuild_file(new_fm, entry["body"])

        if APPLIED:
            new_path.parent.mkdir(parents=True, exist_ok=True)
            write_file(new_path, new_content)

        new_rel = new_path.relative_to(KB_ROOT).as_posix()
        REPORT.add(cat, "RENAME", f"{file_rel} -> {new_rel} ({current_tid}->{new_tid})")


# ============================================================
# 缓存本地扫描数据（用于 missing_subs 获取父技术名）
# ============================================================

_LOCAL_SCAN_CACHE = None

def load_local_scan():
    global _LOCAL_SCAN_CACHE
    if _LOCAL_SCAN_CACHE is None:
        path = DATA_DIR / "_local_scan.json"
        if path.exists():
            _LOCAL_SCAN_CACHE = json.loads(path.read_text(encoding="utf-8"))
        else:
            _LOCAL_SCAN_CACHE = {}
    return _LOCAL_SCAN_CACHE


# ============================================================
# 主流程
# ============================================================

def main():
    global APPLIED

    parser = argparse.ArgumentParser(
        description="ATT&CK 知识库差异修复脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--apply", action="store_true", help="实际执行修复（默认 dry-run）")
    parser.add_argument("--report", type=str, default=None, help="输出报告到指定文件")
    args = parser.parse_args()

    APPLIED = args.apply

    print(f"[apply_fixes] 知识库根目录: {KB_ROOT}")
    print(f"[apply_fixes] 模式: {'APPLY' if APPLIED else 'DRY-RUN'}")
    print(f"[apply_fixes] 修复清单目录: {FIX_LIST_DIR}")
    print()

    # 加载所有修复清单
    print("[1/8] 加载修复清单...")
    missing_parents = load_fix_list("missing_parents")
    extra_parents = load_fix_list("extra_parents")
    name_mismatch_parents = load_fix_list("name_mismatch_parents")
    missing_subs = load_fix_list("missing_subs")
    extra_subs = load_fix_list("extra_subs")
    name_mismatch_subs = load_fix_list("name_mismatch_subs")

    print(f"  missing_parents: {len(missing_parents)} 项")
    print(f"  extra_parents: {len(extra_parents)} 项")
    print(f"  name_mismatch_parents: {len(name_mismatch_parents)} 项")
    print(f"  missing_subs: {len(missing_subs)} 项")
    print(f"  extra_subs: {len(extra_subs)} 项")
    print(f"  name_mismatch_subs: {len(name_mismatch_subs)} 项")

    # 检查 _tid_remap.json
    remap_path = FIX_LIST_DIR / "_tid_remap.json"
    remap_data = None
    if remap_path.exists():
        remap_data = json.loads(remap_path.read_text(encoding="utf-8"))
        # 嵌套结构: {metadata, verified_correct, fixes: [{group, items}]}
        if isinstance(remap_data, dict) and "fixes" in remap_data:
            n_groups = len(remap_data.get("fixes", []))
            n_items = sum(len(g.get("items", [])) for g in remap_data["fixes"])
            n_verified = len(remap_data.get("verified_correct", []))
            print(f"  _tid_remap: {n_groups} 组 / {n_items} 待处理 / {n_verified} 已验证正确（已加载）")
        else:
            print(f"  _tid_remap: 已加载（旧格式，{len(remap_data)} 项）")
    else:
        print(f"  _tid_remap: 不存在（重编号将跳过）")

    print()

    # 执行 6 类修复
    print("[2/8] 修复 missing_parents...")
    fix_missing_parents(missing_parents)

    print("[3/8] 修复 extra_parents...")
    fix_extra_parents(extra_parents)

    print("[4/8] 修复 name_mismatch_parents...")
    fix_name_mismatch_parents(name_mismatch_parents)

    print("[5/8] 修复 missing_subs...")
    fix_missing_subs(missing_subs)

    print("[6/8] 修复 extra_subs...")
    fix_extra_subs(extra_subs)

    print("[7/8] 修复 name_mismatch_subs（简单重命名，跳过 9 组重编号）...")
    fix_name_mismatch_subs_simple(name_mismatch_subs)

    if remap_data:
        print("[8/8] 修复 9 组 TID 重编号...")
        fix_tid_remap(remap_data)
    else:
        print("[8/8] 跳过 9 组 TID 重编号（_tid_remap.json 不存在）")

    print()

    # 输出报告
    report_text = REPORT.summary()
    print(report_text)

    if args.report:
        report_path = Path(args.report)
        report_path.write_text(report_text, encoding="utf-8")
        print(f"\n[apply_fixes] 报告已写入: {report_path}")

    # 提示后续步骤
    if APPLIED:
        print("\n[后续步骤]")
        print("  1. python _tools/attack_mapping.py scan")
        print("  2. python _tools/attack_mapping.py generate")
        print("  3. python _tools/attack_mapping.py verify")
        print("  验证标准: 0 issues / 0 warnings")
    else:
        print("\n[提示] 这是 DRY-RUN。确认无误后，运行:")
        print(f"  python _tools/_apply_fixes.py --apply")

    return 0


if __name__ == "__main__":
    sys.exit(main())
