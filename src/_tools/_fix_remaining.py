#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一次性修复脚本：处理 audit_diff 发现的全部差异。
- 类别1: 删除 42 个已撤销/误放置文件
- 类别2: 已包含在类别1（T1574/T1550/T1207 误放置）
- 类别3: T1546.009/.010 在 TA0004 名称对齐（与 TA0003 一致）
- 类别4: T1055.008/.012/.013/.014 在 TA0004 从 TA0005 复制覆盖
- 类别5: T1564.* 在 TA0005 更新 attack_name_en + 重命名文件
- 类别6: 缺失子技术保留现状（无需操作）
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data"
DRY_RUN = "--apply" not in sys.argv

def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def save_json(p, data):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ============================================================
# 类别 1+2: 删除 42 个已撤销/误放置文件
# ============================================================

def collect_extra_files():
    """从 _local_scan.json + _mitre_official.json 自动找出所有 extra 文件。"""
    local = load_json(DATA / "_local_scan.json")
    official = load_json(DATA / "_mitre_official.json")

    # Build official TID set per tactic
    def official_tids(ta_id):
        s = set()
        for p in official[ta_id]["parent_techniques"]:
            s.add(p["id"])
            for sub in p["subtechniques"]:
                s.add(sub["id"])
        return s

    extra_files = []
    for ta_id, tdir in [
        ("TA0043","01-Reconnaissance"),("TA0042","02-Resource-Development"),
        ("TA0001","03-Initial-Access"),("TA0002","04-Execution"),
        ("TA0003","05-Persistence"),("TA0004","06-Privilege-Escalation"),
        ("TA0005","07-Stealth"),("TA0112","08-Defense-Impairment"),
        ("TA0006","09-Credential-Access"),("TA0007","10-Discovery"),
        ("TA0008","11-Lateral-Movement"),("TA0009","12-Collection"),
        ("TA0011","13-Command-and-Control"),("TA0010","14-Exfiltration"),
        ("TA0040","15-Impact"),
    ]:
        off = official_tids(ta_id)
        t = local[tdir]
        for p in t["parents"]:
            if p["attack_id"] not in off:
                fpath = ROOT / tdir / p["file"]
                extra_files.append((fpath, f"{tdir}/parent/{p['attack_id']}"))
        for s in t["subtechs"]:
            if s["attack_id"] not in off:
                fpath = ROOT / tdir / s["parent_dir"] / s["file"]
                extra_files.append((fpath, f"{tdir}/sub/{s['attack_id']}"))
    return extra_files

def delete_extra_files():
    extra = collect_extra_files()
    print(f"\n=== 类别1+2: 删除 {len(extra)} 个已撤销/误放置文件 ===")
    deleted = 0
    for fpath, desc in extra:
        if fpath.exists():
            if not DRY_RUN:
                fpath.unlink()
            print(f"  {'[DRY] ' if DRY_RUN else ''}DELETE: {desc} -> {fpath.name}")
            deleted += 1
        else:
            print(f"  SKIP (不存在): {desc} -> {fpath}")
    print(f"  共删除: {deleted}")
    return deleted

# ============================================================
# 类别 3: T1546.009/.010 在 TA0004 名称对齐
# ============================================================

def fix_t1546_ta0004():
    """06-Privilege-Escalation/T1546/ 下 .009/.010 名称与 TA0003 不一致。"""
    print("\n=== 类别3: T1546 双目录名称对齐 (TA0004) ===")
    ta4_dir = ROOT / "06-Privilege-Escalation" / "T1546"
    ta3_dir = ROOT / "05-Persistence" / "T1546"

    fixes = [
        # (old_filename, new_filename, new_name_en)
        ("T1546.009-AppCert-DLL.md", "T1546.009-AppCert-DLLs.md", "AppCert DLLs"),
        ("T1546.010-AppInit-DLL.md", "T1546.010-AppInit-DLLs.md", "AppInit DLLs"),
    ]

    for old_fn, new_fn, new_name in fixes:
        old_path = ta4_dir / old_fn
        new_path = ta4_dir / new_fn
        ref_path = ta3_dir / new_fn  # TA0003 的正确版本

        if not old_path.exists():
            print(f"  SKIP (不存在): {old_fn}")
            continue

        # 读取 TA0004 旧文件
        text = old_path.read_text(encoding="utf-8")

        # 更新 frontmatter 中的 attack_name_en
        text = re.sub(
            r'(attack_name_en:\s*").*?(")',
            rf'\g<1>{new_name}\g<2>',
            text,
            count=1,
        )

        # 写入新文件名
        if not DRY_RUN:
            new_path.write_text(text, encoding="utf-8")
            old_path.unlink()
        print(f"  {'[DRY] ' if DRY_RUN else ''}RENAME+UPDATE: {old_fn} -> {new_fn} (attack_name_en='{new_name}')")

# ============================================================
# 类别 4: T1055.008/.012/.013/.014 在 TA0004 从 TA0005 复制覆盖
# ============================================================

