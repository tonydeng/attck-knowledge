# TA0112 防御损害 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v19.1 中 TA0112 (Defense Impairment/防御损害) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v19.1
- **官方数据**：18 项父技术 / 38 项子技术
- **本地数据**：18 项父技术 / 38 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1686 | Disable or Modify System Firewall | 禁用或修改系统防火墙 | ./T1686-Disable-or-Modify-System-Firewall.md | 3/3 | ✅ | - |
| T1685 | Disable or Modify Tools | 禁用或修改工具 | ./T1685-Disable-or-Modify-Tools.md | 6/6 | ✅ | - |
| T1484 | Domain or Tenant Policy Modification | 域或租户策略修改 | ./T1484-Domain-or-Tenant-Policy-Modification.md | 2/2 | ✅ | - |
| T1689 | Downgrade Attack | 降级攻击 | ./T1689-Downgrade-Attack.md | 0/0 | ✅ | - |
| T1687 | Exploitation for Defense Impairment | 利用漏洞削弱防御 | ./T1687-Exploitation-for-Defense-Impairment.md | 0/0 | ✅ | - |
| T1222 | File and Directory Permissions Modification | 文件权限修改 | ./T1222-File-And-Directory-Permissions-Modification.md | 2/2 | ✅ | - |
| T1556 | Modify Authentication Process | 修改认证过程 | ./T1556-Modify-Authentication-Process.md | 9/9 | ✅ | 子技术数frontmatter=6 |
| T1578 | Modify Cloud Compute Infrastructure | 修改云计算基础设施 | ./T1578-Modify-Cloud-Compute-Infrastructure.md | 5/5 | ✅ | - |
| T1666 | Modify Cloud Resource Hierarchy | 修改云资源层级 | ./T1666-Modify-Cloud-Resource-Hierarchy.md | 0/0 | ✅ | - |
| T1112 | Modify Registry | 修改注册表 | ./T1112-Modify-Registry.md | 0/0 | ✅ | - |
| T1601 | Modify System Image | 修改系统镜像 | ./T1601-Modify-System-Image.md | 2/2 | ✅ | - |
| T1599 | Network Boundary Bridging | 网络边界桥接 | ./T1599-Network-Boundary-Bridging.md | 1/1 | ✅ | - |
| T1647 | Plist File Modification | Plist文件修改 | ./T1647-Plist-File-Modification.md | 0/0 | ✅ | - |
| T1690 | Prevent Command History Logging | 阻止命令历史记录 | ./T1690-Prevent-Command-History-Logging.md | 0/0 | ✅ | - |
| T1207 | Rogue Domain Controller | 伪域控制器 | ./T1207-Rogue-Domain-Controller.md | 0/0 | ✅ | - |
| T1688 | Safe Mode Boot | 安全模式启动 | ./T1688-Safe-Mode-Boot.md | 0/0 | ✅ | - |
| T1553 | Subvert Trust Controls | 颠覆信任控制 | ./T1553-Subvert-Trust-Controls.md | 6/6 | ✅ | 子技术数frontmatter=5 |
| T1600 | Weaken Encryption | 削弱加密 | ./T1600-Weaken-Encryption.md | 2/2 | ✅ | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1686.001 | Cloud Firewall | 云防火墙 | T1686 | ./T1686/T1686.001-Cloud-Firewall.md | ✅ | - |
| T1686.002 | Network Device Firewall | 网络设备防火墙 | T1686 | ./T1686/T1686.002-Network-Device-Firewall.md | ✅ | - |
| T1686.003 | Windows Host Firewall | Windows主机防火墙 | T1686 | ./T1686/T1686.003-Windows-Host-Firewall.md | ✅ | - |
| T1685.001 | Disable or Modify Windows Event Log | 禁用或修改Windows事件日志 | T1685 | ./T1685/T1685.001-Disable-or-Modify-Windows-Event-Log.md | ✅ | - |
| T1685.002 | Disable or Modify Cloud Log | 禁用或修改云日志 | T1685 | ./T1685/T1685.002-Disable-or-Modify-Cloud-Log.md | ✅ | - |
| T1685.003 | Modify or Spoof Tool UI | 修改或伪造工具UI | T1685 | ./T1685/T1685.003-Modify-or-Spoof-Tool-UI.md | ✅ | - |
| T1685.004 | Disable or Modify Linux Audit System Log | 禁用或修改Linux审计系统日志 | T1685 | ./T1685/T1685.004-Disable-or-Modify-Linux-Audit-System-Log.md | ✅ | - |
| T1685.005 | Clear Windows Event Logs | 清除Windows事件日志 | T1685 | ./T1685/T1685.005-Clear-Windows-Event-Logs.md | ✅ | - |
| T1685.006 | Clear Linux or Mac System Logs | 清除Linux或Mac系统日志 | T1685 | ./T1685/T1685.006-Clear-Linux-or-Mac-System-Logs.md | ✅ | - |
| T1484.001 | Group Policy Modification | 组策略修改 | T1484 | ./T1484/T1484.001-Group-Policy-Modification.md | ✅ | - |
| T1484.002 | Trust Modification | 信任关系修改 | T1484 | ./T1484/T1484.002-Trust-Modification.md | ✅ | - |
| T1222.001 | Windows Permissions | Windows文件/目录权限修改 | T1222 | ./T1222/T1222.001-Windows-Permissions.md | ✅ | - |
| T1222.002 | Linux and Mac Permissions | Linux/Mac文件/目录权限修改 | T1222 | ./T1222/T1222.002-Linux-And-Mac-Permissions.md | ✅ | - |
| T1556.001 | Domain Controller Authentication | 域控制器认证 | T1556 | ./T1556/T1556.001-Domain-Controller-Authentication.md | ✅ | - |
| T1556.002 | Password Filter DLL | 密码过滤器DLL | T1556 | ./T1556/T1556.002-Password-Filter-DLL.md | ✅ | - |
| T1556.003 | Pluggable Authentication Modules | 可插拔认证模块 | T1556 | ./T1556/T1556.003-Pluggable-Authentication-Modules.md | ✅ | - |
| T1556.004 | Network Device Authentication | 网络设备认证 | T1556 | ./T1556/T1556.004-Network-Device-Authentication.md | ✅ | - |
| T1556.005 | Reversible Encryption | 可逆加密 | T1556 | ./T1556/T1556.005-Reversible-Encryption.md | ✅ | - |
| T1556.006 | Multi-Factor Authentication | 多因素认证操作 | T1556 | ./T1556/T1556.006-Multi-factor-Authentication.md | ✅ | - |
| T1556.007 | Hybrid Identity | 混合身份 | T1556 | ./T1556/T1556.007-Hybrid-Identity.md | ✅ | - |
| T1556.008 | Network Provider DLL | 网络提供程序DLL | T1556 | ./T1556/T1556.008-Network-Provider-DLL.md | ✅ | - |
| T1556.009 | Conditional Access Policies | 条件访问策略 | T1556 | ./T1556/T1556.009-Conditional-Access-Policies.md | ✅ | - |
| T1578.001 | Create Snapshot | 创建快照 | T1578 | ./T1578/T1578.001-Create-Snapshot.md | ✅ | - |
| T1578.002 | Create Cloud Instance | 创建云实例 | T1578 | ./T1578/T1578.002-Create-Cloud-Instance.md | ✅ | - |
| T1578.003 | Delete Cloud Instance | 删除云实例 | T1578 | ./T1578/T1578.003-Delete-Cloud-Instance.md | ✅ | - |
| T1578.004 | Revert Cloud Instance | 回滚云实例 | T1578 | ./T1578/T1578.004-Revert-Cloud-Instance.md | ✅ | - |
| T1578.005 | Modify Cloud Compute Configurations | 修改云计算配置 | T1578 | ./T1578/T1578.005-Modify-Cloud-Compute-Configurations.md | ✅ | - |
| T1601.001 | Patch System Image | 修补系统镜像 | T1601 | ./T1601/T1601.001-Patch-System-Image.md | ✅ | - |
| T1601.002 | Downgrade System Image | 降级系统镜像 | T1601 | ./T1601/T1601.002-Downgrade-System-Image.md | ✅ | - |
| T1599.001 | Network Address Translation Traversal | 网络地址转换穿越 | T1599 | ./T1599/T1599.001-Network-Address-Translation-Traversal.md | ✅ | - |
| T1553.001 | Gatekeeper Bypass | 代码签名 | T1553 | ./T1553/T1553.001-Gatekeeper-Bypass.md | ✅ | - |
| T1553.002 | Code Signing | 安装根证书 | T1553 | ./T1553/T1553.002-Code-Signing.md | ✅ | - |
| T1553.003 | SIP and Trust Provider Hijacking | SIP信任提供方劫持 | T1553 | ./T1553/T1553.003-SIP-And-Trust-Provider-Hijacking.md | ✅ | - |
| T1553.004 | Install Root Certificate | 安全启动绕过 | T1553 | ./T1553/T1553.004-Install-Root-Certificate.md | ✅ | - |
| T1553.005 | Mark-of-the-Web Bypass | Mark-of-the-Web绕过 | T1553 | ./T1553/T1553.005-Mark-of-the-Web-Bypass.md | ✅ | - |
| T1553.006 | Code Signing Policy Modification | 代码签名策略修改 | T1553 | ./T1553/T1553.006-Code-Signing-Policy-Modification.md | ✅ | - |
| T1600.001 | Reduce Key Space | 缩减密钥空间 | T1600 | ./T1600/T1600.001-Reduce-Key-Space.md | ✅ | - |
| T1600.002 | Disable Crypto Hardware | 禁用加密硬件 | T1600 | ./T1600/T1600.002-Disable-Crypto-Hardware.md | ✅ | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v19.1已撤销或迁移

## 缺失与不一致清单

无缺失或不一致项，本地知识库与 MITRE ATT&CK v19.1 官方数据完全对齐。
## 参考来源

- [MITRE ATT&CK - TA0112](https://attack.mitre.org/tactics/TA0112/)
- [MITRE ATT&CK STIX Data v19.1](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-07-28
