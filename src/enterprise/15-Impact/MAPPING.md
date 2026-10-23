---
status: 【已完成】
template_version: "1.0"
last_updated: "2026-10-22"
tactic_id: "TA0040"
tactic_name_cn: "影响"
tactic_name_en: "Impact"
attack_version: "v20"
official_technique_count: 15
official_subtechnique_count: 18
local_technique_count: 15
local_subtechnique_count: 18
coverage_percentage: 100.0
---

# TA0040 影响 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v20 中 TA0040 (Impact/影响) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v20
- **官方数据**：15 项父技术 / 18 项子技术
- **本地数据**：15 项父技术 / 18 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1531 | Account Access Removal | 账户访问移除 | ./T1531-Account-Access-Removal.md | 0/0 | 📝 | - |
| T1485 | Data Destruction | 数据销毁 | ./T1485-Data-Destruction.md | 1/1 | 📝 | 子技术数frontmatter=0 |
| T1486 | Data Encrypted for Impact | 数据加密勒索 | ./T1486-Data-Encrypted-for-Impact.md | 0/0 | 📝 | - |
| T1565 | Data Manipulation | 数据篡改 | ./T1565-Data-Manipulation.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1491 | Defacement | 网页篡改 | ./T1491-Defacement.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1561 | Disk Wipe | 磁盘擦除 | ./T1561-Disk-Wipe.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1667 | Email Bombing | 邮件轰炸 | ./T1667-Email-Bombing.md | 0/0 | 📝 | - |
| T1499 | Endpoint Denial of Service | 端点拒绝服务 | ./T1499-Endpoint-Denial-of-Service.md | 4/4 | 📝 | 子技术数frontmatter=0 |
| T1657 | Financial Theft | 金融盗窃 | ./T1657-Financial-Theft.md | 0/0 | 📝 | - |
| T1495 | Firmware Corruption | 固件破坏 | ./T1495-Firmware-Corruption.md | 0/0 | 📝 | - |
| T1490 | Inhibit System Recovery | 阻止系统恢复 | ./T1490-Inhibit-System-Recovery.md | 0/0 | 📝 | - |
| T1498 | Network Denial of Service | 网络拒绝服务 | ./T1498-Network-Denial-of-Service.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1496 | Resource Hijacking | 资源劫持 | ./T1496-Resource-Hijacking.md | 4/4 | 📝 | 子技术数frontmatter=0 |
| T1489 | Service Stop | 停止服务 | ./T1489-Service-Stop.md | 0/0 | 📝 | - |
| T1529 | System Shutdown/Reboot | 系统关机重启 | ./T1529-System-Shutdown-Reboot.md | 0/0 | 📝 | 🔄 本地名: System Shutdown Reboot |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1485.001 | Lifecycle-Triggered Deletion | 生命周期触发删除 | T1485 | ./T1485/T1485.001-Lifecycle-Triggered-Deletion.md | 📝 | 🔄 本地名: Lifecycle Triggered Deletion |
| T1565.001 | Stored Data Manipulation | 存储数据篡改 | T1565 | ./T1565/T1565.001-Stored-Data-Manipulation.md | 📝 | - |
| T1565.002 | Transmitted Data Manipulation | 传输数据篡改 | T1565 | ./T1565/T1565.002-Transmitted-Data-Manipulation.md | 📝 | - |
| T1565.003 | Runtime Data Manipulation | 实时系统数据篡改 | T1565 | ./T1565/T1565.003-Runtime-Data-Manipulation.md | 📝 | - |
| T1491.001 | Internal Defacement | 内部网页篡改 | T1491 | ./T1491/T1491.001-Internal-Defacement.md | 📝 | - |
| T1491.002 | External Defacement | 外部网页篡改 | T1491 | ./T1491/T1491.002-External-Defacement.md | 📝 | - |
| T1561.001 | Disk Content Wipe | 磁盘内容擦除 | T1561 | ./T1561/T1561.001-Disk-Content-Wipe.md | 📝 | - |
| T1561.002 | Disk Structure Wipe | 磁盘结构擦除 | T1561 | ./T1561/T1561.002-Disk-Structure-Wipe.md | 📝 | - |
| T1499.001 | OS Exhaustion Flood | 操作系统资源耗尽 | T1499 | ./T1499/T1499.001-OS-Exhaustion-Flood.md | 📝 | - |
| T1499.002 | Service Exhaustion Flood | 服务资源耗尽 | T1499 | ./T1499/T1499.002-Service-Exhaustion-Flood.md | 📝 | - |
| T1499.003 | Application Exhaustion Flood | 应用层资源耗尽 | T1499 | ./T1499/T1499.003-Application-Exhaustion-Flood.md | 📝 | - |
| T1499.004 | Application or System Exploitation | 应用或系统漏洞利用 | T1499 | ./T1499/T1499.004-Application-or-System-Exploitation.md | 📝 | - |
| T1498.001 | Direct Network Flood | 直接网络洪水 | T1498 | ./T1498/T1498.001-Direct-Network-Flood.md | 📝 | - |
| T1498.002 | Reflection Amplification | 反射放大 | T1498 | ./T1498/T1498.002-Reflection-Amplification.md | 📝 | - |
| T1496.001 | Compute Hijacking | 计算资源劫持 | T1496 | ./T1496/T1496.001-Compute-Hijacking.md | 📝 | - |
| T1496.002 | Bandwidth Hijacking | 带宽资源劫持 | T1496 | ./T1496/T1496.002-Bandwidth-Hijacking.md | 📝 | - |
| T1496.003 | SMS Pumping | 短信轰炸 | T1496 | ./T1496/T1496.003-SMS-Pumping.md | 📝 | - |
| T1496.004 | Cloud Service Hijacking | 云服务劫持 | T1496 | ./T1496/T1496.004-Cloud-Service-Hijacking.md | 📝 | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v20已撤销或迁移

## 缺失与不一致清单

### 名称不一致 (2 项)
- **T1529** (parent): 官方=`System Shutdown/Reboot` vs 本地=`System Shutdown Reboot`
- **T1485.001** (subtech): 官方=`Lifecycle-Triggered Deletion` vs 本地=`Lifecycle Triggered Deletion`

## 参考来源

- [MITRE ATT&CK - TA0040](https://attack.mitre.org/tactics/TA0040/)
- [MITRE ATT&CK STIX Data v20](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-10-22
