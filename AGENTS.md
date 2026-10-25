# ATT&CK & ATLAS 知识库 — 开发运维指南

## 项目概述

本项目基于 mdBook 搭建，是**中文版对抗威胁双矩阵知识库**：

- **`src/enterprise/`** — MITRE ATT&CK® Enterprise：15 战术 / 258 技术 / 622 子技术，共 880 篇文档，已完成（内容锚定 v20）。
- **`src/atlas/`** — MITRE ATLAS（AI/ML 对抗威胁矩阵）：规划 16 战术 / 120 技术 / 88 子技术 / 73 案例研究（锚定内容版 2026.09），建设中。

完整设计决策见 [issue #2](https://github.com/tonydeng/attck-knowledge/issues/2)。

## 构建与开发命令

```bash
bash scripts/build.sh          # 完整构建：链接检查 → 预处理 → mdbook 编译 → CJK 搜索索引处理
bash scripts/build.sh build    # 功能同上
bash scripts/build.sh serve    # 预处理 + 本地预览（不执行 CIK 搜索后置处理）
scripts/build.bat              # Windows 系统对应执行脚本
bash scripts/setup.sh          # 首次环境初始化：安装 mdBook、Mermaid 及主题资源

mdbook build                   # 直接编译（跳过预处理，可能导致链接失效）
mdbook serve                   # 直接本地预览（无预处理、无 CJK 搜索功能）
node scripts/cjk-search.js     # CJK 搜索后置处理程序（完整构建脚本会自动调用）

python scripts/check-links.py              # 断链检查（仅对新增断链失败，存量债见基线文件）
python scripts/check-links.py --write-baseline   # 重建断链基线（清理存量债后执行）
python scripts/fix-broken-links.py         # 按技术 ID 锚定修复断链（默认 dry-run，加 --apply 写入）
python scripts/gen-summary.py              # 重新生成 src/SUMMARY.md
```

**构建顺序有严格要求**：链接检查 → Python 预处理 → mdbook 编译 → 执行 cjk-search.js。`build.sh` 脚本已按该流程封装。

## 项目目录结构

- **`src/enterprise/`**：ATT&CK Enterprise 命名空间。战术文件夹 `01-Reconnaissance/` 至 `15-Impact/`（编号=攻击链位置，非 TA 号），主技术 `T####-英文名称.md`，子技术 `T####/T####.NNN-名称.md`。
- **`src/atlas/`**：MITRE ATLAS 命名空间。战术文件夹按官方矩阵 `sequences` 顺序编号 `01-`…`16-`，主技术 `AML.T####-英文名称.md`，子技术 `AML.T####/AML.T####.NNN-名称.md`，案例研究扁平存放于 `case-studies/AML.CS####-名称.md`。
- **`src/_data/`**：官方数据快照与审计产物（`_mitre_official.json`、`broken-links-baseline.txt`）。**不参与文档渲染**。
- **`src/_tools/`**：一次性内容审计与修复脚本。**不参与文档渲染**。
- **`scripts/`**：构建、预处理、链接检查、CJK 搜索后置处理脚本。
- **`theme/`**：Catppuccin 主题样式、Mermaid 脚本、运行时 CJK 分词补丁脚本。
- **`_book/`**：编译输出目录（已配置忽略版本追踪）。

## 预处理流程

`book.toml` 中的 `[preprocessor.attck-preprocess]` **处于启用状态**（每次构建自动执行）：

1. **`gen-summary.py`**：遍历 `enterprise/` 与 `atlas/` 两棵命名空间树，读取 H1 标题，生成三分节（ATT&CK Enterprise / MITRE ATLAS / ATLAS 案例研究）的 `src/SUMMARY.md`。ATLAS 命名空间不存在时自动跳过对应分节。
2. **`preprocess-md.py`**：修复 `README.md` 跳转至 `index.html` 的链接问题。若跳过该步骤，会出现 `README.html` 404 错误。

以上脚本通过 `mdbook-preprocessor.py`（mdBook 预处理器适配桩文件）运行。

## 中日韩（CJK）搜索功能：两大组成部分

1. **`scripts/cjk-search.js`**（编译阶段，基于 Node.js 运行）：通过 `vm.Script` 解析 elasticlunr 搜索索引，向字典树中新增约 3000 条中日韩字符分词数据，再重新序列化。该脚本在 `mdbook` 编译完成后执行。
2. **`theme/cjk-search.js`**（页面运行阶段）：改写 `elasticlunr` 分词器，将中文检索词拆分为单字，实现与索引数据的匹配。

索引文件外层封装为 `JSON.parse('...')` 格式，并做 JavaScript 单引号转义处理。如需二次修改索引文件，标准流程为：通过 `vm.Script` 解析外层 JS 封装 → 编辑内存中的索引对象 → 调用 `JSON.stringify` 序列化 → 重新封装并转义。

## 内容编写规范

- **文档结构**：所有技术文档统一分为 13 个板块（通俗理解、技术描述、攻击流程、真实案例、红蓝队视角……参考资料），具体规则参见 `README.md#文章结构规范`。
- **无 YAML frontmatter**：文档直接以 H1 标题开头，格式 `# 中文名称 (T####)` 或 `# 中文名称 (AML.T####)`。技术 ID 只出现在 H1 与文件名中，这是审计管线的对齐依据。
- **子技术命名规则**：示例 `T1589/T1589.001-Credential-Collection.md`，子技术文件统一放在对应主技术的同名文件夹内。
- **链接规则**：基于 `src/` 目录使用相对路径；新增/修改链接后必须通过 `scripts/check-links.py`（`book.toml` 的 `create-missing = false` 会在编译期直接报错）。
- **ATLAS 文档特有板块**：官方 `ATT&CK-reference` 映射生成的「关联 ATT&CK 技术」；难度等级采用官方 maturity 三级映射（Feasible=⭐ / Demonstrated=⭐⭐ / Realized=⭐⭐⭐）。

## 持续集成/持续部署（CI/CD）

配置文件位于 `.github/workflows/deploy.yml`，基于 GitHub Actions 实现：
- 触发条件：向 `main` 分支推送代码，或手动触发工作流
- 执行步骤：安装 mdBook、mdbook-mermaid、Catppuccin 主题 → 运行 Python 预处理脚本（随 mdbook 编译执行）→ 执行 Node.js 版 CJK 后置处理 → 将 `_book/` 编译产物部署至 GitHub Pages

## 常见问题与注意事项

- `mdbook serve` 会在文件变更时自动重新编译，**覆盖已优化的 CJK 搜索索引**。如需测试中文搜索功能，请执行 `bash scripts/build.sh build && mdbook serve`。
- 新增、重命名任意技术文档后**无需手动执行 `gen-summary.py`**（已接入构建流程）；仅在需要单独预览 SUMMARY 时手动运行。
- `book.toml` 中 `create-missing = false`：若 SUMMARY.md 或正文引用了不存在的文件，编译会直接报错，不会自动创建缺失文件。
- **断链门禁**：`check-links.py` 只对**新增**断链失败。`src/_data/broken-links-baseline.txt` 当前为空（v20 升级时已清偿全部 56 处 v19 重编号存量债：revoked 对象重定向至继任文档，幻觉 ID 降级为纯文本）。出现新的存量债时，先修复再执行 `--write-baseline` 收缩基线。
- **命名空间迁移影响**：站点 URL 已由 `/01-Reconnaissance/...` 变为 `/enterprise/01-Reconnaissance/...`，外部旧深链会 404（一次性，不做重定向）。
