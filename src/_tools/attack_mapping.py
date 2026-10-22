#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ATT&CK 知识库 MAPPING.md 审计工具链（统一 CLI）

合并 5 个历史脚本为单一工具，提供 6 个子命令：
  scan      扫描本地 15 个战术目录的 frontmatter，输出 _data/_local_scan.json
  fetch     从 attack.mitre.org 抓取 15 个战术页，输出 _data/_mitre_official.json
  generate  读取两份 JSON，生成各战术目录下的 MAPPING.md
  verify    验证 15 个 MAPPING.md 与 JSON 数据的一致性
  status    打印总体统计表（官方/本地计数、MAPPING.md 文件大小）
  all       顺序执行 scan → fetch → generate → verify

仅依赖 Python 3.7+ 标准库（urllib/ssl/re/json/pathlib/argparse）。

用法示例:
    python attack_mapping.py scan
    python attack_mapping.py fetch
    python attack_mapping.py generate
    python attack_mapping.py verify
    python attack_mapping.py status
    python attack_mapping.py all
    python attack_mapping.py generate --skip-mitre   # 仅用本地数据生成
"""

import argparse
import json
import re
import ssl
import sys
import time
import urllib.request
from pathlib import Path

# ============================================================
# 路径自适配：脚本位于 src/_tools/ 下
#   - SRC_DIR = src/（_data 数据目录所在层）
#   - TACTICS_ROOT = src/enterprise/（战术目录所在层，双命名空间重构后）
# ============================================================
SCRIPT_DIR = Path(__file__).resolve().parent
SRC_DIR = SCRIPT_DIR.parent
TACTICS_ROOT = SRC_DIR / "enterprise"
DATA_DIR = SRC_DIR / "_data"
LOCAL_SCAN_PATH = DATA_DIR / "_local_scan.json"
MITRE_OFFICIAL_PATH = DATA_DIR / "_mitre_official.json"

# ============================================================
# 战术清单（v20 起：拆分 Defense Evasion 为 Stealth + Defense Impairment）
# ============================================================
# (目录名, 战术ID, 中文战术名, 英文战术名)
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

# 目录名 -> 战术ID
DIR_TO_TID = {d: tid for d, tid, _, _ in TACTICS}
# 战术ID -> 目录名
TID_TO_DIR = {tid: d for d, tid, _, _ in TACTICS}

# ============================================================
# 通用工具
# ============================================================

def parse_frontmatter(text):
    """解析 YAML frontmatter，返回 dict。仅支持简单 key: value 格式。"""
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end < 0:
        return {}
    fm_text = text[3:end].strip()
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
    return fm


def parse_yaml_frontmatter(content):
    """解析 YAML frontmatter 并尝试转换数值类型（用于 verify）。"""
    yaml_fields = {}
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return yaml_fields
    for line in m.group(1).split("\n"):
        mm = re.match(r"^(\w+):\s*(.*)$", line)
        if mm:
            key, val = mm.group(1), mm.group(2).strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            try:
                val = int(val)
            except ValueError:
                try:
                    val = float(val)
                except ValueError:
                    pass
            yaml_fields[key] = val
    return yaml_fields


def status_icon(status):
    """状态 -> 图标。"""
    if not status:
        return "📝"
    if "已完成" in status:
        return "✅"
    return "📝"


def load_json(path):
    """加载 JSON 文件，不存在返回 None。"""
    p = Path(path)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def ensure_data_dir():
    """确保 _data/ 目录存在。"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 子命令 1：scan - 扫描本地知识库
# ============================================================

def parse_doc_meta(text, filename, tactic_id):
    """从文档提取元数据：frontmatter 优先（历史兼容），否则回退到文件名 + H1。

    文件名约定：T####-English-Name.md 或 T####.NNN-English-Name.md
    H1 约定：# 中文名 (T####) 或 # 中文名 (T####.NNN)
    """
    fm = parse_frontmatter(text)
    meta = {
        "attack_id": fm.get("attack_id", ""),
        "attack_name_en": fm.get("attack_name_en", ""),
        "attack_name_cn": fm.get("attack_name_cn", ""),
        "tactic_id": fm.get("tactic_id", ""),
        "sub_techniques_count": fm.get("sub_techniques_count", "0"),
        "status": fm.get("status", ""),
        "parent_technique": fm.get("parent_technique", ""),
        "parent_name_en": fm.get("parent_name_en", ""),
        "parent_name_cn": fm.get("parent_name_cn", ""),
    }

    # --- 回退 1：文件名提取 attack_id / attack_name_en ---
    m = re.match(r"^(T\d+(?:\.\d+)?)-(.+?)\.md$", filename)
    if m:
        if not meta["attack_id"]:
            meta["attack_id"] = m.group(1)
        if not meta["attack_name_en"]:
            meta["attack_name_en"] = m.group(2).replace("-", " ")

    # --- 回退 2：H1 提取 attack_name_cn ---
    if not meta["attack_name_cn"]:
        h1 = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        if h1:
            meta["attack_name_cn"] = re.sub(r"\s*\((?:AML\.)?T[\d.]+\)\s*$", "", h1.group(1)).strip()

    # --- 回退 3：tactic_id 取目录所属战术 ---
    if not meta["tactic_id"]:
        meta["tactic_id"] = tactic_id or ""

    return meta


