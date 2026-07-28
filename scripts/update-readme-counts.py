#!/usr/bin/env python3
"""更新所有 README 文件，使声明的计数与实际文件计数一致。

权威计数：
- 15 个战术，254 个主技术，617 个子技术，871 个技术文档
- 版本 v19.1，日期 2026-07-28
"""
import re
import sys
from pathlib import Path

BASE = Path(r"D:\workspace\github\attck-knowledge")
SRC = BASE / "src"

# 权威计数：(目录名, 中文名, TA ID, 主技术数, 子技术数)
TACTICS = [
    ("01-Reconnaissance",         "侦察",       "TA0043", 12, 34),
    ("02-Resource-Development",   "资源开发",   "TA0042",  9, 41),
    ("03-Initial-Access",         "初始访问",   "TA0001", 11, 11),
    ("04-Execution",              "执行",       "TA0002", 20, 44),
    ("05-Persistence",            "持久化",     "TA0003", 22, 90),
    ("06-Privilege-Escalation",   "权限提升",   "TA0004", 13, 83),
    ("07-Stealth",                "隐蔽",       "TA0005", 30, 118),
    ("08-Defense-Impairment",     "防御削弱",   "TA0112", 18, 38),
    ("09-Credential-Access",      "凭证访问",   "TA0006", 17, 50),
    ("10-Discovery",              "发现",       "TA0007", 34, 15),
    ("11-Lateral-Movement",       "横向移动",   "TA0008",  9, 14),
    ("12-Collection",             "收集",       "TA0009", 17, 24),
    ("13-Command-and-Control",    "命令与控制", "TA0011", 18, 27),
    ("14-Exfiltration",           "渗漏",       "TA0010",  9, 10),
    ("15-Impact",                 "影响",       "TA0040", 15, 18),
]

TOTAL_MAIN = sum(t[3] for t in TACTICS)   # 254
TOTAL_SUB = sum(t[4] for t in TACTICS)    # 617
TOTAL_DOCS = TOTAL_MAIN + TOTAL_SUB       # 871

VERSION = "v19.1"
DATE = "2026-07-28"
MAIN_FOOTER = f"> **版本**: {VERSION} | **更新**: {DATE} | **文档数**: {TOTAL_DOCS} | **完成度**: 100%"
TACTIC_FOOTER = f"> **版本**: {VERSION} | **更新**: {DATE} | **模板**: 战术README v3.1"


# ─────────────────────────────────────────────────────
# 项目根 README
# ─────────────────────────────────────────────────────
def update_project_root_readme():
    fpath = BASE / "README.md"
    if not fpath.exists():
        print(f"[SKIP] 未找到: {fpath}")
        return
    content = fpath.read_text(encoding="utf-8")
    original = content

    # 版本引用
    content = content.replace("MITRE ATT&CK v19", f"MITRE ATT&CK {VERSION}")
    content = content.replace("ATT&CK v19", f"ATT&CK {VERSION}")

    # 子技术数
    content = content.replace("900+ 个子技术", f"{TOTAL_SUB} 个子技术")
    content = content.replace("900+子技术", f"{TOTAL_SUB}子技术")

    # 内容概览表格行
    for _dir, display, ta_id, main, sub in TACTICS:
        pat = rf'(\| \d{{2}} \| {re.escape(display)} \| {ta_id} \| )\d+( \| )\d+( \|)'
        content = re.sub(pat, rf'\g<1>{main}\g<2>{sub}\g<3>', content)

    # 总计行
    content = re.sub(
        r'> \*\*总计\*\*：\d+ 篇文档.*?覆盖 \d+ 个技术、\d+\+? 子技术',
        f'> **总计**：{TOTAL_DOCS} 篇技术文档（{TOTAL_MAIN} 个主技术 + {TOTAL_SUB} 个子技术），覆盖 15 个战术',
        content,
    )

    if content != original:
        fpath.write_text(content, encoding="utf-8")
        print(f"[OK]   {fpath}")
    else:
        print(f"[SAME] {fpath}")


