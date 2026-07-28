# TA0003 持久化 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v19.1 中 TA0003 (Persistence/持久化) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v19.1
- **官方数据**：22 项父技术 / 91 项子技术
- **本地数据**：22 项父技术 / 91 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1098 | Account Manipulation | 账户操纵 | ./T1098-Account-Manipulation.md | 7/7 | ✅ | - |
| T1197 | BITS Jobs | BITS作业 | ./T1197-BITS-Jobs.md | 0/0 | ✅ | - |
| T1547 | Boot or Logon Autostart Execution | 启动或登录自动执行 | ./T1547-Boot-or-Logon-Autostart-Execution.md | 14/14 | ✅ | - |
| T1037 | Boot or Logon Initialization Scripts | 启动或登录初始化脚本 | ./T1037-Boot-or-Logon-Initialization-Scripts.md | 5/5 | ✅ | - |
| T1671 | Cloud Application Integration | 云应用集成 | ./T1671-Cloud-Application-Integration.md | 0/0 | ✅ | - |
| T1554 | Compromise Host Software Binary | 篡改客户端软件二进制 | ./T1554-Compromise-Host-Software-Binary.md | 0/0 | ✅ | - |
| T1136 | Create Account | 创建账户 | ./T1136-Create-Account.md | 3/3 | ✅ | - |
| T1543 | Create or Modify System Process | 创建或修改系统进程 | ./T1543-Create-or-Modify-System-Process.md | 5/5 | ✅ | - |
| T1546 | Event Triggered Execution | 事件触发执行 | ./T1546-Event-Triggered-Execution.md | 18/18 | ✅ | 子技术数frontmatter=12 |
| T1668 | Exclusive Control | 独占控制 | ./T1668-Exclusive-Control.md | 0/0 | ✅ | - |
| T1133 | External Remote Services | 外部远程服务 | ./T1133-External-Remote-Services.md | 0/0 | ✅ | - |
| T1525 | Implant Internal Image | 植入内部镜像 | ./T1525-Implant-Internal-Image.md | 0/0 | ✅ | - |
| T1556 | Modify Authentication Process | 修改认证流程 | ./T1556-Modify-Authentication-Process.md | 9/9 | ✅ | - |
| T1112 | Modify Registry |  | ./T1112-Modify-Registry.md | 0/0 | 📝 | - |
| T1137 | Office Application Startup | Office应用启动 | ./T1137-Office-Application-Startup.md | 6/6 | ✅ | - |
| T1653 | Power Settings | 电源设置 | ./T1653-Power-Settings.md | 0/0 | ✅ | - |
| T1542 | Pre-OS Boot | 预启动 | ./T1542-Pre-OS-Boot.md | 5/5 | ✅ | - |
| T1053 | Scheduled Task/Job | 计划任务/作业 | ./T1053-Scheduled-Task-Job.md | 5/5 | ✅ | - |
| T1505 | Server Software Component | 服务器软件组件 | ./T1505-Server-Software-Component.md | 6/6 | ✅ | 子技术数frontmatter=5 |
| T1176 | Software Extensions | 软件扩展 | ./T1176-Software-Extensions.md | 2/2 | ✅ | - |
| T1205 | Traffic Signaling | 流量信号 | ./T1205-Traffic-Signaling.md | 2/2 | ✅ | - |
| T1078 | Valid Accounts | 有效账户 | ./T1078-Valid-Accounts.md | 4/4 | ✅ | 子技术数frontmatter=5 |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1098.001 | Additional Cloud Credentials | 额外云凭据 | T1098 | ./T1098/T1098.001-Additional-Cloud-Credentials.md | ✅ | - |
| T1098.002 | Additional Email Delegate Permissions | 额外邮箱委托权限 | T1098 | ./T1098/T1098.002-Additional-Email-Delegate-Permissions.md | ✅ | - |
| T1098.003 | Additional Cloud Roles | 额外云角色 | T1098 | ./T1098/T1098.003-Additional-Cloud-Roles.md | ✅ | - |
| T1098.004 | SSH Authorized Keys | SSH授权密钥 | T1098 | ./T1098/T1098.004-SSH-Authorized-Keys.md | ✅ | - |
| T1098.005 | Device Registration | 设备注册 | T1098 | ./T1098/T1098.005-Device-Registration.md | ✅ | - |
| T1098.006 | Additional Container Cluster Roles | 额外容器集群角色 | T1098 | ./T1098/T1098.006-Additional-Container-Cluster-Roles.md | ✅ | - |
| T1098.007 | Additional Local or Domain Groups | 额外本地或域组 | T1098 | ./T1098/T1098.007-Additional-Local-or-Domain-Groups.md | ✅ | - |
| T1547.001 | Registry Run Keys / Startup Folder | 注册表Run键/启动文件夹 | T1547 | ./T1547/T1547.001-Registry-Run-Keys-Startup-Folder.md | ✅ | - |
| T1547.002 | Authentication Package | 认证包 | T1547 | ./T1547/T1547.002-Authentication-Package.md | ✅ | - |
| T1547.003 | Time Providers | 时间提供者 | T1547 | ./T1547/T1547.003-Time-Providers.md | ✅ | - |
| T1547.004 | Winlogon Helper DLL | Winlogon辅助DLL | T1547 | ./T1547/T1547.004-Winlogon-Helper-DLL.md | ✅ | - |
| T1547.005 | Security Support Provider | 安全支持提供者 | T1547 | ./T1547/T1547.005-Security-Support-Provider.md | ✅ | - |
| T1547.006 | Kernel Modules and Extensions | 内核模块和扩展 | T1547 | ./T1547/T1547.006-Kernel-Modules-and-Extensions.md | ✅ | - |
| T1547.007 | Re-opened Applications | 重新打开的应用程序 | T1547 | ./T1547/T1547.007-Re-opened-Applications.md | ✅ | - |
| T1547.008 | LSASS Driver | LSASS驱动程序 | T1547 | ./T1547/T1547.008-LSASS-Driver.md | ✅ | - |
| T1547.009 | Shortcut Modification | 快捷方式修改 | T1547 | ./T1547/T1547.009-Shortcut-Modification.md | ✅ | - |
| T1547.010 | Port Monitors | 端口监视器 | T1547 | ./T1547/T1547.010-Port-Monitors.md | ✅ | - |
| T1547.012 | Print Processors | 打印处理器 | T1547 | ./T1547/T1547.012-Print-Processors.md | ✅ | - |
| T1547.013 | XDG Autostart Entries | XDG自动启动条目 | T1547 | ./T1547/T1547.013-XDG-Autostart-Entries.md | ✅ | - |
| T1547.014 | Active Setup | Active Setup | T1547 | ./T1547/T1547.014-Active-Setup.md | ✅ | - |
| T1547.015 | Login Items | 登录项 | T1547 | ./T1547/T1547.015-Login-Items.md | ✅ | - |
| T1037.001 | Logon Script (Windows) | 登录脚本（Windows） | T1037 | ./T1037/T1037.001-Logon-Script-Windows.md | ✅ | - |
| T1037.002 | Login Hook | 登录脚本（Mac） | T1037 | ./T1037/T1037.002-Login-Hook.md | ✅ | - |
| T1037.003 | Network Logon Script | 登录脚本（Linux） | T1037 | ./T1037/T1037.003-Network-Logon-Script.md | ✅ | - |
| T1037.004 | RC Scripts | 登录脚本（网络） | T1037 | ./T1037/T1037.004-RC-Scripts.md | ✅ | - |
| T1037.005 | Startup Items | 登录脚本（跨平台） | T1037 | ./T1037/T1037.005-Startup-Items.md | ✅ | - |
| T1136.001 | Local Account | 本地账户 | T1136 | ./T1136/T1136.001-Local-Account.md | ✅ | - |
| T1136.002 | Domain Account | 域账户 | T1136 | ./T1136/T1136.002-Domain-Account.md | ✅ | - |
| T1136.003 | Cloud Account | 云账户 | T1136 | ./T1136/T1136.003-Cloud-Account.md | ✅ | - |
| T1543.001 | Launch Agent | 启动代理 | T1543 | ./T1543/T1543.001-Launch-Agent.md | ✅ | - |
| T1543.002 | Systemd Service | SystemD服务 | T1543 | ./T1543/T1543.002-SystemD-Service.md | ✅ | 🔄 本地名: SystemD Service |
| T1543.003 | Windows Service | Windows服务 | T1543 | ./T1543/T1543.003-Windows-Service.md | ✅ | - |
| T1543.004 | Launch Daemon | 启动守护进程 | T1543 | ./T1543/T1543.004-Launch-Daemon.md | ✅ | - |
| T1543.005 | Container Service | 容器 | T1543 | ./T1543/T1543.005-Container-Service.md | ✅ | - |
| T1546.001 | Change Default File Association | 更改默认文件关联 | T1546 | ./T1546/T1546.001-Change-Default-File-Association.md | ✅ | - |
| T1546.002 | Screensaver | 屏幕保护程序 | T1546 | ./T1546/T1546.002-Screensaver.md | ✅ | - |
| T1546.003 | Windows Management Instrumentation Event Subscription | WMI事件订阅 | T1546 | ./T1546/T1546.003-Windows-Management-Instrumentation-Event-Subscription.md | ✅ | - |
| T1546.004 | Unix Shell Configuration Modification | Unix Shell配置修改 | T1546 | ./T1546/T1546.004-Unix-Shell-Configuration-Modification.md | ✅ | - |
| T1546.005 | Trap | Trap | T1546 | ./T1546/T1546.005-Trap.md | ✅ | - |
| T1546.006 | LC_LOAD_DYLIB Addition | LC_LOAD_DYLIB添加 | T1546 | ./T1546/T1546.006-LC-LOAD-DYLIB-Addition.md | ✅ | - |
| T1546.007 | Netsh Helper DLL | Netsh辅助DLL | T1546 | ./T1546/T1546.007-Netsh-Helper-DLL.md | ✅ | - |
| T1546.008 | Accessibility Features | 辅助功能 | T1546 | ./T1546/T1546.008-Accessibility-Features.md | ✅ | - |
| T1546.009 | AppCert DLLs | AppCert DLLs | T1546 | ./T1546/T1546.009-Appcert-Dlls.md | ✅ | - |
| T1546.010 | AppInit DLLs | AppInit DLLs | T1546 | ./T1546/T1546.010-Appinit-Dlls.md | ✅ | - |
| T1546.011 | Application Shimming | 应用程序兼容性垫片 | T1546 | ./T1546/T1546.011-Application-Shimming.md | ✅ | - |
| T1546.012 | Image File Execution Options Injection | 映像文件执行选项 | T1546 | ./T1546/T1546.012-Image-File-Execution-Options-Injection.md | ✅ | - |
| T1546.013 | PowerShell Profile | PowerShell配置文件 | T1546 | ./T1546/T1546.013-PowerShell-Profile.md | ✅ | - |
| T1546.014 | Emond | 电子邮件 | T1546 | ./T1546/T1546.014-Emond.md | ✅ | - |
| T1546.015 | Component Object Model Hijacking | 更新编排器 | T1546 | ./T1546/T1546.015-Component-Object-Model-Hijacking.md | ✅ | - |
| T1546.016 | Installer Packages | 安装程序包 | T1546 | ./T1546/T1546.016-Installer-Packages.md | ✅ | - |
| T1546.017 | Udev Rules | Udev 规则 | T1546 | ./T1546/T1546.017-Udev-Rules.md | ✅ | - |
| T1546.018 | Python Startup Hooks | Python 启动钩子 | T1546 | ./T1546/T1546.018-Python-Startup-Hooks.md | ✅ | - |
| T1556.001 | Domain Controller Authentication | 域控制器认证 | T1556 | ./T1556/T1556.001-Domain-Controller-Authentication.md | ✅ | - |
| T1556.002 | Password Filter DLL | 密码过滤器 | T1556 | ./T1556/T1556.002-Password-Filter-DLL.md | ✅ | - |
| T1556.003 | Pluggable Authentication Modules | PAM | T1556 | ./T1556/T1556.003-Pluggable-Authentication-Modules-PAM.md | ✅ | - |
| T1556.004 | Network Device Authentication | 网络设备认证 | T1556 | ./T1556/T1556.004-Network-Device-Authentication.md | ✅ | - |
| T1556.005 | Reversible Encryption | 多因素认证 | T1556 | ./T1556/T1556.005-Reversible-Encryption.md | ✅ | - |
| T1556.006 | Multi-Factor Authentication | 混合身份 | T1556 | ./T1556/T1556.006-Multi-factor-Authentication.md | ✅ | - |
| T1556.007 | Hybrid Identity | 混合身份同步 | T1556 | ./T1556/T1556.007-Hybrid-Identity.md | ✅ | - |
| T1556.008 | Network Provider DLL | 网络提供程序DLL | T1556 | ./T1556/T1556.008-Network-Provider-DLL.md | ✅ | - |
| T1556.009 | Conditional Access Policies | 条件访问策略 | T1556 | ./T1556/T1556.009-Conditional-Access-Policies.md | ✅ | - |
| T1137.001 | Office Template Macros | Office模板宏 | T1137 | ./T1137/T1137.001-Office-Template-Macros.md | ✅ | - |
| T1137.002 | Office Test | Office加载项 | T1137 | ./T1137/T1137.002-Office-Test.md | ✅ | - |
| T1137.003 | Outlook Forms | Outlook表单 | T1137 | ./T1137/T1137.003-Outlook-Forms.md | ✅ | - |
| T1137.004 | Outlook Home Page | Outlook主页 | T1137 | ./T1137/T1137.004-Outlook-Home-Page.md | ✅ | - |
| T1137.005 | Outlook Rules | Outlook规则 | T1137 | ./T1137/T1137.005-Outlook-Rules.md | ✅ | - |
| T1137.006 | Add-ins | Outlook API | T1137 | ./T1137/T1137.006-Add-ins.md | ✅ | - |
| T1542.001 | System Firmware | 系统固件 | T1542 | ./T1542/T1542.001-System-Firmware.md | ✅ | - |
| T1542.002 | Component Firmware | 组件固件 | T1542 | ./T1542/T1542.002-Component-Firmware.md | ✅ | - |
| T1542.003 | Bootkit | 引导工具包 | T1542 | ./T1542/T1542.003-Bootkit.md | ✅ | - |
| T1542.004 | ROMMONkit | ROMMONkit | T1542 | ./T1542/T1542.004-ROMMONkit.md | ✅ | - |
| T1542.005 | TFTP Boot | TFTP启动 | T1542 | ./T1542/T1542.005-TFTP-Boot.md | ✅ | - |
| T1053.002 | At | At（Linux） | T1053 | ./T1053/T1053.002-At.md | ✅ | - |
| T1053.003 | Cron | 定时任务 | T1053 | ./T1053/T1053.003-Cron.md | ✅ | - |
| T1053.005 | Scheduled Task | 计划任务（Windows） | T1053 | ./T1053/T1053.005-Scheduled-Task.md | ✅ | - |
| T1053.006 | Systemd Timers | Systemd定时器 | T1053 | ./T1053/T1053.006-Systemd-Timers.md | ✅ | - |
| T1053.007 | Container Orchestration Job | 容器编排作业 | T1053 | ./T1053/T1053.007-Container-Orchestration-Job.md | ✅ | - |
| T1505.001 | SQL Stored Procedures | SQL存储过程 | T1505 | ./T1505/T1505.001-SQL-Stored-Procedures.md | ✅ | - |
| T1505.002 | Transport Agent | 传输代理 | T1505 | ./T1505/T1505.002-Transport-Agent.md | ✅ | - |
| T1505.003 | Web Shell | WebShell | T1505 | ./T1505/T1505.003-Web-Shell.md | ✅ | - |
| T1505.004 | IIS Components | IIS组件 | T1505 | ./T1505/T1505.004-IIS-Components.md | ✅ | - |
| T1505.005 | Terminal Services DLL | 终端服务 | T1505 | ./T1505/T1505.005-Terminal-Services-DLL.md | ✅ | - |
| T1505.006 | vSphere Installation Bundles |  | T1505 | ./T1505/T1505.006-Vsphere-Installation-Bundles.md | 📝 | - |
| T1176.001 | Browser Extensions | Microsoft Office加载项 | T1176 | ./T1176/T1176.001-Browser-Extensions.md | ✅ | - |
| T1176.002 | IDE Extensions | 浏览器扩展 | T1176 | ./T1176/T1176.002-IDE-Extensions.md | ✅ | - |
| T1205.001 | Port Knocking | 端口敲门 | T1205 | ./T1205/T1205.001-Port-Knocking.md | ✅ | - |
| T1205.002 | Socket Filters | 套接字过滤器 | T1205 | ./T1205/T1205.002-Socket-Filters.md | ✅ | - |
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

### 名称不一致 (1 项)
- **T1543.002** (subtech): 官方=`Systemd Service` vs 本地=`SystemD Service`

## 参考来源

- [MITRE ATT&CK - TA0003](https://attack.mitre.org/tactics/TA0003/)
- [MITRE ATT&CK STIX Data v19.1](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-07-28
