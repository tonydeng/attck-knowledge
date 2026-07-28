"""打印指定战术的详细 name_mismatch_subs。"""
import json
import sys
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "_data" / "_audit_report.json"
data = json.load(p.open(encoding="utf-8"))

# 默认打印问题最严重的 TA0005 和 TA0004
target_ids = sys.argv[1:] or ["TA0005", "TA0004", "TA0006"]

for ta_id in target_ids:
    tac = data["tactics"].get(ta_id)
    if not tac:
        continue
    diff = tac["diff"]
    print(f"\n{'=' * 80}")
    print(f"{ta_id} {tac['tactic_name_en']} (本地父{tac['local_parent_count']}/官{tac['official_parent_count']} | 本地子{tac['local_sub_count']}/官{tac['official_sub_count']})")
    print('=' * 80)

    if diff["missing_parents"]:
        print(f"\n[缺失父技术 {len(diff['missing_parents'])} 个]")
        for s in diff["missing_parents"]:
            print(f"  {s['tid']:<14} {s['official_name']}")
    if diff["extra_parents"]:
        print(f"\n[多余父技术 {len(diff['extra_parents'])} 个]")
        for s in diff["extra_parents"]:
            print(f"  {s['tid']:<14} {s['local_name']}  [{s['local_file']}]")
    if diff["missing_subs"]:
        print(f"\n[缺失子技术 {len(diff['missing_subs'])} 个]")
        for s in diff["missing_subs"]:
            print(f"  {s['tid']:<14} {s['official_name']}")
    if diff["extra_subs"]:
        print(f"\n[多余子技术 {len(diff['extra_subs'])} 个]")
        for s in diff["extra_subs"]:
            print(f"  {s['tid']:<14} {s['local_name']}  [{s['local_file']}]")
    if diff["name_mismatch_parents"]:
        print(f"\n[父技术名称不一致 {len(diff['name_mismatch_parents'])} 个]")
        for s in diff["name_mismatch_parents"]:
            print(f"  {s['tid']:<14} 本地: {s['local_name']}")
            print(f"  {'':<14} 官方: {s['official_name']}")
    if diff["name_mismatch_subs"]:
        print(f"\n[子技术名称不一致 {len(diff['name_mismatch_subs'])} 个]")
        for s in diff["name_mismatch_subs"]:
            print(f"  {s['tid']:<14} 本地: {s['local_name']}")
            print(f"  {'':<14} 官方: {s['official_name']}")
