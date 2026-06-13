# 权限提升 (TA0004)

## 一句话理解

> 权限提升就像从普通员工变成公司管理员——拿到门禁卡后，想办法进入总经理办公室，获取更高的系统控制权。

## 战术概述

权限提升是攻击者在获得初始访问后，试图获取更高权限级别的技术总称。想象一下：你通过钓鱼邮件拿到了一个普通员工的电脑账号，但这个账号只能看看邮件、写写文档。你想看财务报表、修改系统配置、甚至删库跑路——这些都需要管理员权限。权限提升就是从"普通员工"变成"IT管理员"甚至"系统管理员"的过程。

在实际攻击中，权限提升通常是攻击链中的关键一步。攻击者通过初始访问（比如钓鱼邮件、漏洞利用）进入目标系统后，往往只获得了低权限的用户身份。要真正控制目标系统、访问敏感数据、部署恶意软件或进行横向移动，攻击者必须提升自己的权限到 SYSTEM（Windows 最高权限）或 root（Linux 最高权限）级别。

权限提升的常见手段包括：
- **利用系统漏洞**：操作系统或应用程序中的安全缺陷
- **滥用合法功能**：如 UAC 绕过、计划任务、服务配置错误
- **窃取高权限凭据**：获取管理员密码或令牌
- **进程注入**：将恶意代码注入高权限进程中运行
- **配置错误利用**：利用系统或云环境的错误配置

## 战术在攻击链中的位置

### 攻击链全景图

```mermaid
graph LR
    A["侦察<br/>TA0043"] --> B["资源开发<br/>TA0042"]
    B --> C["初始访问<br/>TA0001"]
    C --> D["执行<br/>TA0002"]
    D --> E["持久化<br/>TA0003"]
    E --> F["权限提升<br/>TA0004"]
    F --> G["隐蔽<br/>TA0005"]
    G --> H["防御削弱<br/>TA0112"]
    H --> I["凭证访问<br/>TA0006"]
    I --> J["发现<br/>TA0007"]
    J --> K["横向移动<br/>TA0008"]
    K --> L["收集<br/>TA0009"]
    L --> M["命令与控制<br/>TA0011"]
    M --> N["数据窃取<br/>TA0010"]
    N --> O["影响<br/>TA0040"]

    style F fill:#ff6b6b,stroke:#333,stroke-width:2px
```

### 当前战术的角色

权限提升是攻击链中的核心环节，通常在攻击者获得初始访问（TA0001）和执行（TA0002）之后进行。没有足够的权限，攻击者无法安装持久化组件、窃取敏感数据或横向移动到其他系统。权限提升为后续的隐蔽（TA0005）、凭证访问（TA0006）和横向移动（TA0008）等战术提供了必要的权限基础。

### 前置战术

- **初始访问（TA0001）**：攻击者需要先获得目标系统的初始入口，通常是一个低权限的用户账户或服务账户
- **执行（TA0002）**：获得初始访问后，攻击者需要能在目标系统上执行代码，才能运行提权工具和漏洞利用程序
- **持久化（TA0003）**：部分提权技术（如创建服务、修改自启动项）同时也是持久化手段，两者经常结合使用

### 后续战术

- **隐蔽（TA0005）**：获得高权限后，攻击者可以更有效地隐藏自身活动，如禁用安全工具、清除日志
- **防御削弱（TA0112）**：高权限允许攻击者修改防火墙规则、禁用端点保护、关闭审计日志
- **凭证访问（TA0006）**：SYSTEM/root 权限可以访问所有进程的内存和文件，方便窃取其他用户的凭据
- **发现（TA0007）**：高权限使攻击者能执行更深入的发现操作，包括查看所有用户的数据和系统配置
- **横向移动（TA0008）**：获得高权限后，攻击者可以更自由地通过网络在系统间移动

## 技术索引表

