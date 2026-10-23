#!/usr/bin/env python3
"""
Check that every relative Markdown link under src/ resolves to an existing
file or directory. External links (http/https/mailto) and pure anchors are
skipped. Exits 1 with a report when broken links are found.
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_pos = [a for a in sys.argv[1:] if not a.startswith("-")]
SRC_DIR = os.path.abspath(_pos[0]) if _pos else os.path.join(
    os.path.dirname(SCRIPT_DIR), "src"
)

EXCLUDE_DIRS = {"_data", "_tools"}
BASELINE_FILE = os.path.join(SRC_DIR, "_data", "broken-links-baseline.txt")
MD_LINK_RE = re.compile(r"\]\(([^)\s]+[^)]*?)\)")
EXTERNAL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def link_key(rel_path, target):
    return f"{rel_path} -> {target}"


def load_baseline():
    if not os.path.exists(BASELINE_FILE):
        return set()
    with open(BASELINE_FILE, "r", encoding="utf-8") as f:
        return {line.rstrip("\n") for line in f if line.strip()}


def main():
    errors = []
    checked = 0

    for dirpath, dirnames, filenames in os.walk(SRC_DIR):
        dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_DIRS)
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
            except Exception as e:
                errors.append(f"{path}: unreadable ({e})")
                continue

            for m in MD_LINK_RE.finditer(text):
                target = m.group(1).strip()
                if not target or EXTERNAL_RE.match(target):
                    continue
                # Strip anchor / query, decode URL-encoded spaces
                target = target.split("#", 1)[0].split("?", 1)[0]
                if not target:
                    continue
                target = target.replace("%20", " ").replace("%22", '"')
                checked += 1
                resolved = os.path.normpath(os.path.join(dirpath, target))
                if not os.path.exists(resolved):
                    errors.append(
                        link_key(os.path.relpath(path, SRC_DIR), m.group(1))
                    )

    baseline = load_baseline()
    new_broken = [e for e in errors if e not in baseline]
    known = [e for e in errors if e in baseline]
    stale = [b for b in baseline if b not in set(errors)]

    if "--write-baseline" in sys.argv:
        os.makedirs(os.path.dirname(BASELINE_FILE), exist_ok=True)
        with open(BASELINE_FILE, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(sorted(errors)) + ("\n" if errors else ""))
        print(f"Baseline written: {BASELINE_FILE} ({len(errors)} entries)")
        return

    print(f"Checked {checked} internal links under src/")
    if known:
        print(f"{len(known)} known broken link(s) tracked in baseline (debt)")
    if stale:
        print(f"{len(stale)} baseline entry/entries no longer broken (clean up: {os.path.relpath(BASELINE_FILE, SRC_DIR)})")
    if new_broken:
        print(f"\n{len(new_broken)} NEW BROKEN LINK(S):")
        for e in new_broken:
            print(f"  {e}")
        sys.exit(1)
    if not errors:
        print("All internal links OK")
    else:
        print("No new broken links (baseline debt remains)")


if __name__ == "__main__":
    main()
