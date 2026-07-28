# TA0042 资源开发 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v19.1 中 TA0042 (Resource Development/资源开发) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v19.1
- **官方数据**：9 项父技术 / 41 项子技术
- **本地数据**：9 项父技术 / 41 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1650 | Acquire Access | 获取访问权限 | ./T1650-Acquire-Access.md | 0/0 | ✅ | - |
| T1583 | Acquire Infrastructure | 获取基础设施 | ./T1583-Acquire-Infrastructure.md | 8/8 | ✅ | - |
| T1586 | Compromise Accounts | 损害账户 | ./T1586-Compromise-Accounts.md | 3/3 | ✅ | - |
| T1584 | Compromise Infrastructure | 损害基础设施 | ./T1584-Compromise-Infrastructure.md | 8/8 | ✅ | - |
| T1587 | Develop Capabilities | 开发能力 | ./T1587-Develop-Capabilities.md | 4/4 | ✅ | - |
| T1585 | Establish Accounts | 建立账户 | ./T1585-Establish-Accounts.md | 3/3 | ✅ | - |
| T1683 | Generate Content | 生成内容 | ./T1683-Generate-Content.md | 2/2 | ✅ | - |
| T1588 | Obtain Capabilities | 获取能力 | ./T1588-Obtain-Capabilities.md | 7/7 | ✅ | - |
| T1608 | Stage Capabilities | 预置能力 | ./T1608-Stage-Capabilities.md | 6/6 | ✅ | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1583.001 | Domains | 域名 | T1583 | ./T1583/T1583.001-Domains.md | ✅ | - |
| T1583.002 | DNS Server | DNS服务器 | T1583 | ./T1583/T1583.002-DNS-Server.md | ✅ | - |
| T1583.003 | Virtual Private Server | 虚拟专用服务器(VPS) | T1583 | ./T1583/T1583.003-Virtual-Private-Server.md | ✅ | - |
| T1583.004 | Server | 服务器 | T1583 | ./T1583/T1583.004-Server.md | ✅ | - |
| T1583.005 | Botnet | 机器人网络 | T1583 | ./T1583/T1583.005-Botnet.md | ✅ | - |
| T1583.006 | Web Services | Web服务 | T1583 | ./T1583/T1583.006-Web-Services.md | ✅ | - |
| T1583.007 | Serverless | 无服务器 | T1583 | ./T1583/T1583.007-Serverless.md | ✅ | - |
| T1583.008 | Malvertising | 恶意广告(Malvertising) | T1583 | ./T1583/T1583.008-Malvertising.md | ✅ | - |
| T1586.001 | Social Media Accounts | 社交媒体账户 | T1586 | ./T1586/T1586.001-Social-Media-Accounts.md | ✅ | - |
| T1586.002 | Email Accounts | 电子邮件账户 | T1586 | ./T1586/T1586.002-Email-Accounts.md | ✅ | - |
| T1586.003 | Cloud Accounts | 云账户 | T1586 | ./T1586/T1586.003-Cloud-Accounts.md | ✅ | - |
| T1584.001 | Domains | 域名 | T1584 | ./T1584/T1584.001-Domains.md | ✅ | - |
| T1584.002 | DNS Server | DNS服务器 | T1584 | ./T1584/T1584.002-DNS-Server.md | ✅ | - |
| T1584.003 | Virtual Private Server | 虚拟专用服务器(VPS) | T1584 | ./T1584/T1584.003-Virtual-Private-Server.md | ✅ | - |
| T1584.004 | Server | 服务器 | T1584 | ./T1584/T1584.004-Server.md | ✅ | - |
| T1584.005 | Botnet | 机器人网络 | T1584 | ./T1584/T1584.005-Botnet.md | ✅ | - |
| T1584.006 | Web Services | Web服务 | T1584 | ./T1584/T1584.006-Web-Services.md | ✅ | - |
| T1584.007 | Serverless | 无服务器 | T1584 | ./T1584/T1584.007-Serverless.md | ✅ | - |
| T1584.008 | Network Devices | 网络设备 | T1584 | ./T1584/T1584.008-Network-Devices.md | ✅ | - |
| T1587.001 | Malware | 恶意软件 | T1587 | ./T1587/T1587.001-Malware.md | ✅ | - |
| T1587.002 | Code Signing Certificates | 代码签名证书 | T1587 | ./T1587/T1587.002-Code-Signing-Certificates.md | ✅ | - |
| T1587.003 | Digital Certificates | 数字证书 | T1587 | ./T1587/T1587.003-Digital-Certificates.md | ✅ | - |
| T1587.004 | Exploits | 漏洞利用 | T1587 | ./T1587/T1587.004-Exploits.md | ✅ | - |
| T1585.001 | Social Media Accounts | 社交媒体账户 | T1585 | ./T1585/T1585.001-Social-Media-Accounts.md | ✅ | - |
| T1585.002 | Email Accounts | 电子邮件账户 | T1585 | ./T1585/T1585.002-Email-Accounts.md | ✅ | - |
| T1585.003 | Cloud Accounts | 云账户 | T1585 | ./T1585/T1585.003-Cloud-Accounts.md | ✅ | - |
| T1683.001 | Written Content | 书面内容 | T1683 | ./T1683/T1683.001-Written-Content.md | ✅ | - |
| T1683.002 | Audio-Visual Content | 音视频内容 | T1683 | ./T1683/T1683.002-Audio-visual-Content.md | ✅ | - |
| T1588.001 | Malware | 恶意软件 | T1588 | ./T1588/T1588.001-Malware.md | ✅ | - |
| T1588.002 | Tool | 工具 | T1588 | ./T1588/T1588.002-Tool.md | ✅ | - |
| T1588.003 | Code Signing Certificates | 代码签名证书 | T1588 | ./T1588/T1588.003-Code-Signing-Certificates.md | ✅ | - |
| T1588.004 | Digital Certificates | 数字证书 | T1588 | ./T1588/T1588.004-Digital-Certificates.md | ✅ | - |
| T1588.005 | Exploits | 漏洞利用 | T1588 | ./T1588/T1588.005-Exploits.md | ✅ | - |
| T1588.006 | Vulnerabilities | 漏洞信息 | T1588 | ./T1588/T1588.006-Vulnerabilities.md | ✅ | - |
| T1588.007 | Artificial Intelligence | 人工智能 | T1588 | ./T1588/T1588.007-Artificial-Intelligence.md | ✅ | - |
| T1608.001 | Upload Malware | 上传恶意软件 | T1608 | ./T1608/T1608.001-Upload-Malware.md | ✅ | - |
| T1608.002 | Upload Tool | 上传工具 | T1608 | ./T1608/T1608.002-Upload-Tool.md | ✅ | - |
| T1608.003 | Install Digital Certificate | 安装数字证书 | T1608 | ./T1608/T1608.003-Install-Digital-Certificate.md | ✅ | - |
| T1608.004 | Drive-by Target | 驱动式目标 | T1608 | ./T1608/T1608.004-Drive-by-Target.md | ✅ | - |
| T1608.005 | Link Target | 链接目标 | T1608 | ./T1608/T1608.005-Link-Target.md | ✅ | - |
| T1608.006 | SEO Poisoning | SEO中毒 | T1608 | ./T1608/T1608.006-SEO-Poisoning.md | ✅ | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v19.1已撤销或迁移

## 缺失与不一致清单

无缺失或不一致项，本地知识库与 MITRE ATT&CK v19.1 官方数据完全对齐。
## 参考来源

- [MITRE ATT&CK - TA0042](https://attack.mitre.org/tactics/TA0042/)
- [MITRE ATT&CK STIX Data v19.1](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-07-28
