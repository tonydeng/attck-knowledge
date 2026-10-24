# ATT&CK & ATLAS 知识库

[![mdbook build](https://github.com/tonydeng/attck-knowledge/actions/workflows/deploy.yml/badge.svg)](https://github.com/tonydeng/attck-knowledge/actions/workflows/deploy.yml)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-online-brightgreen)](https://tonydeng.github.io/attck-knowledge/)
[![MITRE ATT&CK v20](https://img.shields.io/badge/MITRE%20ATT%26CK-v20-blue)](https://attack.mitre.org/matrices/enterprise/)
[![MITRE ATLAS 2026.09](https://img.shields.io/badge/MITRE%20ATLAS-2026.09-blue)](https://atlas.mitre.org/)
[![中文](https://img.shields.io/badge/lang-中文-red)](.)

基于 [MITRE ATT&CK® Enterprise](https://attack.mitre.org/matrices/enterprise/) 与 [MITRE ATLAS](https://atlas.mitre.org/) 双矩阵的中文对抗威胁知识库，**两部分内容均已全部完成**：

- **ATT&CK Enterprise**（锚定 v20）：15 个战术、**258 个技术**、**622 个子技术**，共 880 篇文档
- **MITRE ATLAS**（AI/ML 对抗威胁矩阵，锚定 2026.09）：16 战术、120 技术、88 子技术、**73 篇案例研究**

ATLAS 部分的设计决策与实施记录见 [issue #2（设计 spec，已交付）](https://github.com/tonydeng/attck-knowledge/issues/2)。

> 每篇技术文档包含：通俗理解、技术原理、真实案例、红蓝队视角、检测建议、动手实验。适合安全分析师、渗透测试工程师、蓝队防御人员、安全学习者阅读。

> **⚠️ 免责声明**
>
> 本知识库仅供网络安全教育、研究及防御目的使用。所有内容基于 MITRE ATT&CK® 与 MITRE ATLAS® 框架的公开信息整理，旨在帮助安全从业人员了解攻击技术、提升防御能力。
>
> **禁止**将本知识库中的任何技术、方法用于未经授权的非法活动。任何利用本知识库内容进行的违法行为，均由行为人自行承担全部法律责任。
>
> 作者及贡献者不对因使用本知识库内容而产生的任何直接或间接损失承担责任。使用者应遵守所在地相关法律法规，合法合规地使用本知识库。

---

## 在线阅读

📖 **[attck-knowledge.vercel.app](https://attck-knowledge.vercel.app/)**（推荐，带全文搜索 + Mermaid 图表）

或直接访问 GitHub Pages：[tonydeng.github.io/attck-knowledge](https://tonydeng.github.io/attck-knowledge/)

---

## 内容概览

### ATT&CK Enterprise（15 战术）

| 序号 | 战术名称 | TA ID | 技术数 | 子技术数 | 目录 |
|:---:|---------|:-----:|:------:|:--------:|------|
| 01 | 侦察 | TA0043 | 12 | 34 | [`01-Reconnaissance`](./src/enterprise/01-Reconnaissance/README.md) |
| 02 | 资源开发 | TA0042 | 9 | 42 | [`02-Resource-Development`](./src/enterprise/02-Resource-Development/README.md) |
| 03 | 初始访问 | TA0001 | 11 | 11 | [`03-Initial-Access`](./src/enterprise/03-Initial-Access/README.md) |
| 04 | 执行 | TA0002 | 22 | 44 | [`04-Execution`](./src/enterprise/04-Execution/README.md) |
| 05 | 持久化 | TA0003 | 22 | 91 | [`05-Persistence`](./src/enterprise/05-Persistence/README.md) |
| 06 | 权限提升 | TA0004 | 13 | 83 | [`06-Privilege-Escalation`](./src/enterprise/06-Privilege-Escalation/README.md) |
| 07 | 隐蔽 | TA0005 | 31 | 120 | [`07-Stealth`](./src/enterprise/07-Stealth/README.md) |
| 08 | 防御削弱 | TA0112 | 18 | 39 | [`08-Defense-Impairment`](./src/enterprise/08-Defense-Impairment/README.md) |
| 09 | 凭证访问 | TA0006 | 18 | 50 | [`09-Credential-Access`](./src/enterprise/09-Credential-Access/README.md) |
| 10 | 发现 | TA0007 | 34 | 15 | [`10-Discovery`](./src/enterprise/10-Discovery/README.md) |
| 11 | 横向移动 | TA0008 | 9 | 14 | [`11-Lateral-Movement`](./src/enterprise/11-Lateral-Movement/README.md) |
| 12 | 收集 | TA0009 | 17 | 24 | [`12-Collection`](./src/enterprise/12-Collection/README.md) |
| 13 | 命令与控制 | TA0011 | 17 | 27 | [`13-Command-and-Control`](./src/enterprise/13-Command-and-Control/README.md) |
| 14 | 渗漏 | TA0010 | 10 | 10 | [`14-Exfiltration`](./src/enterprise/14-Exfiltration/README.md) |
| 15 | 影响 | TA0040 | 15 | 18 | [`15-Impact`](./src/enterprise/15-Impact/README.md) |

> **总计**：258 个主技术 + 622 个子技术 = 880 篇技术文档。注：T1659（内容注入）官方双归属初始访问/命令与控制，文档收录于初始访问战术。

### MITRE ATLAS（16 战术）

| 序号 | 战术名称 | TA ID | 技术数 | 子技术数 | 目录 |
|:---:|---------|:-----:|:------:|:--------:|------|
| 01 | 侦察 | AML.TA0002 | 9 | 9 | [`01-Reconnaissance`](./src/atlas/01-Reconnaissance/README.md) |
| 02 | 资源开发 | AML.TA0003 | 9 | 20 | [`02-Resource-Development`](./src/atlas/02-Resource-Development/README.md) |
| 03 | AI 攻击适配 | AML.TA0001 | 11 | 14 | [`03-AI-Attack-Adaptation`](./src/atlas/03-AI-Attack-Adaptation/README.md) |
| 04 | 初始访问 | AML.TA0004 | 10 | 8 | [`04-Initial-Access`](./src/atlas/04-Initial-Access/README.md) |
| 05 | AI 模型访问 | AML.TA0000 | 4 | 0 | [`05-AI-Model-Access`](./src/atlas/05-AI-Model-Access/README.md) |
| 06 | 执行 | AML.TA0005 | 6 | 7 | [`06-Execution`](./src/atlas/06-Execution/README.md) |
| 07 | 持久化 | AML.TA0006 | 9 | 5 | [`07-Persistence`](./src/atlas/07-Persistence/README.md) |
| 08 | 权限提升 | AML.TA0012 | 2 | 0 | [`08-Privilege-Escalation`](./src/atlas/08-Privilege-Escalation/README.md) |
| 09 | 防御规避 | AML.TA0007 | 15 | 1 | [`09-Defense-Evasion`](./src/atlas/09-Defense-Evasion/README.md) |
| 10 | 凭证访问 | AML.TA0013 | 7 | 0 | [`10-Credential-Access`](./src/atlas/10-Credential-Access/README.md) |
| 11 | 发现 | AML.TA0008 | 10 | 7 | [`11-Discovery`](./src/atlas/11-Discovery/README.md) |
| 12 | 横向移动 | AML.TA0015 | 2 | 2 | [`12-Lateral-Movement`](./src/atlas/12-Lateral-Movement/README.md) |
| 13 | 收集 | AML.TA0009 | 6 | 2 | [`13-Collection`](./src/atlas/13-Collection/README.md) |
| 14 | 命令与控制 | AML.TA0014 | 5 | 0 | [`14-Command-and-Control`](./src/atlas/14-Command-and-Control/README.md) |
| 15 | 数据渗漏 | AML.TA0010 | 6 | 3 | [`15-Exfiltration`](./src/atlas/15-Exfiltration/README.md) |
| 16 | 影响 | AML.TA0011 | 9 | 10 | [`16-Impact`](./src/atlas/16-Impact/README.md) |

> **总计**：120 个主技术 + 88 个子技术 + [73 篇案例研究](./src/atlas/case-studies/README.md)（来自 MITRE ATLAS 官方案例库的真实攻击事件与安全研究）。ATLAS 战术编号按官方矩阵顺序（非 TA 号顺序）。

---

## 项目结构

```
attck-knowledge/
├── .github/workflows/deploy.yml   # GitHub Pages CI/CD
├── book.toml                       # mdBook 配置（Catppuccin 主题 + Mermaid + CJK 搜索）
├── scripts/
│   ├── preprocess-md.py            # 链接预处理（构建前自动修复 README.md 链接）
│   ├── build.sh / build.bat        # 构建脚本（链接检查 + 预处理 + mdbook build）
│   ├── setup.sh                    # 本地环境初始化
│   ├── gen-summary.py              # SUMMARY.md 自动生成器（双命名空间）
│   ├── check-links.py              # 断链检查门禁（--write-baseline 重建基线）
│   └── fix-broken-links.py         # 按技术 ID 锚定修复断链
├── theme/                          # 主题资源（Catppuccin CSS, Mermaid JS, CJK 搜索补丁）
└── src/                            # 文档源码
    ├── README.md                   # 知识库主页（双矩阵攻击链全景图 + 战术速览）
    ├── SUMMARY.md                  # mdBook 导航目录（Enterprise / ATLAS / 案例研究）
    ├── _data/                      # 官方数据快照与断链基线（不参与渲染）
    ├── _tools/                     # 审计与生成脚本（不参与渲染）
    ├── enterprise/                 # ATT&CK Enterprise 矩阵（15 个战术目录，880 篇文档）
    │   ├── 01-Reconnaissance/      # 侦察 - 12 个技术
    │   │   ├── README.md           # 战术概览
    │   │   ├── T1589-Gather-Victim-Identity-Information.md
    │   │   └── T1589/              # 子技术目录
    │   └── ...                     # 其余 14 个战术
    └── atlas/                      # MITRE ATLAS 矩阵（16 个战术目录 + 案例研究）
        ├── 01-Reconnaissance/      # 侦察 - 9 个技术
        ├── ...                     # 其余 15 个战术
        └── case-studies/           # 73 篇案例研究
```

---

## 本地构建

### 前置条件

- [Rust / Cargo](https://rustup.rs/)（用于安装 mdBook）
- Python 3.x、Node.js（CJK 搜索后处理）

### 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/tonydeng/attck-knowledge.git
cd attck-knowledge

# 2. 初始化环境（安装 mdBook、主题、Mermaid 插件）
bash scripts/setup.sh

# 3. 构建并预览
bash scripts/build.sh serve
# 浏览器打开 http://localhost:3000
```

### Windows 用户

```bat
:: 环境初始化
bash scripts\setup.sh

:: 构建并预览
scripts\build.bat serve
```

### 构建命令说明

| 命令 | 说明 |
|------|------|
| `bash scripts/build.sh` | 链接检查 → 预处理 Markdown → 构建静态网站 |
| `bash scripts/build.sh serve` | 预处理 → 本地预览（含热重载） |
| `bash scripts/build.sh build` | 预处理 → 仅构建 |
| `mdbook serve` | 直接预览（**不预处理**，修改 README 后链接可能失效） |

> **为什么需要预处理？** mdBook 将 `README.md` 渲染为 `index.html`，但 Markdown 链接中的 `README.md` 会被转为 `README.html`（404）。`preprocess-md.py` 自动修正这些链接，确保本地预览和线上部署均可正常访问。

---

## 推荐学习路径

### ATT&CK Enterprise

**基础篇（适合入门）**
1. **侦察** → **初始访问** → **执行**：攻击者如何踩点、进门、动手
2. **影响**：勒索软件、DDoS 等最直观的攻击手法

**进阶篇（需要一定基础）**
3. **持久化** → **权限提升**：攻击者在系统里安家和升权
4. **发现** → **横向移动**：摸清环境后跳转到更多系统

**高级篇（深入技术理解）**
5. **隐蔽** → **防御削弱**：隐身、关闭安全防护
6. **凭证访问** → **收集**：偷钥匙、拿数据
7. **命令与控制** → **渗漏**：遥控肉鸡、偷运数据

### MITRE ATLAS（AI/ML 对抗威胁）

1. **入门**：浏览各 [ATLAS 战术 README](./src/atlas/01-Reconnaissance/README.md) 的一句话理解 + [案例研究选读](./src/atlas/case-studies/README.md)——建立"AI 系统会被怎么打"的全景认知
2. **进阶**：提示词注入攻击链——LLM 提示词注入（AML.T0051）→ LLM 数据泄露（AML.T0057）→ LLM 响应渲染渗漏（AML.T0077）
3. **高级**：智能体攻击链——AI 智能体工具投毒（AML.T0110）→ 间接注入 → 智能体工具调用渗漏（AML.T0086）与数据破坏（AML.T0101）

---

## 文章结构

每篇技术文档按统一规范编写：

| 章节 | 内容 |
|------|------|
| **一句话通俗理解** | 生活化类比，秒懂技术本质 |
| **难度等级** | ⭐ ~ ⭐⭐⭐（ATLAS 文档采用官方 maturity 三级映射：Feasible=⭐ / Demonstrated=⭐⭐ / Realized=⭐⭐⭐） |
| **技术描述** | 通俗解释 + 技术原理 + 用途影响 |
| **子技术列表** | 全部子技术的中文说明 |
| **攻击流程** | 典型攻击步骤 + Mermaid 流程图 |
| **真实案例** | 2-4 个历史攻击事件（APT 组织、手法、参考链接） |
| **红队视角** | 实战技巧 + 常用工具 + 注意事项 |
| **蓝队视角** | 检测要点 + 监控建议 |
| **检测建议** | 网络层/主机层/应用层检测 + Sigma 规则示例 |
| **缓解措施** | 优先级分级（关键/重要/建议）+ MITRE 缓解映射 |
| **动手实验** | 实验环境 + 分级实验步骤 |
| **术语解释** | 关键术语中英文对照 + 通俗解释 |
| **参考资料** | 官方文档 + 安全报告 + 工具链接 |

> ATLAS 文档在此规范上增加两个特有板块：**「关联 ATT&CK 技术」**（官方 ATT&CK-reference 映射与对照表）与案例研究板块（标注直接命中/父级家族）。子技术难度为官方独立评定，非继承父技术。

---

## 数据来源

- [MITRE ATT&CK® Enterprise Matrix v20](https://attack.mitre.org/matrices/enterprise/)
- [MITRE ATT&CK STIX Data](https://github.com/mitre-attack/attack-stix-data)
- [MITRE ATLAS](https://atlas.mitre.org/)（AI/ML 对抗威胁矩阵）
- [MITRE ATLAS Data](https://github.com/mitre-atlas/atlas-data)（Apache 2.0）
- 互联网公开威胁情报、安全研究报告、APT 分析报告

---

## 许可证

本项目内容基于 MITRE ATT&CK® 与 MITRE ATLAS® 框架，遵循两者的使用条款（[ATT&CK Terms of Use](https://attack.mitre.org/resources/terms-of-use/)）。代码部分采用 MIT 许可证。
