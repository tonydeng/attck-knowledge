#!/usr/bin/env python3
"""
One-time script: Strip YAML front matter from all markdown files in src/.
Preserves original files via backup or direct edit.
"""

import os
import re
import sys

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")


def strip_yaml_from_file(filepath):
    """Remove YAML front matter (---...---) from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, count=1, flags=re.DOTALL)

    if new_content == content:
        return False  # No YAML found

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    stripped = 0
    total = 0

    for root, dirs, files in os.walk(SRC):
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            total += 1
            if strip_yaml_from_file(fpath):
                rel = os.path.relpath(fpath, SRC)
                print(f"  stripped: {rel}")
                stripped += 1

    print(f"\nProcessed {total} files, stripped YAML from {stripped} files")


if __name__ == "__main__":
    main()
