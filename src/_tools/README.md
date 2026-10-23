# ATT&CK 知识库审计工具

> 统一 CLI 工具，用于本地知识库与 MITRE ATT&CK v20 官方数据的完整性审计。

## 工具说明

`attack_mapping.py` 是 ATT&CK 知识库的统一审计工具，合并了历史上的 5 个独立脚本
（scan_local / fetch_mitre / gen_mapping / verify_mapping / summary_check）为单一 CLI，
提供 6 个子命令覆盖"扫描→抓取→生成→验证→统计"完整流程。

- **依赖**：仅 Python 3.7+ 标准库（urllib / ssl / re / json / pathlib / argparse），无需安装任何第三方包
- **路径自适配**：脚本通过 `__file__` 自动定位知识库根目录，可在任意工作目录下运行
- **平台**：Windows / Linux / macOS 均可

## 目录结构

```
知识库/
├── _tools/
│   ├── attack_mapping.py      # 统一 CLI 工具（本目录）
│   └── README.md              # 本文件
├── _data/
│   ├── _local_scan.json       # 本地扫描结果（由 scan 生成）
│   ├── _mitre_official.json   # MITRE 官方数据（由 fetch 生成）
│   └── README.md
├── 01-Reconnaissance/
│   ├── MAPPING.md             # 由 generate 生成
│   ├── T1595-Active-Scanning.md
│   └── T1595/
│       └── T1595.001-Scanning-IP-Blocks.md
└── ... (其余 14 个战术目录)
```

## 子命令说明

### 1. `scan` — 扫描本地知识库

扫描 15 个战术目录下所有 `.md` 文件的 YAML frontmatter，提取技术 ID、名称、状态等元数据，
输出到 `_data/_local_scan.json`。

```bash
python _tools/attack_mapping.py scan
```

- 自动跳过 `README.md`、`MAPPING.md`、`模板*.md`
- 顶层 `.md` 文件视为父技术，子目录（如 `T1595/`）内的 `.md` 视为子技术
- 输出 JSON 包含每个战术目录的 `parent_count` / `subtech_count` 及详细列表

### 2. `fetch` — 抓取 MITRE 官方数据

从 `https://attack.mitre.org/tactics/{TID}/` 抓取 15 个战术页 HTML，解析父技术/子技术清单，
输出到 `_data/_mitre_official.json`。

```bash
python _tools/attack_mapping.py fetch
```

- 使用 `urllib.request` + SSL 默认上下文，无需额外证书配置
- 内置 3 次重试，每次间隔 2 秒
- 每个战术页之间间隔 0.5 秒，避免对官方站点造成压力
- HTML 解析基于正则表达式，匹配 `<tr class="technique">` 和 `<tr class="sub technique">` 行

### 3. `generate` — 生成 MAPPING.md

读取 `_data/_local_scan.json` 和 `_data/_mitre_official.json`，对比后生成 15 个
`{战术目录}/MAPPING.md` 文件。

```bash
python _tools/attack_mapping.py generate
python _tools/attack_mapping.py generate --skip-mitre   # 仅用本地数据（不对比官方）
```

每个 MAPPING.md 包含：
- **YAML frontmatter**：战术元数据 + 官方/本地计数 + 覆盖率
- **概述**：数据陈述与覆盖率
- **父技术映射表**：技术 ID、官方/中文名称、本地文件路径、子技术数、状态图标、备注
- **子技术映射表**：子技术 ID、官方/中文名称、父技术、本地文件路径、状态、备注
- **状态图例**：✅ 已完成 / 📝 草稿 / ❌ 缺失 / 🔄 名称不一致 / ⚠️ 已撤销或迁移
- **缺失与不一致清单**：分类列出所有差异项

### 4. `verify` — 验证 MAPPING.md 一致性

重新从两份 JSON 计算期望值，逐项验证 15 个 MAPPING.md 的：
- YAML frontmatter 计数字段（6 项）
- 父技术表/子技术表行数
- 每一行的状态标记（✅/❌/🔄/⚠️）是否与重算结果匹配
- 缺失与不一致清单的计数

```bash
python _tools/attack_mapping.py verify
```

返回码：
- `0`：全部一致（0 issues / 0 warnings）
- `2`：存在硬错误（issues）
- `1`：致命错误（JSON 文件缺失等）

### 5. `status` — 打印总体统计

打印 15 个战术的官方/本地计数、MAPPING.md 文件大小、JSON 文件状态的汇总表。

```bash
python _tools/attack_mapping.py status
```

### 6. `all` — 全流程执行

顺序执行 `scan → fetch → generate → verify`，端到端完成审计。

```bash
python _tools/attack_mapping.py all
```

适合首次部署或定期全量审计时使用。任何一步失败都会中止流程（`verify` 返回 2 不中止）。

## AI 智能体调用方式

本工具专为 AI 编码智能体（OpenCode / Claude Code / Codex 等）设计，调用约定如下：

### 调用入口

```bash
# 从知识库根目录调用
python _tools/attack_mapping.py <子命令>

# 或从任意目录调用（路径自适配）
python F:/user-requ/ATTCK知识库/知识库/_tools/attack_mapping.py <子命令>
```

### 推荐调用顺序

| 场景 | 调用序列 |
|------|---------|
| 首次部署 | `all`（一站式） |
| 新增/修改本地技术文件后 | `scan` → `generate` → `verify` |
| MITRE 升级版本后 | `fetch` → `generate` → `verify` |
| 仅检查一致性 | `verify` |
| 查看覆盖率 | `status` |

### AI 调用约定

1. **修改本地技术文件后**，必须运行 `scan` 刷新 `_local_scan.json`，再运行 `generate` 更新 MAPPING.md
2. **新增技术文件**后，运行 `scan → generate → verify`，确认 0 issues
3. **判断任务完成**的硬性标准：`verify` 输出 `0 issues / 0 warnings`
4. **禁止手工编辑 MAPPING.md**——该文件由 `generate` 自动生成，手工修改会被下次生成覆盖
5. **禁止手工编辑 `_data/*.json`**——这两个 JSON 由 `scan` / `fetch` 自动生成

### 输出判读

- `❌ Issues`：硬错误（计数不符、状态标记错误），必须修复
- `⚠️ Warnings`：软警告（撤销/迁移技术未标 ⚠️、名称不一致未标 🔄），建议关注
- `✅ 全部一致`：该战术的 MAPPING.md 与 JSON 数据完全对齐

## 历史脚本映射

| 历史脚本 | 统一工具子命令 |
|---------|--------------|
| `scan_local.py` | `scan` |
| `fetch_mitre.py` | `fetch` |
| `gen_mapping.py` | `generate` |
| `verify_mapping.py` | `verify` |
| `summary_check.py` | `status` |
| —（新增） | `all` |

历史脚本已于 2026-07-24 合并为本统一工具，原脚本已删除。

## 维护说明

- **新增战术目录**：在 `TACTICS` 列表中添加条目，并确保目录命名遵循 `NN-Tactic-Name` 格式
- **MITRE 版本升级**：修改 `attack_version` 字段（当前 `v19.1`），重新运行 `fetch`
- **Defense Evasion 拆分**：v19.1 将原 TA0005 拆分为 Stealth (TA0005) + Defense Impairment (TA0112)，本工具已适配

## 版本

- **工具版本**：1.0
- **MITRE ATT&CK 版本**：v20
- **最后更新**：2026-10-22
