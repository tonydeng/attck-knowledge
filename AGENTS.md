# ATT&CK 知识库 — 开发运维指南

## 项目概述

本项目基于 mdBook 搭建，是**中文版 MITRE ATT&CK v19 企业级知识库**。共包含 274 份文档，覆盖 15 项战术、254 项技术以及 900 余项子技术，内容已全部完善。

## 构建与开发命令

```bash
bash scripts/build.sh          # 完整构建：预处理 → mdbook 编译 → 中日韩（CJK）搜索索引处理
bash scripts/build.sh build    # 功能同上
bash scripts/build.sh serve    # 预处理 + 本地预览（不执行 CJK 搜索后置处理）
scripts/build.bat              # Windows 系统对应执行脚本
bash scripts/setup.sh          # 首次环境初始化：安装 mdBook、Mermaid 及主题资源

mdbook build                   # 直接编译（跳过预处理，可能导致链接失效）
mdbook serve                   # 直接本地预览（无预处理、无 CJK 搜索功能）
node scripts/cjk-search.js     # CJK 搜索后置处理程序（完整构建脚本会自动调用）
```

**构建顺序有严格要求**：Python 预处理 → mdbook 编译 → 执行 cjk-search.js。`build.sh` 脚本已按该流程封装。

## 项目目录结构

- **`src/`**：文档源码目录。包含按序号命名的战术文件夹（如 `01-Reconnaissance/` 至 `15-Impact/`）、主技术文档（命名格式：`T####-英文名称.md`）；子技术统一存放于对应主技术子目录下，格式为 `T####/T####.NNN-名称.md`。
- **`scripts/`**：Python 预处理脚本、构建脚本、CJK 搜索后置处理程序。
- **`theme/`**：Catppuccin 主题样式、Mermaid 脚本、运行时 CJK 分词补丁脚本。
- **`_book/`**：编译输出目录（已配置忽略版本追踪）。

## 预处理流程

项目内置两个 Python 脚本，**目前未接入自动构建流程**（`book.toml` 中 `[preprocessor.attck-preprocess]` 配置已注释）：

1. **`gen-summary.py`**：遍历 `src/` 目录结构，读取文档头部 YAML 配置与一级标题，自动生成 `src/SUMMARY.md`。新增、重命名文件后需手动执行。
2. **`preprocess-md.py`**：修复 `README.md` 跳转至 `index.html` 的链接问题。若跳过该步骤，会出现 `README.html` 404 错误。

以上脚本通过 `mdbook-preprocessor.py`（mdBook 预处理器适配桩文件）运行。如需启用自动执行，取消 `book.toml` 中 `[preprocessor.attck-preprocess]` 的注释即可。当前需手动执行脚本，或直接使用已修正链接的文件进行构建。

## 中日韩（CJK）搜索功能：两大组成部分

1. **`scripts/cjk-search.js`**（编译阶段，基于 Node.js 运行）：通过 `vm.Script` 解析 28 MB 的 elasticlunr 搜索索引，向字典树中新增约 3000 条中日韩字符分词数据，再重新序列化。该脚本在 `mdbook` 编译完成后执行，最终生成 51 MB 的索引文件。
2. **`theme/cjk-search.js`**（页面运行阶段）：改写 `elasticlunr` 分词器，将中文检索词拆分为单字，实现与索引数据的匹配。

索引文件外层封装为 `JSON.parse('...')` 格式，并做 JavaScript 单引号转义处理。如需二次修改索引文件，标准流程为：通过 `vm.Script` 解析外层 JS 封装 → 编辑内存中的索引对象 → 调用 `JSON.stringify` 序列化 → 重新封装并转义。

## 内容编写规范

- **文档结构**：所有技术文档统一分为 13 个板块（通俗理解、技术描述、攻击流程、真实案例、红蓝队视角……参考资料），具体规则参见 `README.md#文章结构规范`。
- **文档头部配置**：每份 Markdown 文件头部均包含 YAML 配置项，字段包括：技术编号、所属战术、中文标题、难度等级。
- **子技术命名规则**：示例 `T1589/T1589.001-Credential-Collection.md`，子技术文件统一放在对应主技术的同名文件夹内。
- **链接规则**：基于 `src/` 目录使用相对路径；`README.md` 相关链接可由预处理脚本自动修复。

## 持续集成/持续部署（CI/CD）

配置文件位于 `.github/workflows/deploy.yml`，基于 GitHub Actions 实现：
- 触发条件：向 `main` 分支推送代码，或手动触发工作流
- 执行步骤：安装 mdBook、mdbook-mermaid、Catppuccin 主题 → 运行 Python 预处理脚本（随 mdbook 编译执行）→ 执行 Node.js 版 CJK 后置处理 → 将 `_book/` 编译产物部署至 GitHub Pages

## 常见问题与注意事项

- `mdbook serve` 会在文件变更时自动重新编译，**覆盖已优化的 CJK 搜索索引**。如需测试中文搜索功能，请执行 `bash scripts/build.sh build && mdbook serve`。
- 索引文件大小：未处理 CJK 前约 28 MB，处理后约 51 MB。浏览器加载优化后的索引文件，`JSON.parse` 解析耗时约 1~2 秒。
- 新增、重命名任意技术文档后，**必须重新运行 `scripts/gen-summary.py`**；该脚本暂未接入自动构建流程（配置文件中相关预处理器已注释）。
- `book.toml` 中 `create-missing = false`：若文档中引用了不存在的文件，编译会直接报错，不会自动创建缺失文件。