#!/usr/bin/env python3
"""
Generate SUMMARY.md for the ATT&CK & ATLAS Knowledge Base with Chinese technique names.
Walks both matrix namespaces (src/enterprise/, src/atlas/) and the ATLAS case-study folder.
Reads H1 headings from each technique file to extract Chinese names.
Also indexes sub-techniques from TXXXX/ or AML.TXXXX/ subdirectories.
ATLAS sections are emitted only when the corresponding directories exist.
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

# ATLAS tactic display names, filled per official ATLAS matrix sequence.
# Keyed by the two-digit folder prefix of src/atlas/NN-*/ directories.
# 顺序依据 ATLAS-2026.09.yaml 的 ATLAS-matrix sequences 关系（position 1-16）。
ATLAS_TACTIC_NAMES = {
    "01": ("侦察", "AML.TA0002"),
    "02": ("资源开发", "AML.TA0003"),
    "03": ("AI 攻击适配", "AML.TA0001"),
    "04": ("初始访问", "AML.TA0004"),
    "05": ("AI 模型访问", "AML.TA0000"),
    "06": ("执行", "AML.TA0005"),
    "07": ("持久化", "AML.TA0006"),
    "08": ("权限提升", "AML.TA0012"),
    "09": ("防御规避", "AML.TA0007"),
    "10": ("凭证访问", "AML.TA0013"),
    "11": ("发现", "AML.TA0008"),
    "12": ("横向移动", "AML.TA0015"),
    "13": ("收集", "AML.TA0009"),
    "14": ("命令与控制", "AML.TA0014"),
    "15": ("数据渗漏", "AML.TA0010"),
    "16": ("影响", "AML.TA0011"),
}

# Matrix namespaces: (folder, section title, tactic-name map)
NAMESPACES = [
    ("enterprise", "ATT&CK Enterprise", TACTIC_NAMES),
    ("atlas", "MITRE ATLAS", ATLAS_TACTIC_NAMES),
]

# IDs: T1589 / T1589.001 (Enterprise) and AML.T0051 / AML.T0051.001 (ATLAS)
TECH_ID_RE = re.compile(r"((?:AML\.)?T\d+)$")
SUB_ID_RE = re.compile(r"((?:AML\.)?T\d+\.\d+)$")
H1_ID_RE = re.compile(r"\s*\((?:AML\.)?T\d+(?:\.\d+)?\)\s*$")


def parse_yaml_front_matter(filepath):
    """Extract YAML front matter fields from a markdown file."""
    fields = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return fields

    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not m:
        return fields

    for line in m.group(1).split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip('"').strip("'")

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


def strip_id_from_h1(h1):
    """Remove a trailing ' (TXXXX)' or ' (AML.TXXXX)' from an H1 label."""
    if not h1:
        return None
    return H1_ID_RE.sub("", h1).strip() or None


def get_technique_name(filepath, tech_id):
    """Get Chinese name for a technique from its YAML front matter or H1 title."""
    fields = parse_yaml_front_matter(filepath)
    cn_name = fields.get("attack_name_cn", "")
    if cn_name:
        return f"{tech_id} {cn_name}"

    label = strip_id_from_h1(get_h1_title(filepath))
    if label:
        return f"{tech_id} {label}"

    return tech_id


def get_subtechnique_label(filepath, sub_tech_id):
    """Get label for a sub-technique: '描述 (TXXXX.XXX)' from its H1 title."""
    label = strip_id_from_h1(get_h1_title(filepath))
    if label:
        return f"{label} ({sub_tech_id})"

    fields = parse_yaml_front_matter(filepath)
    cn_name = fields.get("attack_name_cn", "")
    if cn_name:
        return f"{cn_name} ({sub_tech_id})"

    name_part = re.sub(r"^(?:AML\.)?T\d+\.\d+-", "", os.path.splitext(os.path.basename(filepath))[0])
    return f"{name_part.replace('-', ' ')} ({sub_tech_id})"


def url_encode_spaces(url):
    """Replace spaces with %20 in URLs for mdBook compatibility."""
    return url.replace(" ", "%20")


def deduplicate_sub_files(sub_files):
    """Deduplicate sub-technique files by sub_tech_id, preferring hyphenated names over spaces."""
    groups = {}
    for sf in sub_files:
        m = re.match(r"((?:AML\.)?T\d+\.\d+)", sf)
        if not m:
            continue
        sub_id = m.group(1)
        if sub_id not in groups:
            groups[sub_id] = sf
        elif " " in groups[sub_id] and " " not in sf:
            groups[sub_id] = sf
    return [groups[sub_id] for sub_id in sorted(groups.keys())]


def find_subtechniques(dirpath, tactic_dir, tech_id):
    """Find sub-technique files in a TXXXX/ or AML.TXXXX/ subdirectory and return formatted lines."""
    sub_dir = os.path.join(dirpath, tech_id)
    if not os.path.isdir(sub_dir):
        return []

    sub_files = sorted(
        f for f in os.listdir(sub_dir)
        if f.endswith(".md") and re.match(r"(?:AML\.)?T\d+\.\d+-", f)
    )
    sub_files = deduplicate_sub_files(sub_files)

    lines = []
    for sf in sub_files:
        sub_match = re.match(r"((?:AML\.)?T\d+\.\d+)", sf)
        if not sub_match:
            continue
        sub_id = sub_match.group(1)
        full_path = os.path.join(sub_dir, sf)
        label = get_subtechnique_label(full_path, sub_id)
        link = url_encode_spaces(f"{tactic_dir}/{tech_id}/{sf}")
        lines.append(f"    - [{label}]({link})")

    return lines


def emit_namespace(lines, ns_folder, section_title, tactic_names):
    """Append SUMMARY lines for one matrix namespace. Returns None if the folder is absent."""
    ns_dir = os.path.join(SRC_DIR, ns_folder)
    if not os.path.isdir(ns_dir):
        return

    lines.append("")
    lines.append(f"# {section_title}")

    dirs = sorted(d for d in os.listdir(ns_dir) if re.match(r"^\d{2}-", d) and os.path.isdir(os.path.join(ns_dir, d)))

    for d in dirs:
        num = d[:2]
        tac_name, tac_id = tactic_names.get(num, (d, ""))
        dirpath = os.path.join(ns_dir, d)
        tactic_dir = f"{ns_folder}/{d}"

        if tac_id:
            lines.append(f"- [{num} {tac_name} ({tac_id})]({tactic_dir}/README.md)")
        else:
            lines.append(f"- [{num} {tac_name}]({tactic_dir}/README.md)")

        tech_files = sorted(
            f for f in os.listdir(dirpath)
            if f.endswith(".md") and f != "README.md" and f != "MAPPING.md"
        )

        # Deduplicate: group by tech_id, prefer file without spaces
        tech_groups = {}
        for tf in tech_files:
            m = re.match(r"((?:AML\.)?T\d+)", tf)
            if not m:
                continue
            tid = m.group(1)
            if tid not in tech_groups:
                tech_groups[tid] = tf
            elif " " in tech_groups[tid] and " " not in tf:
                tech_groups[tid] = tf

        processed_tids = set()

        for tf in tech_files:
            tech_id_match = re.match(r"((?:AML\.)?T\d+)", tf)
            if tech_id_match:
                tech_id = tech_id_match.group(1)

                if tf != tech_groups.get(tech_id):
                    continue

                full_path = os.path.join(dirpath, tf)
                label = get_technique_name(full_path, tech_id)
                link = url_encode_spaces(f"{tactic_dir}/{tf}")
                lines.append(f"  - [{label}]({link})")

                if tech_id not in processed_tids:
                    processed_tids.add(tech_id)
                    lines.extend(find_subtechniques(dirpath, tactic_dir, tech_id))
            else:
                lines.append(f"  - [{tf}]({tactic_dir}/{tf})")

        lines.append("")


def emit_case_studies(lines):
    """Append SUMMARY lines for the ATLAS case-study folder, if present."""
    cs_dir = os.path.join(SRC_DIR, "atlas", "case-studies")
    if not os.path.isdir(cs_dir):
        return

    files = sorted(f for f in os.listdir(cs_dir) if f.endswith(".md") and f != "README.md" and re.match(r"AML\.CS\d+-", f))
    if not files:
        return

    lines.append("")
    lines.append("# ATLAS 案例研究")

    for cf in files:
        cs_id = re.match(r"(AML\.CS\d+)", cf).group(1)
        full_path = os.path.join(cs_dir, cf)
        label = strip_id_from_h1(get_h1_title(full_path)) or cf
        link = url_encode_spaces(f"atlas/case-studies/{cf}")
        lines.append(f"- [{label} ({cs_id})]({link})")

    lines.append("")


def main():
    lines = ["# ATT&CK & ATLAS 知识库", "", "[简介](README.md)", ""]

    for ns_folder, section_title, tactic_names in NAMESPACES:
        emit_namespace(lines, ns_folder, section_title, tactic_names)

    emit_case_studies(lines)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    tech_count = sum(1 for l in lines if l.strip().startswith("- [") and re.match(r".*\[(?:AML\.)?T\d+ ", l))
    sub_count = sum(1 for l in lines if l.strip().startswith("- [") and re.search(r"\((?:AML\.)?T\d+\.\d+\)", l))
    print(f"SUMMARY.md generated: {len(lines)} lines")
    print(f"  Technique entries: {tech_count}")
    print(f"  Sub-technique entries: {sub_count}")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()
