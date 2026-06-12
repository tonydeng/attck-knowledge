# ATT&CK 知识库

[![mdbook build](https://github.com/tonydeng/attck-knowledge/actions/workflows/deploy.yml/badge.svg)](https://github.com/tonydeng/attck-knowledge/actions/workflows/deploy.yml)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-online-brightgreen)](https://tonydeng.github.io/attck-knowledge/)
[![MITRE ATT&CK v19](https://img.shields.io/badge/MITRE%20ATT%26CK-v19-blue)](https://attack.mitre.org/matrices/enterprise/)
[![中文](https://img.shields.io/badge/lang-中文-red)](.)

基于 [MITRE ATT&CK® v19 Enterprise](https://attack.mitre.org/matrices/enterprise/) 矩阵的完整中文知识库，覆盖全部 **15 个战术**、**254 个技术** 和 **900+ 个子技术**。

> 每篇技术文档包含：通俗理解、技术原理、真实案例、红蓝队视角、检测建议、动手实验。适合安全分析师、渗透测试工程师、蓝队防御人员、安全学习者阅读。

---

## 在线阅读

📖 **[attck-knowledge.vercel.app](https://attck-knowledge.vercel.app/)**（推荐，带全文搜索 + Mermaid 图表）

或直接访问 GitHub Pages：[tonydeng.github.io/attck-knowledge](https://tonydeng.github.io/attck-knowledge/)

---

## 内容概览

| 序号 | 战术名称 | TA ID | 技术数 | 子技术数 | 目录 |
|:---:|---------|:-----:|:------:|:--------:|------|
| 01 | 侦察 | TA0043 | 12 | 34 | [`01-Reconnaissance`](./src/01-Reconnaissance/README.md) |
| 02 | 资源开发 | TA0042 | 10 | 41 | [`02-Resource-Development`](./src/02-Resource-Development/README.md) |
| 03 | 初始访问 | TA0001 | 10 | 11 | [`03-Initial-Access`](./src/03-Initial-Access/README.md) |
| 04 | 执行 | TA0002 | 20 | 46 | [`04-Execution`](./src/04-Execution/README.md) |
| 05 | 持久化 | TA0003 | 25 | 106 | [`05-Persistence`](./src/05-Persistence/README.md) |
| 06 | 权限提升 | TA0004 | 13 | 89 | [`06-Privilege-Escalation`](./src/06-Privilege-Escalation/README.md) |
| 07 | 隐蔽 | TA0005 | 25 | 172 | [`07-Stealth`](./src/07-Stealth/README.md) |
| 08 | 防御削弱 | TA0112 | 24 | 134 | [`08-Defense-Impairment`](./src/08-Defense-Impairment/README.md) |
| 09 | 凭证访问 | TA0006 | 19 | 63 | [`09-Credential-Access`](./src/09-Credential-Access/README.md) |
| 10 | 发现 | TA0007 | 34 | 24 | [`10-Discovery`](./src/10-Discovery/README.md) |
| 11 | 横向移动 | TA0008 | 11 | 14 | [`11-Lateral-Movement`](./src/11-Lateral-Movement/README.md) |
| 12 | 收集 | TA0009 | 17 | 18 | [`12-Collection`](./src/12-Collection/README.md) |
| 13 | 命令与控制 | TA0011 | 18 | 33 | [`13-Command-and-Control`](./src/13-Command-and-Control/README.md) |
| 14 | 渗漏 | TA0010 | 9 | 9 | [`14-Exfiltration`](./src/14-Exfiltration/README.md) |
| 15 | 影响 | TA0040 | 11 | 12 | [`15-Impact`](./src/15-Impact/README.md) |

> **总计**：274 篇文档（15 篇战术概览 + 259 篇技术文档），覆盖 254 个技术、900+ 子技术

---

## 项目结构

```
attck-knowledge/
├── .github/workflows/deploy.yml   # GitHub Pages CI/CD
├── book.toml                       # mdBook 配置（Catppuccin 主题 + Mermaid + CJK 搜索）
├── scripts/
│   ├── preprocess-md.py            # 链接预处理（构建前自动修复 README.md 链接）
│   ├── build.sh / build.bat        # 构建脚本（预处理 + mdbook build）
│   ├── setup.sh                    # 本地环境初始化
│   ├── gen-summary.py              # SUMMARY.md 自动生成器
│   └── strip-frontmatter.py        # YAML front matter 剥离（一次性）
├── theme/                          # 主题资源（Catppuccin CSS, Mermaid JS）
└── src/                            # 文档源码
    ├── README.md                   # 知识库主页（攻击链全景图 + 战术速览）
    ├── SUMMARY.md                  # mdBook 导航目录
    ├── 01-Reconnaissance/          # 侦察 - 12 个技术
    │   ├── README.md               # 战术概览
    │   ├── T1589-Gather-Victim-Identity-Information.md
    │   └── ...
    ├── 02-Resource-Development/    # 资源开发 - 10 个技术
    └── ...                         # 其余 13 个战术
```

---

## 本地构建

### 前置条件

- [Rust / Cargo](https://rustup.rs/)（用于安装 mdBook）
- Python 3.x

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
| `bash scripts/build.sh` | 预处理 Markdown → 构建静态网站 |
| `bash scripts/build.sh serve` | 预处理 → 本地预览（含热重载） |
| `bash scripts/build.sh build` | 预处理 → 仅构建 |
| `mdbook serve` | 直接预览（**不预处理**，修改 README 后链接可能失效） |

> **为什么需要预处理？** mdBook 将 `README.md` 渲染为 `index.html`，但 Markdown 链接中的 `README.md` 会被转为 `README.html`（404）。`preprocess-md.py` 自动修正这些链接，确保本地预览和线上部署均可正常访问。

---

## 推荐学习路径

### 基础篇（适合入门）
1. **侦察** → **初始访问** → **执行**：攻击者如何踩点、进门、动手
2. **影响**：勒索软件、DDoS 等最直观的攻击手法

### 进阶篇（需要一定基础）
3. **持久化** → **权限提升**：攻击者在系统里安家和升权
4. **发现** → **横向移动**：摸清环境后跳转到更多系统

### 高级篇（深入技术理解）
5. **隐蔽** → **防御削弱**：隐身、关闭安全防护
6. **凭证访问** → **收集**：偷钥匙、拿数据
7. **命令与控制** → **渗漏**：遥控肉鸡、偷运数据

---

## 文章结构

每篇技术文档按统一规范编写：

| 章节 | 内容 |
|------|------|
| **一句话通俗理解** | 生活化类比，秒懂技术本质 |
| **难度等级** | ⭐ ~ ⭐⭐⭐ |
| **技术描述** | 通俗解释 + 技术原理 + 用途影响 |
| **子技术列表** | 全部子技术的中文说明 |
| **攻击流程** | 典型攻击步骤 + Mermaid 流程图 |
| **真实案例** | 2-4 个历史攻击事件（APT 组织、手法、参考链接） |
| **红队视角** | 实战技巧 + 常用工具 + 注意事项 |
| **蓝队视角** | 检测要点 + 监控建议 |
| **检测建议** | 网络层/主机层/应用层检测 + Sigma 规则示例 |
| **缓解措施** | 优先级分级（关键/重要/建议）+ MITRE 缓解映射 |
| **动手实验** | 实验环境 + 分级实验步骤 |
| **参考资料** | 官方文档 + 安全报告 + 工具链接 |

---

## 数据来源

- [MITRE ATT&CK® Enterprise Matrix v19](https://attack.mitre.org/matrices/enterprise/)
- [MITRE ATT&CK STIX Data](https://github.com/mitre-attack/attack-stix-data)
- 互联网公开威胁情报、安全研究报告、APT 分析报告

---

## 许可证

本项目内容基于 MITRE ATT&CK® 框架，遵循 ATT&CK 的 [使用条款](https://attack.mitre.org/resources/terms-of-use/)。代码部分采用 MIT 许可证。