def fix_t1055_ta0004():
    """06-Privilege-Escalation/T1055/ 下 4 个文件名称过时，从 07-Stealth 复制正确版本。"""
    print("\n=== 类别4: T1055 多战术副本同步 (TA0004 <- TA0005) ===")
    ta4_dir = ROOT / "06-Privilege-Escalation" / "T1055"
    ta5_dir = ROOT / "07-Stealth" / "T1055"

    # 这些 TID 的文件在 TA0004 需要用 TA0005 的版本覆盖
    tids = ["T1055.008", "T1055.012", "T1055.013", "T1055.014"]

    for tid in tids:
        # 在 TA0005 找到正确文件
        ref_files = list(ta5_dir.glob(f"{tid}-*.md"))
        if not ref_files:
            print(f"  ERROR: TA0005 中找不到 {tid}-*.md")
            continue
        ref_path = ref_files[0]

        # 在 TA0004 找到旧文件
        old_files = list(ta4_dir.glob(f"{tid}-*.md"))
        if not old_files:
            print(f"  WARN: TA0004 中找不到 {tid}-*.md, 直接复制")
            target_path = ta4_dir / ref_path.name
        else:
            old_path = old_files[0]
            if old_path.name != ref_path.name:
                # 文件名不同，需要删除旧的
                if not DRY_RUN:
                    old_path.unlink()
                print(f"  {'[DRY] ' if DRY_RUN else ''}DELETE OLD: {old_path.name}")
            target_path = ta4_dir / ref_path.name

        # 复制
        if not DRY_RUN:
            shutil.copy2(ref_path, target_path)
        print(f"  {'[DRY] ' if DRY_RUN else ''}COPY: {ref_path.name} (TA0005 -> TA0004)")

# ============================================================
# 类别 5: T1564.* 在 TA0005 更新 attack_name_en + 重命名
# ============================================================

def fix_t1564_ta0005():
    """07-Stealth/T1564/ 下 9 个子技术 attack_name_en 与官方不一致。"""
    print("\n=== 类别5: T1564 系列命名差异修复 (TA0005) ===")
    ta5_dir = ROOT / "07-Stealth" / "T1564"

    # (tid, new_name_en) — 从 _mitre_official.json 获取的官方名称
    fixes = [
        ("T1564.001", "Hidden Files and Directories"),
        ("T1564.002", "Hidden Users"),
        ("T1564.003", "Hidden Window"),
        ("T1564.008", "Email Hiding Rules"),
        ("T1564.009", "Resource Forking"),
        ("T1564.011", "Ignore Process Interrupts"),
        ("T1564.012", "File/Path Exclusions"),
        ("T1564.013", "Bind Mounts"),
        ("T1564.014", "Extended Attributes"),
    ]

    for tid, new_name in fixes:
        old_files = list(ta5_dir.glob(f"{tid}-*.md"))
        if not old_files:
            print(f"  ERROR: 找不到 {tid}-*.md")
            continue
        old_path = old_files[0]

        # 生成新文件名: TID-New-Name.md (空格转连字符, 斜杠保留为连字符)
        name_for_file = new_name.replace(" ", "-").replace("/", "-")
        new_fn = f"{tid}-{name_for_file}.md"
        new_path = ta5_dir / new_fn

        # 读取并更新 frontmatter
        text = old_path.read_text(encoding="utf-8")
        text = re.sub(
            r'(attack_name_en:\s*").*?(")',
            rf'\g<1>{new_name}\g<2>',
            text,
            count=1,
        )

        if not DRY_RUN:
            new_path.write_text(text, encoding="utf-8")
            if old_path != new_path:
                old_path.unlink()
        action = "UPDATE+RENAME" if old_path.name != new_fn else "UPDATE"
        print(f"  {'[DRY] ' if DRY_RUN else ''}{action}: {old_path.name} -> {new_fn} ('{new_name}')")

# ============================================================
# 主函数
# ============================================================

def main():
    mode = "APPLY" if not DRY_RUN else "DRY-RUN"
    print(f"{'='*60}")
    print(f"ATT&CK 知识库差异修复 — {mode}")
    print(f"{'='*60}")

    n1 = delete_extra_files()
    fix_t1546_ta0004()
    fix_t1055_ta0004()
    fix_t1564_ta0005()

    print(f"\n{'='*60}")
    print(f"修复完成 ({mode})")
    print(f"  删除文件: {n1}")
    print(f"  T1546 对齐: 2 项")
    print(f"  T1055 同步: 4 项")
    print(f"  T1564 重命名: 9 项")
    if DRY_RUN:
        print(f"\n这是 DRY-RUN。执行 --apply 以实际修改文件。")
    else:
        print(f"\n下一步: python _tools/attack_mapping.py scan && python _tools/attack_mapping.py generate && python _tools/attack_mapping.py verify && python _tools/audit_diff.py")

if __name__ == "__main__":
    main()
