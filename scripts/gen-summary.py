#!/usr/bin/env python3
"""
Generate SUMMARY.md for ATT&CK Knowledge Base with Chinese technique names.
Reads YAML front matter from each technique file to extract Chinese names.
"""

import os
import re
import sys

SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
OUTPUT = os.path.join(SRC_DIR, "SUMMARY.md")

TACTIC_NAMES = {
    "01": ("侦察", "TA0043"),
    "02": ("资源开发", "TA0042"),
    "03": ("初始访问", "TA0001"),
    "04": ("执行", "TA0002"),
    "05": ("持久化", "TA0003"),
    "06": ("权限提升", "TA0004"),
    "07": ("隐蔽", "TA0005"),
    "08": ("防御削弱", "TA0112"),
    "09": ("凭证访问", "TA0006"),
    "10": ("发现", "TA0007"),
    "11": ("横向移动", "TA0008"),
    "12": ("收集", "TA0009"),
    "13": ("命令与控制", "TA0011"),
    "14": ("渗漏", "TA0010"),
    "15": ("影响", "TA0040"),
}

def parse_yaml_front_matter(filepath):
    """Extract YAML front matter fields from a markdown file."""
    fields = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return fields

    # Match content between opening --- and closing ---
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not m:
        return fields

    yaml_block = m.group(1)
    for line in yaml_block.split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            fields[key] = value

    return fields


def get_technique_name(filepath, tech_id):
    """Get Chinese name for a technique from its YAML front matter."""
    fields = parse_yaml_front_matter(filepath)
    cn_name = fields.get("attack_name_cn", "")
    if cn_name:
        return f"{tech_id} {cn_name}"
    return tech_id


def main():
    lines = ["# ATT&CK 知识库", "", "[简介](../README.md)", ""]

    dirs = sorted([d for d in os.listdir(SRC_DIR) if re.match(r"^\d{2}-", d)])

    for d in dirs:
        num = d[:2]
        tac_name, tac_id = TACTIC_NAMES.get(num, (d, ""))
        dirpath = os.path.join(SRC_DIR, d)

        # Chapter entry
        if tac_id:
            lines.append(f"- [{num} {tac_name} ({tac_id})]({d}/README.md)")
        else:
            lines.append(f"- [{num} {tac_name}]({d}/README.md)")

        # Technique entries with Chinese names
        tech_files = sorted(
            f for f in os.listdir(dirpath)
            if f.endswith(".md") and f != "README.md"
        )

        for tf in tech_files:
            tech_id_match = re.match(r"(T\d+)", tf)
            if tech_id_match:
                tech_id = tech_id_match.group(1)
                full_path = os.path.join(dirpath, tf)
                label = get_technique_name(full_path, tech_id)
                lines.append(f"  - [{label}]({d}/{tf})")
            else:
                lines.append(f"  - [{tf}]({d}/{tf})")

        lines.append("")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # Count results
    tech_count = sum(1 for l in lines if l.strip().startswith("- [T"))
    print(f"SUMMARY.md generated: {len(lines)} lines, {tech_count} technique entries")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()