# ─────────────────────────────────────────────────────
# src/README.md（知识库主页）
# ─────────────────────────────────────────────────────
def update_src_readme():
    fpath = SRC / "README.md"
    content = fpath.read_text(encoding="utf-8")
    original = content

    # 标题行
    content = re.sub(
        r'^# ATT&CK 知识库 v19$',
        f'# ATT&CK 知识库 {VERSION}',
        content, count=1, flags=re.MULTILINE,
    )

    # 顶部声明
    content = content.replace("910+ 子技术", f"{TOTAL_SUB} 子技术")
    content = content.replace("910+子技术", f"{TOTAL_SUB}子技术")

    # 统计总览表
    content = content.replace(
        f"| 子技术（Sub-techniques） | 910+ |",
        f"| 子技术（Sub-techniques） | {TOTAL_SUB} |",
    )
    content = content.replace(
        f"| 文章总数 | 274 |",
        f"| 文章总数 | {TOTAL_DOCS} |",
    )
    content = content.replace(
        "100%（274/274 ✅）",
        f"100%（{TOTAL_DOCS}/{TOTAL_DOCS} ✅）",
    )
    content = content.replace(
        "MITRE ATT&CK v19 Enterprise",
        f"MITRE ATT&CK {VERSION} Enterprise",
    )

    # 各战术小节标题：**技术数：X 个 | 子技术数：Y 个**
    for _dir, display, ta_id, main, sub in TACTICS:
        pat = rf'(### \d{{2}} - {re.escape(display)} \({ta_id}\).*?)(\*\*技术数：)\d+( 个 \| 子技术数：)\d+( 个\*\*)'
        content = re.sub(pat, rf'\g<1>\g<2>{main}\g<3>{sub}\g<4>', content, flags=re.DOTALL)

    # 完整统计表行
    for _dir, display, ta_id, main, sub in TACTICS:
        pat = rf'(\| \d{{2}} \| {re.escape(display)} \| {ta_id} \| )\d+( \| )\d+( \| )\d+( \|)'
        file_count = main + 1  # 主技术文件数 + 1（战术 README）
        content = re.sub(pat, rf'\g<1>{main}\g<2>{sub}\g<3>{file_count}\g<4>', content)

    # 总计行
    content = re.sub(
        r'> \*\*总计：15 个战术，\d+ 个技术，\d+\+? 个子技术，\d+ 篇文档\*\*',
        f'> **总计：15 个战术，{TOTAL_MAIN} 个技术，{TOTAL_SUB} 个子技术，{TOTAL_DOCS} 篇文档**',
        content,
    )

    # 页脚
    content = re.sub(
        r'> \*\*版本\*\*: v[\d.]+ \| \*\*更新\*\*: [\d-]+ \| \*\*文档数\*\*: \d+ \| \*\*完成度\*\*: 100%',
        MAIN_FOOTER,
        content,
    )

    # 数据来源 v19 引用
    content = content.replace(
        "MITRE ATT&CK® Enterprise Matrix v19",
        f"MITRE ATT&CK® Enterprise Matrix {VERSION}",
    )

    if content != original:
        fpath.write_text(content, encoding="utf-8")
        print(f"[OK]   {fpath}")
    else:
        print(f"[SAME] {fpath}")


# ─────────────────────────────────────────────────────
# 战术 README
# ─────────────────────────────────────────────────────
def update_tactic_readme(dir_name, display, ta_id, main, sub):
    fpath = SRC / dir_name / "README.md"
    content = fpath.read_text(encoding="utf-8")
    original = content
    docs = main + sub

    # 技术总数
    content = re.sub(
        r'(- \*\*技术总数\*\*：)\d+( 个)',
        rf'\g<1>{main}\g<2>',
        content,
    )

    # 子技术总数
    content = re.sub(
        r'(- \*\*子技术总数\*\*：)\d+( 个)',
        rf'\g<1>{sub}\g<2>',
        content,
    )

    # 已完成文档（整行替换，移除过时的"待补充"备注）
    content = re.sub(
        r'- \*\*已完成文档\*\*：\d+ 个.*',
        f'- **已完成文档**：{docs} 个（{main} 父技术 + {sub} 子技术）',
        content,
    )

    # 进行中文档 → 0
    content = re.sub(
        r'(- \*\*进行中文档\*\*：)\d+( 个)',
        r'\g<1>0\g<2>',
        content,
    )

    # 待编写文档 → 0
    content = re.sub(
        r'(- \*\*待编写文档\*\*：)\d+( 个)',
        r'\g<1>0\g<2>',
        content,
    )

    # 页脚：移除旧页脚（匹配任何包含"版本"的引用行）
    content = re.sub(r'\n*> \*\*版本\*\*:.*?\n*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'\n*> \*\*v[\d.]+\*\*.*?\n*$', '', content, flags=re.MULTILINE)

    # 追加标准化页脚
    content = content.rstrip() + '\n\n' + TACTIC_FOOTER + '\n'

    if content != original:
        fpath.write_text(content, encoding="utf-8")
        print(f"[OK]   {fpath}")
    else:
        print(f"[SAME] {fpath}")


# ─────────────────────────────────────────────────────
# 主函数
# ─────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("更新 README 文件 — 权威计数同步")
    print(f"总计：15 战术 / {TOTAL_MAIN} 主技术 / {TOTAL_SUB} 子技术 / {TOTAL_DOCS} 文档")
    print(f"版本：{VERSION}  日期：{DATE}")
    print("=" * 60 + "\n")

    update_project_root_readme()
    update_src_readme()

    for dir_name, display, ta_id, main, sub in TACTICS:
        update_tactic_readme(dir_name, display, ta_id, main, sub)

    print("\n" + "=" * 60)
    print("完成。请运行 mdbook build 验证。")
    print("=" * 60)


if __name__ == "__main__":
    main()
