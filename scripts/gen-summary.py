#!/usr/bin/env python3
"""
Generate SUMMARY.md for ATT&CK Knowledge Base with Chinese technique names.
Reads YAML front matter and/or H1 heading from each technique file to extract Chinese names.
Also indexes sub-techniques from TXXXX/ subdirectories.
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


def get_h1_title(filepath):
    """Extract the first H1 title (# Title) from a markdown file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# ") and not line.startswith("## "):
                    return line[2:].strip()
    except Exception:
        return None
    return None


def get_technique_name(filepath, tech_id):
    """Get Chinese name for a technique from its YAML front matter or H1 title."""
    fields = parse_yaml_front_matter(filepath)
    cn_name = fields.get("attack_name_cn", "")
    if cn_name:
        return f"{tech_id} {cn_name}"

    # Fallback: extract from H1 title (e.g. "# 收集受害者身份信息 (T1589)" -> "收集受害者身份信息")
    h1 = get_h1_title(filepath)
    if h1:
        label = re.sub(r"\s*\(T\d+\)\s*$", "", h1).strip()
        if label:
            return f"{tech_id} {label}"

    return tech_id


def get_subtechnique_label(filepath, sub_tech_id):
    """Get label for a sub-technique: '描述 (TXXXX.XXX)' from its H1 title."""
    h1 = get_h1_title(filepath)
    if h1:
        # Remove the parenthesized ID from the title if present
        # e.g. "凭证收集 (T1589.001)" -> "凭证收集"
        label = re.sub(r"\s*\(T\d+\.\d+\)\s*$", "", h1).strip()
        if not label:
            label = re.sub(r"\s*\(T\d+\.\d+\)\s*", "", h1).strip()
        if label:
            return f"{label} ({sub_tech_id})"

    # Fallback: parse from YAML front matter
    fields = parse_yaml_front_matter(filepath)
    attack_name = fields.get("attack_name_cn", "")
    if attack_name:
        return f"{attack_name} ({sub_tech_id})"

    # Last resort: extract from filename
    name_part = re.sub(r"^T\d+\.\d+-", "", os.path.splitext(os.path.basename(filepath))[0])
    name_part = name_part.replace("-", " ")
    return f"{name_part} ({sub_tech_id})"


def url_encode_spaces(url):
    """Replace spaces with %20 in URLs for mdBook compatibility."""
    return url.replace(" ", "%20")


def deduplicate_sub_files(sub_files):
    """Deduplicate sub-technique files by sub_tech_id, preferring hyphenated names over spaces."""
    groups = {}  # sub_id -> best file
    for sf in sub_files:
        m = re.match(r"(T\d+\.\d+)", sf)
        if not m:
            continue
        sub_id = m.group(1)
        if sub_id not in groups:
            groups[sub_id] = sf
        else:
            # Prefer the file without spaces (hyphenated version)
            existing = groups[sub_id]
            if " " in existing and " " not in sf:
                groups[sub_id] = sf
            # If current has no spaces and existing has spaces, keep current
            # (already handled by the condition above)
    # Return sorted by sub_id
    return [groups[sub_id] for sub_id in sorted(groups.keys())]


def find_subtechniques(dirpath, tactic_dir, tech_id):
    """Find sub-technique files in a TXXXX/ subdirectory and return formatted lines."""
    sub_dir = os.path.join(dirpath, tech_id)
    if not os.path.isdir(sub_dir):
        return []

    sub_files = sorted(
        f for f in os.listdir(sub_dir)
        if f.endswith(".md") and re.match(r"T\d+\.\d+-", f)
    )

    # Deduplicate: prefer hyphenated names over spaces
    sub_files = deduplicate_sub_files(sub_files)

    lines = []
    for sf in sub_files:
        sub_match = re.match(r"(T\d+\.\d+)", sf)
        if not sub_match:
            continue
        sub_id = sub_match.group(1)
        full_path = os.path.join(sub_dir, sf)
        label = get_subtechnique_label(full_path, sub_id)
        link = url_encode_spaces(f"{tactic_dir}/{tech_id}/{sf}")
        lines.append(f"    - [{label}]({link})")

    return lines


def main():
    lines = ["# ATT&CK 知识库", "", "[简介](README.md)", ""]

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

        # Technique entries with Chinese names, deduplicated by TID
        tech_files = sorted(
            f for f in os.listdir(dirpath)
            if f.endswith(".md") and f != "README.md"
        )

        # Deduplicate: group by tech_id, prefer file without spaces
        tech_groups = {}
        for tf in tech_files:
            m = re.match(r"(T\d+)", tf)
            if not m:
                continue
            tid = m.group(1)
            if tid not in tech_groups:
                tech_groups[tid] = tf
            else:
                existing = tech_groups[tid]
                if " " in existing and " " not in tf:
                    tech_groups[tid] = tf

        # Track which TIDs we've already processed for sub-techniques
        processed_tids = set()

        for tf in tech_files:
            tech_id_match = re.match(r"(T\d+)", tf)
            if tech_id_match:
                tech_id = tech_id_match.group(1)

                # Skip duplicate techniques (already have a preferred file for this TID)
                if tf != tech_groups.get(tech_id):
                    continue

                full_path = os.path.join(dirpath, tf)
                label = get_technique_name(full_path, tech_id)
                link = url_encode_spaces(f"{d}/{tf}")
                lines.append(f"  - [{label}]({link})")

                # Find and add sub-techniques for this technique (once per TID)
                if tech_id not in processed_tids:
                    processed_tids.add(tech_id)
                    sub_lines = find_subtechniques(dirpath, d, tech_id)
                    lines.extend(sub_lines)
            else:
                lines.append(f"  - [{tf}]({d}/{tf})")

        lines.append("")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # Count results
    tech_count = sum(1 for l in lines if l.strip().startswith("- [T"))
    sub_count = sum(1 for l in lines if l.strip().startswith("- [") and re.match(r".*\(T\d+\.\d+\)", l))
    print(f"SUMMARY.md generated: {len(lines)} lines")
    print(f"  Technique entries: {tech_count}")
    print(f"  Sub-technique entries: {sub_count}")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()