| 技术ID | 中文名称 | 难度 | 子技术数 | 一句话理解 | 文档状态 |
|--------|----------|:----:|:--------:|------------|:--------:|
| [T1548](./T1548-Abuse-Elevation-Control-Mechanism.md) | 滥用提升控制机制 | ⭐⭐ | 4 | 绕过系统自带的权限"门禁"机制 | ✅ 已完成 |
| [T1134](./T1134-Access-Token-Manipulation.md) | 访问令牌操纵 | ⭐⭐⭐ | 5 | 偷别人的"工牌"冒充高权限用户 | ✅ 已完成 |
| [T1098](./T1098-Account-Manipulation.md) | 账户操纵 | ⭐⭐ | 7 | 悄悄给自己升职加薪 | ✅ 已完成 |
| [T1547](./T1547-Boot-or-Logon-Autostart-Execution.md) | 引导或登录自启动执行 | ⭐⭐ | 14 | 让恶意程序在开机时自动以高权限运行 | ✅ 已完成 |
| [T1037](./T1037-Boot-or-Logon-Initialization-Scripts.md) | 引导或登录初始化脚本 | ⭐⭐ | 5 | 在系统启动脚本里塞入恶意命令 | ✅ 已完成 |
| [T1543](./T1543-Create-or-Modify-System-Process.md) | 创建或修改系统进程 | ⭐⭐ | 4 | 创建一个"合法"的系统服务来运行恶意代码 | ✅ 已完成 |
| [T1484](./T1484-Domain-or-Tenant-Policy-Modification.md) | 域或租户策略修改 | ⭐⭐⭐ | 4 | 修改公司的"规章制度"让自己为所欲为 | ✅ 已完成 |
| [T1611](./T1611-Escape-to-Host.md) | 逃逸到主机 | ⭐⭐⭐ | 4 | 从虚拟机/容器里"越狱"到宿主机 | ✅ 已完成 |
| [T1546](./T1546-Event-Triggered-Execution.md) | 事件触发执行 | ⭐⭐⭐ | 12 | 设置一个"定时炸弹"，特定事件发生时自动执行 | ✅ 已完成 |
| [T1068](./T1068-Exploitation-for-Privilege-Escalation.md) | 利用漏洞提升权限 | ⭐⭐⭐ | 0 | 利用系统漏洞直接获取最高权限 | ✅ 已完成 |
| [T1055](./T1055-Process-Injection.md) | 进程注入 | ⭐⭐⭐ | 14 | 把恶意代码"寄生"在合法的高权限进程里 | ✅ 已完成 |
| [T1053](./T1053-Scheduled-Task-Job.md) | 计划任务/作业 | ⭐ | 7 | 利用系统的"定时闹钟"功能执行恶意代码 | ✅ 已完成 |
| [T1078](./T1078-Valid-Accounts.md) | 有效账户 | ⭐ | 4 | 直接用别人的账号密码登录高权限账户 | ✅ 已完成 |



## 子技术索引

