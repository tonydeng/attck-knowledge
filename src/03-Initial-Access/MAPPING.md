# TA0001 初始访问 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v19.1 中 TA0001 (Initial Access/初始访问) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v19.1
- **官方数据**：11 项父技术 / 11 项子技术
- **本地数据**：11 项父技术 / 11 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1659 | Content Injection | 内容注入 | ./T1659-Content-Injection.md | 0/0 | ✅ | - |
| T1189 | Drive-by Compromise | 水坑攻击 | ./T1189-Drive-by-Compromise.md | 0/0 | ✅ | - |
| T1190 | Exploit Public-Facing Application | 利用面向公众的应用 | ./T1190-Exploit-Public-Facing-Application.md | 0/0 | ✅ | - |
| T1133 | External Remote Services |  | ./T1133-External-Remote-Services.md | 0/0 | 📝 | - |
| T1200 | Hardware Additions | 硬件添加 | ./T1200-Hardware-Additions.md | 0/0 | ✅ | - |
| T1566 | Phishing | 钓鱼 | ./T1566-Phishing.md | 4/4 | ✅ | - |
| T1091 | Replication Through Removable Media | 通过可移动介质复制 | ./T1091-Replication-Through-Removable-Media.md | 0/0 | ✅ | - |
| T1195 | Supply Chain Compromise | 供应链妥协 | ./T1195-Supply-Chain-Compromise.md | 3/3 | ✅ | - |
| T1199 | Trusted Relationship | 信任关系 | ./T1199-Trusted-Relationship.md | 0/0 | ✅ | - |
| T1078 | Valid Accounts | 有效账户 | ./T1078-Valid-Accounts.md | 4/4 | ✅ | 子技术数frontmatter=5 |
| T1669 | Wi-Fi Networks | Wi-Fi网络 | ./T1669-Wi-Fi-Networks.md | 0/0 | ✅ | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1566.001 | Spearphishing Attachment | 鱼叉式钓鱼附件 | T1566 | ./T1566/T1566.001-Spearphishing-Attachment.md | ✅ | - |
| T1566.002 | Spearphishing Link | 鱼叉式钓鱼链接 | T1566 | ./T1566/T1566.002-Spearphishing-Link.md | ✅ | - |
| T1566.003 | Spearphishing via Service | 通过服务进行鱼叉式钓鱼 | T1566 | ./T1566/T1566.003-Spearphishing-via-Service.md | ✅ | - |
| T1566.004 | Spearphishing Voice | 鱼叉式钓鱼语音（Vishing） | T1566 | ./T1566/T1566.004-Spearphishing-Voice.md | ✅ | - |
| T1195.001 | Compromise Software Dependencies and Development Tools | 破坏软件依赖和开发工具 | T1195 | ./T1195/T1195.001-Compromise-Software-Dependencies-And-Development-Tools.md | ✅ | - |
| T1195.002 | Compromise Software Supply Chain | 破坏软件供应链 | T1195 | ./T1195/T1195.002-Compromise-Software-Supply-Chain.md | ✅ | - |
| T1195.003 | Compromise Hardware Supply Chain | 破坏硬件供应链 | T1195 | ./T1195/T1195.003-Compromise-Hardware-Supply-Chain.md | ✅ | - |
| T1078.001 | Default Accounts | 默认账户 | T1078 | ./T1078/T1078.001-Default-Accounts.md | ✅ | - |
| T1078.002 | Domain Accounts | 域账户 | T1078 | ./T1078/T1078.002-Domain-Accounts.md | ✅ | - |
| T1078.003 | Local Accounts | 本地账户 | T1078 | ./T1078/T1078.003-Local-Accounts.md | ✅ | - |
| T1078.004 | Cloud Accounts | 云账户 | T1078 | ./T1078/T1078.004-Cloud-Accounts.md | ✅ | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v19.1已撤销或迁移

## 缺失与不一致清单

无缺失或不一致项，本地知识库与 MITRE ATT&CK v19.1 官方数据完全对齐。
## 参考来源

- [MITRE ATT&CK - TA0001](https://attack.mitre.org/tactics/TA0001/)
- [MITRE ATT&CK STIX Data v19.1](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-07-28
