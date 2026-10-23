---
status: 【已完成】
template_version: "1.0"
last_updated: "2026-10-22"
tactic_id: "TA0007"
tactic_name_cn: "发现"
tactic_name_en: "Discovery"
attack_version: "v20"
official_technique_count: 34
official_subtechnique_count: 15
local_technique_count: 34
local_subtechnique_count: 15
coverage_percentage: 100.0
---

# TA0007 发现 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v20 中 TA0007 (Discovery/发现) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v20
- **官方数据**：34 项父技术 / 15 项子技术
- **本地数据**：34 项父技术 / 15 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1087 | Account Discovery | 账户发现 | ./T1087-Account-Discovery.md | 4/4 | 📝 | 子技术数frontmatter=0 |
| T1010 | Application Window Discovery | 应用程序窗口发现 | ./T1010-Application-Window-Discovery.md | 0/0 | 📝 | - |
| T1217 | Browser Information Discovery | 浏览器书签发现 | ./T1217-Browser-Information-Discovery.md | 0/0 | 📝 | - |
| T1580 | Cloud Infrastructure Discovery | 云基础设施发现 | ./T1580-Cloud-Infrastructure-Discovery.md | 0/0 | 📝 | - |
| T1538 | Cloud Service Dashboard | 云服务仪表盘 | ./T1538-Cloud-Service-Dashboard.md | 0/0 | 📝 | - |
| T1526 | Cloud Service Discovery | 云服务发现 | ./T1526-Cloud-Service-Discovery.md | 0/0 | 📝 | - |
| T1619 | Cloud Storage Object Discovery | 云存储对象发现 | ./T1619-Cloud-Storage-Object-Discovery.md | 0/0 | 📝 | - |
| T1613 | Container and Resource Discovery | 容器和资源发现 | ./T1613-Container-and-Resource-Discovery.md | 0/0 | 📝 | - |
| T1622 | Debugger Evasion | 调试器规避 | ./T1622-Debugger-Evasion.md | 0/0 | 📝 | - |
| T1652 | Device Driver Discovery | 设备驱动发现 | ./T1652-Device-Driver-Discovery.md | 0/0 | 📝 | - |
| T1482 | Domain Trust Discovery | 域信任发现 | ./T1482-Domain-Trust-Discovery.md | 0/0 | 📝 | - |
| T1083 | File and Directory Discovery | 文件和目录发现 | ./T1083-File-and-Directory-Discovery.md | 0/0 | 📝 | - |
| T1615 | Group Policy Discovery | 组策略发现 | ./T1615-Group-Policy-Discovery.md | 0/0 | 📝 | - |
| T1680 | Local Storage Discovery | 本地存储发现 | ./T1680-Local-Storage-Discovery.md | 0/0 | 📝 | - |
| T1654 | Log Enumeration | 日志枚举 | ./T1654-Log-Enumeration.md | 0/0 | 📝 | - |
| T1046 | Network Service Discovery | 网络服务扫描 | ./T1046-Network-Service-Discovery.md | 0/0 | 📝 | - |
| T1135 | Network Share Discovery | 网络共享发现 | ./T1135-Network-Share-Discovery.md | 0/0 | 📝 | - |
| T1040 | Network Sniffing | Network Sniffing | ./T1040-Network-Sniffing.md | 0/0 | 📝 | - |
| T1201 | Password Policy Discovery | 密码策略发现 | ./T1201-Password-Policy-Discovery.md | 0/0 | 📝 | - |
| T1120 | Peripheral Device Discovery | 外围设备发现 | ./T1120-Peripheral-Device-Discovery.md | 0/0 | 📝 | - |
| T1069 | Permission Groups Discovery | 权限组发现 | ./T1069-Permission-Groups-Discovery.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1057 | Process Discovery | 进程发现 | ./T1057-Process-Discovery.md | 0/0 | 📝 | - |
| T1012 | Query Registry | 查询注册表 | ./T1012-Query-Registry.md | 0/0 | 📝 | - |
| T1018 | Remote System Discovery | 远程系统发现 | ./T1018-Remote-System-Discovery.md | 0/0 | 📝 | - |
| T1518 | Software Discovery | 软件发现 | ./T1518-Software-Discovery.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1082 | System Information Discovery | 系统信息发现 | ./T1082-System-Information-Discovery.md | 0/0 | 📝 | - |
| T1614 | System Location Discovery | 系统位置发现 | ./T1614-System-Location-Discovery.md | 1/1 | 📝 | 子技术数frontmatter=0 |
| T1016 | System Network Configuration Discovery | 系统网络配置发现 | ./T1016-System-Network-Configuration-Discovery.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1049 | System Network Connections Discovery | 系统网络连接发现 | ./T1049-System-Network-Connections-Discovery.md | 0/0 | 📝 | - |
| T1033 | System Owner/User Discovery | 系统所有者/用户发现 | ./T1033-System-Owner-User-Discovery.md | 0/0 | 📝 | 🔄 本地名: System Owner User Discovery |
| T1007 | System Service Discovery | 系统服务发现 | ./T1007-System-Service-Discovery.md | 0/0 | 📝 | - |
| T1124 | System Time Discovery | 系统时间发现 | ./T1124-System-Time-Discovery.md | 0/0 | 📝 | - |
| T1673 | Virtual Machine Discovery | 虚拟机发现 | ./T1673-Virtual-Machine-Discovery.md | 0/0 | 📝 | - |
| T1497 | Virtualization/Sandbox Evasion | 虚拟化/沙箱规避 | ./T1497-Virtualization-Sandbox-Evasion.md | 3/3 | 📝 | 🔄 本地名: Virtualization Sandbox Evasion | 子技术数frontmatter=0 |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1087.001 | Local Account | Local Account | T1087 | ./T1087/T1087.001-Local-Account.md | 📝 | - |
| T1087.002 | Domain Account | Domain Account | T1087 | ./T1087/T1087.002-Domain-Account.md | 📝 | - |
| T1087.003 | Email Account | Email Account | T1087 | ./T1087/T1087.003-Email-Account.md | 📝 | - |
| T1087.004 | Cloud Account | Cloud Account | T1087 | ./T1087/T1087.004-Cloud-Account.md | 📝 | - |
| T1069.001 | Local Groups | Local Groups | T1069 | ./T1069/T1069.001-Local-Groups.md | 📝 | - |
| T1069.002 | Domain Groups | Domain Groups | T1069 | ./T1069/T1069.002-Domain-Groups.md | 📝 | - |
| T1069.003 | Cloud Groups | Cloud Groups | T1069 | ./T1069/T1069.003-Cloud-Groups.md | 📝 | - |
| T1518.001 | Security Software Discovery | 安全软件发现 | T1518 | ./T1518/T1518.001-Security-Software-Discovery.md | 📝 | - |
| T1518.002 | Backup Software Discovery | 已安装软件 | T1518 | ./T1518/T1518.002-Backup-Software-Discovery.md | 📝 | - |
| T1614.001 | System Language Discovery | 系统语言发现 | T1614 | ./T1614/T1614.001-System-Language-Discovery.md | 📝 | - |
| T1016.001 | Internet Connection Discovery | Internet Connection Discovery | T1016 | ./T1016/T1016.001-Internet-Connection-Discovery.md | 📝 | - |
| T1016.002 | Wi-Fi Discovery | Wi-Fi Discovery | T1016 | ./T1016/T1016.002-Wi-Fi-Discovery.md | 📝 | 🔄 本地名: Wi Fi Discovery |
| T1497.001 | System Checks | 系统检查 | T1497 | ./T1497/T1497.001-System-Checks.md | 📝 | - |
| T1497.002 | User Activity Based Checks | 基于用户活动的检查 | T1497 | ./T1497/T1497.002-User-Activity-Based-Checks.md | 📝 | - |
| T1497.003 | Time Based Checks | 基于时间的规避 | T1497 | ./T1497/T1497.003-Time-Based-Checks.md | 📝 | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v20已撤销或迁移

## 缺失与不一致清单

### 名称不一致 (3 项)
- **T1033** (parent): 官方=`System Owner/User Discovery` vs 本地=`System Owner User Discovery`
- **T1497** (parent): 官方=`Virtualization/Sandbox Evasion` vs 本地=`Virtualization Sandbox Evasion`
- **T1016.002** (subtech): 官方=`Wi-Fi Discovery` vs 本地=`Wi Fi Discovery`

## 参考来源

- [MITRE ATT&CK - TA0007](https://attack.mitre.org/tactics/TA0007/)
- [MITRE ATT&CK STIX Data v20](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-10-22
