---
status: 【已完成】
template_version: "1.0"
last_updated: "2026-10-22"
tactic_id: "TA0009"
tactic_name_cn: "收集"
tactic_name_en: "Collection"
attack_version: "v20"
official_technique_count: 17
official_subtechnique_count: 24
local_technique_count: 17
local_subtechnique_count: 24
coverage_percentage: 100.0
---

# TA0009 收集 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v20 中 TA0009 (Collection/收集) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v20
- **官方数据**：17 项父技术 / 24 项子技术
- **本地数据**：17 项父技术 / 24 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1557 | Adversary-in-the-Middle | 中间人攻击 | ./T1557-Adversary-in-the-Middle.md | 4/4 | 📝 | 🔄 本地名: Adversary in the Middle | 子技术数frontmatter=0 |
| T1560 | Archive Collected Data | 压缩收集的数据 | ./T1560-Archive-Collected-Data.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1123 | Audio Capture | 音频捕获 | ./T1123-Audio-Capture.md | 0/0 | 📝 | - |
| T1119 | Automated Collection | 自动化收集 | ./T1119-Automated-Collection.md | 0/0 | 📝 | - |
| T1185 | Browser Session Hijacking | 浏览器会话劫持 | ./T1185-Browser-Session-Hijacking.md | 0/0 | 📝 | - |
| T1115 | Clipboard Data | 剪贴板数据 | ./T1115-Clipboard-Data.md | 0/0 | 📝 | - |
| T1530 | Data from Cloud Storage | 从云存储收集数据 | ./T1530-Data-from-Cloud-Storage.md | 0/0 | 📝 | - |
| T1602 | Data from Configuration Repository | 来自配置存储库的数据 | ./T1602-Data-from-Configuration-Repository.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1213 | Data from Information Repositories | 从信息仓库收集数据 | ./T1213-Data-from-Information-Repositories.md | 6/6 | 📝 | 子技术数frontmatter=0 |
| T1005 | Data from Local System | 本地系统数据 | ./T1005-Data-from-Local-System.md | 0/0 | 📝 | - |
| T1039 | Data from Network Shared Drive | 网络共享数据 | ./T1039-Data-from-Network-Shared-Drive.md | 0/0 | 📝 | - |
| T1025 | Data from Removable Media | 可移动介质数据 | ./T1025-Data-from-Removable-Media.md | 0/0 | 📝 | - |
| T1074 | Data Staged | 数据分段 | ./T1074-Data-Staged.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1114 | Email Collection | 邮件收集 | ./T1114-Email-Collection.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1056 | Input Capture | 输入捕获 | ./T1056-Input-Capture.md | 4/4 | 📝 | 子技术数frontmatter=0 |
| T1113 | Screen Capture | 屏幕捕获 | ./T1113-Screen-Capture.md | 0/0 | 📝 | - |
| T1125 | Video Capture | 视频捕获 | ./T1125-Video-Capture.md | 0/0 | 📝 | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1557.001 | Name Resolution Poisoning and SMB Relay | LLMNR/NBT-NS中毒和Windows名称解析欺骗 | T1557 | ./T1557/T1557.001-Name-Resolution-Poisoning-And-SMB-Relay.md | 📝 | 🔄 本地名: Name Resolution Poisoning And SMB Relay |
| T1557.002 | ARP Cache Poisoning | ARP缓存中毒 | T1557 | ./T1557/T1557.002-ARP-Cache-Poisoning.md | 📝 | - |
| T1557.003 | DHCP Spoofing | DHCP欺骗 | T1557 | ./T1557/T1557.003-DHCP-Spoofing.md | 📝 | - |
| T1557.004 | Evil Twin | Evil Twin | T1557 | ./T1557/T1557.004-Evil-Twin.md | 📝 | - |
| T1560.001 | Archive via Utility | 使用工具归档 | T1560 | ./T1560/T1560.001-Archive-via-Utility.md | 📝 | - |
| T1560.002 | Archive via Library | 通过库归档 | T1560 | ./T1560/T1560.002-Archive-via-Library.md | 📝 | - |
| T1560.003 | Archive via Custom Method | 通过内置命令归档 | T1560 | ./T1560/T1560.003-Archive-Via-Custom-Method.md | 📝 | 🔄 本地名: Archive Via Custom Method |
| T1602.001 | SNMP (MIB Dump) | SNMP（MIB 转储） | T1602 | ./T1602/T1602.001-SNMP-MIB-Dump.md | 📝 | 🔄 本地名: SNMP MIB Dump |
| T1602.002 | Network Device Configuration Dump | 通过网络设备管理收集 | T1602 | ./T1602/T1602.002-Network-Device-Configuration-Dump.md | 📝 | - |
| T1213.001 | Confluence | 从Confluence Wiki收集 | T1213 | ./T1213/T1213.001-Confluence.md | 📝 | - |
| T1213.002 | Sharepoint | 从SharePoint收集 | T1213 | ./T1213/T1213.002-Sharepoint.md | 📝 | - |
| T1213.003 | Code Repositories | 从代码仓库收集 | T1213 | ./T1213/T1213.003-Code-Repositories.md | 📝 | - |
| T1213.004 | Customer Relationship Management Software | 客户关系管理软件 | T1213 | ./T1213/T1213.004-Customer-Relationship-Management-Software.md | 📝 | - |
| T1213.005 | Messaging Applications | Messaging Applications | T1213 | ./T1213/T1213.005-Messaging-Applications.md | 📝 | - |
| T1213.006 | Databases | Databases | T1213 | ./T1213/T1213.006-Databases.md | 📝 | - |
| T1074.001 | Local Data Staging | 本地数据分段 | T1074 | ./T1074/T1074.001-Local-Data-Staging.md | 📝 | - |
| T1074.002 | Remote Data Staging | 远程数据分段 | T1074 | ./T1074/T1074.002-Remote-Data-Staging.md | 📝 | - |
| T1114.001 | Local Email Collection | 本地邮件收集 | T1114 | ./T1114/T1114.001-Local-Email-Collection.md | 📝 | - |
| T1114.002 | Remote Email Collection | 远程邮件收集 | T1114 | ./T1114/T1114.002-Remote-Email-Collection.md | 📝 | - |
| T1114.003 | Email Forwarding Rule | 电子邮件转发规则 | T1114 | ./T1114/T1114.003-Email-Forwarding-Rule.md | 📝 | - |
| T1056.001 | Keylogging | 键盘记录 Keylogging | T1056 | ./T1056/T1056.001-Keylogging.md | 📝 | - |
| T1056.002 | GUI Input Capture | GUI输入捕获 | T1056 | ./T1056/T1056.002-GUI-Input-Capture.md | 📝 | - |
| T1056.003 | Web Portal Capture | Web门户捕获 | T1056 | ./T1056/T1056.003-Web-Portal-Capture.md | 📝 | - |
| T1056.004 | Credential API Hooking | 凭证API钩取 | T1056 | ./T1056/T1056.004-Credential-API-Hooking.md | 📝 | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v20已撤销或迁移

## 缺失与不一致清单

### 名称不一致 (4 项)
- **T1557** (parent): 官方=`Adversary-in-the-Middle` vs 本地=`Adversary in the Middle`
- **T1557.001** (subtech): 官方=`Name Resolution Poisoning and SMB Relay` vs 本地=`Name Resolution Poisoning And SMB Relay`
- **T1560.003** (subtech): 官方=`Archive via Custom Method` vs 本地=`Archive Via Custom Method`
- **T1602.001** (subtech): 官方=`SNMP (MIB Dump)` vs 本地=`SNMP MIB Dump`

## 参考来源

- [MITRE ATT&CK - TA0009](https://attack.mitre.org/tactics/TA0009/)
- [MITRE ATT&CK STIX Data v20](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-10-22
