---
status: 【已完成】
template_version: "1.0"
last_updated: "2026-10-22"
tactic_id: "TA0010"
tactic_name_cn: "渗漏"
tactic_name_en: "Exfiltration"
attack_version: "v20"
official_technique_count: 10
official_subtechnique_count: 10
local_technique_count: 10
local_subtechnique_count: 10
coverage_percentage: 100.0
---

# TA0010 渗漏 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v20 中 TA0010 (Exfiltration/渗漏) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v20
- **官方数据**：10 项父技术 / 10 项子技术
- **本地数据**：10 项父技术 / 10 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1700 | AI-Enabled Exfiltration | AI 驱动的数据渗漏 | ./T1700-AI-Enabled-Exfiltration.md | 0/0 | 📝 | 🔄 本地名: AI Enabled Exfiltration |
| T1020 | Automated Exfiltration | 自动化渗漏 | ./T1020-Automated-Exfiltration.md | 1/1 | 📝 | 子技术数frontmatter=0 |
| T1030 | Data Transfer Size Limits | 数据大小限制 | ./T1030-Data-Transfer-Size-Limits.md | 0/0 | 📝 | - |
| T1048 | Exfiltration Over Alternative Protocol | 通过替代协议渗漏 | ./T1048-Exfiltration-Over-Alternative-Protocol.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1041 | Exfiltration Over C2 Channel | 通过C2通道渗漏 | ./T1041-Exfiltration-Over-C2-Channel.md | 0/0 | 📝 | - |
| T1011 | Exfiltration Over Other Network Medium | 通过其他网络介质渗漏 | ./T1011-Exfiltration-Over-Other-Network-Medium.md | 1/1 | 📝 | 子技术数frontmatter=0 |
| T1052 | Exfiltration Over Physical Medium | 通过物理介质渗漏 | ./T1052-Exfiltration-Over-Physical-Medium.md | 1/1 | 📝 | 子技术数frontmatter=0 |
| T1567 | Exfiltration Over Web Service | 通过Web服务渗漏 | ./T1567-Exfiltration-Over-Web-Service.md | 4/4 | 📝 | 子技术数frontmatter=0 |
| T1029 | Scheduled Transfer | 定时传输 | ./T1029-Scheduled-Transfer.md | 0/0 | 📝 | - |
| T1537 | Transfer Data to Cloud Account | 传输数据到云账户 | ./T1537-Transfer-Data-to-Cloud-Account.md | 0/0 | 📝 | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1020.001 | Traffic Duplication | 流量复制 | T1020 | ./T1020/T1020.001-Traffic-Duplication.md | 📝 | - |
| T1048.001 | Exfiltration Over Symmetric Encrypted Non-C2 Protocol | 通过对称加密非 C2 协议外传 | T1048 | ./T1048/T1048.001-Exfiltration-Over-Symmetric-Encrypted-Non-C2-Protocol.md | 📝 | 🔄 本地名: Exfiltration Over Symmetric Encrypted Non C2 Protocol |
| T1048.002 | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | 通过非对称加密非 C2 协议外传 | T1048 | ./T1048/T1048.002-Exfiltration-Over-Asymmetric-Encrypted-Non-C2-Protocol.md | 📝 | 🔄 本地名: Exfiltration Over Asymmetric Encrypted Non C2 Protocol |
| T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | 未加密渗出 | T1048 | ./T1048/T1048.003-Exfiltration-Over-Unencrypted-Non-C2-Protocol.md | 📝 | 🔄 本地名: Exfiltration Over Unencrypted Non C2 Protocol |
| T1011.001 | Exfiltration Over Bluetooth | 通过蓝牙渗漏 | T1011 | ./T1011/T1011.001-Exfiltration-Over-Bluetooth.md | 📝 | - |
| T1052.001 | Exfiltration over USB | USB | T1052 | ./T1052/T1052.001-Exfiltration-Over-USB.md | 📝 | 🔄 本地名: Exfiltration Over USB |
| T1567.001 | Exfiltration to Code Repository | 外传至代码仓库 | T1567 | ./T1567/T1567.001-Exfiltration-to-Code-Repository.md | 📝 | - |
| T1567.002 | Exfiltration to Cloud Storage | 外传至云存储 | T1567 | ./T1567/T1567.002-Exfiltration-to-Cloud-Storage.md | 📝 | - |
| T1567.003 | Exfiltration to Text Storage Sites | 文本分享网站 | T1567 | ./T1567/T1567.003-Exfiltration-To-Text-Storage-Sites.md | 📝 | 🔄 本地名: Exfiltration To Text Storage Sites |
| T1567.004 | Exfiltration Over Webhook | Webhook | T1567 | ./T1567/T1567.004-Exfiltration-Over-Webhook.md | 📝 | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v20已撤销或迁移

## 缺失与不一致清单

### 名称不一致 (6 项)
- **T1700** (parent): 官方=`AI-Enabled Exfiltration` vs 本地=`AI Enabled Exfiltration`
- **T1048.001** (subtech): 官方=`Exfiltration Over Symmetric Encrypted Non-C2 Protocol` vs 本地=`Exfiltration Over Symmetric Encrypted Non C2 Protocol`
- **T1048.002** (subtech): 官方=`Exfiltration Over Asymmetric Encrypted Non-C2 Protocol` vs 本地=`Exfiltration Over Asymmetric Encrypted Non C2 Protocol`
- **T1048.003** (subtech): 官方=`Exfiltration Over Unencrypted Non-C2 Protocol` vs 本地=`Exfiltration Over Unencrypted Non C2 Protocol`
- **T1052.001** (subtech): 官方=`Exfiltration over USB` vs 本地=`Exfiltration Over USB`
- **T1567.003** (subtech): 官方=`Exfiltration to Text Storage Sites` vs 本地=`Exfiltration To Text Storage Sites`

## 参考来源

- [MITRE ATT&CK - TA0010](https://attack.mitre.org/tactics/TA0010/)
- [MITRE ATT&CK STIX Data v20](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-10-22
