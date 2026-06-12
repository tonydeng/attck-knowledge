#!/usr/bin/env python3
"""
preprocess-md.py - Markdown 预处理脚本

在 mdbook build 之前执行，自动修正所有 README.md 中的链接兼容性问题。

修正内容：
1. README.md 链接修正 → ./XX-Tactic/README.md 改为 ./XX-Tactic/（mdbook 兼容）
2. 技战术 ID 链接补全 → T#### 添加指向对应 .md 文档的超链接

用法:
    python scripts/preprocess-md.py          # 处理所有 README.md
    python scripts/preprocess-md.py --check  # 仅检查，不修改

集成到 mdbook 构建:
    mdbook build 前执行: python scripts/preprocess-md.py
"""

import os
import re
import sys

SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")


def find_technique_files(tactic_dir):
    """返回该战术目录下的 { T####: filename } 映射"""
    tech_map = {}
    tactic_path = os.path.join(SRC_DIR, tactic_dir)
    if not os.path.isdir(tactic_path):
        return tech_map
    for fname in os.listdir(tactic_path):
        if not fname.endswith(".md") or fname == "README.md":
            continue
        m = re.match(r"(T\d{4})", fname)
        if m:
            tid = m.group(1)
            if tid not in tech_map:
                tech_map[tid] = fname
    return tech_map


def fix_readme_links(text):
    """
    修正 README.md 链接：
    ./XX-Tactic/README.md → ./XX-Tactic/
    ../XX-Tactic/README.md → ../XX-Tactic/
    """
    return re.sub(r"(\.\.?/[^)\s]+)/README\.md", r"\1/", text)


def _protect_links_and_code(text):
    """
    将受保护区域（代码块、行内代码、已有 T#### 链接）替换为占位符。
    返回 (processed_text, placeholders: [(placeholder, original), ...])
    """
    placeholders = []
    counter = [0]

    def _replace(m):
        counter[0] += 1
        ph = f"\x00PH{counter[0]}\x00"
        placeholders.append((ph, m.group(0)))
        return ph

    # 1. 保护代码块 ```...```
    # 注意: MULTILINE 使 ^ 匹配行首，DOTALL 使 . 匹配换行
    text = re.sub(r"^```.*?^```", _replace, text, flags=re.MULTILINE | re.DOTALL)
    # 2. 保护行内代码 `...`
    text = re.sub(r"`[^`]+`", _replace, text)
    # 3. 保护已有 markdown 链接中含 T#### 的
    text = re.sub(
        r"\[([^\]]*T\d{4}[^\]]*)\]\([^)]*\)"
        r"|\[[^\]]*\]\([^)]*T\d{4}[^)]*\)",
        _replace,
        text,
    )
    return text, placeholders


def _restore(text, placeholders):
    for ph, orig in placeholders:
        text = text.replace(ph, orig)
    return text


def add_technique_links(text, tech_map):
    """
    为文本中的 T#### 添加超链接。
    tech_map: { T####: filename.md }
    策略：先保护已有链接/代码，再用 re.sub 全局替换裸 T####。
    """
    if not tech_map:
        return text

    # 1. 保护已有区域
    text, placeholders = _protect_links_and_code(text)

    # 2. 按 T#### 长度降序替换（避免 T100 和 T1003 冲突）
    tids = sorted(tech_map.keys(), key=lambda x: -len(x))
    for tid in tids:
        filename = tech_map[tid]
        pattern = re.compile(r"(?<!A)" + re.escape(tid))
        text = pattern.sub(f"[{tid}]({filename})", text)

    # 3. 恢复受保护区域
    text = _restore(text, placeholders)
    return text


def process_readme(filepath, tech_map, dry_run=False):
    """处理单个 README.md 文件，返回是否被修改。"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    content = fix_readme_links(content)
    content = add_technique_links(content, tech_map)

    if content == original:
        return False

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return True


def main():
    dry_run = "--check" in sys.argv

    # 1. 收集每个战术目录下的技术文件映射
    tactic_maps = {}
    for entry in sorted(os.listdir(SRC_DIR)):
        entry_path = os.path.join(SRC_DIR, entry)
        if os.path.isdir(entry_path) and re.match(r"\d{2}-", entry):
            tactic_maps[entry] = find_technique_files(entry)

    # 2. 构建 src/README.md 的全局映射（含相对路径前缀）
    all_tech_map = {}
    for tactic_dir, tech_map in tactic_maps.items():
        for tid, fname in tech_map.items():
            if tid not in all_tech_map:
                all_tech_map[tid] = f"{tactic_dir}/{fname}"

    total_changed = 0

    # 3. 处理 src/README.md
    src_readme = os.path.join(SRC_DIR, "README.md")
    if os.path.exists(src_readme):
        print(f"Processing: src/README.md")
        if process_readme(src_readme, all_tech_map, dry_run):
            total_changed += 1

    # 4. 处理每个战术目录下的 README.md
    for tactic_dir in sorted(tactic_maps.keys()):
        readme_path = os.path.join(SRC_DIR, tactic_dir, "README.md")
        if not os.path.exists(readme_path):
            continue
        tech_map = tactic_maps[tactic_dir]
        print(f"Processing: {tactic_dir}/README.md ({len(tech_map)} techs)")
        if process_readme(readme_path, tech_map, dry_run):
            total_changed += 1

    mode = " (dry-run)" if dry_run else ""
    print(f"\nResult: {total_changed} file(s) modified{mode}")


if __name__ == "__main__":
    main()
