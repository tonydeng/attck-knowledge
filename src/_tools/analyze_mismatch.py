"""分析 _audit_report.json 中的名称不一致模式。"""
import json
from pathlib import Path
from collections import Counter

p = Path(__file__).resolve().parent.parent / "_data" / "_audit_report.json"
data = json.load(p.open(encoding="utf-8"))

# 按战术打印所有 name_mismatch_subs
for ta_id, tac in data["tactics"].items():
    diff = tac["diff"]
    nm = diff["name_mismatch_subs"]
    if not nm:
        continue
    print(f"\n{'=' * 80}")
    print(f"{ta_id} {tac['tactic_name_en']} - 子技术名称不一致 {len(nm)} 个")
    print('=' * 80)
    for s in nm:
        print(f"  {s['tid']:<14}")
        print(f"    本地: {s['local_name']}")
        print(f"    官方: {s['official_name']}")

# 同样打印 name_mismatch_parents
print("\n\n" + "#" * 80)
print("# 父技术名称不一致")
print("#" * 80)
for ta_id, tac in data["tactics"].items():
    diff = tac["diff"]
    nm = diff["name_mismatch_parents"]
    if not nm:
        continue
    print(f"\n{ta_id} {tac['tactic_name_en']} - 父技术名称不一致 {len(nm)} 个")
    for s in nm:
        print(f"  {s['tid']:<14}")
        print(f"    本地: {s['local_name']}")
        print(f"    官方: {s['official_name']}")