| 子技术ID | 名称 | 难度 | 一句话理解 | 文档状态 |
|----------|------|:----:|-----------|:--------:|
| [T1037.001](./T1037/T1037.001-Logon Script (Windows)-登录脚本 (Windows).md) | 登录脚本 (Windows) | ⭐⭐ | 在 Windows 组策略或注册表中的登录脚本里塞入恶意命令 | ✅ 已完成 |
| [T1037.002](./T1037/T1037.002-Login Hook (macOS)-登录钩子 (macOS).md) | 登录钩子 (macOS) | ⭐⭐ | 利用 macOS 的 Login Hook 机制在用户登录时执行恶意代码 | ✅ 已完成 |
| [T1037.003](./T1037/T1037.003-Network Logon Script (Windows)-网络登录脚本 (Windows).md) | 网络登录脚本 (Windows) | ⭐⭐ | 修改域控制器上分发的网络登录脚本，影响所有域用户 | ✅ 已完成 |
| [T1037.004](./T1037/T1037.004-RC Scripts (Linux-macOS)-RC 脚本 (Linux-macOS).md) | RC 脚本 (Linux/macOS) | ⭐⭐ | 在 Linux 的 `/etc/rc.local` 等启动脚本中植入恶意命令 | ✅ 已完成 |
| [T1037.005](./T1037/T1037.005-Startup Item (macOS)-启动项 (macOS).md) | 启动项 (macOS) | ⭐⭐ | 在 macOS 的启动项目录中放置恶意程序 | ✅ 已完成 |
| [T1053.001](./T1053/T1053.001-At-At (Windows).md) | At (Windows) | ⭐ | 使用 Windows 的 at 命令创建一次性定时任务（已弃用但可能仍可用） | ✅ 已完成 |
| [T1053.002](./T1053/T1053.002-At-At (Linux).md) | At (Linux) | ⭐ | 使用 Linux 的 at 命令创建一次性定时任务 | ✅ 已完成 |
| [T1053.003](./T1053/T1053.003-Cron-Cron.md) | Cron | ⭐ | 利用 Linux/macOS 的 cron 定时执行恶意命令 | ✅ 已完成 |
| [T1053.005](./T1053/T1053.005-计划任务-计划任务 (Windows).md) | 计划任务 (Windows) | ⭐ | 使用 Windows 任务计划程序创建以 SYSTEM 权限运行的任务 | ✅ 已完成 |
| [T1053.006](./T1053/T1053.006-Systemd-定时器.md) | Systemd 定时器 | ⭐ | 利用 Linux systemd 的定时器功能执行恶意代码 | ✅ 已完成 |
| [T1053.007](./T1053/T1053.007-Container-Orchestration-Job.md) | 容器编排作业 | ⭐ | 在 Kubernetes 中创建恶意 CronJob 以高权限运行容器 | ✅ 已完成 |
| [T1055.001](./T1055/T1055.001-DLL-Injection.md) | DLL 注入 | ⭐⭐⭐ | 让系统进程加载恶意的动态链接库 | ✅ 已完成 |
| [T1055.002](./T1055/T1055.002-PE-Injection.md) | PE 注入 | ⭐⭐⭐ | 直接把完整的恶意程序塞进目标进程内存 | ✅ 已完成 |
| [T1055.003](./T1055/T1055.003-Thread-Execution-Hijacking.md) | 线程执行劫持 | ⭐⭐⭐ | 劫持目标进程的线程，让它执行恶意代码 | ✅ 已完成 |
| [T1055.004](./T1055/T1055.004-Asynchronous Procedure Call-异步过程调用 (APC).md) | 异步过程调用 (APC) | ⭐⭐⭐ | 利用系统的"排队执行"机制注入代码 | ✅ 已完成 |
| [T1055.005](./T1055/T1055.005-Thread Local Storage-线程本地存储 (TLS).md) | 线程本地存储 (TLS) | ⭐⭐⭐ | 利用线程存储回调机制执行恶意代码 | ✅ 已完成 |
| [T1055.007](./T1055/T1055.007-Ptrace-System-Calls.md) | Ptrace 系统调用 | ⭐⭐⭐ | Linux 上的进程调试接口，被滥用来注入代码 | ✅ 已完成 |
| [T1055.008](./T1055/T1055.008-VDSO-Hijacking.md) | VDSO 劫持 | ⭐⭐⭐ | 覆盖 Linux 的虚拟动态共享对象 | ✅ 已完成 |
| [T1055.009](./T1055/T1055.009-Proc-Memory.md) | Proc 内存 | ⭐⭐⭐ | 通过 /proc 文件系统直接修改进程内存 | ✅ 已完成 |
| [T1055.010](./T1055/T1055.010-Process-Hollowing.md) | 进程空心化 | ⭐⭐⭐ | 创建合法进程然后替换其内存内容 | ✅ 已完成 |
| [T1055.011](./T1055/T1055.011-Extra-Window-Memory-Injection.md) | 额外窗口内存注入 | ⭐⭐⭐ | 利用 Windows 窗口机制存储恶意代码 | ✅ 已完成 |
| [T1055.012](./T1055/T1055.012-Process-Herpaderping.md) | 进程重影 | ⭐⭐⭐ | 利用 NTFS 事务功能创建"隐形"进程 | ✅ 已完成 |
| [T1055.013](./T1055/T1055.013-ProcMem-Linux-ProcMem-Linux.md) | ProcMem Linux | ⭐⭐⭐ | Linux 上通过 /proc/mem 注入代码 | ✅ 已完成 |
| [T1055.014](./T1055/T1055.014-VDSO-Linux-VDSO-Linux.md) | VDSO Linux | ⭐⭐⭐ | 覆盖 Linux VDSO 页面执行恶意代码 | ✅ 已完成 |
| [T1078.001](./T1078/T1078.001-Default-Accounts.md) | 默认账户 | ⭐ | 使用设备或软件的出厂默认用户名和密码（如 admin/admin） | ✅ 已完成 |
| [T1078.002](./T1078/T1078.002-Domain-Account.md) | 域账户 | ⭐ | 使用 Active Directory 域中的账户凭据登录域资源 | ✅ 已完成 |
| [T1078.003](./T1078/T1078.003-Local-Account.md) | 本地账户 | ⭐ | 使用操作系统本地账户的凭据登录计算机 | ✅ 已完成 |
| [T1078.004](./T1078/T1078.004-Cloud-Account.md) | 云账户 | ⭐ | 使用云平台（AWS、Azure、GCP）的账户凭据访问云资源 | ✅ 已完成 |
| [T1098.001](./T1098/T1098.001-Additional-Cloud-Credentials.md) | 额外云凭据 | ⭐⭐ | 为云账户创建额外的 API 密钥或访问令牌 | ✅ 已完成 |
| [T1098.002](./T1098/T1098.002-Additional-Email-Delegate-Permissions.md) | 额外电子邮件委派权限 | ⭐⭐ | 给自己授予访问他人邮箱的权限 | ✅ 已完成 |
| [T1098.003](./T1098/T1098.003-Additional-Cloud-Roles.md) | 额外云角色 | ⭐⭐ | 为云账户分配高权限的 IAM 角色 | ✅ 已完成 |
| [T1098.004](./T1098/T1098.004-SSH-Authorized-Keys.md) | SSH 授权密钥 | ⭐⭐ | 在服务器上植入自己的 SSH 公钥实现免密 root 登录 | ✅ 已完成 |
| [T1098.005](./T1098/T1098.005-Device-Registration.md) | 设备注册 | ⭐⭐ | 在身份提供商中注册受控设备 | ✅ 已完成 |
| [T1098.006](./T1098/T1098.006-Additional-Container-Cluster-Roles.md) | 额外容器集群角色 | ⭐⭐ | 为 Kubernetes 服务账户绑定高权限角色 | ✅ 已完成 |
| [T1098.007](./T1098/T1098.007-Additional-Local-or-Domain-Groups.md) | 额外本地或域组 | ⭐⭐ | 将用户添加到本地管理员或域管理员组 | ✅ 已完成 |
| [T1134.001](./T1134/T1134.001-Token-Impersonation-Theft-令牌冒充.md) | 令牌冒充/盗取 | ⭐⭐⭐ | 从高权限进程"偷"令牌来冒充管理员 | ✅ 已完成 |
| [T1134.002](./T1134/T1134.002-Create-Process-with-Token.md) | 使用令牌创建进程 | ⭐⭐⭐ | 用偷来的令牌启动新进程，新进程也有高权限 | ✅ 已完成 |
| [T1134.003](./T1134/T1134.003-Make-and-Impersonate-Token.md) | 制作并冒充令牌 | ⭐⭐⭐ | 自己伪造一个高权限令牌 | ✅ 已完成 |
| [T1134.004](./T1134/T1134.004-Parent-PID-Spoofing.md) | 父进程ID欺骗 | ⭐⭐⭐ | 伪装进程的"父进程"，让系统以为是合法程序启动的 | ✅ 已完成 |
| [T1134.005](./T1134/T1134.005-SID-History-Injection-SID.md) | SID-History 注入 | ⭐⭐⭐ | 在域中注入虚假的历史身份信息 | ✅ 已完成 |
| [T1484.001](./T1484/T1484.001-Group-Policy-Modification.md) | 组策略修改 | ⭐⭐⭐ | 修改 Windows 域的 GPO，影响域内所有计算机 | ✅ 已完成 |
| [T1484.002](./T1484/T1484.002-Trust-Modification.md) | 信任修改 | ⭐⭐⭐ | 修改 AD 信任关系或联合身份验证配置，伪造身份令牌 | ✅ 已完成 |
| [T1484.003](./T1484/T1484.003-Cloud-Policy-Modification.md) | 云策略修改 | ⭐⭐⭐ | 修改 Azure AD/Office 365 的条件访问和安全策略 | ✅ 已完成 |
| [T1484.004](./T1484/T1484.004-Cloud-Implicit-Trust-Modification.md) | 云隐式信任修改 | ⭐⭐⭐ | 修改云环境中的隐式信任关系 | ✅ 已完成 |
| [T1543.001](./T1543/T1543.001-Windows-Service.md) | Windows 服务 | ⭐⭐ | 创建或修改 Windows 服务，使其以 SYSTEM 权限自动运行 | ✅ 已完成 |
| [T1543.002](./T1543/T1543.002-System-Daemon.md) | 系统守护进程 | ⭐⭐ | 在 Linux/Mac 上创建或修改系统守护进程（systemd/launchd） | ✅ 已完成 |
| [T1543.003](./T1543/T1543.003-Windows Service (Alternative)-Windows 服务（另一视角）.md) | Windows 服务（另一视角） | ⭐⭐ | IOC 视野下关注的 Windows 服务异常行为 | ✅ 已完成 |
| [T1543.004](./T1543/T1543.004-launchd-launchd.md) | launchd | ⭐⭐ | 在 macOS 上创建或修改 launchd 守护进程或代理 | ✅ 已完成 |
| [T1546.001](./T1546/T1546.001-Change-Default-File-Association.md) | 更改默认文件关联 | ⭐⭐ | 改修文件类型默认打开程序，点击.tx t文件变成启动恶意软件 | ✅ 已完成 |
| [T1546.002](./T1546/T1546.002-Screensaver.md) | 屏幕保护程序 | ⭐⭐ | 设置恶意程序为屏保程序，屏幕锁定时触发 | ✅ 已完成 |
| [T1546.003](./T1546/T1546.003-WMI-Event-Subscription.md) | Windows 管理规范事件订阅 | ⭐⭐ | 注册 WMI 事件，系统条件满足时触发恶意脚本 | ✅ 已完成 |
| [T1546.004](./T1546/T1546.004-bash_profile-and-.bashrc.md) | .bash_profile 和 .bashrc | ⭐⭐ | 修改 Linux 用户的 shell 配置文件，登录时触发 | ✅ 已完成 |
| [T1546.005](./T1546/T1546.005-Application-Initialization.md) | 应用程序初始化 | ⭐⭐ | 修改 DLL 劫持配置，程序启动时加载恶意 DLL | ✅ 已完成 |
| [T1546.006](./T1546/T1546.006-Accessibility-Features.md) | 辅助功能 | ⭐⭐ | 替换登录界面的辅助功能程序（如放大镜），在登录前以 SYSTEM 运行 | ✅ 已完成 |
| [T1546.007](./T1546/T1546.007-Netsh-Helper-DLL.md) | Netsh 帮助程序 DLL | ⭐⭐ | 通过 netsh 加载恶意 DLL，在管理员上下文中执行 | ✅ 已完成 |
| [T1546.008](./T1546/T1546.008-Accessibility-Features.md) | 访问功能 | ⭐⭐ | 修改登录界面的访问功能，类似辅助功能 | ✅ 已完成 |
| [T1546.009](./T1546/T1546.009-AppCert-DLL-AppCert-DLL.md) | AppCert DLL | ⭐⭐ | 通过 AppCert DLL 注册，所有调用 CreateProcess 的进程都加载恶意 DLL | ✅ 已完成 |
| [T1546.010](./T1546/T1546.010-AppInit-DLL-AppInit-DLL.md) | AppInit DLL | ⭐⭐ | 通过 AppInit DLL 注入，所有加载 user32.dll 的进程加载恶意 DLL | ✅ 已完成 |
| [T1546.011](./T1546/T1546.011-Application-Shutdown.md) | 应用程序关闭 | ⭐⭐ | 设置程序退出时的自动执行逻辑 | ✅ 已完成 |
| [T1546.012](./T1546/T1546.012-Security-Support-Provider.md) | 安全支持提供器 | ⭐⭐ | 注册 SSP 在 LSASS 启动后自动加载，监控所有认证事件 | ✅ 已完成 |
| [T1547.001](./T1547/T1547.001-Registry-Auto-start-Entry.md) | 注册表自启项 | ⭐ | 在注册表 Run/RunOnce 中添加启动项，最经典的自动启动方法 | ✅ 已完成 |
| [T1547.002](./T1547/T1547.002-Authentication-Package.md) | 身份验证包 | ⭐ | 注册身份验证包 DLL，在 LSASS 中加载 | ✅ 已完成 |
| [T1547.003](./T1547/T1547.003-Time-Providers.md) | 时间提供程序 | ⭐ | 注册 Windows 时间服务扩展 DLL | ✅ 已完成 |
| [T1547.004](./T1547/T1547.004-Winlogon-Helper-DLL.md) | Winlogon 辅助 DLL | ⭐ | 注册 Winlogon 通知包，在用户登录时加载 | ✅ 已完成 |
| [T1547.005](./T1547/T1547.005-Kernel-Modules-and-Extensions.md) | 内核模块和扩展 | ⭐ | 加载恶意的内核驱动程序或内核模块 | ✅ 已完成 |
| [T1547.006](./T1547/T1547.006-Enable-Startup-Folder.md) | 启用启动文件夹 | ⭐ | 在开始菜单启动文件夹中放置快捷方式 | ✅ 已完成 |
| [T1547.007](./T1547/T1547.007-Re-open-Applications.md) | 重新打开应用程序 | ⭐ | 利用 Windows 10/11 的自动重新打开应用功能 | ✅ 已完成 |
| [T1547.008](./T1547/T1547.008-LSASS-Driver.md) | LSASS 驱动 | ⭐ | 在 LSASS 中加载恶意驱动程序 | ✅ 已完成 |
| [T1547.009](./T1547/T1547.009-Shortcut-Modification.md) | 快捷方式修改 | ⭐ | 修改系统启动自动加载的快捷方式目标路径 | ✅ 已完成 |
| [T1547.010](./T1547/T1547.010-Port-Monitors.md) | 端口监视器 | ⭐ | 注册端口监视器 DLL，打印子系统加载时自动执行 | ✅ 已完成 |
| [T1547.011](./T1547/T1547.011-Print-Processors.md) | 打印机进程 | ⭐ | 利用打印子系统加载恶意 DLL | ✅ 已完成 |
| [T1547.012](./T1547/T1547.012-Print-Processors.md) | 打印处理器 | ⭐ | 注册打印处理器组件 | ✅ 已完成 |
| [T1547.013](./T1547/T1547.013-Startup-Agent.md) | 启动代理 | ⭐ | macOS 启动代理（LaunchAgent）持久化 | ✅ 已完成 |
| [T1547.014](./T1547/T1547.014-Active-Setup-Modification.md) | 活动设置修改 | ⭐ | 修改活动设置实现持久化 | ✅ 已完成 |
| [T1548.001](./T1548/T1548.001-Bypass-User-Account-Control.md) | 绕过 UAC | ⭐⭐ | 欺骗 Windows 让恶意程序以管理员权限运行而不弹窗确认 | ✅ 已完成 |
| [T1548.002](./T1548/T1548.002-Bypass-sudo.md) | 绕过 sudo | ⭐⭐ | 利用 sudo 配置错误在 Linux/Mac 上以 root 权限运行 | ✅ 已完成 |
| [T1548.003](./T1548/T1548.003-Sudo-Caching.md) | Sudo 权限缓存 | ⭐⭐ | 利用 sudo 的"记住密码"特性，在缓存过期前使用 root 权限 | ✅ 已完成 |
| [T1548.004](./T1548/T1548.004-Bypass-System-Authorization-Components.md) | 绕过系统授权组件 | ⭐⭐ | 绕过系统的授权验证框架（如 Polkit） | ✅ 已完成 |
| [T1611.001](./T1611/T1611.001-Virtual-Machine-Escape.md) | 虚拟机逃逸 | ⭐⭐⭐ | 从客户虚拟机突破到虚拟机管理程序或宿主机 | ✅ 已完成 |
| [T1611.002](./T1611/T1611.002-Container-Escape.md) | 容器逃逸 | ⭐⭐⭐ | 从 Docker/容器运行时突破到宿主机 | ✅ 已完成 |
| [T1611.003](./T1611/T1611.003-Application-Sandbox-Escape.md) | 应用程序沙箱逃逸 | ⭐⭐⭐ | 从浏览器或应用程序沙箱中逃逸到操作系统 | ✅ 已完成 |
| [T1611.004](./T1611/T1611.004-Hardware-Peripheral-Escape-硬件.md) | 硬件/外设隔离逃逸 | ⭐⭐⭐ | 利用 GPU、USB、网络设备等硬件虚拟化漏洞逃逸 | ✅ 已完成 |

