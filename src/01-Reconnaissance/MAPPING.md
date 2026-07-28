# TA0043 侦察 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v19.1 中 TA0043 (Reconnaissance/侦察) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v19.1
- **官方数据**：12 项父技术 / 34 项子技术
- **本地数据**：12 项父技术 / 34 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1595 | Active Scanning | 主动扫描 | ./T1595-Active-Scanning.md | 3/3 | ✅ | - |
| T1592 | Gather Victim Host Information | 收集受害者主机信息 | ./T1592-Gather-Victim-Host-Information.md | 4/4 | ✅ | - |
| T1589 | Gather Victim Identity Information | 收集受害者身份信息 | ./T1589-Gather-Victim-Identity-Information.md | 3/3 | ✅ | - |
| T1590 | Gather Victim Network Information | 收集受害者网络信息 | ./T1590-Gather-Victim-Network-Information.md | 6/6 | ✅ | - |
| T1591 | Gather Victim Org Information | 收集受害者组织信息 | ./T1591-Gather-Victim-Org-Information.md | 4/4 | ✅ | - |
| T1598 | Phishing for Information | 钓鱼获取信息 | ./T1598-Phishing-for-Information.md | 4/4 | ✅ | - |
| T1682 | Query Public AI Services | 查询公开AI服务 | ./T1682-Query-Public-AI-Services.md | 0/0 | ✅ | - |
| T1597 | Search Closed Sources | 搜索闭源资料 | ./T1597-Search-Closed-Sources.md | 2/2 | ✅ | - |
| T1596 | Search Open Technical Databases | 搜索开放技术数据库 | ./T1596-Search-Open-Technical-Databases.md | 5/5 | ✅ | - |
| T1593 | Search Open Websites/Domains | 搜索开放网站/域名 | ./T1593-Search-Open-Websites-Domains.md | 3/3 | ✅ | - |
| T1681 | Search Threat Vendor Data | 搜索威胁供应商数据 | ./T1681-Search-Threat-Vendor-Data.md | 0/0 | ✅ | - |
| T1594 | Search Victim-Owned Websites | 搜索受害者拥有的网站 | ./T1594-Search-Victim-Owned-Websites.md | 0/0 | ✅ | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1595.001 | Scanning IP Blocks | 扫描IP块 | T1595 | ./T1595/T1595.001-Scanning-IP-Blocks.md | ✅ | - |
| T1595.002 | Vulnerability Scanning | 漏洞扫描 | T1595 | ./T1595/T1595.002-Vulnerability-Scanning.md | ✅ | - |
| T1595.003 | Wordlist Scanning | 字典扫描 | T1595 | ./T1595/T1595.003-Wordlist-Scanning.md | ✅ | - |
| T1592.001 | Hardware | 硬件 | T1592 | ./T1592/T1592.001-Hardware.md | ✅ | - |
| T1592.002 | Software | 软件 | T1592 | ./T1592/T1592.002-Software.md | ✅ | - |
| T1592.003 | Firmware | 固件 | T1592 | ./T1592/T1592.003-Firmware.md | ✅ | - |
| T1592.004 | Client Configurations | 客户端配置 | T1592 | ./T1592/T1592.004-Client-Configurations.md | ✅ | - |
| T1589.001 | Credentials | 凭证收集 | T1589 | ./T1589/T1589.001-Credentials.md | ✅ | - |
| T1589.002 | Email Addresses | 电子邮件地址收集 | T1589 | ./T1589/T1589.002-Email-Addresses.md | ✅ | - |
| T1589.003 | Employee Names | 员工姓名收集 | T1589 | ./T1589/T1589.003-Employee-Names.md | ✅ | - |
| T1590.001 | Domain Properties | 域名属性 | T1590 | ./T1590/T1590.001-Domain-Properties.md | ✅ | - |
| T1590.002 | DNS | DNS协议 | T1590 | ./T1590/T1590.002-DNS.md | ✅ | - |
| T1590.003 | Network Trust Dependencies | 网络信任依赖 | T1590 | ./T1590/T1590.003-Network-Trust-Dependencies.md | ✅ | - |
| T1590.004 | Network Topology | 网络拓扑 | T1590 | ./T1590/T1590.004-Network-Topology.md | ✅ | - |
| T1590.005 | IP Addresses | IP地址 | T1590 | ./T1590/T1590.005-IP-Addresses.md | ✅ | - |
| T1590.006 | Network Security Appliances | 网络安全设备 | T1590 | ./T1590/T1590.006-Network-Security-Appliances.md | ✅ | - |
| T1591.001 | Determine Physical Locations | 确定物理位置 | T1591 | ./T1591/T1591.001-Determine-Physical-Locations.md | ✅ | - |
| T1591.002 | Business Relationships | 识别业务关系 | T1591 | ./T1591/T1591.002-Business-Relationships.md | ✅ | - |
| T1591.003 | Identify Business Tempo | 识别业务节奏 | T1591 | ./T1591/T1591.003-Identify-Business-Tempo.md | ✅ | - |
| T1591.004 | Identify Roles | 识别角色 | T1591 | ./T1591/T1591.004-Identify-Roles.md | ✅ | - |
| T1598.001 | Spearphishing Service | 服务型钓鱼 | T1598 | ./T1598/T1598.001-Spearphishing-Service.md | ✅ | - |
| T1598.002 | Spearphishing Attachment | 附件型钓鱼 | T1598 | ./T1598/T1598.002-Spearphishing-Attachment.md | ✅ | - |
| T1598.003 | Spearphishing Link | 链接型钓鱼 | T1598 | ./T1598/T1598.003-Spearphishing-Link.md | ✅ | - |
| T1598.004 | Spearphishing Voice | 语音型钓鱼 | T1598 | ./T1598/T1598.004-Spearphishing-Voice.md | ✅ | - |
| T1597.001 | Threat Intel Vendors | 威胁情报供应商 | T1597 | ./T1597/T1597.001-Threat-Intel-Vendors.md | ✅ | - |
| T1597.002 | Purchase Technical Data | 购买技术数据 | T1597 | ./T1597/T1597.002-Purchase-Technical-Data.md | ✅ | - |
| T1596.001 | DNS/Passive DNS | DNS/被动DNS | T1596 | ./T1596/T1596.001-DNS-Passive-DNS.md | ✅ | - |
| T1596.002 | WHOIS | WHOIS查询 | T1596 | ./T1596/T1596.002-WHOIS.md | ✅ | - |
| T1596.003 | Digital Certificates | 数字证书 | T1596 | ./T1596/T1596.003-Digital-Certificates.md | ✅ | - |
| T1596.004 | CDNs | CDN服务 | T1596 | ./T1596/T1596.004-Cdns.md | ✅ | - |
| T1596.005 | Scan Databases | 扫描数据库 | T1596 | ./T1596/T1596.005-Scan-Databases.md | ✅ | - |
| T1593.001 | Social Media | 社交媒体 | T1593 | ./T1593/T1593.001-Social-Media.md | ✅ | - |
| T1593.002 | Search Engines | 搜索引擎 | T1593 | ./T1593/T1593.002-Search-Engines.md | ✅ | - |
| T1593.003 | Code Repositories | 代码仓库 | T1593 | ./T1593/T1593.003-Code-Repositories.md | ✅ | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v19.1已撤销或迁移

## 缺失与不一致清单

无缺失或不一致项，本地知识库与 MITRE ATT&CK v19.1 官方数据完全对齐。
## 参考来源

- [MITRE ATT&CK - TA0043](https://attack.mitre.org/tactics/TA0043/)
- [MITRE ATT&CK STIX Data v19.1](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-07-28
