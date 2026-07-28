# TA0004 权限提升 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v19.1 中 TA0004 (Privilege Escalation/权限提升) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v19.1
- **官方数据**：13 项父技术 / 83 项子技术
- **本地数据**：13 项父技术 / 83 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1548 | Abuse Elevation Control Mechanism | 滥用权限提升控制机制 | ./T1548-Abuse-Elevation-Control-Mechanism.md | 6/6 | ✅ | 子技术数frontmatter=4 |
| T1134 | Access Token Manipulation | 访问令牌操纵 | ./T1134-Access-Token-Manipulation.md | 5/5 | ✅ | 子技术数frontmatter=6 |
| T1098 | Account Manipulation | 账户操纵 | ./T1098-Account-Manipulation.md | 7/7 | ✅ | - |
| T1547 | Boot or Logon Autostart Execution | 启动或登录自动执行 | ./T1547-Boot-or-Logon-Autostart-Execution.md | 14/14 | ✅ | - |
| T1037 | Boot or Logon Initialization Scripts | 启动或登录初始化脚本 | ./T1037-Boot-or-Logon-Initialization-Scripts.md | 5/5 | ✅ | - |
| T1543 | Create or Modify System Process | 创建或修改系统进程 | ./T1543-Create-or-Modify-System-Process.md | 5/5 | ✅ | - |
| T1484 | Domain or Tenant Policy Modification | 域或租户策略修改 | ./T1484-Domain-or-Tenant-Policy-Modification.md | 2/2 | ✅ | - |
| T1611 | Escape to Host | 逃逸到宿主机 | ./T1611-Escape-to-Host.md | 0/0 | ✅ | 子技术数frontmatter=4 |
| T1546 | Event Triggered Execution | 事件触发执行 | ./T1546-Event-Triggered-Execution.md | 18/18 | ✅ | 子技术数frontmatter=12 |
| T1068 | Exploitation for Privilege Escalation | 利用漏洞提升权限 | ./T1068-Exploitation-for-Privilege-Escalation.md | 0/0 | ✅ | - |
| T1055 | Process Injection | 进程注入 | ./T1055-Process-Injection.md | 12/12 | ✅ | - |
| T1053 | Scheduled Task/Job | 计划任务/作业 | ./T1053-Scheduled-Task-Job.md | 5/5 | ✅ | - |
| T1078 | Valid Accounts | 有效账户 | ./T1078-Valid-Accounts.md | 4/4 | ✅ | 子技术数frontmatter=5 |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1548.001 | Setuid and Setgid | Setuid 和 Setgid 特权位滥用 | T1548 | ./T1548/T1548.001-Setuid-and-Setgid.md | 📝 | - |
| T1548.002 | Bypass User Account Control | 绕过 UAC | T1548 | ./T1548/T1548.002-Bypass-User-Account-Control.md | ✅ | - |
| T1548.003 | Sudo and Sudo Caching | Sudo 权限缓存 | T1548 | ./T1548/T1548.003-Sudo-And-Sudo-Caching.md | ✅ | - |
| T1548.004 | Elevated Execution with Prompt | 绕过系统授权组件 | T1548 | ./T1548/T1548.004-Elevated-Execution-With-Prompt.md | ✅ | - |
| T1548.005 | Temporary Elevated Cloud Access |  | T1548 | ./T1548/T1548.005-Temporary-Elevated-Cloud-Access.md | 📝 | - |
| T1548.006 | TCC Manipulation |  | T1548 | ./T1548/T1548.006-TCC-Manipulation.md | 📝 | - |
| T1134.001 | Token Impersonation/Theft | 令牌冒充/盗取 | T1134 | ./T1134/T1134.001-Token-Impersonation-Theft.md | ✅ | - |
| T1134.002 | Create Process with Token | 使用令牌创建进程 | T1134 | ./T1134/T1134.002-Create-Process-with-Token.md | ✅ | - |
| T1134.003 | Make and Impersonate Token | 制作并冒充令牌 | T1134 | ./T1134/T1134.003-Make-and-Impersonate-Token.md | ✅ | - |
| T1134.004 | Parent PID Spoofing | 父进程ID欺骗 | T1134 | ./T1134/T1134.004-Parent-PID-Spoofing.md | ✅ | - |
| T1134.005 | SID-History Injection | SID-History 注入 | T1134 | ./T1134/T1134.005-SID-History-Injection.md | ✅ | - |
| T1098.001 | Additional Cloud Credentials | 额外云凭据 | T1098 | ./T1098/T1098.001-Additional-Cloud-Credentials.md | ✅ | - |
| T1098.002 | Additional Email Delegate Permissions | 额外电子邮件委派权限 | T1098 | ./T1098/T1098.002-Additional-Email-Delegate-Permissions.md | ✅ | - |
| T1098.003 | Additional Cloud Roles | 额外云角色 | T1098 | ./T1098/T1098.003-Additional-Cloud-Roles.md | ✅ | - |
| T1098.004 | SSH Authorized Keys | SSH 授权密钥 | T1098 | ./T1098/T1098.004-SSH-Authorized-Keys.md | ✅ | - |
| T1098.005 | Device Registration | 设备注册 | T1098 | ./T1098/T1098.005-Device-Registration.md | ✅ | - |
| T1098.006 | Additional Container Cluster Roles | 额外容器集群角色 | T1098 | ./T1098/T1098.006-Additional-Container-Cluster-Roles.md | ✅ | - |
| T1098.007 | Additional Local or Domain Groups | 额外本地或域组 | T1098 | ./T1098/T1098.007-Additional-Local-or-Domain-Groups.md | ✅ | - |
| T1547.001 | Registry Run Keys / Startup Folder | 注册表自启项 | T1547 | ./T1547/T1547.001-Registry-Run-Keys---Startup-Folder.md | ✅ | - |
| T1547.002 | Authentication Package | 身份验证包 | T1547 | ./T1547/T1547.002-Authentication-Package.md | ✅ | - |
| T1547.003 | Time Providers | 时间提供程序 | T1547 | ./T1547/T1547.003-Time-Providers.md | ✅ | - |
| T1547.004 | Winlogon Helper DLL | Winlogon 辅助 DLL | T1547 | ./T1547/T1547.004-Winlogon-Helper-DLL.md | ✅ | - |
| T1547.005 | Security Support Provider | 内核模块和扩展 | T1547 | ./T1547/T1547.005-Security-Support-Provider.md | ✅ | - |
| T1547.006 | Kernel Modules and Extensions | 启用启动文件夹 | T1547 | ./T1547/T1547.006-Kernel-Modules-And-Extensions.md | ✅ | - |
| T1547.007 | Re-opened Applications | 重新打开应用程序 | T1547 | ./T1547/T1547.007-Re-opened-Applications.md | ✅ | - |
| T1547.008 | LSASS Driver | LSASS 驱动 | T1547 | ./T1547/T1547.008-LSASS-Driver.md | ✅ | - |
| T1547.009 | Shortcut Modification | 快捷方式修改 | T1547 | ./T1547/T1547.009-Shortcut-Modification.md | ✅ | - |
| T1547.010 | Port Monitors | 端口监视器 | T1547 | ./T1547/T1547.010-Port-Monitors.md | ✅ | - |
| T1547.012 | Print Processors | 打印处理器 | T1547 | ./T1547/T1547.012-Print-Processors.md | ✅ | - |
| T1547.013 | XDG Autostart Entries | 启动代理 | T1547 | ./T1547/T1547.013-XDG-Autostart-Entries.md | ✅ | - |
| T1547.014 | Active Setup | 活动设置修改 | T1547 | ./T1547/T1547.014-Active-Setup.md | ✅ | - |
| T1547.015 | Login Items |  | T1547 | ./T1547/T1547.015-Login-Items.md | 📝 | - |
| T1037.001 | Logon Script (Windows) | 登录脚本 (Windows) | T1037 | ./T1037/T1037.001-Logon-Script-Windows.md | ✅ | - |
| T1037.002 | Login Hook | 登录钩子 (macOS) | T1037 | ./T1037/T1037.002-Login-Hook.md | ✅ | - |
| T1037.003 | Network Logon Script | 网络登录脚本 (Windows) | T1037 | ./T1037/T1037.003-Network-Logon-Script.md | ✅ | - |
| T1037.004 | RC Scripts | RC 脚本 (Linux/macOS) | T1037 | ./T1037/T1037.004-RC-Scripts.md | ✅ | - |
| T1037.005 | Startup Items | 启动项 (macOS) | T1037 | ./T1037/T1037.005-Startup-Items.md | ✅ | - |
| T1543.001 | Launch Agent | Launch Agent / 启动代理 | T1543 | ./T1543/T1543.001-Launch-Agent.md | 📝 | - |
| T1543.002 | Systemd Service | 系统守护进程 | T1543 | ./T1543/T1543.002-Systemd-Service.md | ✅ | - |
| T1543.003 | Windows Service | Windows 服务 | T1543 | ./T1543/T1543.003-Windows-Service.md | ✅ | - |
| T1543.004 | Launch Daemon | launchd | T1543 | ./T1543/T1543.004-Launch-Daemon.md | ✅ | - |
| T1543.005 | Container Service |  | T1543 | ./T1543/T1543.005-Container-Service.md | 📝 | - |
| T1484.001 | Group Policy Modification | 组策略修改 | T1484 | ./T1484/T1484.001-Group-Policy-Modification.md | ✅ | - |
| T1484.002 | Trust Modification | 信任修改 | T1484 | ./T1484/T1484.002-Trust-Modification.md | ✅ | - |
| T1546.001 | Change Default File Association | 更改默认文件关联 | T1546 | ./T1546/T1546.001-Change-Default-File-Association.md | ✅ | - |
| T1546.002 | Screensaver | 屏幕保护程序 | T1546 | ./T1546/T1546.002-Screensaver.md | ✅ | - |
| T1546.003 | Windows Management Instrumentation Event Subscription | Windows 管理规范事件订阅 | T1546 | ./T1546/T1546.003-Windows-Management-Instrumentation-Event-Subscription.md | ✅ | - |
| T1546.004 | Unix Shell Configuration Modification | .bash_profile 和 .bashrc | T1546 | ./T1546/T1546.004-Unix-Shell-Configuration-Modification.md | ✅ | - |
| T1546.005 | Trap | 应用程序初始化 | T1546 | ./T1546/T1546.005-Trap.md | ✅ | - |
| T1546.006 | LC_LOAD_DYLIB Addition | 辅助功能 | T1546 | ./T1546/T1546.006-LC_LOAD_DYLIB-Addition.md | ✅ | - |
| T1546.007 | Netsh Helper DLL | Netsh 帮助程序 DLL | T1546 | ./T1546/T1546.007-Netsh-Helper-DLL.md | ✅ | - |
| T1546.008 | Accessibility Features | 访问功能 | T1546 | ./T1546/T1546.008-Accessibility-Features.md | ✅ | - |
| T1546.009 | AppCert DLLs | AppCert DLL | T1546 | ./T1546/T1546.009-AppCert-DLLs.md | ✅ | - |
| T1546.010 | AppInit DLLs | AppInit DLL | T1546 | ./T1546/T1546.010-AppInit-DLLs.md | ✅ | - |
| T1546.011 | Application Shimming | 应用程序关闭 | T1546 | ./T1546/T1546.011-Application-Shimming.md | ✅ | - |
| T1546.012 | Image File Execution Options Injection | 安全支持提供器 | T1546 | ./T1546/T1546.012-Image-File-Execution-Options-Injection.md | ✅ | - |
| T1546.013 | PowerShell Profile |  | T1546 | ./T1546/T1546.013-Powershell-Profile.md | 📝 | - |
| T1546.014 | Emond |  | T1546 | ./T1546/T1546.014-Emond.md | 📝 | - |
| T1546.015 | Component Object Model Hijacking |  | T1546 | ./T1546/T1546.015-Component-Object-Model-Hijacking.md | 📝 | - |
| T1546.016 | Installer Packages |  | T1546 | ./T1546/T1546.016-Installer-Packages.md | 📝 | - |
| T1546.017 | Udev Rules |  | T1546 | ./T1546/T1546.017-Udev-Rules.md | 📝 | - |
| T1546.018 | Python Startup Hooks |  | T1546 | ./T1546/T1546.018-Python-Startup-Hooks.md | 📝 | - |
| T1055.001 | Dynamic-link Library Injection | DLL 注入 | T1055 | ./T1055/T1055.001-Dynamic-link-Library-Injection.md | ✅ | - |
| T1055.002 | Portable Executable Injection | PE 注入 | T1055 | ./T1055/T1055.002-Portable-Executable-Injection.md | ✅ | - |
| T1055.003 | Thread Execution Hijacking | 线程执行劫持 | T1055 | ./T1055/T1055.003-Thread-Execution-Hijacking.md | ✅ | - |
| T1055.004 | Asynchronous Procedure Call | 异步过程调用 (APC) | T1055 | ./T1055/T1055.004-Asynchronous-Procedure-Call.md | ✅ | - |
| T1055.005 | Thread Local Storage | 线程本地存储 (TLS) | T1055 | ./T1055/T1055.005-Thread-Local-Storage.md | ✅ | - |
| T1055.008 | Ptrace System Calls | Ptrace系统调用 | T1055 | ./T1055/T1055.008-Ptrace-System-Calls.md | 📝 | - |
| T1055.009 | Proc Memory | Proc 内存 | T1055 | ./T1055/T1055.009-Proc-Memory.md | ✅ | - |
| T1055.011 | Extra Window Memory Injection | 额外窗口内存注入 | T1055 | ./T1055/T1055.011-Extra-Window-Memory-Injection.md | ✅ | - |
| T1055.012 | Process Hollowing | 进程镂空 | T1055 | ./T1055/T1055.012-Process-Hollowing.md | ✅ | - |
| T1055.013 | Process Doppelgänging | 进程双胞胎 | T1055 | ./T1055/T1055.013-Process-Doppelgänging.md | ✅ | - |
| T1055.014 | VDSO Hijacking | VDSO劫持 | T1055 | ./T1055/T1055.014-VDSO-Hijacking.md | ✅ | - |
| T1055.015 | ListPlanting |  | T1055 | ./T1055/T1055.015-Listplanting.md | 📝 | - |
| T1053.002 | At | At (Linux) | T1053 | ./T1053/T1053.002-At.md | ✅ | - |
| T1053.003 | Cron | 定时任务 | T1053 | ./T1053/T1053.003-Cron.md | ✅ | - |
| T1053.005 | Scheduled Task | 计划任务 (Windows) | T1053 | ./T1053/T1053.005-Scheduled-Task.md | ✅ | - |
| T1053.006 | Systemd Timers | Systemd 定时器 | T1053 | ./T1053/T1053.006-Systemd-Timers.md | ✅ | - |
| T1053.007 | Container Orchestration Job | 容器编排作业 | T1053 | ./T1053/T1053.007-Container-Orchestration-Job.md | ✅ | - |
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

- [MITRE ATT&CK - TA0004](https://attack.mitre.org/tactics/TA0004/)
- [MITRE ATT&CK STIX Data v19.1](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-07-28
