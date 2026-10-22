---
status: 【已完成】
template_version: "1.0"
last_updated: "2026-10-22"
tactic_id: "TA0011"
tactic_name_cn: "命令与控制"
tactic_name_en: "Command and Control"
attack_version: "v20"
official_technique_count: 18
official_subtechnique_count: 27
local_technique_count: 18
local_subtechnique_count: 27
coverage_percentage: 100.0
---

# TA0011 命令与控制 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v20 中 TA0011 (Command and Control/命令与控制) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v20
- **官方数据**：18 项父技术 / 27 项子技术
- **本地数据**：18 项父技术 / 27 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1071 | Application Layer Protocol | 应用层协议 | ./T1071-Application-Layer-Protocol.md | 5/5 | 📝 | 子技术数frontmatter=0 |
| T1092 | Communication Through Removable Media | 通过可移动介质通信 | ./T1092-Communication-Through-Removable-Media.md | 0/0 | 📝 | - |
| T1659 | Content Injection | Content Injection | ./T1659-Content-Injection.md | 0/0 | 📝 | - |
| T1132 | Data Encoding | 数据编码 | ./T1132-Data-Encoding.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1001 | Data Obfuscation | 数据混淆 | ./T1001-Data-Obfuscation.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1568 | Dynamic Resolution | 动态解析 | ./T1568-Dynamic-Resolution.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1573 | Encrypted Channel | 加密通道 | ./T1573-Encrypted-Channel.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1008 | Fallback Channels | 备用通道 | ./T1008-Fallback-Channels.md | 0/0 | 📝 | - |
| T1665 | Hide Infrastructure | 隐藏基础设施 | ./T1665-Hide-Infrastructure.md | 0/0 | 📝 | - |
| T1105 | Ingress Tool Transfer | 工具导入 | ./T1105-Ingress-Tool-Transfer.md | 0/0 | 📝 | - |
| T1104 | Multi-Stage Channels | 多阶段通道 | ./T1104-Multi-Stage-Channels.md | 0/0 | 📝 | 🔄 本地名: Multi Stage Channels |
| T1095 | Non-Application Layer Protocol | 非应用层协议 | ./T1095-Non-Application-Layer-Protocol.md | 0/0 | 📝 | 🔄 本地名: Non Application Layer Protocol |
| T1571 | Non-Standard Port | 非标准端口 | ./T1571-Non-Standard-Port.md | 0/0 | 📝 | 🔄 本地名: Non Standard Port |
| T1572 | Protocol Tunneling | 协议隧道 | ./T1572-Protocol-Tunneling.md | 0/0 | 📝 | - |
| T1090 | Proxy | 代理 | ./T1090-Proxy.md | 4/4 | 📝 | 子技术数frontmatter=0 |
| T1219 | Remote Access Tools | 远程访问软件 | ./T1219-Remote-Access-Tools.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1205 | Traffic Signaling | 流量信号 | ./T1205-Traffic-Signaling.md | 2/2 | 📝 | 子技术数frontmatter=0 |
| T1102 | Web Service | Web服务 | ./T1102-Web-Service.md | 3/3 | 📝 | 子技术数frontmatter=0 |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1071.001 | Web Protocols | Web协议 | T1071 | ./T1071/T1071.001-Web-Protocols.md | 📝 | - |
| T1071.002 | File Transfer Protocols | 文件传输协议 | T1071 | ./T1071/T1071.002-File-Transfer-Protocols.md | 📝 | - |
| T1071.003 | Mail Protocols | 邮件协议 | T1071 | ./T1071/T1071.003-Mail-Protocols.md | 📝 | - |
| T1071.004 | DNS | DNS | T1071 | ./T1071/T1071.004-DNS.md | 📝 | - |
| T1071.005 | Publish/Subscribe Protocols | SMB | T1071 | ./T1071/T1071.005-Publish-subscribe-Protocols.md | 📝 | 🔄 本地名: Publish subscribe Protocols |
| T1132.001 | Standard Encoding | 标准编码 | T1132 | ./T1132/T1132.001-Standard-Encoding.md | 📝 | - |
| T1132.002 | Non-Standard Encoding | 非标准编码 | T1132 | ./T1132/T1132.002-Non-Standard-Encoding.md | 📝 | 🔄 本地名: Non Standard Encoding |
| T1001.001 | Junk Data | 垃圾数据 | T1001 | ./T1001/T1001.001-Junk-Data.md | 📝 | - |
| T1001.002 | Steganography | 隐写术 | T1001 | ./T1001/T1001.002-Steganography.md | 📝 | - |
| T1001.003 | Protocol or Service Impersonation | 协议模仿 | T1001 | ./T1001/T1001.003-Protocol-Or-Service-Impersonation.md | 📝 | 🔄 本地名: Protocol Or Service Impersonation |
| T1568.001 | Fast Flux DNS | Fast Flux DNS | T1568 | ./T1568/T1568.001-Fast-Flux-DNS.md | 📝 | - |
| T1568.002 | Domain Generation Algorithms | 域名生成算法（DGA） | T1568 | ./T1568/T1568.002-Domain-Generation-Algorithms.md | 📝 | - |
| T1568.003 | DNS Calculation | DNS计算 | T1568 | ./T1568/T1568.003-DNS-Calculation.md | 📝 | - |
| T1573.001 | Symmetric Cryptography | 对称加密 | T1573 | ./T1573/T1573.001-Symmetric-Cryptography.md | 📝 | - |
| T1573.002 | Asymmetric Cryptography | 非对称加密 | T1573 | ./T1573/T1573.002-Asymmetric-Cryptography.md | 📝 | - |
| T1090.001 | Internal Proxy | 内部代理 | T1090 | ./T1090/T1090.001-Internal-Proxy.md | 📝 | - |
| T1090.002 | External Proxy | 外部代理 | T1090 | ./T1090/T1090.002-External-Proxy.md | 📝 | - |
| T1090.003 | Multi-hop Proxy | 多跳代理 | T1090 | ./T1090/T1090.003-Multi-hop-Proxy.md | 📝 | 🔄 本地名: Multi hop Proxy |
| T1090.004 | Domain Fronting | Domain Fronting | T1090 | ./T1090/T1090.004-Domain-Fronting.md | 📝 | - |
| T1219.001 | IDE Tunneling | IDE Tunneling | T1219 | ./T1219/T1219.001-IDE-Tunneling.md | 📝 | - |
| T1219.002 | Remote Desktop Software | Remote Desktop Software | T1219 | ./T1219/T1219.002-Remote-Desktop-Software.md | 📝 | - |
| T1219.003 | Remote Access Hardware | Remote Access Hardware | T1219 | ./T1219/T1219.003-Remote-Access-Hardware.md | 📝 | - |
| T1205.001 | Port Knocking | 端口敲门 | T1205 | ./T1205/T1205.001-Port-Knocking.md | 📝 | - |
| T1205.002 | Socket Filters | 套接字过滤器 | T1205 | ./T1205/T1205.002-Socket-Filters.md | 📝 | - |
| T1102.001 | Dead Drop Resolver | 死户解析 | T1102 | ./T1102/T1102.001-Dead-Drop-Resolver.md | 📝 | - |
| T1102.002 | Bidirectional Communication | 双向通信 | T1102 | ./T1102/T1102.002-Bidirectional-Communication.md | 📝 | - |
| T1102.003 | One-Way Communication | One-Way Communication | T1102 | ./T1102/T1102.003-One-Way-Communication.md | 📝 | 🔄 本地名: One Way Communication |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v20已撤销或迁移

## 缺失与不一致清单

### 名称不一致 (8 项)
- **T1104** (parent): 官方=`Multi-Stage Channels` vs 本地=`Multi Stage Channels`
- **T1095** (parent): 官方=`Non-Application Layer Protocol` vs 本地=`Non Application Layer Protocol`
- **T1571** (parent): 官方=`Non-Standard Port` vs 本地=`Non Standard Port`
- **T1071.005** (subtech): 官方=`Publish/Subscribe Protocols` vs 本地=`Publish subscribe Protocols`
- **T1132.002** (subtech): 官方=`Non-Standard Encoding` vs 本地=`Non Standard Encoding`
- **T1001.003** (subtech): 官方=`Protocol or Service Impersonation` vs 本地=`Protocol Or Service Impersonation`
- **T1090.003** (subtech): 官方=`Multi-hop Proxy` vs 本地=`Multi hop Proxy`
- **T1102.003** (subtech): 官方=`One-Way Communication` vs 本地=`One Way Communication`

## 参考来源

- [MITRE ATT&CK - TA0011](https://attack.mitre.org/tactics/TA0011/)
- [MITRE ATT&CK STIX Data v20](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-10-22
