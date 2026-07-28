# TA0008 横向移动 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v19.1 中 TA0008 (Lateral Movement/横向移动) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v19.1
- **官方数据**：9 项父技术 / 14 项子技术
- **本地数据**：9 项父技术 / 14 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1210 | Exploitation of Remote Services | 远程服务漏洞利用 | ./T1210-Exploitation-of-Remote-Services.md | 0/0 | ✅ | - |
| T1534 | Internal Spearphishing | 内部鱼叉式钓鱼 | ./T1534-Internal-Spearphishing.md | 0/0 | ✅ | - |
| T1570 | Lateral Tool Transfer | 横向工具传输 | ./T1570-Lateral-Tool-Transfer.md | 0/0 | ✅ | - |
| T1563 | Remote Service Session Hijacking | 远程服务会话劫持 | ./T1563-Remote-Service-Session-Hijacking.md | 2/2 | ✅ | - |
| T1021 | Remote Services | 远程服务 | ./T1021-Remote-Services.md | 8/8 | ✅ | - |
| T1091 | Replication Through Removable Media |  | ./T1091-Replication-Through-Removable-Media.md | 0/0 | 📝 | - |
| T1072 | Software Deployment Tools |  | ./T1072-Software-Deployment-Tools.md | 0/0 | 📝 | - |
| T1080 | Taint Shared Content | 污染共享内容 | ./T1080-Taint-Shared-Content.md | 0/0 | ✅ | - |
| T1550 | Use Alternate Authentication Material | 使用替代认证材料 | ./T1550-Use-Alternate-Authentication-Material.md | 4/4 | ✅ | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1563.001 | SSH Hijacking | SSH劫持 | T1563 | ./T1563/T1563.001-SSH-Hijacking.md | ✅ | - |
| T1563.002 | RDP Hijacking | RDP劫持 | T1563 | ./T1563/T1563.002-RDP-Hijacking.md | ✅ | - |
| T1021.001 | Remote Desktop Protocol | 远程桌面协议 | T1021 | ./T1021/T1021.001-Remote-Desktop-Protocol.md | ✅ | - |
| T1021.002 | SMB/Windows Admin Shares | SMB/Windows管理共享 | T1021 | ./T1021/T1021.002-SMB-Admin-Shares.md | ✅ | - |
| T1021.003 | Distributed Component Object Model | 分布式组件对象模型 | T1021 | ./T1021/T1021.003-DCOM.md | ✅ | - |
| T1021.004 | SSH | SSH协议 | T1021 | ./T1021/T1021.004-SSH.md | ✅ | - |
| T1021.005 | VNC | VNC远程控制 | T1021 | ./T1021/T1021.005-VNC.md | ✅ | - |
| T1021.006 | Windows Remote Management | Windows远程管理 | T1021 | ./T1021/T1021.006-Windows-Remote-Management.md | ✅ | - |
| T1021.007 | Cloud Services | 微软管理控制台 | T1021 | ./T1021/T1021.007-Cloud-Services.md | ✅ | - |
| T1021.008 | Direct Cloud VM Connections | 远程桌面网关 | T1021 | ./T1021/T1021.008-Direct-Cloud-VM-Connections.md | ✅ | - |
| T1550.001 | Application Access Token | 应用访问令牌 | T1550 | ./T1550/T1550.001-Application-Access-Token.md | ✅ | - |
| T1550.002 | Pass the Hash | 哈希传递 | T1550 | ./T1550/T1550.002-Pass-the-Hash.md | ✅ | - |
| T1550.003 | Pass the Ticket | 票据传递 | T1550 | ./T1550/T1550.003-Pass-the-Ticket.md | ✅ | - |
| T1550.004 | Web Session Cookie | Web会话Cookie | T1550 | ./T1550/T1550.004-Web-Session-Cookie.md | ✅ | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v19.1已撤销或迁移

## 缺失与不一致清单

无缺失或不一致项，本地知识库与 MITRE ATT&CK v19.1 官方数据完全对齐。
## 参考来源

- [MITRE ATT&CK - TA0008](https://attack.mitre.org/tactics/TA0008/)
- [MITRE ATT&CK STIX Data v19.1](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-07-28
