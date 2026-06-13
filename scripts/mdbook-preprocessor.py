#!/usr/bin/env python3
"""
mdBook Preprocessor - ATT&CK 知识库预处理

在 mdbook build/serve 时自动执行以下 Python 脚本：
  1. gen-summary.py   — 根据文件结构自动生成 SUMMARY.md
  2. preprocess-md.py — 修正 README.md 中的链接兼容性问题

用法 (由 book.toml 自动调用):
    mdbook build     # 自动触发本预处理器
    mdbook serve     # 自动触发本预处理器

本脚本遵循 mdBook 预处理器协议：
  - 参数 supports <renderer> → 退出码 0 (支持所有渲染器)
  - 无参数 → 读取 stdin 的 book JSON, 运行脚本, 原样输出 book JSON
"""

import json
import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    # ── mdBook 预处理器协议：supports 检查 ──
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        # 支持所有渲染器 (html, pdf, ...)
        sys.exit(0)

    # ── 运行预处理脚本 ──
    scripts = [
        ("gen-summary.py", "生成 SUMMARY.md"),
        ("preprocess-md.py", "修正 README.md 链接"),
    ]

    for script_name, description in scripts:
        script_path = os.path.join(SCRIPT_DIR, script_name)
        if not os.path.isfile(script_path):
            print(f"[preprocessor] 跳过 (文件不存在): {script_name}", file=sys.stderr)
            continue

        try:
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                check=True,
            )
            # 输出脚本自身的 stdout
            for line in result.stdout.strip().split("\n"):
                if line.strip():
                    print(f"[preprocessor:{script_name}] {line}", file=sys.stderr)
        except subprocess.CalledProcessError as e:
            print(
                f"[preprocessor] 错误: {script_name} 执行失败 (exit={e.returncode})",
                file=sys.stderr,
            )
            if e.stderr:
                print(e.stderr, file=sys.stderr)
            sys.exit(1)

    # ── 原样传 pass book JSON ──
    book = json.load(sys.stdin)
    json.dump(book, sys.stdout)


if __name__ == "__main__":
    main()