def scan_dir(tactic_dir):
    """扫描单个战术目录，返回父技术 + 子技术清单。"""
    tactic_id = DIR_TO_TID.get(tactic_dir, "")
    tactic_path = TACTICS_ROOT / tactic_dir
    parents = []
    subtechs = []
    if not tactic_path.exists():
        return {"tactic_dir": tactic_dir, "parents": [], "subtechs": [], "error": "dir not found"}

    # 顶层 .md 文件 = 父技术（排除 README 和 模板）
    for entry in sorted(tactic_path.iterdir()):
        if entry.is_file() and entry.suffix == ".md":
            if entry.name in ("README.md",) or entry.name.startswith("模板") or entry.name == "MAPPING.md":
                continue
            text = entry.read_text(encoding="utf-8", errors="replace")
            meta = parse_doc_meta(text, entry.name, tactic_id)
            parents.append({
                "file": entry.name,
                "path": str(entry.relative_to(TACTICS_ROOT)),
                **{k: meta[k] for k in ("attack_id", "attack_name_en", "attack_name_cn", "tactic_id", "sub_techniques_count", "status")},
            })
        elif entry.is_dir():
            # 子目录 = Txxxx/，里面是 Txxxx.001-*.md 子技术文件
            for sub in sorted(entry.iterdir()):
                if sub.is_file() and sub.suffix == ".md":
                    text = sub.read_text(encoding="utf-8", errors="replace")
                    meta = parse_doc_meta(text, sub.name, tactic_id)
                    subtechs.append({
                        "file": sub.name,
                        "path": str(sub.relative_to(TACTICS_ROOT)),
                        "parent_dir": entry.name,
                        **{k: meta[k] for k in ("attack_id", "attack_name_en", "attack_name_cn", "status")},
                        "parent_technique": meta["parent_technique"] or entry.name,
                    })

    return {
        "tactic_dir": tactic_dir,
        "parent_count": len(parents),
        "subtech_count": len(subtechs),
        "parents": parents,
        "subtechs": subtechs,
    }


def cmd_scan(args):
    """扫描本地知识库，输出 _data/_local_scan.json"""
    ensure_data_dir()
    print(f"[scan] 知识库根目录: {TACTICS_ROOT}")
    output = {}
    for tactic_dir, _, _, _ in TACTICS:
        print(f"  Scanning {tactic_dir}...", flush=True)
        output[tactic_dir] = scan_dir(tactic_dir)
        print(f"    parents={output[tactic_dir]['parent_count']} subtechs={output[tactic_dir]['subtech_count']}", flush=True)

    LOCAL_SCAN_PATH.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    total_p = sum(v["parent_count"] for v in output.values())
    total_s = sum(v["subtech_count"] for v in output.values())
    print(f"\n[scan] 完成: {LOCAL_SCAN_PATH}")
    print(f"[scan] 汇总: {total_p} 父技术, {total_s} 子技术, 跨 15 个战术")
    return 0


# ============================================================
# 子命令 2：fetch - 抓取 MITRE 官方数据
# ============================================================

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
CTX = ssl.create_default_context()