### 统计信息

- **技术总数**：13 个
- **子技术总数**：82 个
- **已完成文档**：82 个
- **进行中文档**：0 个
- **待编写文档**：0 个

## 推荐阅读顺序

### 入门阶段（第1-2周）

> 适合零基础的安全爱好者，从最简单、最直观的提权技术开始。

**前置知识：** 了解基本的操作系统用户权限概念，会使用命令行终端。

**推荐阅读：**

1. **[T1078 有效账户](./T1078-Valid-Accounts.md)** - 最简单的提权方式，直接用别人的账号，无需任何漏洞利用
2. **[T1053 计划任务/作业](./T1053-Scheduled-Task-Job.md)** - 利用系统自带的定时任务功能，容易理解且操作直观
3. **[T1548 滥用提升控制机制](./T1548-Abuse-Elevation-Control-Mechanism.md)** - 了解 UAC、sudo 等权限控制机制的工作原理

**学习建议：**
- 建议在虚拟机中搭建 Windows 10/11 和 Ubuntu 环境进行实验
- 每个技术先读完所有内容，再动手做实验
- 如果某个实验不成功，仔细检查权限要求和系统版本

### 进阶阶段（第3-4周）

> 适合有一定基础的学习者，开始接触更复杂的权限维持和提权技术。

