#!/usr/bin/env python3
"""
One-shot repair for broken relative links surfaced by check-links.py.

Strategy: technique IDs (T#### / AML.T#### / T####.NNN) are stable anchors
across content revisions, while file names and tactic folders changed in the
v19.1 reorganization. For every broken link whose target basename carries a
technique ID, re-point it to an existing file with the same ID, preferring:
  1. the directory the link intended (if it holds a file with that ID)
  2. the source file's own tactic folder
  3. a globally unique file with that ID (flag if ambiguous)
Links without an ID, or with no candidate file, are reported as unresolved.

Default is dry-run; pass --apply to write changes.
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("-") \
    else os.path.join(os.path.dirname(SCRIPT_DIR), "src")
APPLY = "--apply" in sys.argv

EXCLUDE_DIRS = {"_data", "_tools"}
MD_LINK_RE = re.compile(r"\]\(([^)]+?)\)")
EXTERNAL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
ID_PREFIX_RE = re.compile(r"^((?:AML\.)?T\d+(?:\.\d+)?)")


def tactic_root(path):
    """Return the tactic folder portion ('enterprise/07-Stealth') of a file path, or None."""
    rel = os.path.relpath(path, SRC_DIR)
    parts = rel.replace("\\", "/").split("/")
    if len(parts) >= 3 and parts[0] in ("enterprise", "atlas") and re.match(r"^\d{2}-", parts[1]):
        return (parts[0], parts[1])
    if len(parts) >= 2 and re.match(r"^\d{2}-", parts[0]):
        return ("", parts[0])
    return None


def build_id_index(files):
    index = {}
    for f in files:
        m = ID_PREFIX_RE.match(os.path.basename(f))
        if m:
            index.setdefault(m.group(1), []).append(f)
    return index


def collect_md_files():
    files = []
    for dirpath, dirnames, filenames in os.walk(SRC_DIR):
        dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_DIRS)
        for fn in sorted(filenames):
            if fn.endswith(".md"):
                files.append(os.path.join(dirpath, fn))
    return files


def main():
    files = collect_md_files()
    id_index = build_id_index(files)

    fixed = 0
    unresolved = []
    ambiguous = []

    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        if "](" not in text:
            continue

        src_tactic = tactic_root(path)
        changes = {}

        for m in MD_LINK_RE.finditer(text):
            raw = m.group(1).strip()
            if not raw or EXTERNAL_RE.match(raw):
                continue
            target = raw.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(path), target.replace("%20", " ")))
            if os.path.exists(resolved):
                continue  # not broken

            basename = os.path.basename(target.replace("%20", " "))
            idm = ID_PREFIX_RE.match(basename)
            if not idm:
                unresolved.append(f"{os.path.relpath(path, SRC_DIR)} -> {raw} (no technique ID)")
                continue
            tech_id = idm.group(1)
            candidates = id_index.get(tech_id, [])
            if not candidates:
                unresolved.append(f"{os.path.relpath(path, SRC_DIR)} -> {raw} (no file with ID {tech_id})")
                continue

            intended_dir = os.path.dirname(resolved)
            pick = None
            # 1. intended directory holds a file with this ID
            for c in candidates:
                if os.path.dirname(c) == intended_dir:
                    pick = c
                    break
            # 2. source file's own tactic folder
            if pick is None and src_tactic:
                for c in candidates:
                    if tactic_root(c) == src_tactic:
                        pick = c
                        break
            # 3. unique global, else first (flag ambiguity)
            if pick is None:
                if len(candidates) == 1:
                    pick = candidates[0]
                else:
                    pick = sorted(candidates)[0]
                    ambiguous.append(f"{os.path.relpath(path, SRC_DIR)} -> {raw} :: picked {pick} of {len(candidates)}")

            new_rel = os.path.relpath(pick, os.path.dirname(path)).replace("\\", "/")
            if not new_rel.startswith("."):
                new_rel = "./" + new_rel
            new_rel = new_rel.replace(" ", "%20")
            changes[raw] = new_rel

        if changes:
            def repl(mm):
                t = mm.group(1).strip()
                return "](" + changes[t] + ")" if t in changes else mm.group(0)

            new_text = MD_LINK_RE.sub(repl, text)
            if new_text != text:
                fixed += len(changes)
                if APPLY:
                    with open(path, "w", encoding="utf-8", newline="\n") as f:
                        f.write(new_text)
                print(f"{'FIXED' if APPLY else 'WOULD FIX'} {len(changes):3d} links in {os.path.relpath(path, SRC_DIR)}")

    mode = "applied" if APPLY else "dry-run"
    print(f"\n[{mode}] {fixed} links repairable, {len(unresolved)} unresolved, {len(ambiguous)} ambiguous")
    if unresolved:
        print("\nUNRESOLVED:")
        for u in unresolved:
            print("  " + u)
    if ambiguous:
        print("\nAMBIGUOUS (picked first):")
        for a in ambiguous:
            print("  " + a)


if __name__ == "__main__":
    main()