def fetch_url(url, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            r = urllib.request.urlopen(req, timeout=30, context=CTX)
            return r.read().decode("utf-8")
        except Exception as e:
            print(f"    retry {attempt+1}/{retries}: {e}")
            time.sleep(2)
    return None


def parse_tactic_page(html):
    """解析战术页 HTML，返回父技术列表（每个含 id/name_en/subtechniques）。"""
    parents = {}
    order = []

    # 父技术块
    tech_block = re.compile(
        r'<tr class="technique">[\s\S]*?<a href="/techniques/(T\d{4})/?"[^>]*>\s*\1\s*</a>[^<]*</td>\s*<td[^>]*>\s*<a href="/techniques/\1/?"[^>]*>\s*([^<]+?)\s*</a>',
        re.IGNORECASE
    )
    for m in tech_block.finditer(html):
        tid = m.group(1)
        name = m.group(2).strip()
        if tid not in parents:
            parents[tid] = {"id": tid, "name_en": name, "subtechniques": []}
            order.append(tid)
        else:
            parents[tid]["name_en"] = name

    # 子技术块（class="sub technique" 带空格）
    sub_block = re.compile(
        r'<tr class="sub technique">[\s\S]*?<a href="/techniques/(T\d{4})/(\d+)/?"[^>]*>\s*\.\s*\2\s*</a>[^<]*</td>\s*<td[^>]*>\s*<a href="/techniques/\1/\2/?"[^>]*>\s*([^<]+?)\s*</a>',
        re.IGNORECASE
    )
    for m in sub_block.finditer(html):
        parent_id = m.group(1)
        sub_num = m.group(2)
        name = m.group(3).strip()
        full_id = f"{parent_id}.{sub_num}"
        if parent_id not in parents:
            parents[parent_id] = {"id": parent_id, "name_en": "", "subtechniques": []}
            order.append(parent_id)
        existing = [s["id"] for s in parents[parent_id]["subtechniques"]]
        if full_id not in existing:
            parents[parent_id]["subtechniques"].append({"id": full_id, "name_en": name})

    return [parents[pid] for pid in order]


def cmd_fetch(args):
    """从 attack.mitre.org 抓取 15 个战术页，输出 _data/_mitre_official.json"""
    ensure_data_dir()
    print(f"[fetch] 开始抓取 MITRE ATT&CK v20（15 个战术）")
    result = {}

    for tactic_id, tactic_en in [(tid, en) for _, tid, _, en in TACTICS]:
        print(f"\n  [{tactic_id}] {tactic_en}", flush=True)
        url = f"https://attack.mitre.org/tactics/{tactic_id}/"
        html = fetch_url(url)
        if not html:
            print(f"    FAILED to fetch, skipping")
            result[tactic_id] = {
                "tactic_id": tactic_id,
                "tactic_name_en": tactic_en,
                "parent_techniques": [],
                "error": "fetch failed"
            }
            continue

        parents = parse_tactic_page(html)
        total_sub = sum(len(p["subtechniques"]) for p in parents)
        print(f"    parents={len(parents)} subtechs={total_sub}", flush=True)

        result[tactic_id] = {
            "tactic_id": tactic_id,
            "tactic_name_en": tactic_en,
            "parent_techniques": parents,
        }
        time.sleep(0.5)

    MITRE_OFFICIAL_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[fetch] 完成: {MITRE_OFFICIAL_PATH}")

    # 汇总表
    print("\n[fetch] 汇总:")
    print(f"  {'Tactic':<10} {'Parents':<10} {'Subtechs':<10}")
    total_p = total_s = 0
    for _, tid, _, _ in TACTICS:
        p = len(result[tid].get("parent_techniques", []))
        s = sum(len(x["subtechniques"]) for x in result[tid].get("parent_techniques", []))
        total_p += p
        total_s += s
        print(f"  {tid:<10} {p:<10} {s:<10}")
    print(f"  {'TOTAL':<10} {total_p:<10} {total_s:<10}")
    return 0


# ============================================================
# 子命令 3：generate - 生成 MAPPING.md
# ============================================================

def find_local_parent(local_data, attack_id):
    """从本地数据中按 attack_id 找父技术。"""
    if not local_data:
        return None
    for p in local_data.get("parents", []):
        if p.get("attack_id") == attack_id:
            return p
    return None


def find_local_subtech(local_data, attack_id):
    """从本地数据中按 attack_id 找子技术。"""
    if not local_data:
        return None
    for s in local_data.get("subtechs", []):
        if s.get("attack_id") == attack_id:
            return s
    return None


def gen_mapping(tactic_dir, tactic_id, tactic_cn, tactic_en, local_data, mitre_data):
    """生成单个战术的 MAPPING.md 内容。"""
    # 收集数据
    mitre_parents = mitre_data.get("parent_techniques", []) if mitre_data else []
    mitre_parent_count = len(mitre_parents)
    mitre_subtech_count = sum(len(p.get("subtechniques", [])) for p in mitre_parents)

    local_parents = local_data.get("parents", []) if local_data else []
    local_subtechs = local_data.get("subtechs", []) if local_data else []
    local_parent_count = len(local_parents)
    local_subtech_count = len(local_subtechs)

    # 构建本地索引
    local_parent_by_id = {p["attack_id"]: p for p in local_parents if p.get("attack_id")}
    local_subtech_by_id = {s["attack_id"]: s for s in local_subtechs if s.get("attack_id")}

    # 找出本地有但 MITRE 没有的（可能是撤销/迁移/命名变更）
    mitre_parent_ids = {p["id"] for p in mitre_parents}
    mitre_subtech_ids = set()
    for p in mitre_parents:
        for s in p.get("subtechniques", []):
            mitre_subtech_ids.add(s["id"])

    local_only_parents = [p for p in local_parents if p.get("attack_id") and p["attack_id"] not in mitre_parent_ids]
    local_only_subtechs = [s for s in local_subtechs if s.get("attack_id") and s["attack_id"] not in mitre_subtech_ids]

    # 缺失（MITRE 有但本地无）
    missing_parents = [p for p in mitre_parents if p["id"] not in local_parent_by_id]
    missing_subtechs = []
    for p in mitre_parents:
        for s in p.get("subtechniques", []):
            if s["id"] not in local_subtech_by_id:
                missing_subtechs.append((p, s))

    # 名称不一致检测（精确比较，不做归一化）
    name_mismatches = []
    for mp in mitre_parents:
        lp = local_parent_by_id.get(mp["id"])
        if lp and mp["name_en"] != lp.get("attack_name_en", ""):
            name_mismatches.append(("parent", mp["id"], mp["name_en"], lp.get("attack_name_en", "")))
    for p in mitre_parents:
        for s in p.get("subtechniques", []):
            ls = local_subtech_by_id.get(s["id"])
            if ls and s["name_en"] != ls.get("attack_name_en", ""):
                name_mismatches.append(("subtech", s["id"], s["name_en"], ls.get("attack_name_en", "")))

    coverage = 0
    if mitre_parent_count > 0:
        coverage = round((local_parent_count - len(local_only_parents)) / mitre_parent_count * 100, 1)
        if coverage > 100:
            coverage = 100.0

    # 构建 YAML frontmatter
    lines = []
    lines.append("---")
    lines.append('status: 【已完成】')
    lines.append('template_version: "1.0"')
    lines.append(f'last_updated: "{time.strftime("%Y-%m-%d")}"')
    lines.append(f'tactic_id: "{tactic_id}"')
    lines.append(f'tactic_name_cn: "{tactic_cn}"')
    lines.append(f'tactic_name_en: "{tactic_en}"')
    lines.append('attack_version: "v20"')
    lines.append(f'official_technique_count: {mitre_parent_count}')
    lines.append(f'official_subtechnique_count: {mitre_subtech_count}')
    lines.append(f'local_technique_count: {local_parent_count}')
    lines.append(f'local_subtechnique_count: {local_subtech_count}')
    lines.append(f'coverage_percentage: {coverage}')
    lines.append("---")
    lines.append("")
    lines.append(f"# {tactic_id} {tactic_cn} - 官方数据与本地文件映射表")
    lines.append("")
    lines.append("## 概述")
    lines.append("")
    lines.append(f"本文件记录 MITRE ATT&CK v20 中 {tactic_id} ({tactic_en}/{tactic_cn}) 战术的")
    lines.append("官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。")
    lines.append("")
    lines.append(f"- **官方版本**：MITRE ATT&CK Enterprise v20")
    lines.append(f"- **官方数据**：{mitre_parent_count} 项父技术 / {mitre_subtech_count} 项子技术")
    lines.append(f"- **本地数据**：{local_parent_count} 项父技术 / {local_subtech_count} 项子技术")
    lines.append(f"- **覆盖率**：{coverage}%")
    lines.append("")
    lines.append("## 父技术映射表")
    lines.append("")
    lines.append("| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |")
    lines.append("|--------|-------------|-------------|-------------|:-----------------:|:----:|------|")

    # 先列 MITRE 有的
    for mp in mitre_parents:
        lp = local_parent_by_id.get(mp["id"])
        official_sub_count = len(mp.get("subtechniques", []))
        if lp:
            local_sub_count = lp.get("sub_techniques_count", "0")
            actual_local_sub = sum(1 for s in local_subtechs if s.get("parent_technique") == mp["id"])
            file_path = f"./{lp['file']}"
            icon = status_icon(lp.get("status", ""))
            name_note = ""
            if mp["name_en"] != lp.get("attack_name_en", ""):
                name_note = f"🔄 本地名: {lp.get('attack_name_en', '')}"
            count_note = ""
            if str(official_sub_count) != str(local_sub_count):
                count_note = f"子技术数frontmatter={local_sub_count}"
            elif actual_local_sub != official_sub_count:
                count_note = f"实际文件={actual_local_sub}"
            note = " | ".join(x for x in [name_note, count_note] if x)
            if not note:
                note = "-"
            local_cn = lp.get("attack_name_cn", "")
            lines.append(f"| {mp['id']} | {mp['name_en']} | {local_cn} | {file_path} | {official_sub_count}/{actual_local_sub} | {icon} | {note} |")
        else:
            lines.append(f"| {mp['id']} | {mp['name_en']} | - | ❌ 缺失 | {official_sub_count}/0 | ❌ | 本地无文件 |")

    # 列本地有但 MITRE 没有的（撤销/迁移）
    if local_only_parents:
        for lp in local_only_parents:
            actual_local_sub = sum(1 for s in local_subtechs if s.get("parent_technique") == lp.get("attack_id"))
            lines.append(f"| {lp.get('attack_id', '?')} | - | {lp.get('attack_name_cn', '')} | ./{lp['file']} | 0/{actual_local_sub} | ⚠️ | 官方v20无此技术(可能已撤销/迁移) |")

    lines.append("")
    lines.append("## 子技术映射表")
    lines.append("")
    lines.append("| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |")
    lines.append("|---------|-------------|-------------|--------|-------------|:----:|------|")

    for mp in mitre_parents:
        for s in mp.get("subtechniques", []):
            ls = local_subtech_by_id.get(s["id"])
            if ls:
                file_path = f"./{ls['parent_dir']}/{ls['file']}"
                icon = status_icon(ls.get("status", ""))
                name_note = ""
                if s["name_en"] != ls.get("attack_name_en", ""):
                    name_note = f"🔄 本地名: {ls.get('attack_name_en', '')}"
                note = name_note if name_note else "-"
                local_cn = ls.get("attack_name_cn", "")
                lines.append(f"| {s['id']} | {s['name_en']} | {local_cn} | {mp['id']} | {file_path} | {icon} | {note} |")
            else:
                lines.append(f"| {s['id']} | {s['name_en']} | - | {mp['id']} | ❌ 缺失 | ❌ | 本地无文件 |")

    if local_only_subtechs:
        for ls in local_only_subtechs:
            file_path = f"./{ls['parent_dir']}/{ls['file']}"
            lines.append(f"| {ls.get('attack_id', '?')} | - | {ls.get('attack_name_cn', '')} | {ls.get('parent_technique', '')} | {file_path} | ⚠️ | 官方v20无此子技术 |")

    lines.append("")
    lines.append("## 状态图例")
    lines.append("")
    lines.append("- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】")
    lines.append("- 📝 草稿：文件存在但 frontmatter status 非【已完成】")
    lines.append("- ❌ 缺失：官方有但本地无文件")
    lines.append("- 🔄 名称不一致：本地文件名/EN名与官方不符")
    lines.append("- ⚠️ Revoked/迁移：本地有但官方v20已撤销或迁移")
    lines.append("")
    lines.append("## 缺失与不一致清单")
    lines.append("")

    issues = []
    if missing_parents:
        issues.append(f"### 缺失父技术 ({len(missing_parents)} 项)")
        for p in missing_parents:
            issues.append(f"- **{p['id']}** {p['name_en']}：本地无文件")
        issues.append("")
    if missing_subtechs:
        issues.append(f"### 缺失子技术 ({len(missing_subtechs)} 项)")
        for p, s in missing_subtechs:
            issues.append(f"- **{s['id']}** {s['name_en']} (父技术 {p['id']})：本地无文件")
        issues.append("")
    if local_only_parents:
        issues.append(f"### 本地多余父技术 ({len(local_only_parents)} 项) - 可能为已撤销/迁移技术")
        for p in local_only_parents:
            issues.append(f"- **{p.get('attack_id', '?')}** {p.get('attack_name_en', '')}：官方v20无此ID")
        issues.append("")
    if local_only_subtechs:
        issues.append(f"### 本地多余子技术 ({len(local_only_subtechs)} 项)")
        for s in local_only_subtechs:
            issues.append(f"- **{s.get('attack_id', '?')}** {s.get('attack_name_en', '')}：官方v20无此ID")
        issues.append("")
    if name_mismatches:
        issues.append(f"### 名称不一致 ({len(name_mismatches)} 项)")
        for kind, tid, official, local_name in name_mismatches:
            issues.append(f"- **{tid}** ({kind}): 官方=`{official}` vs 本地=`{local_name}`")
        issues.append("")

    if not issues:
        lines.append("无缺失或不一致项，本地知识库与 MITRE ATT&CK v20 官方数据完全对齐。")
    else:
        lines.extend(issues)

    lines.append("## 参考来源")
    lines.append("")
    lines.append(f"- [MITRE ATT&CK - {tactic_id}](https://attack.mitre.org/tactics/{tactic_id}/)")
    lines.append("- [MITRE ATT&CK STIX Data v20](https://github.com/mitre-attack/attack-stix-data)")
    lines.append(f"- 本地审计时间：{time.strftime('%Y-%m-%d')}")
    lines.append("")

    return "\n".join(lines)


def cmd_generate(args):
    """读取两份 JSON，生成各战术目录下的 MAPPING.md"""
    print(f"[generate] 知识库根目录: {TACTICS_ROOT}")

    local = load_json(LOCAL_SCAN_PATH)
    if not local:
        print(f"[generate] 错误: {LOCAL_SCAN_PATH} 不存在，请先运行 scan")
        return 1

    skip_mitre = getattr(args, "skip_mitre", False)
    mitre = None
    if not skip_mitre:
        mitre = load_json(MITRE_OFFICIAL_PATH)
        if not mitre:
            print(f"[generate] 警告: {MITRE_OFFICIAL_PATH} 不存在，将以空 MITRE 数据生成（建议先运行 fetch）")

    # mitre_official 结构归一化
    mitre_by_id = {}
    if mitre:
        if isinstance(mitre, list):
            for item in mitre:
                tid = item.get("tactic_id")
                if tid:
                    mitre_by_id[tid] = item
        elif isinstance(mitre, dict):
            for k, v in mitre.items():
                if k.startswith("TA"):
                    mitre_by_id[k] = v

    summary = []
    for tactic_dir, tactic_id, tactic_cn, tactic_en in TACTICS:
        local_data = local.get(tactic_dir, {}) if local else {}
        mitre_data = mitre_by_id.get(tactic_id)

        if not mitre_data:
            print(f"  警告: 无 {tactic_id} 的 MITRE 数据，以空数据生成")
            mitre_data = {"tactic_id": tactic_id, "tactic_name_en": tactic_en, "parent_techniques": []}

        content = gen_mapping(tactic_dir, tactic_id, tactic_cn, tactic_en, local_data, mitre_data)
        out_path = TACTICS_ROOT / tactic_dir / "MAPPING.md"
        out_path.write_text(content, encoding="utf-8")
        print(f"  写入: {tactic_dir}/MAPPING.md ({len(content)} 字节)")

        summary.append({
            "tactic_id": tactic_id,
            "tactic_dir": tactic_dir,
            "official_parents": len(mitre_data.get("parent_techniques", [])),
            "official_subtechs": sum(len(p.get("subtechniques", [])) for p in mitre_data.get("parent_techniques", [])),
            "local_parents": local_data.get("parent_count", 0),
            "local_subtechs": local_data.get("subtech_count", 0),
        })

    print(f"\n[generate] 完成: {len(summary)} 个 MAPPING.md")
    print(f"\n{'Tactic':<12} {'官方(P/S)':<18} {'本地(P/S)':<15}")
    for s in summary:
        print(f"{s['tactic_id']:<12} {s['official_parents']}/{s['official_subtechs']:<15} {s['local_parents']}/{s['local_subtechs']}")
    return 0


# ============================================================
# 子命令 4：verify - 验证 MAPPING.md
# ============================================================

def parse_markdown_table(content, section_header):
    """解析指定 section 下的 markdown 表格，返回行列表。"""
    rows = []
    in_section = False
    in_table = False
    for line in content.split("\n"):
        if line.startswith("## ") and section_header in line:
            in_section = True
            in_table = False
            continue
        if line.startswith("## ") and in_section:
            break
        if not in_section:
            continue
        if line.startswith("|"):
            # 仅匹配整行都是分隔符的情况（|---|---|...|），避免误判含 `---` 的数据行
            # 如 `T1547.001-Registry-Run-Keys---Startup-Folder.md`
            if re.match(r"^\|[-:\s|]+\|\s*$", line):
                in_table = True
                continue
            if in_table:
                cols = [c.strip() for c in line.split("|")[1:-1]]
                if cols and cols[0].startswith("T"):
                    rows.append(cols)
    return rows


def parse_summary_section(content, sub_header):
    """解析 '## 缺失与不一致清单' 下的子节计数。"""
    pattern = rf"### {re.escape(sub_header)}\s*\((\d+)\s*项\)"
    m = re.search(pattern, content)
    if m:
        return int(m.group(1))
    pattern2 = rf"### {re.escape(sub_header)}\s*\n((?:- \*\*[^\n]+\n?)+)"
    m2 = re.search(pattern2, content)
    if m2:
        return m2.group(1).count("\n- **")
    return None


def compute_expected(dir_name, local_data, official_by_id):
    """从 JSON 重新计算每个战术的对比结果。"""
    tid = DIR_TO_TID.get(dir_name)
    if not tid:
        # 尝试从 local_data 推断
        if local_data.get("parents"):
            tid = local_data["parents"][0].get("tactic_id")
    if not tid:
        return None
    off_data = official_by_id.get(tid, {})

    off_parents = off_data.get("parent_techniques", [])
    off_parent_count = len(off_parents)
    off_sub_count = sum(len(p.get("subtechniques", [])) for p in off_parents)

    local_parents = local_data.get("parents", [])
    local_subtechs = local_data.get("subtechs", [])
    local_parent_count = len(local_parents)
    local_sub_count = len(local_subtechs)

    local_parent_by_id = {p["attack_id"]: p for p in local_parents if p.get("attack_id")}
    local_sub_by_id = {s["attack_id"]: s for s in local_subtechs if s.get("attack_id")}

    off_parent_by_id = {p["id"]: p for p in off_parents}
    off_sub_by_id = {}
    for p in off_parents:
        for s in p.get("subtechniques", []):
            off_sub_by_id[s["id"]] = s

    missing_parents = [pid for pid in off_parent_by_id if pid not in local_parent_by_id]
    missing_subtechs = [sid for sid in off_sub_by_id if sid not in local_sub_by_id]
    extra_parents = [pid for pid in local_parent_by_id if pid not in off_parent_by_id]
    extra_subtechs = [sid for sid in local_sub_by_id if sid not in off_sub_by_id]

    name_mismatch_parents = []
    for pid in off_parent_by_id:
        if pid in local_parent_by_id:
            off_name = off_parent_by_id[pid]["name_en"]
            local_name = local_parent_by_id[pid].get("attack_name_en", "")
            if off_name != local_name:
                name_mismatch_parents.append((pid, off_name, local_name))

    name_mismatch_subtechs = []
    for sid in off_sub_by_id:
        if sid in local_sub_by_id:
            off_name = off_sub_by_id[sid]["name_en"]
            local_name = local_sub_by_id[sid].get("attack_name_en", "")
            if off_name != local_name:
                name_mismatch_subtechs.append((sid, off_name, local_name))

    if off_parent_count > 0:
        coverage = round((off_parent_count - len(missing_parents)) / off_parent_count * 100, 1)
    else:
        coverage = 100.0

    return {
        "tactic_id": tid,
        "official_technique_count": off_parent_count,
        "official_subtechnique_count": off_sub_count,
        "local_technique_count": local_parent_count,
        "local_subtechnique_count": local_sub_count,
        "coverage_percentage": coverage,
        "missing_parents": missing_parents,
        "missing_subtechs": missing_subtechs,
        "extra_parents": extra_parents,
        "extra_subtechs": extra_subtechs,
        "name_mismatch_parents": name_mismatch_parents,
        "name_mismatch_subtechs": name_mismatch_subtechs,
    }


def verify_one(dir_name, local_data, expected):
    """验证单个战术的 MAPPING.md。"""
    tid = expected["tactic_id"]
    mapping_path = TACTICS_ROOT / dir_name / "MAPPING.md"
    result = {
        "tactic_id": tid,
        "dir": dir_name,
        "exists": mapping_path.exists(),
        "issues": [],
        "warnings": [],
    }

    if not mapping_path.exists():
        result["issues"].append("MAPPING.md 不存在")
        return result

    content = mapping_path.read_text(encoding="utf-8")

    # 1. 验证 YAML frontmatter
    yaml_fields = parse_yaml_frontmatter(content)
    for field in [
        "official_technique_count",
        "official_subtechnique_count",
        "local_technique_count",
        "local_subtechnique_count",
        "coverage_percentage",
        "tactic_id",
    ]:
        exp_val = expected.get(field)
        actual = yaml_fields.get(field)
        if actual != exp_val:
            result["issues"].append(
                f"YAML {field}: 声明={actual!r}, 实际={exp_val!r}"
            )

    # 2. 验证父技术表行数
    parent_rows = parse_markdown_table(content, "父技术映射表")
    expected_parent_rows = expected["official_technique_count"] + len(expected["extra_parents"])
    if len(parent_rows) != expected_parent_rows:
        result["issues"].append(
            f"父技术表行数: 声明={len(parent_rows)}, 期望={expected_parent_rows} (官方{expected['official_technique_count']}+多余{len(expected['extra_parents'])})"
        )

    # 3. 验证子技术表行数
    sub_rows = parse_markdown_table(content, "子技术映射表")
    expected_sub_rows = expected["official_subtechnique_count"] + len(expected["extra_subtechs"])
    if len(sub_rows) != expected_sub_rows:
        result["issues"].append(
            f"子技术表行数: 声明={len(sub_rows)}, 期望={expected_sub_rows} (官方{expected['official_subtechnique_count']}+多余{len(expected['extra_subtechs'])})"
        )

    # 4. 验证父技术表每一行状态标记
    for row in parent_rows:
        if len(row) < 6:
            continue
        tech_id = row[0]
        status_cell = row[5]

        if tech_id in expected["missing_parents"]:
            if "❌" not in status_cell:
                result["issues"].append(
                    f"父技术 {tech_id}: 应标 ❌缺失, 实际标 '{status_cell}'"
                )
        elif tech_id in expected["extra_parents"]:
            if "⚠️" not in status_cell:
                result["warnings"].append(
                    f"父技术 {tech_id}: 本地多余(官方已撤销), 应标 ⚠️, 实际标 '{status_cell}'"
                )
        else:
            mismatch = any(m[0] == tech_id for m in expected["name_mismatch_parents"])
            if mismatch and len(row) >= 7 and "🔄" not in row[6]:
                result["warnings"].append(
                    f"父技术 {tech_id}: 名称不一致但备注列无 🔄 标记"
                )
            if "❌" in status_cell and tech_id not in expected["missing_parents"]:
                result["issues"].append(
                    f"父技术 {tech_id}: 错误标记 ❌ 但本地文件存在"
                )

    # 5. 验证子技术表每一行状态标记
    for row in sub_rows:
        if len(row) < 6:
            continue
        tech_id = row[0]
        status_cell = row[5]

        if tech_id in expected["missing_subtechs"]:
            if "❌" not in status_cell:
                result["issues"].append(
                    f"子技术 {tech_id}: 应标 ❌缺失, 实际标 '{status_cell}'"
                )
        elif tech_id in expected["extra_subtechs"]:
            if "⚠️" not in status_cell:
                result["warnings"].append(
                    f"子技术 {tech_id}: 本地多余, 应标 ⚠️, 实际标 '{status_cell}'"
                )
        else:
            mismatch = any(m[0] == tech_id for m in expected["name_mismatch_subtechs"])
            if mismatch and len(row) >= 7 and "🔄" not in row[6]:
                result["warnings"].append(
                    f"子技术 {tech_id}: 名称不一致但备注列无 🔄 标记"
                )

    # 6. 验证缺失与不一致清单计数
    declared_missing_parents = parse_summary_section(content, "缺失父技术")
    declared_missing_subtechs = parse_summary_section(content, "缺失子技术")
    declared_extra_parents = parse_summary_section(content, "本地多余父技术")
    declared_extra_subtechs = parse_summary_section(content, "本地多余子技术")
    declared_name_mismatch = parse_summary_section(content, "名称不一致")

    if declared_missing_parents is not None and declared_missing_parents != len(expected["missing_parents"]):
        result["issues"].append(
            f"清单'缺失父技术': 声明={declared_missing_parents}项, 实际={len(expected['missing_parents'])}项"
        )
    if declared_missing_subtechs is not None and declared_missing_subtechs != len(expected["missing_subtechs"]):
        result["issues"].append(
            f"清单'缺失子技术': 声明={declared_missing_subtechs}项, 实际={len(expected['missing_subtechs'])}项"
        )
    if declared_extra_parents is not None and declared_extra_parents != len(expected["extra_parents"]):
        result["warnings"].append(
            f"清单'本地多余父技术': 声明={declared_extra_parents}项, 实际={len(expected['extra_parents'])}项"
        )
    if declared_extra_subtechs is not None and declared_extra_subtechs != len(expected["extra_subtechs"]):
        result["warnings"].append(
            f"清单'本地多余子技术': 声明={declared_extra_subtechs}项, 实际={len(expected['extra_subtechs'])}项"
        )

    total_mismatch = len(expected["name_mismatch_parents"]) + len(expected["name_mismatch_subtechs"])
    if declared_name_mismatch is not None and declared_name_mismatch != total_mismatch:
        result["issues"].append(
            f"清单'名称不一致': 声明={declared_name_mismatch}项, 实际={total_mismatch}项 (父{len(expected['name_mismatch_parents'])}+子{len(expected['name_mismatch_subtechs'])})"
        )

    return result


def cmd_verify(args):
    """验证 15 个 MAPPING.md 与 JSON 数据的一致性。"""
    print(f"[verify] 知识库根目录: {TACTICS_ROOT}")

    local = load_json(LOCAL_SCAN_PATH)
    if not local:
        print(f"[verify] 错误: {LOCAL_SCAN_PATH} 不存在，请先运行 scan")
        return 1

    official = load_json(MITRE_OFFICIAL_PATH)
    if not official:
        print(f"[verify] 错误: {MITRE_OFFICIAL_PATH} 不存在，请先运行 fetch")
        return 1

    # 官方数据归一化
    if isinstance(official, dict):
        official_by_id = {k: v for k, v in official.items() if k.startswith("TA")}
    else:
        official_by_id = {x["tactic_id"]: x for x in official}

    print("=" * 80)
    print("MAPPING.md 验证报告")
    print("=" * 80)

    all_results = []
    for dir_name in DIR_TO_TID.keys():
        local_data = local.get(dir_name, {})
        if not local_data:
            # 目录未扫描到，构造空数据
            local_data = {"parents": [], "subtechs": [], "parent_count": 0, "subtech_count": 0}
        expected = compute_expected(dir_name, local_data, official_by_id)
        if expected is None:
            all_results.append({
                "tactic_id": "?", "dir": dir_name, "exists": False,
                "issues": ["无法确定 tactic_id"], "warnings": []
            })
            continue
        result = verify_one(dir_name, local_data, expected)
        all_results.append((result, expected))

    total_issues = 0
    total_warnings = 0
    for item in all_results:
        if isinstance(item, tuple):
            result, expected = item
        else:
            result, expected = item, None

        tid = result["tactic_id"]
        dir_name = result["dir"]
        print(f"\n--- {tid} ({dir_name}) ---")
        if not result["exists"]:
            print("  ❌ MAPPING.md 不存在")
            total_issues += 1
            continue

        if expected:
            print(
                f"  官方P/S: {expected['official_technique_count']}/{expected['official_subtechnique_count']}  "
                f"本地P/S: {expected['local_technique_count']}/{expected['local_subtechnique_count']}  "
                f"覆盖率: {expected['coverage_percentage']}%"
            )
            print(
                f"  缺失: P={len(expected['missing_parents'])} S={len(expected['missing_subtechs'])}  "
                f"多余: P={len(expected['extra_parents'])} S={len(expected['extra_subtechs'])}  "
                f"名称不一致: P={len(expected['name_mismatch_parents'])} S={len(expected['name_mismatch_subtechs'])}"
            )

        if not result["issues"] and not result["warnings"]:
            print("  ✅ 全部一致")
        else:
            for issue in result["issues"]:
                print(f"  ❌ {issue}")
                total_issues += 1
            for warn in result["warnings"]:
                print(f"  ⚠️ {warn}")
                total_warnings += 1

    print(f"\n{'=' * 80}")
    print(f"总计: {len(all_results)} 个战术")
    print(f"  ❌ Issues (硬错误): {total_issues}")
    print(f"  ⚠️ Warnings (软警告): {total_warnings}")
    print("=" * 80)
    return 0 if total_issues == 0 else 2


# ============================================================
# 子命令 5：status - 总体统计
# ============================================================

def cmd_status(args):
    """打印总体统计表。"""
    print(f"[status] 知识库根目录: {TACTICS_ROOT}")

    local = load_json(LOCAL_SCAN_PATH)
    official = load_json(MITRE_OFFICIAL_PATH)

    if not local:
        print(f"[status] 错误: {LOCAL_SCAN_PATH} 不存在，请先运行 scan")
        return 1
    if not official:
        print(f"[status] 警告: {MITRE_OFFICIAL_PATH} 不存在，部分统计不可用")

    if isinstance(official, dict):
        official_by_id = {k: v for k, v in official.items() if k.startswith("TA")}
    elif official:
        official_by_id = {x["tactic_id"]: x for x in official}
    else:
        official_by_id = {}

    print("\nTactic    Dir                             OffP/OffS  LocP/LocS  MapSize")
    print("-" * 80)
    tp = ts = lp = ls = 0
    for d, tid, _, _ in TACTICS:
        md = official_by_id.get(tid, {})
        ld = local.get(d, {})
        op = len(md.get("parent_techniques", []))
        os_ = sum(len(p.get("subtechniques", [])) for p in md.get("parent_techniques", []))
        lpc = ld.get("parent_count", 0)
        lsc = ld.get("subtech_count", 0)
        mpath = TACTICS_ROOT / d / "MAPPING.md"
        ms = mpath.stat().st_size if mpath.exists() else 0
        ms_str = f"{ms}B" if ms < 1024 else f"{ms/1024:.1f}KB"
        print(f"{tid:<10}{d:<32}{op}/{os_:<10}{lpc}/{lsc:<10}{ms_str}")
        tp += op; ts += os_; lp += lpc; ls += lsc

    print("-" * 80)
    print(f"TOTAL     {'':<32}{tp}/{ts:<10}{lp}/{ls}")

    mp_files = list(TACTICS_ROOT.rglob("MAPPING.md"))
    print(f"\nMAPPING.md 文件数: {len(mp_files)}")
    print(f"总字节数: {sum(p.stat().st_size for p in mp_files)} ({sum(p.stat().st_size for p in mp_files)/1024:.1f} KB)")

    # JSON 文件状态
    print(f"\n数据文件:")
    print(f"  _data/_local_scan.json: {'存在' if LOCAL_SCAN_PATH.exists() else '缺失'}", end="")
    if LOCAL_SCAN_PATH.exists():
        print(f" ({LOCAL_SCAN_PATH.stat().st_size/1024:.1f} KB)")
    else:
        print()
    print(f"  _data/_mitre_official.json: {'存在' if MITRE_OFFICIAL_PATH.exists() else '缺失'}", end="")
    if MITRE_OFFICIAL_PATH.exists():
        print(f" ({MITRE_OFFICIAL_PATH.stat().st_size/1024:.1f} KB)")
    else:
        print()

    return 0


# ============================================================
# 子命令 6：all - 顺序执行全流程
# ============================================================

def cmd_all(args):
    """顺序执行 scan → fetch → generate → verify。"""
    print("=" * 80)
    print("ATT&CK 知识库 MAPPING.md 全流程审计")
    print("=" * 80)

    steps = [
        ("scan", cmd_scan),
        ("fetch", cmd_fetch),
        ("generate", cmd_generate),
        ("verify", cmd_verify),
    ]

    for name, func in steps:
        print(f"\n{'='*80}")
        print(f">>> 步骤: {name}")
        print(f"{'='*80}")
        rc = func(args)
        if rc != 0 and name == "verify":
            # verify 返回 2 表示有 issues，不阻断
            print(f"[all] {name} 返回 {rc}（有 issues，继续）")
        elif rc != 0:
            print(f"[all] {name} 失败 (返回码 {rc})，中止")
            return rc

    print(f"\n{'='*80}")
    print("全流程完成")
    print("=" * 80)
    return 0


# ============================================================
# CLI 入口
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        prog="attack_mapping",
        description="ATT&CK 知识库 MAPPING.md 审计工具链",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
示例:
  python attack_mapping.py scan          # 扫描本地知识库
  python attack_mapping.py fetch         # 抓取 MITRE 官方数据
  python attack_mapping.py generate      # 生成 MAPPING.md
  python attack_mapping.py verify        # 验证 MAPPING.md
  python attack_mapping.py status        # 打印统计
  python attack_mapping.py all           # 全流程
""",
    )
    sub = parser.add_subparsers(dest="command", help="子命令")

    p_scan = sub.add_parser("scan", help="扫描本地知识库 frontmatter")
    p_scan.set_defaults(func=cmd_scan)

    p_fetch = sub.add_parser("fetch", help="从 attack.mitre.org 抓取 15 个战术页")
    p_fetch.set_defaults(func=cmd_fetch)

    p_generate = sub.add_parser("generate", help="生成 MAPPING.md")
    p_generate.add_argument("--skip-mitre", action="store_true", help="仅用本地数据生成（跳过 MITRE 数据）")
    p_generate.set_defaults(func=cmd_generate)

    p_verify = sub.add_parser("verify", help="验证 MAPPING.md 与 JSON 一致性")
    p_verify.set_defaults(func=cmd_verify)

    p_status = sub.add_parser("status", help="打印总体统计")
    p_status.set_defaults(func=cmd_status)

    p_all = sub.add_parser("all", help="顺序执行 scan → fetch → generate → verify")
    p_all.set_defaults(func=cmd_all)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