**前置知识：** 掌握用户账户和权限系统基础，了解 Windows 注册表和 Linux 文件系统。

**推荐阅读：**

1. **[T1547 引导或登录自启动执行](./T1547-Boot-or-Logon-Autostart-Execution.md)** - 理解持久化与提权的结合，Windows 有 15+ 种自启动机制
2. **[T1543 创建或修改系统进程](./T1543-Create-or-Modify-System-Process.md)** - 服务提权的核心技术，Windows 和 Linux 都可实践
3. **[T1037 引导或登录初始化脚本](./T1037-Boot-or-Logon-Initialization-Scripts.md)** - 脚本层面的提权，跨平台适用
4. **[T1098 账户操纵](./T1098-Account-Manipulation.md)** - 云环境和 AD 域中的提权手段，现代企业中越来越重要

**学习建议：**
- 搭建一个简单的 AD 域环境（可以用 Windows Server 虚拟机）
- 练习使用 PowerShell 和 Bash 脚本操作注册表、服务、计划任务
- 尝试使用 BloodHound 分析 AD 权限关系

### 高级阶段（第5-6周）

> 适合有较好技术基础的学习者，深入理解复杂的提权技术原理。

**前置知识：** 理解操作系统内核概念、进程和内存管理、Windows 令牌机制。

