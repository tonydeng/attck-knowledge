"""生成 ATT&CK 知识库与官方 v19.1 的逐 TID 差异审计报告。

LOCAL schema:
  {"01-Reconnaissance": {
     "tactic_dir": "...", "parent_count": N, "subtech_count": N,
     "parents": [{"attack_id": "T1589", "attack_name_en": "...", "attack_name_cn": "...", "tactic_id": "TA0043", ...}],
     "subtechs": [{"attack_id": "T1589.001", "attack_name_en": "...", ...}]
  }}

OFFICIAL schema:
  {"TA0043": {
     "tactic_id": "TA0043", "tactic_name_en": "Reconnaissance",
     "parent_techniques": [{"id": "T1595", "name_en": "Active Scanning",
       "subtechniques": [{"id": "T1595.001", "name_en": "Scanning IP Blocks"}, ...]}]
  }}
"""

import json
from pathlib import Path
from collections import defaultdict

DATA_DIR = Path(__file__).resolve().parent.parent / "_data"
LOCAL = DATA_DIR / "_local_scan.json"
OFFICIAL = DATA_DIR / "_mitre_official.json"
OUT = DATA_DIR / "_audit_report.json"

DIR_TO_TA = {
    "01-Reconnaissance": "TA0043",
    "02-Resource-Development": "TA0042",
    "03-Initial-Access": "TA0001",
    "04-Execution": "TA0002",
    "05-Persistence": "TA0003",
    "06-Privilege-Escalation": "TA0004",
    "07-Stealth": "TA0005",
    "08-Defense-Impairment": "TA0112",
    "09-Credential-Access": "TA0006",
    "10-Discovery": "TA0007",
    "11-Lateral-Movement": "TA0008",
    "12-Collection": "TA0009",
    "13-Command-and-Control": "TA0011",
    "14-Exfiltration": "TA0010",
    "15-Impact": "TA0040",
}
TA_TO_DIR = {v: k for k, v in DIR_TO_TA.items()}


def load(p):
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def normalize_name(s):
    if not s:
        return ""
    return " ".join(str(s).strip().split()).lower()


def build_local_index(local):
    idx = defaultdict(lambda: {"parents": {}, "subs": {}})
    for dir_name, ta_data in local.items():
        ta_id = DIR_TO_TA.get(dir_name)
        if not ta_id:
            continue
        for p in ta_data.get("parents", []):
            tid = p.get("attack_id")
            if tid:
                idx[ta_id]["parents"][tid] = {
                    "name_en": p.get("attack_name_en", ""),
                    "name_cn": p.get("attack_name_cn", ""),
                    "file": p.get("file", ""),
                    "path": p.get("path", ""),
                }
        for s in ta_data.get("subtechs", []):
            tid = s.get("attack_id")
            if tid:
                idx[ta_id]["subs"][tid] = {
                    "name_en": s.get("attack_name_en", ""),
                    "name_cn": s.get("attack_name_cn", ""),
                    "file": s.get("file", ""),
                    "path": s.get("path", ""),
                }
    return idx


def build_official_index(official):
    idx = defaultdict(lambda: {"parents": {}, "subs": {}})
    for ta_id, ta_data in official.items():
        for p in ta_data.get("parent_techniques", []):
            pid = p.get("id")
            if pid:
                idx[ta_id]["parents"][pid] = {"name_en": p.get("name_en", "")}
            for s in p.get("subtechniques", []):
                sid = s.get("id")
                if sid:
                    idx[ta_id]["subs"][sid] = {
                        "name_en": s.get("name_en", ""),
                        "parent": pid,
                    }
    return idx


def diff_tactic(local_tac, official_tac):
    result = {
        "missing_parents": [],
        "extra_parents": [],
        "name_mismatch_parents": [],
        "missing_subs": [],
        "extra_subs": [],
        "name_mismatch_subs": [],
    }

    lp, op = local_tac["parents"], official_tac["parents"]
    for tid, o in op.items():
        if tid not in lp:
            result["missing_parents"].append({"tid": tid, "official_name": o["name_en"]})
        elif normalize_name(lp[tid]["name_en"]) != normalize_name(o["name_en"]):
            result["name_mismatch_parents"].append({
                "tid": tid,
                "local_name": lp[tid]["name_en"],
                "official_name": o["name_en"],
                "local_file": lp[tid]["file"],
            })
    for tid, l in lp.items():
        if tid not in op:
            result["extra_parents"].append({
                "tid": tid,
                "local_name": l["name_en"],
                "local_file": l["file"],
            })

    ls, os_ = local_tac["subs"], official_tac["subs"]
    for tid, o in os_.items():
        if tid not in ls:
            result["missing_subs"].append({"tid": tid, "official_name": o["name_en"], "parent": o.get("parent", "")})
        elif normalize_name(ls[tid]["name_en"]) != normalize_name(o["name_en"]):
            result["name_mismatch_subs"].append({
                "tid": tid,
                "local_name": ls[tid]["name_en"],
                "official_name": o["name_en"],
                "local_file": ls[tid]["file"],
            })
    for tid, l in ls.items():
        if tid not in os_:
            result["extra_subs"].append({
                "tid": tid,
                "local_name": l["name_en"],
                "local_file": l["file"],
            })

    return result


def main():
    local = load(LOCAL)
    official = load(OFFICIAL)
    local_idx = build_local_index(local)
    official_idx = build_official_index(official)

    report = {}
    totals = defaultdict(int)

    print("=" * 90)
    print(f"{'战术':<35} {'TA ID':<8} {'缺父':>4} {'多父':>4} {'名异父':>6} {'缺子':>4} {'多子':>4} {'名异子':>6}")
    print("=" * 90)

    for ta_id in DIR_TO_TA.values():
        local_tac = local_idx.get(ta_id, {"parents": {}, "subs": {}})
        official_tac = official_idx.get(ta_id, {"parents": {}, "subs": {}})
        d = diff_tactic(local_tac, official_tac)
        report[ta_id] = {
            "tactic_dir": TA_TO_DIR.get(ta_id, ""),
            "tactic_name_en": official.get(ta_id, {}).get("tactic_name_en", ""),
            "local_parent_count": len(local_tac["parents"]),
            "official_parent_count": len(official_tac["parents"]),
            "local_sub_count": len(local_tac["subs"]),
            "official_sub_count": len(official_tac["subs"]),
            "diff": d,
        }
        for k, v in d.items():
            totals[k] += len(v)
        name = official.get(ta_id, {}).get("tactic_name_en", "?")
        print(f"{name:<35} {ta_id:<8} {len(d['missing_parents']):>4} {len(d['extra_parents']):>4} "
              f"{len(d['name_mismatch_parents']):>6} {len(d['missing_subs']):>4} {len(d['extra_subs']):>4} "
              f"{len(d['name_mismatch_subs']):>6}")

    print("=" * 90)
    print(f"{'TOTAL':<35} {'':<8} {totals['missing_parents']:>4} {totals['extra_parents']:>4} "
          f"{totals['name_mismatch_parents']:>6} {totals['missing_subs']:>4} {totals['extra_subs']:>4} "
          f"{totals['name_mismatch_subs']:>6}")
    print()

    with OUT.open("w", encoding="utf-8") as f:
        json.dump({"totals": dict(totals), "tactics": report}, f, ensure_ascii=False, indent=2)
    print(f"详细报告已写入: {OUT}")


if __name__ == "__main__":
    main()
