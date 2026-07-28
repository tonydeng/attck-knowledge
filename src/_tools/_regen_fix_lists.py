"""从最新 _audit_report.json 重新生成 6 个修复清单 JSON。

审计报告结构：
  {
    "tactics": {
      "TA0043": {
        "tactic_dir": "01-Reconnaissance",
        "diff": {
          "missing_parents": [...],
          "extra_parents": [...],
          "name_mismatch_parents": [...],
          "missing_subs": [...],
          "extra_subs": [...],
          "name_mismatch_subs": [...]
        }
      },
      ...
    }
  }

每个 diff 条目原样保留字段，再补充 _tactic_id 和 _tactic_dir。
"""
import json
from pathlib import Path

BASE = Path(__file__).parent.parent
DATA = BASE / "_data"
FIX_DIR = DATA / "_fix_lists"
FIX_DIR.mkdir(parents=True, exist_ok=True)

report = json.loads((DATA / "_audit_report.json").read_text(encoding="utf-8"))

categories = [
    "missing_parents",
    "extra_parents",
    "name_mismatch_parents",
    "missing_subs",
    "extra_subs",
    "name_mismatch_subs",
]

totals = {c: 0 for c in categories}

for tactic_id, tactic_data in report["tactics"].items():
    tactic_dir = tactic_data.get("tactic_dir", "")
    diff = tactic_data.get("diff", {})
    for cat in categories:
        items = diff.get(cat, []) or []
        for item in items:
            # 补充定位字段
            item["_tactic_id"] = tactic_id
            item["_tactic_dir"] = tactic_dir
            # missing_subs 需要 parent 字段（父 TID）
            if cat == "missing_subs" and "parent" not in item:
                tid = item.get("tid", "")
                if "." in tid:
                    item["parent"] = tid.split(".")[0]
            totals[cat] += 1

# 按类别合并所有战术的条目
merged = {c: [] for c in categories}
for tactic_id, tactic_data in report["tactics"].items():
    diff = tactic_data.get("diff", {})
    for cat in categories:
        for item in diff.get(cat, []) or []:
            item_with_loc = dict(item)
            item_with_loc["_tactic_id"] = tactic_id
            item_with_loc["_tactic_dir"] = tactic_data.get("tactic_dir", "")
            if cat == "missing_subs" and "parent" not in item_with_loc:
                tid = item_with_loc.get("tid", "")
                if "." in tid:
                    item_with_loc["parent"] = tid.split(".")[0]
            merged[cat].append(item_with_loc)

# 写入 6 个 JSON
for cat in categories:
    out_path = FIX_DIR / f"{cat}.json"
    out_path.write_text(
        json.dumps(merged[cat], ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"  {cat}: {len(merged[cat])} 项 -> {out_path.name}")

print(f"\n[regen] 完成。汇总：")
for cat in categories:
    print(f"  {cat}: {len(merged[cat])}")