**推荐阅读：**

1. **[T1068 利用漏洞提升权限](./T1068-Exploitation-for-Privilege-Escalation.md)** - 内核漏洞利用和 BYOVD 攻击，了解 CVE 和 PoC 的工作原理
2. **[T1055 进程注入](./T1055-Process-Injection.md)** - 最复杂的提权技术之一，需要理解 Windows 内存管理和 API 调用
3. **[T1134 访问令牌操纵](./T1134-Access-Token-Manipulation.md)** - Windows 令牌机制的深度利用，了解 SeImpersonatePrivilege 等高级概念
4. **[T1546 事件触发执行](./T1546-Event-Triggered-Execution.md)** - 高级持久化提权技术，WMI 事件订阅等无文件攻击
5. **[T1484 域或租户策略修改](./T1484-Domain-or-Tenant-Policy-Modification.md)** - AD 域和云环境的高级提权，GPO 和 Azure AD 策略
6. **[T1611 逃逸到主机](./T1611-Escape-to-Host.md)** - 容器和虚拟化环境的提权，云原生安全的新兴领域

**学习建议：**
- 在隔离的实验室环境中练习漏洞利用（推荐使用 Hack The Box 或 TryHackMe）
- 学习使用 WinDbg、GDB 等调试工具理解底层原理
- 关注 CISA KEV 目录了解最新被积极利用的提权漏洞
- 建议搭建 Kubernetes 实验环境练习容器逃逸技术

