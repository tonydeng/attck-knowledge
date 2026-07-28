#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATT&CK 知识库内容同步脚本

功能：
1. 遍历外部知识库 15 个战术目录下的所有 .md 文件
2. 剥离 YAML frontmatter（--- 包裹的头部）
3. 覆盖到 src/ 对应路径
4. 跳过 README.md、_data/、_tools/、模板文件
5. 报告 src/ 中存在但外部不存在的文件（删除候选）

用法：
    python scripts/sync-content.py
"""

import os
import re
import shutil
from pathlib import Path

# 路径配置
EXTERNAL_ROOT = Path(r"F:\user-requ\ATTCK知识库\知识库")
SRC_ROOT = Path(r"D:\workspace\github\attck-knowledge\src")

# 跳过的顶层目录（非战术目录）
SKIP_DIRS = {"_data", "_tools"}

# 跳过的文件名
SKIP_FILES = {"README.md", "SUMMARY.md"}

# 模板文件特征（文件名包含 template）
TEMPLATE_PATTERN = re.compile(r"template", re.IGNORECASE)


def strip_yaml_frontmatter(content: str) -> str:
    """剥离 YAML frontmatter（文件开头的 --- ... --- 块）"""
    # 仅处理文件开头的 frontmatter
    if not content.startswith("---"):
        return content

    # 找第二个 --- 的位置（frontmatter 结束标记）
    # 跳过第一行 ---，从第二行开始搜索
    second_delimiter = content.find("\n---", 3)
    if second_delimiter == -1:
        # 没有结束标记，不处理
        return content

    # frontmatter 结束后可能有 \n 或 \r\n
    after_frontmatter = content[second_delimiter + 4:]  # 跳过 \n---
    # 去除开头的换行符
    after_frontmatter = after_frontmatter.lstrip("\r\n")

    return after_frontmatter


def is_template_file(filepath: Path) -> bool:
    """判断是否为模板文件"""
    name = filepath.name
    # 文件名含 template
    if TEMPLATE_PATTERN.search(name):
        return True
    # 路径中含 _data 或 _tools
    parts = filepath.parts
    for part in parts:
        if part in SKIP_DIRS:
            return True
    return False


def collect_external_files() -> dict:
    """收集外部知识库中所有需要同步的 .md 文件

    返回：{相对路径（相对外部根目录）: 绝对路径}
    """
    external_files = {}

    for root, dirs, files in os.walk(EXTERNAL_ROOT):
        # 跳过 _data 和 _tools 目录
        rel_root = Path(root).relative_to(EXTERNAL_ROOT)
        parts = rel_root.parts
        if parts and parts[0] in SKIP_DIRS:
            # 清空 dirs 防止继续遍历
            dirs[:] = []
            continue

        for fname in files:
            if not fname.endswith(".md"):
                continue
            if fname in SKIP_FILES:
                continue

            abs_path = Path(root) / fname
            if is_template_file(abs_path):
                print(f"  [SKIP-TEMPLATE] {abs_path}")
                continue

            rel_path = abs_path.relative_to(EXTERNAL_ROOT)
            external_files[str(rel_path).replace("\\", "/")] = abs_path

    return external_files


def collect_src_files() -> dict:
    """收集 src/ 中所有现有的 .md 文件（排除 SUMMARY.md）

    返回：{相对路径（相对 src/）: 绝对路径}
    """
    src_files = {}

    for root, dirs, files in os.walk(SRC_ROOT):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            if fname in SKIP_FILES:
                # README.md 和 SUMMARY.md 跳过
                continue

            abs_path = Path(root) / fname
            rel_path = abs_path.relative_to(SRC_ROOT)
            src_files[str(rel_path).replace("\\", "/")] = abs_path

    return src_files


def sync_file(external_path: Path, src_path: Path) -> tuple:
    """同步单个文件：剥离 frontmatter 并写入 src/

    返回：(状态, 原始大小, 同步后大小)
    状态：'updated'（已存在并覆盖）、'new'（新增）、'error'
    """
    try:
        # 读取外部文件
        with open(external_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_size = len(content.encode("utf-8"))

        # 剥离 frontmatter
        stripped_content = strip_yaml_frontmatter(content)

        # 确保目标目录存在
        src_path.parent.mkdir(parents=True, exist_ok=True)

        # 判断是新增还是覆盖
        is_new = not src_path.exists()

        # 写入 src/
        with open(src_path, "w", encoding="utf-8") as f:
            f.write(stripped_content)

        new_size = len(stripped_content.encode("utf-8"))
        status = "new" if is_new else "updated"
        return (status, original_size, new_size)

    except Exception as e:
        return ("error", 0, 0)


def main():
    print("=" * 70)
    print("ATT&CK 知识库内容同步")
    print(f"外部源: {EXTERNAL_ROOT}")
    print(f"目标:   {SRC_ROOT}")
    print("=" * 70)

    # 收集文件
    print("\n[1/4] 收集外部知识库文件...")
    external_files = collect_external_files()
    print(f"  外部需同步文件: {len(external_files)} 个")

    print("\n[2/4] 收集当前 src/ 文件...")
    src_files = collect_src_files()
    print(f"  当前 src/ 文件: {len(src_files)} 个（排除 README.md/SUMMARY.md）")

    # 执行同步
    print("\n[3/4] 同步文件（剥离 frontmatter）...")
    stats = {"new": 0, "updated": 0, "error": 0}
    errors = []

    for rel_path, external_path in external_files.items():
        src_path = SRC_ROOT / rel_path
        status, orig_size, new_size = sync_file(external_path, src_path)

        stats[status] = stats.get(status, 0) + 1

        if status == "error":
            errors.append((rel_path, external_path))
        elif status == "new":
            print(f"  [NEW] {rel_path} ({new_size} bytes)")

    print(f"\n  同步完成:")
    print(f"    新增: {stats['new']} 个")
    print(f"    覆盖: {stats['updated']} 个")
    print(f"    错误: {stats['error']} 个")

    if errors:
        print("\n  错误详情:")
        for rel_path, ext_path in errors:
            print(f"    {rel_path} <- {ext_path}")

    # 识别删除候选（src/ 有但外部没有的）
    print("\n[4/4] 识别删除候选（src/ 有但外部没有的文件）...")
    external_rel_set = set(external_files.keys())
    src_rel_set = set(src_files.keys())
    delete_candidates = src_rel_set - external_rel_set

    if delete_candidates:
        print(f"  发现 {len(delete_candidates)} 个删除候选:")
        for rel_path in sorted(delete_candidates):
            abs_path = src_files[rel_path]
            size = abs_path.stat().st_size
            print(f"    [DELETE] {rel_path} ({size} bytes)")
        print(f"\n  注意：这些文件未自动删除，请手动确认后执行删除。")
        print(f"  删除命令示例：")
        for rel_path in sorted(delete_candidates):
            abs_path = src_files[rel_path]
            print(f"    Remove-Item -LiteralPath \"{abs_path}\"")
    else:
        print("  无删除候选")

    print("\n" + "=" * 70)
    print("同步完成")
    print("=" * 70)


if __name__ == "__main__":
    main()
