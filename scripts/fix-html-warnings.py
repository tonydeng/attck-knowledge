#!/usr/bin/env python3
"""
fix-html-warnings.py - 自动修复 mdbook 构建中的 unclosed HTML tag 警告

当 Markdown 内容中包含类似 /proc/<pid>/mem、\\<IP>、<tabs> 等文本时，
mdBook 会将其解析为未闭合的 HTML 标签并发出警告。

本脚本扫描 src/ 目录下的所有 .md 文件，将裸写的 <tag> 替换为 `<tag>`（行内代码），
避免 mdBook 将其当作 HTML 标签处理。

用法:
    python scripts/fix-html-warnings.py              # 扫描并修复
    python scripts/fix-html-warnings.py --check      # 仅检查，不修改
    python scripts/fix-html-warnings.py --verbose    # 显示每个修复位置

集成到构建流程:
    在 mdbook build 之前执行: python scripts/fix-html-warnings.py

白名单机制:
    某些 <tag> 是 mdBook 语法的合法 HTML（如 <br>, <details>, <summary>），
    通过 WHITELIST 集合排除，避免误修复。
"""

import os
import re
import sys

SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")

# 白名单：这些是合法的 mdBook/HTML 标签，不应被替换（大小写不敏感）
WHITELIST_TAGS = {
    tag.lower()
    for tag in {
        "br", "hr", "p", "b", "i", "u", "em", "strong",
        "details", "summary",
        "table", "tr", "th", "td", "thead", "tbody",
        "ol", "ul", "li", "dl", "dt", "dd",
        "div", "span", "pre", "code",
        "h1", "h2", "h3", "h4", "h5", "h6",
        "img", "a", "link",
        "blockquote", "cite",
        "sup", "sub",
        "center", "font", "color",
        "abbr", "acronym", "address", "area",
        "base", "basefont",
        "bdo", "big", "body", "caption",
        "col", "colgroup",
        "del", "dfn", "dir",
        "fieldset", "form", "frame", "frameset",
        "head", "header", "html",
        "iframe", "input", "ins", "isindex",
        "kbd",
        "label", "legend", "line",
        "main", "map", "mark", "menu", "meta",
        "nav", "noframes", "noscript",
        "object", "optgroup", "option", "output",
        "param",
        "q",
        "rp", "rt", "ruby",
        "s", "samp", "script", "section", "select", "small", "source",
        "strike", "style", "sub", "summary",
        "tab", "tbody", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "tt",
        "u", "ul",
        "var", "video", "wbr",
        # Mermaid 相关
        "svg", "g", "rect", "path", "text", "tspan", "defs", "linearGradient", "stop",
        "ellipse", "circle", "line", "polygon", "polyline",
        # 标记语言
        "markdown", "html",
    }
}

# 编译正则：匹配裸写的 <tag> 且 tag 为字母（1-15个字符，大小写混合）
# 注意：不在正则层面排除反引号包围（因为 > 后紧跟的反引号可能属于另一个内联代码），
# 而是通过 _is_in_inline_code() 函数检查。
# 排除：
#   - 已用反引号包裹的 `<tag>`（由 _is_in_inline_code 处理）
#   - 已用 HTML 实体 &lt;tag&gt; 
#   - 位于代码块中（由 _is_in_code_block 处理）
#   - 合法 HTML 标签（白名单）
TAG_PATTERN = re.compile(r"<([A-Za-z][A-Za-z0-9]{0,14})>")


def _is_in_code_block(text, pos):
    """检查位置 pos 是否在代码块内（```...```）。"""
    before = text[:pos]
    count = 0
    for m in re.finditer(r"^`{3,}", before, re.MULTILINE):
        count += 1
    return count % 2 == 1


def _is_in_inline_code(text, pos):
    """检查位置 pos 是否在行内代码 `...` 内（基于反引号奇偶校验）。"""
    before = text[:pos]
    after = text[pos:]
    return (before.count("`") % 2 == 1) and (after.count("`") % 2 == 1)


def fix_markdown_file(filepath, dry_run=False, verbose=False):
    """处理单个 .md 文件，返回是否被修改。"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changes = []
    lines = content.split("\n")

    for i in range(len(lines)):
        line = lines[i]
        pos = 0
        while True:
            m = TAG_PATTERN.search(line, pos)
            if not m:
                break

            tag = m.group(1)
            abs_pos = sum(len(l) + 1 for l in lines[:i]) + m.start()

            # 跳过白名单标签
            if tag.lower() in WHITELIST_TAGS:
                pos = m.end()
                continue

            # 跳过代码块内的标签
            if _is_in_code_block(content, abs_pos):
                pos = m.end()
                continue

            # 判断是否在行内代码内
            if _is_in_inline_code(content, abs_pos):
                # 在行内代码内：使用 HTML 实体 &lt;tag&gt;（包裹反引号会破坏原内联代码）
                replacement = f"&lt;{tag}&gt;"
            else:
                # 不在行内代码内：包裹为 `<tag>`（行内代码）
                replacement = f"`<{tag}>`"
            line = line[:m.start()] + replacement + line[m.end():]
            pos = m.start() + len(replacement)

            if verbose:
                changes.append(
                    f"  {filepath}:{i+1}:{m.start()+1}  '<{tag}>' -> '`<{tag}>`'"
                )

        lines[i] = line  # 关键：将修改后的行写回列表

    new_content = "\n".join(lines)

    if new_content == original:
        return False, changes

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return True, changes


def main():
    dry_run = "--check" in sys.argv
    verbose = "--verbose" in sys.argv

    files_modified = 0
    total_warnings = 0

    for root, dirs, files in os.walk(SRC_DIR):
        # 跳过隐藏目录
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            filepath = os.path.join(root, fname)
            modified, changes = fix_markdown_file(filepath, dry_run, verbose)
            if modified:
                files_modified += 1
                total_warnings += len(changes)
                if verbose:
                    for c in changes:
                        print(c)
                relpath = os.path.relpath(filepath, SRC_DIR)
                print(f"{'[DRY-RUN]' if dry_run else '[FIXED]'} {relpath}")

    mode = " (dry-run)" if dry_run else ""
    print(f"\nResult: {files_modified} file(s) modified, {total_warnings} warning(s) fixed{mode}")

    if dry_run and files_modified > 0:
        print("\nRun without --check to apply fixes.")


if __name__ == "__main__":
    main()