## 参考资料

### 官方文档

- [MITRE ATT&CK - Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [MITRE ATT&CK STIX Data](https://github.com/mitre-attack/attack-stix-data)

### 学习资源

- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) - 已知被积极利用的漏洞列表，优先修补
- [Microsoft Security Update Guide](https://msrc.microsoft.com/update-guide) - 微软安全更新指南
- [NVD - National Vulnerability Database](https://nvd.nist.gov/) - 美国国家漏洞数据库
- [GTFOBins](https://gtfobins.github.io/) - Linux 提权命令参考
- [LOLBAS](https://lolbas-project.github.io/) - Windows 提权命令参考
- [UACME](https://github.com/hfiref0x/UACME) - UAC 绕过技术集合

### 相关工具

- [BloodHound](https://github.com/BloodHoundAD/BloodHound) - AD 权限关系分析工具
- [Mimikatz](https://github.com/gentilkiwi/mimikatz) - Windows 凭据和令牌操作工具
- [WinPEAS](https://github.com/carlospolop/PEASS-ng) - Windows 提权辅助枚举脚本
- [LinPEAS](https://github.com/carlospolop/PEASS-ng) - Linux 提权辅助枚举脚本
- [Metasploit](https://www.metasploit.com/) - 漏洞利用框架，包含大量提权模块

---

> **版本**: v2.0 | **更新**: 2026-06-10 | **模板**: 战术README v2.0
