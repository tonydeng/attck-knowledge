# TA0006 凭证访问 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v19.1 中 TA0006 (Credential Access/凭证访问) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v19.1
- **官方数据**：17 项父技术 / 50 项子技术
- **本地数据**：17 项父技术 / 50 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1557 | Adversary-in-the-Middle | 中间人攻击 | ./T1557-Adversary-in-the-Middle.md | 4/4 | ✅ | - |
| T1110 | Brute Force | 暴力破解 | ./T1110-Brute-Force.md | 4/4 | ✅ | - |
| T1555 | Credentials from Password Stores | 密码存储凭证提取 | ./T1555-Credentials-from-Password-Stores.md | 6/6 | ✅ | - |
| T1212 | Exploitation for Credential Access | 凭证访问漏洞利用 | ./T1212-Exploitation-for-Credential-Access.md | 0/0 | ✅ | - |
| T1187 | Forced Authentication | 强制认证 | ./T1187-Forced-Authentication.md | 0/0 | ✅ | - |
| T1606 | Forge Web Credentials | 伪造Web凭证 | ./T1606-Forge-Web-Credentials.md | 2/2 | ✅ | - |
| T1056 | Input Capture | 输入捕获 | ./T1056-Input-Capture.md | 4/4 | ✅ | 子技术数frontmatter=6 |
| T1556 | Modify Authentication Process | 修改认证流程 | ./T1556-Modify-Authentication-Process.md | 9/9 | ✅ | - |
| T1111 | Multi-Factor Authentication Interception | 多因素认证拦截 | ./T1111-Multi-Factor-Authentication-Interception.md | 0/0 | ✅ | - |
| T1621 | Multi-Factor Authentication Request Generation | 多因素认证请求生成 | ./T1621-MFA-Request-Generation.md | 0/0 | ✅ | - |
| T1040 | Network Sniffing | 网络嗅探 | ./T1040-Network-Sniffing.md | 0/0 | ✅ | - |
| T1003 | OS Credential Dumping | 操作系统凭证转储 | ./T1003-OS-Credential-Dumping.md | 8/8 | ✅ | - |
| T1528 | Steal Application Access Token | 窃取应用访问令牌 | ./T1528-Steal-Application-Access-Token.md | 0/0 | ✅ | - |
| T1649 | Steal or Forge Authentication Certificates | 窃取或伪造认证证书 | ./T1649-Steal-Authentication-Certificate.md | 0/0 | ✅ | - |
| T1558 | Steal or Forge Kerberos Tickets | 窃取或伪造Kerberos票据 | ./T1558-Steal-or-Forge-Kerberos-Tickets.md | 5/5 | ✅ | 子技术数frontmatter=4 |
| T1539 | Steal Web Session Cookie | 窃取Web会话Cookie | ./T1539-Steal-Web-Session-Cookie.md | 0/0 | ✅ | - |
| T1552 | Unsecured Credentials | 不安全的凭证 | ./T1552-Unsecured-Credentials.md | 8/8 | ✅ | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1557.001 | Name Resolution Poisoning and SMB Relay | LLMNR/NBT-NS Poisoning and SMB Relay | T1557 | ./T1557/T1557.001-Name-Resolution-Poisoning-And-SMB-Relay.md | ✅ | - |
| T1557.002 | ARP Cache Poisoning | ARP缓存中毒 | T1557 | ./T1557/T1557.002-ARP-Cache-Poisoning.md | ✅ | - |
| T1557.003 | DHCP Spoofing | DHCP欺骗 | T1557 | ./T1557/T1557.003-DHCP-Spoofing.md | ✅ | - |
| T1557.004 | Evil Twin | Mutual Authentication Impairment | T1557 | ./T1557/T1557.004-Evil-Twin.md | ✅ | - |
| T1110.001 | Password Guessing | 密码猜测 | T1110 | ./T1110/T1110.001-Password-Guessing.md | ✅ | - |
| T1110.002 | Password Cracking | 密码破解 | T1110 | ./T1110/T1110.002-Password-Cracking.md | ✅ | - |
| T1110.003 | Password Spraying | 密码喷射 | T1110 | ./T1110/T1110.003-Password-Spraying.md | ✅ | - |
| T1110.004 | Credential Stuffing | 凭证填充 | T1110 | ./T1110/T1110.004-Credential-Stuffing.md | ✅ | - |
| T1555.001 | Keychain | 钥匙串 | T1555 | ./T1555/T1555.001-Keychain.md | ✅ | - |
| T1555.002 | Securityd Memory | Securityd | T1555 | ./T1555/T1555.002-Securityd-Memory.md | ✅ | - |
| T1555.003 | Credentials from Web Browsers | Web浏览器 | T1555 | ./T1555/T1555.003-Credentials-From-Web-Browsers.md | ✅ | - |
| T1555.004 | Windows Credential Manager | Windows Credential Manager | T1555 | ./T1555/T1555.004-Windows-Credential-Manager.md | ✅ | - |
| T1555.005 | Password Managers | 密码管理器 | T1555 | ./T1555/T1555.005-Password-Managers.md | ✅ | - |
| T1555.006 | Cloud Secrets Management Stores | 组策略 | T1555 | ./T1555/T1555.006-Cloud-Secrets-Management-Stores.md | ✅ | - |
| T1606.001 | Web Cookies | SAML令牌 | T1606 | ./T1606/T1606.001-Web-Cookies.md | ✅ | - |
| T1606.002 | SAML Tokens | OAuth令牌 | T1606 | ./T1606/T1606.002-SAML-Tokens.md | ✅ | - |
| T1056.001 | Keylogging | 键盘记录 Keylogging | T1056 | ./T1056/T1056.001-Keylogging.md | ✅ | - |
| T1056.002 | GUI Input Capture | GUI输入捕获 | T1056 | ./T1056/T1056.002-GUI-Input-Capture.md | ✅ | - |
| T1056.003 | Web Portal Capture | Web门户捕获 | T1056 | ./T1056/T1056.003-Web-Portal-Capture.md | ✅ | - |
| T1056.004 | Credential API Hooking | 凭证API钩取 | T1056 | ./T1056/T1056.004-Credential-API-Hooking.md | ✅ | - |
| T1556.001 | Domain Controller Authentication | Domain Controller Authentication | T1556 | ./T1556/T1556.001-Domain-Controller-Authentication.md | ✅ | - |
| T1556.002 | Password Filter DLL | 密码过滤器DLL | T1556 | ./T1556/T1556.002-Password-Filter-DLL.md | ✅ | - |
| T1556.003 | Pluggable Authentication Modules | Pluggable Authentication Modules | T1556 | ./T1556/T1556.003-Pluggable-Authentication-Modules.md | ✅ | - |
| T1556.004 | Network Device Authentication | 网络设备认证 | T1556 | ./T1556/T1556.004-Network-Device-Authentication.md | ✅ | - |
| T1556.005 | Reversible Encryption | 可逆加密 | T1556 | ./T1556/T1556.005-Reversible-Encryption.md | ✅ | - |
| T1556.006 | Multi-Factor Authentication | 多因素认证 | T1556 | ./T1556/T1556.006-Multi-Factor-Authentication.md | ✅ | - |
| T1556.007 | Hybrid Identity | 混合身份 | T1556 | ./T1556/T1556.007-Hybrid-Identity.md | ✅ | - |
| T1556.008 | Network Provider DLL | 网络提供程序DLL | T1556 | ./T1556/T1556.008-Network-Provider-DLL.md | ✅ | - |
| T1556.009 | Conditional Access Policies | Conditional Access Policy | T1556 | ./T1556/T1556.009-Conditional-Access-Policies.md | ✅ | - |
| T1003.001 | LSASS Memory | LSASS内存转储 | T1003 | ./T1003/T1003.001-LSASS-Memory.md | ✅ | - |
| T1003.002 | Security Account Manager | SAM注册表 | T1003 | ./T1003/T1003.002-Security-Account-Manager.md | ✅ | - |
| T1003.003 | NTDS | NTDS数据库 | T1003 | ./T1003/T1003.003-NTDS.md | ✅ | - |
| T1003.004 | LSA Secrets | LSA密钥 | T1003 | ./T1003/T1003.004-LSA-Secrets.md | ✅ | - |
| T1003.005 | Cached Domain Credentials | 缓存域凭证 | T1003 | ./T1003/T1003.005-Cached-Domain-Credentials.md | ✅ | - |
| T1003.006 | DCSync | DCSync攻击 | T1003 | ./T1003/T1003.006-DCSync.md | ✅ | - |
| T1003.007 | Proc Filesystem | /proc文件系统 | T1003 | ./T1003/T1003.007-proc-Filesystem.md | ✅ | - |
| T1003.008 | /etc/passwd and /etc/shadow | /etc/passwd和/etc/shadow | T1003 | ./T1003/T1003.008-etc-passwd-and-etc-shadow.md | ✅ | - |
| T1558.001 | Golden Ticket | 黄金票据 | T1558 | ./T1558/T1558.001-Golden-Ticket.md | ✅ | - |
| T1558.002 | Silver Ticket | 白银票据 | T1558 | ./T1558/T1558.002-Silver-Ticket.md | ✅ | - |
| T1558.003 | Kerberoasting | Kerberoasting攻击 | T1558 | ./T1558/T1558.003-Kerberoasting.md | ✅ | - |
| T1558.004 | AS-REP Roasting | AS-REP Roasting | T1558 | ./T1558/T1558.004-AS-REP-Roasting.md | ✅ | - |
| T1558.005 | Ccache Files | Ccache文件 | T1558 | ./T1558/T1558.005-Ccache-Files.md | ✅ | - |
| T1552.001 | Credentials In Files | 文件中的凭证 | T1552 | ./T1552/T1552.001-Credentials-in-Files.md | ✅ | 🔄 本地名: Credentials in Files |
| T1552.002 | Credentials in Registry | 注册表中的凭证 | T1552 | ./T1552/T1552.002-Credentials-in-Registry.md | ✅ | - |
| T1552.003 | Shell History | Bash历史记录 | T1552 | ./T1552/T1552.003-Shell-History.md | ✅ | - |
| T1552.004 | Private Keys | 数字证书 | T1552 | ./T1552/T1552.004-Private-Keys.md | ✅ | - |
| T1552.005 | Cloud Instance Metadata API | Cloud Instance Metadata API | T1552 | ./T1552/T1552.005-Cloud-Instance-Metadata-API.md | ✅ | - |
| T1552.006 | Group Policy Preferences | 组策略首选项 | T1552 | ./T1552/T1552.006-Group-Policy-Preferences.md | ✅ | - |
| T1552.007 | Container API | 容器凭证 | T1552 | ./T1552/T1552.007-Container-API.md | ✅ | - |
| T1552.008 | Chat Messages | 聊天平台凭证 | T1552 | ./T1552/T1552.008-Chat-Messages.md | ✅ | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v19.1已撤销或迁移

## 缺失与不一致清单

### 名称不一致 (1 项)
- **T1552.001** (subtech): 官方=`Credentials In Files` vs 本地=`Credentials in Files`

## 参考来源

- [MITRE ATT&CK - TA0006](https://attack.mitre.org/tactics/TA0006/)
- [MITRE ATT&CK STIX Data v19.1](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-07-28
