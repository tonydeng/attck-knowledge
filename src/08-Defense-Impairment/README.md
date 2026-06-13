# 防御削弱 (TA0112)

## 一句话理解

> **防御削弱就是攻击者想办法让保安系统失效** -- 关掉摄像头、伪造通行证、删掉监控记录，让你发现不了他来过。

## 战术概述

防御削弱是MITRE ATT&CK框架中攻击链中段的战术，编号为TA0112。

**通俗解释：**
想象你开了一家银行，装了监控摄像头、门禁系统、报警器和保安巡逻。现在有一个劫匪想进来抢钱，他不会硬闯，而是会：先把监控关掉（禁用安全工具 -- [T1562](T1562-Impair-Defenses.md)）、把监控录像删了（清除日志痕迹 -- [T1070](T1070-Indicator-Removal.md)）、伪造一张员工卡混进去（伪装技术 -- [T1036](T1036-Masquerading.md)）、偷了保安的钥匙（获取有效账户 -- [T1078](T1078-Valid-Accounts.md)）、在保安的咖啡里下安眠药（利用漏洞削弱防御 -- [T1687](T1687-Exploitation-for-Defense-Impairment.md)）。这就是防御削弱战术的精髓。

**在攻击中的作用：**
防御削弱不是一次性步骤，而是贯穿整个攻击生命周期。从初始访问阶段到最终数据窃取或勒索，攻击者需要持续绕过或禁用安全检测机制。如果防御削弱做不好，攻击者的每一步操作都可能触发告警被发现。这个战术的核心逻辑是：不正面硬刚安全产品，而是让它"看不见"、"管不了"或者"来不及反应"。

**包含的技术类型：**
包括25个技术，覆盖134个子技术，主要分为：直接禁用安全工具（[T1562](T1562-Impair-Defenses.md)）、清除证据痕迹（[T1070](T1070-Indicator-Removal.md)）、混淆和伪装（[T1027](T1027-Obfuscated-Files-or-Info.md)/[T1036](T1036-Masquerading.md)）、隐藏工件（[T1564](T1564-Hide-Artifacts.md)）、修改认证和信任（[T1553](T1553-Subvert-Trust-Controls.md)/[T1556](T1556-Modify-Authentication-Process.md)）、操纵系统和网络配置（[T1484](T1484-Domain-or-Tenant-Policy-Modification.md)/[T1112](T1112-Modify-Registry.md)/[T1222](T1222-File-Permissions-Modification.md)）、利用漏洞绕过防御（[T1687](T1687-Exploitation-for-Defense-Impairment.md)）、降级攻击（[T1689](T1689-Downgrade-Attack.md)）等。

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

    style H fill:#ff6b6b,stroke:#333,stroke-width:3px,color:#fff
```

### 当前战术的角色

防御削弱在攻击链中扮演"扫清障碍"的角色。攻击者完成隐蔽和权限提升后，必须先削弱目标的安全防御才能安全地进行后续操作（凭证访问、发现、横向移动）。没有有效的防御削弱，后续所有攻击行为都面临被检测和阻断的风险。

### 前置战术

- **隐蔽 (TA0005)**：攻击者需要先隐藏自己的活动，然后才能去削弱目标的防御系统
- **权限提升 (TA0004)**：削弱防御通常需要管理员或更高权限，所以通常先提权

### 后续战术

- **凭证访问 (TA0006)**：防御削弱后，攻击者可以安全地窃取凭证
- **发现 (TA0007)**：安全工具被削弱后，攻击者可以自由在内网中探索
- **横向移动 (TA0008)**：防御系统失效后，攻击者可以不受阻碍地横向扩散

## 技术索引表

| 技术ID | 中文名称 | 难度 | 子技术数 | 一句话理解 | 文档状态 |
|--------|----------|:----:|:--------:|-----------|:--------:|
| [T1562](./T1562-Impair-Defenses.md) | 削弱防御 | ⭐⭐ | 11 | 直接关掉保安系统 | ✅ 已完成 |
| [T1070](./T1070-Indicator-Removal.md) | 清除痕迹 | ⭐⭐ | 10 | 删掉监控录像和进出记录 | ✅ 已完成 |
| [T1027](./T1027-Obfuscated-Files-or-Info.md) | 文件信息混淆 | ⭐⭐ | 13 | 把违禁品藏在普通包裹里 | ✅ 已完成 |
| [T1036](./T1036-Masquerading.md) | 伪装技术 | ⭐ | 8 | 穿上保安制服混进去 | ✅ 已完成 |
| [T1564](./T1564-Hide-Artifacts.md) | 隐藏工件 | ⭐⭐ | 10 | 把东西藏在看不见的地方 | ✅ 已完成 |
| [T1553](./T1553-Subvert-Trust-Controls.md) | 颠覆信任控制 | ⭐⭐⭐ | 5 | 伪造一张假通行证 | ✅ 已完成 |
| [T1556](./T1556-Modify-Authentication-Process.md) | 修改认证流程 | ⭐⭐⭐ | 6 | 偷偷改了门锁的钥匙 | ✅ 已完成 |
| [T1484](./T1484-Domain-or-Tenant-Policy-Modification.md) | 域/租户策略修改 | ⭐⭐⭐ | 2 | 改了整个公司的安保规则 | ✅ 已完成 |
| [T1222](./T1222-File-Permissions-Modification.md) | 文件权限修改 | ⭐ | 2 | 改了文件柜的锁 | ✅ 已完成 |
| [T1497](./T1497-Virtualization-Sandbox-Evasion.md) | 虚拟化/沙箱逃逸 | ⭐⭐ | 3 | 检测到被关在实验室就不干活 | ✅ 已完成 |
| [T1014](./T1014-Rootkit.md) | Rootkit | ⭐⭐⭐ | 0 | 穿上隐身衣在系统里活动 | ✅ 已完成 |
| [T1059](./T1059-Command-and-Scripting-Interpreter.md) | 命令和脚本解释器 | ⭐ | 9 | 用系统自带的工具干坏事 | ✅ 已完成 |
| [T1055](./T1055-Process-Injection.md) | 进程注入 | ⭐⭐⭐ | 12 | 附身到合法程序里活动 | ✅ 已完成 |
| [T1218](./T1218-System-Binary-Proxy-Execution.md) | 系统二进制代理执行 | ⭐⭐ | 15 | 让合法系统工具替我干活 | ✅ 已完成 |
| [T1202](./T1202-Indirect-Command-Execution.md) | 间接命令执行 | ⭐⭐ | 0 | 借别人的手发号施令 | ✅ 已完成 |
| [T1112](./T1112-Modify-Registry.md) | 修改注册表 | ⭐ | 0 | 改了系统的配置开关 | ✅ 已完成 |
| [T1098](./T1098-Account-Manipulation.md) | 账户操纵 | ⭐⭐ | 6 | 偷偷给自己开了后门账户 | ✅ 已完成 |
| [T1078](./T1078-Valid-Accounts.md) | 有效账户 | ⭐⭐ | 4 | 用偷来的钥匙光明正大进门 | ✅ 已完成 |
| [T1056](./T1056-Input-Capture.md) | 输入捕获 | ⭐⭐ | 5 | 在键盘上装了记录器 | ✅ 已完成 |
| [T1480](./T1480-Execution-Guardrails.md) | 执行护栏 | ⭐⭐ | 2 | 只在特定环境才露出真面目 | ✅ 已完成 |
| [T1542](./T1542-Pre-OS-Boot.md) | 引导前启动 | ⭐⭐⭐ | 5 | 在系统启动前就动手脚 | ✅ 已完成 |
| [T1548](./T1548-Abuse-Elevation-Control-Mechanism.md) | 滥用提升控制机制 | ⭐⭐ | 6 | 绕过权限检查直接提权 | ✅ 已完成 |
| [T1689](./T1689-Downgrade-Attack.md) | 降级攻击 | ⭐⭐ | 0 | 强迫系统用更弱的安全协议 | ✅ 已完成 |
| [T1687](./T1687-Exploitation-for-Defense-Impairment.md) | 利用漏洞削弱防御 | ⭐⭐⭐ | 0 | 找到保安系统的漏洞并利用它 | ✅ 已完成 |



## 子技术索引

| 子技术ID | 名称 | 难度 | 一句话理解 | 文档状态 |
|----------|------|:----:|-----------|:--------:|
| [T1027.001](./T1027/T1027.001-Binary-Plant.md) | 二进制植入 | ⭐⭐⭐ | 将恶意代码隐藏在图片或合法文件中 | ✅ 已完成 |
| [T1027.002](./T1027/T1027.002-Software-Packing.md) | 软件打包 | ⭐⭐⭐ | 用UPX等方法压缩/加密恶意程序 | ✅ 已完成 |
| [T1027.003](./T1027/T1027.003-Custom-Encoding-Crypto-自定义编码.md) | 自定义编码/加密 | ⭐⭐⭐ | 用Base64、XOR等方法编码恶意载荷 | ✅ 已完成 |
| [T1027.004](./T1027/T1027.004-Compiled-HTML-File.md) | 编译后的HTML文件 | ⭐⭐⭐ | 利用CHM文件执行恶意脚本 | ✅ 已完成 |
| [T1027.005](./T1027/T1027.005-Indicator-Removal.md) | 指示器移除 | ⭐⭐⭐ | 删除文件中的IoC特征（硬编码IP等） | ✅ 已完成 |
| [T1027.006](./T1027/T1027.006-HTML-Smuggling-HTML-Smuggling.md) | HTML Smuggling | ⭐⭐⭐ | 在HTML中编码隐藏恶意文件 | ✅ 已完成 |
| [T1027.007](./T1027/T1027.007-Dynamic-API-Resolution.md) | 动态API解析 | ⭐⭐⭐ | 运行时才解析API，不让导入表暴露 | ✅ 已完成 |
| [T1027.008](./T1027/T1027.008-Clear-PE-Header.md) | 清空PE头部 | ⭐⭐⭐ | 清除可执行文件的PE头使分析工具解析错误 | ✅ 已完成 |
| [T1027.009](./T1027/T1027.009-Embedded-Payload.md) | 嵌入的Payload | ⭐⭐⭐ | 将载荷嵌入可执行文件的其他部分 | ✅ 已完成 |
| [T1027.010](./T1027/T1027.010-Command-Obfuscation.md) | 命令混淆 | ⭐⭐⭐ | 使用混淆的命令行逃避日志检测 | ✅ 已完成 |
| [T1027.011](./T1027/T1027.011-File-Extension-Masquerading.md) | 文件扩展名伪装 | ⭐⭐⭐ | 修改文件扩展名绕过白名单 | ✅ 已完成 |
| [T1027.012](./T1027/T1027.012-LNK-File-Obfuscation.md) | LNK文件混淆 | ⭐⭐⭐ | 使用特殊字符和技巧混淆快捷方式文件 | ✅ 已完成 |
| [T1027.013](./T1027/T1027.013-Encrypted-Encoded-File-加密.md) | 加密/编码文件 | ⭐⭐⭐ | 使用加密算法保护存储的文件内容 | ✅ 已完成 |
| [T1036.001](./T1036/T1036.001-Process-Name-Masquerading.md) | 进程名伪装 | ⭐⭐ | 把恶意程序改名为系统进程名字 | ✅ 已完成 |
| [T1036.002](./T1036/T1036.002-Path-Masquerading.md) | 路径伪装 | ⭐⭐ | 把恶意程序放在系统目录里 | ✅ 已完成 |
| [T1036.003](./T1036/T1036.003-DLL-Masquerading.md) | DLL伪装 | ⭐⭐ | 把恶意DLL命名为系统DLL的名字 | ✅ 已完成 |
| [T1036.004](./T1036/T1036.004-Task-Masquerading.md) | 任务伪装 | ⭐⭐ | 把恶意计划任务命名为系统任务名 | ✅ 已完成 |
| [T1036.005](./T1036/T1036.005-Service-Masquerading.md) | 服务伪装 | ⭐⭐ | 把恶意服务命名为系统服务名 | ✅ 已完成 |
| [T1036.006](./T1036/T1036.006-Double-Extension.md) | 双扩展名 | ⭐⭐ | `document.pdf.exe`用户看到的是pdf文件 | ✅ 已完成 |
| [T1036.007](./T1036/T1036.007-Context-Menu-Masquerading.md) | 右键菜单伪装 | ⭐⭐ | 把恶意程序伪装成右键菜单项 | ✅ 已完成 |
| [T1036.008](./T1036/T1036.008-Process-Masquerading.md) | 进程伪装 | ⭐⭐ | 使用`CreateProcess`修改进程名称 | ✅ 已完成 |
| [T1055.001](./T1055/T1055.001-DLL-Injection.md) | DLL注入 | ⭐⭐⭐ | 把恶意DLL加载到目标进程 | ✅ 已完成 |
| [T1055.002](./T1055/T1055.002-PE-Injection.md) | 可移植可执行文件注入 | ⭐⭐⭐ | 把完整的PE文件写入目标进程 | ✅ 已完成 |
| [T1055.003](./T1055/T1055.003-Thread-Execution-Hijacking.md) | 线程执行劫持 | ⭐⭐⭐ | 暂停合法线程，替换为恶意代码再恢复执行 | ✅ 已完成 |
| [T1055.004](./T1055/T1055.004-Asynchronous-Procedure-Call.md) | 异步过程调用 | ⭐⭐⭐ | 利用APC在目标线程中执行恶意代码 | ✅ 已完成 |
| [T1055.005](./T1055/T1055.005-Thread-Local-Storage.md) | 线程本地存储 | ⭐⭐⭐ | 利用TLS回调在DLL加载时执行代码 | ✅ 已完成 |
| [T1055.008](./T1055/T1055.008-Ptrace-System-Call-Injection.md) | Ptrace系统调用注入 | ⭐⭐⭐ | Linux/macOS上的`ptrace`注入 | ✅ 已完成 |
| [T1055.009](./T1055/T1055.009-Process-Hollowing.md) | 进程空心化 | ⭐⭐⭐ | 创建合法进程后替换其内存为恶意代码 | ✅ 已完成 |
| [T1055.011](./T1055/T1055.011-Extra-Window-Memory-Injection.md) | 额外窗口内存注入 | ⭐⭐⭐ | 利用Explorer的窗口内存存储恶意代码 | ✅ 已完成 |
| [T1055.012](./T1055/T1055.012-Process-Masquerading.md) | 进程伪装 | ⭐⭐⭐ | 创建合法进程后修改参数伪装 | ✅ 已完成 |
| [T1056.001](./T1056/T1056.001-Keylogging.md) | 键盘记录 | ⭐⭐ | 记录用户按下了哪些键 | ✅ 已完成 |
| [T1056.002](./T1056/T1056.002-GUI-Input-Capture.md) | GUI输入捕获 | ⭐⭐ | 创建虚假的登录界面骗取密码 | ✅ 已完成 |
| [T1056.003](./T1056/T1056.003-Web-Portal-Capture.md) | Web门户捕获 | ⭐⭐ | 在Web登录界面拦截密码输入 | ✅ 已完成 |
| [T1056.004](./T1056/T1056.004-凭据API钩子.md) | 凭据API钩子 | ⭐⭐ | Hook系统API读取内存中的凭据 | ✅ 已完成 |
| [T1056.005](./T1056/T1056.005-Text-Capture.md) | 文本捕获 | ⭐⭐ | 记录用户在应用窗口中输入的文本 | ✅ 已完成 |
| [T1059.001](./T1059/T1059.001-PowerShell-PowerShell.md) | PowerShell | ⭐⭐ | 用PowerShell执行各种恶意操作 | ✅ 已完成 |
| [T1059.002](./T1059/T1059.002-Windows-Command-Shell.md) | Windows命令Shell | ⭐⭐ | 使用cmd.exe执行命令 | ✅ 已完成 |
| [T1059.003](./T1059/T1059.003-Windows-Command-Shell.md) | Windows命令Shell | ⭐⭐ | 使用wmic执行系统管理命令 | ✅ 已完成 |
| [T1059.005](./T1059/T1059.005-Visual-Basic-for-Applications-Visual-Basic-for-Applications.md) | Visual Basic for Applications | ⭐⭐ | 利用Office宏执行恶意代码 | ✅ 已完成 |
| [T1059.006](./T1059/T1059.006-Python-Python.md) | Python | ⭐⭐ | 使用Python执行恶意脚本 | ✅ 已完成 |
| [T1059.007](./T1059/T1059.007-JavaScript-JavaScript.md) | JavaScript | ⭐⭐ | 使用Windows Script Host执行JS | ✅ 已完成 |
| [T1059.008](./T1059/T1059.008-Network-Device-CLI.md) | 网络设备CLI | ⭐⭐ | 使用网络设备命令行 | ✅ 已完成 |
| [T1059.009](./T1059/T1059.009-Container-Administration.md) | 容器编排 | ⭐⭐ | 使用kubectl等容器管理命令 | ✅ 已完成 |
| [T1070.001](./T1070/T1070.001-Clear-Windows-Event-Logs.md) | 清除Windows事件日志 | ⭐⭐ | 使用`wevtutil cl`清除安全/系统日志 | ✅ 已完成 |
| [T1070.002](./T1070/T1070.002-Clear-Linux-Mac-System-Logs-清除Linux.md) | 清除Linux/Mac系统日志 | ⭐⭐ | 删除`/var/log/`下的日志文件 | ✅ 已完成 |
| [T1070.003](./T1070/T1070.003-Clear-Command-History.md) | 清除命令历史 | ⭐⭐ | 删除`.bash_history`、PowerShell历史等 | ✅ 已完成 |
| [T1070.004](./T1070/T1070.004-File-Deletion.md) | 文件删除 | ⭐⭐ | 删除攻击者上传的工具和临时文件 | ✅ 已完成 |
| [T1070.005](./T1070/T1070.005-Delete-Network-Share-Connection.md) | 删除网络共享连接 | ⭐⭐ | 清除`net use`的连接记录 | ✅ 已完成 |
| [T1070.006](./T1070/T1070.006-Timestomp.md) | 时间戳篡改 | ⭐⭐ | 修改文件的创建/修改时间，伪装成正常文件 | ✅ 已完成 |
| [T1070.007](./T1070/T1070.007-Clear-Network-History.md) | 清除网络连接历史 | ⭐⭐ | 清除ARP缓存、DNS缓存等 | ✅ 已完成 |
| [T1070.008](./T1070/T1070.008-Clear-Mail-Account-Anomalies.md) | 删除邮件账户异常记录 | ⭐⭐ | 删除邮件转发规则和安全告警邮件 | ✅ 已完成 |
| [T1070.009](./T1070/T1070.009-Clear-Persistence-Records.md) | 清除持久化记录 | ⭐⭐ | 删除计划任务历史和启动项备份 | ✅ 已完成 |
| [T1070.010](./T1070/T1070.010-Clear-System-Artifacts.md) | 清除系统痕迹 | ⭐⭐ | 清除Prefetch、USN Journal、Jump List等取证痕迹 | ✅ 已完成 |
| [T1078.001](./T1078/T1078.001-Default-Accounts.md) | 默认账户 | ⭐ | 使用系统默认的Guest、Administrator账户 | ✅ 已完成 |
| [T1078.002](./T1078/T1078.002-Domain-Account.md) | 域账户 | ⭐ | 使用窃取的域用户凭据登录域内系统 | ✅ 已完成 |
| [T1078.003](./T1078/T1078.003-Local-Account.md) | 本地账户 | ⭐ | 使用窃取的本地管理员密码登录 | ✅ 已完成 |
| [T1078.004](./T1078/T1078.004-Cloud-Account.md) | 云账户 | ⭐ | 使用窃取的云服务凭据 | ✅ 已完成 |
| [T1098.001](./T1098/T1098.001-额外云凭证.md) | 额外云凭证 | ⭐⭐ | 在云账户中添加额外的访问密钥 | ✅ 已完成 |
| [T1098.002](./T1098/T1098.002-Add-SSH-Authorized-Key.md) | 添加SSH授权密钥 | ⭐⭐ | 在Linux系统中添加SSH公钥 | ✅ 已完成 |
| [T1098.003](./T1098/T1098.003-Add-Office-365-Unified-Group.md) | 添加Office 365统一组 | ⭐⭐ | 创建或修改统一组添加成员 | ✅ 已完成 |
| [T1098.004](./T1098/T1098.004-SSH-Authorized-Keys.md) | SSH授权密钥 | ⭐⭐ | 利用SSH服务器配置实现持久化 | ✅ 已完成 |
| [T1098.005](./T1098/T1098.005-Device-Registration.md) | 设备注册 | ⭐⭐ | 在云环境中注册新设备 | ✅ 已完成 |
| [T1098.006](./T1098/T1098.006-Container-Account-Addition.md) | 容器账户添加 | ⭐⭐ | 向容器中添加账户 | ✅ 已完成 |
| [T1218.001](./T1218/T1218.001-cmstp.exe-cmstp.exe.md) | cmstp.exe | ⭐⭐ | 连接管理器配置工具，可执行任意命令 | ✅ 已完成 |
| [T1218.002](./T1218/T1218.002-ODBC-Driver-Manager.md) | ODBCODBC驱动程序管理器 | ⭐⭐ | 利用ODBC驱动执行代码 | ✅ 已完成 |
| [T1218.003](./T1218/T1218.003-IEExec-Remote-Execution.md) | IEExec远程执行 | ⭐⭐ | 使用IEExec执行.NET程序 | ✅ 已完成 |
| [T1218.004](./T1218/T1218.004-InstallUtil-InstallUtil.md) | InstallUtil | ⭐⭐ | 使用.NET安装工具执行恶意程序集 | ✅ 已完成 |
| [T1218.005](./T1218/T1218.005-Mshta-Mshta.md) | Mshta | ⭐⭐ | 执行HTA应用、VBScript、JavaScript | ✅ 已完成 |
| [T1218.007](./T1218/T1218.007-Msiexec-Msiexec.md) | Msiexec | ⭐⭐ | Windows安装程序，可执行DLL | ✅ 已完成 |
| [T1218.008](./T1218/T1218.008-Odbcconf-Odbcconf.md) | Odbcconf | ⭐⭐ | ODBC配置工具，可执行DLL | ✅ 已完成 |
| [T1218.009](./T1218/T1218.009-Register-CimProvider-Register-CimProvider.md) | Register-CimProvider | ⭐⭐ | CIM提供程序注册工具 | ✅ 已完成 |
| [T1218.010](./T1218/T1218.010-Regsvr32-Regsvr32.md) | Regsvr32 | ⭐⭐ | 注册COM组件，可加载远程DLL | ✅ 已完成 |
| [T1218.011](./T1218/T1218.011-Rundll32-Rundll32.md) | Rundll32 | ⭐⭐ | 执行DLL的导出函数 | ✅ 已完成 |
| [T1218.012](./T1218/T1218.012-Verclsid-Verclsid.md) | Verclsid | ⭐⭐ | COM组件兼容性评估器 | ✅ 已完成 |
| [T1218.013](./T1218/T1218.013-Mavinject-Mavinject.md) | Mavinject | ⭐⭐ | App-V注入工具 | ✅ 已完成 |
| [T1218.014](./T1218/T1218.014-MMC-MMC.md) | MMC | ⭐⭐ | Microsoft管理控制台 | ✅ 已完成 |
| [T1218.015](./T1218/T1218.015-WSReset-WSReset.md) | WSReset | ⭐⭐ | Windows Store重置工具 | ✅ 已完成 |
| [T1222.001](./T1222/T1222.001-Windows-File-Directory-Permission-Modification-Windows文件.md) | Windows文件/目录权限修改 | ⭐ | 使用icacls修改文件权限 | ✅ 已完成 |
| [T1222.002](./T1222/T1222.002-Linux-Mac-File-Directory-Permission-Modification-Linux-Mac文件.md) | Linux/Mac文件/目录权限修改 | ⭐ | 使用chmod/chown修改文件权限 | ✅ 已完成 |
| [T1480.001](./T1480/T1480.001-Environmental-Keying.md) | 环境密钥 | ⭐⭐ | 使用特定环境特征（如域名、文件）作为执行条件 | ✅ 已完成 |
| [T1480.002](./T1480/T1480.002-Two-Factor-Authentication.md) | 双向授权 | ⭐⭐ | 使用双向认证确保在目标环境中执行 | ✅ 已完成 |
| [T1484.001](./T1484/T1484.001-Group-Policy-Modification.md) | 组策略修改 | ⭐⭐⭐ | 修改Active Directory组策略 | ✅ 已完成 |
| [T1484.002](./T1484/T1484.002-Trust-Relationship-Modification.md) | 信任关系修改 | ⭐⭐⭐ | 修改域信任关系 | ✅ 已完成 |
| [T1497.001](./T1497/T1497.001-System-Time-Detection.md) | 系统时间检测 | ⭐⭐⭐ | 检测系统运行时间，沙箱通常运行时间短 | ✅ 已完成 |
| [T1497.002](./T1497/T1497.002-User-Activity-Detection.md) | 用户活动检测 | ⭐⭐⭐ | 检测是否有鼠标移动等真实用户操作 | ✅ 已完成 |
| [T1497.003](./T1497/T1497.003-基于时间的逃逸.md) | 基于时间的逃逸 | ⭐⭐⭐ | 延迟执行等待沙箱超时释放 | ✅ 已完成 |
| [T1542.001](./T1542/T1542.001-System-Firmware.md) | 系统固件 | ⭐⭐⭐ | 感染主板固件（UEFI/BIOS），在操作系统之前获得控制权 | ✅ 已完成 |
| [T1542.002](./T1542/T1542.002-Component-Firmware.md) | 组件固件 | ⭐⭐⭐ | 感染硬盘、网卡等硬件组件的固件 | ✅ 已完成 |
| [T1542.003](./T1542/T1542.003-Bootkit-Bootkit.md) | Bootkit | ⭐⭐⭐ | 安装引导工具包，在引导阶段加载内核级Rootkit | ✅ 已完成 |
| [T1542.004](./T1542/T1542.004-ROMMONkit-ROMMONkit.md) | ROMMONkit | ⭐⭐⭐ | 感染网络设备的ROMMON（ROM监控器）固件 | ✅ 已完成 |
| [T1542.005](./T1542/T1542.005-Disk-Area-Wipe.md) | 磁盘区域擦除 | ⭐⭐⭐ | 通过擦除磁盘特定区域破坏引导完整性 | ✅ 已完成 |
| [T1548.001](./T1548/T1548.001-Bypass-User-Account-Control.md) | Windows UAC绕过 | ⭐⭐ | 找到不需要弹窗确认就能以管理员身份运行的方法 | ✅ 已完成 |
| [T1548.002](./T1548/T1548.002-Bypass-sudo.md) | 绕过sudo | ⭐⭐ | 利用sudo配置漏洞不需要密码就获得root权限 | ✅ 已完成 |
| [T1548.003](./T1548/T1548.003-Sudo-and-Sudo-Caching.md) | Sudo和Sudo缓存 | ⭐⭐ | 利用sudo的凭据缓存机制，在超时时间内免密执行 | ✅ 已完成 |
| [T1548.004](./T1548/T1548.004-setuid和setgid.md) | setuid和setgid | ⭐⭐ | 利用存在setuid漏洞的二进制文件提权 | ✅ 已完成 |
| [T1548.005](./T1548/T1548.005-Temporary-Elevation-Control.md) | 临时提升控制 | ⭐⭐ | 利用系统提供的临时提权机制获得更高权限 | ✅ 已完成 |
| [T1548.006](./T1548/T1548.006-Policy-based-Elevation-Bypass.md) | 通过策略绕过提升控制 | ⭐⭐ | 利用组策略或安全策略配置漏洞绕过权限控制 | ✅ 已完成 |
| [T1553.001](./T1553/T1553.001-Code-Signing.md) | 代码签名 | ⭐⭐⭐ | 给恶意程序签上有序的数字签名 | ✅ 已完成 |
| [T1553.002](./T1553/T1553.002-Install-Root-Certificate.md) | 安装根证书 | ⭐⭐⭐ | 在受信任的根证书颁发机构中安装攻击者控制的证书 | ✅ 已完成 |
| [T1553.003](./T1553/T1553.003-SIP-Trust-Provider-Hijacking.md) | SIP信任提供方劫持 | ⭐⭐⭐ | 劫持Windows软件完整性策略（SIP）信任提供方 | ✅ 已完成 |
| [T1553.004](./T1553/T1553.004-安全启动绕过.md) | 安全启动绕过 | ⭐⭐⭐ | 篡改UEFI安全启动数据库允许加载未签名驱动 | ✅ 已完成 |
| [T1553.005](./T1553/T1553.005-Install-Root-Certificate.md) | 安装根证书 | ⭐⭐⭐ | 安装额外的根证书颁发机构以通过签名验证 | ✅ 已完成 |
| [T1556.001](./T1556/T1556.001-Domain-Controller-Authentication.md) | 域控制器认证 | ⭐⭐⭐ | 修改域控制器上的认证过程 | ✅ 已完成 |
| [T1556.002](./T1556/T1556.002-Password-Filter-DLL.md) | 密码过滤器DLL | ⭐⭐⭐ | 通过密码过滤器记录用户密码 | ✅ 已完成 |
| [T1556.003](./T1556/T1556.003-Network-Security-Service-DLL.md) | 网络安全服务DLL | ⭐⭐⭐ | 修改网络认证服务 | ✅ 已完成 |
| [T1556.004](./T1556/T1556.004-Network-Device-Authentication.md) | 网络设备认证 | ⭐⭐⭐ | 修改网络设备的认证过程 | ✅ 已完成 |
| [T1556.005](./T1556/T1556.005-PAM-based-Authentication.md) | 基于PAM的认证 | ⭐⭐⭐ | 修改Linux PAM模块添加后门 | ✅ 已完成 |
| [T1556.006](./T1556/T1556.006-MFA-Manipulation.md) | 多因素认证操作 | ⭐⭐⭐ | 绕过或禁用MFA验证 | ✅ 已完成 |
| [T1562.001](./T1562/T1562.001-Disable-or-Modify-Tools.md) | 禁用或修改工具 | ⭐⭐ | 直接停止/卸载安全产品（如`net stop WinDefend`） | ✅ 已完成 |
| [T1562.002](./T1562/T1562.002-禁用Windows事件日志.md) | 禁用Windows事件日志 | ⭐⭐ | 关闭日志记录，让操作不留痕迹 | ✅ 已完成 |
| [T1562.003](./T1562/T1562.003-Disable-or-Modify-System-Firewall.md) | 禁用或修改系统防火墙 | ⭐⭐ | 放开网络限制，允许恶意流量通过 | ✅ 已完成 |
| [T1562.004](./T1562/T1562.004-Disable-or-Modify-Log-Forwarding.md) | 禁用或修改日志转发 | ⭐⭐ | 阻止日志发送到SIEM，让安全团队看不到告警 | ✅ 已完成 |
| [T1562.006](./T1562/T1562.006-Indicator-Blocking.md) | 指标阻止 | ⭐⭐ | 阻止已知威胁指标被检测系统识别 | ✅ 已完成 |
| [T1562.007](./T1562/T1562.007-Disable-or-Modify-Code-Signing-Policy.md) | 禁用或修改代码签名策略 | ⭐⭐ | 允许未签名的恶意代码被执行 | ✅ 已完成 |
| [T1562.008](./T1562/T1562.008-Disable-or-Modify-Cloud-Logs.md) | 禁用或修改云日志 | ⭐⭐ | 关闭AWS CloudTrail等云审计日志 | ✅ 已完成 |
| [T1562.009](./T1562/T1562.009-Disable-or-Modify-Network-Traffic-Analysis.md) | 禁用或修改网络流量分析 | ⭐⭐ | 干扰IDS/IPS等网络检测设备 | ✅ 已完成 |
| [T1562.010](./T1562/T1562.010-Disable-or-Modify-Boot-Integrity.md) | 禁用或修改启动完整性验证 | ⭐⭐ | 破坏Secure Boot等启动安全机制 | ✅ 已完成 |
| [T1562.011](./T1562/T1562.011-Disable-or-Modify-Cloud-IMDS.md) | 禁用或修改云实例元数据服务 | ⭐⭐ | 利用云元数据服务进行凭据窃取 | ✅ 已完成 |
| [T1564.001](./T1564/T1564.001-Hide-Files-and-Directories.md) | 隐藏文件和目录 | ⭐⭐ | 使用`attrib +h`或点前缀隐藏文件 | ✅ 已完成 |
| [T1564.002](./T1564/T1564.002-Hide-Window.md) | 隐藏窗口 | ⭐⭐ | 使用`-WindowStyle Hidden`隐藏程序窗口 | ✅ 已完成 |
| [T1564.003](./T1564/T1564.003-Alternate Data Stream-备用数据流(ADS).md) | 备用数据流(ADS) | ⭐⭐ | 将恶意数据附加到NTFS文件的备用数据流 | ✅ 已完成 |
| [T1564.004](./T1564/T1564.004-NTFS-File-Attributes.md) | NTFS文件属性 | ⭐⭐ | 利用压缩、加密等属性隐藏文件 | ✅ 已完成 |
| [T1564.005](./T1564/T1564.005-Hidden-File-System.md) | 隐藏文件系统 | ⭐⭐ | 在VHD/ISO映像中存储恶意文件 | ✅ 已完成 |
| [T1564.006](./T1564/T1564.006-Run-Virtual-Instance.md) | 运行虚拟实例 | ⭐⭐ | 在虚拟机中运行恶意代码 | ✅ 已完成 |
| [T1564.007](./T1564/T1564.007-VBA-Stomping-VBA-Stomping.md) | VBA Stomping | ⭐⭐ | 修改Office宏的P-code隐藏恶意逻辑 | ✅ 已完成 |
| [T1564.008](./T1564/T1564.008-Email-Hidden-Rules.md) | 邮件隐藏规则 | ⭐⭐ | 创建邮件规则隐藏安全告警邮件 | ✅ 已完成 |
| [T1564.009](./T1564/T1564.009-Resource-Fork.md) | 资源分支 | ⭐⭐ | 利用macOS资源分支隐藏数据 | ✅ 已完成 |
| [T1564.010](./T1564/T1564.010-Process-Argument-Spoofing.md) | 进程参数欺骗 | ⭐⭐ | 修改进程命令行参数伪装为合法进程 | ✅ 已完成 |

### 统计信息

- **技术总数**：24 个
- **子技术总数**：128 个
- **已完成文档**：128 个
- **进行中文档**：0 个
- **待编写文档**：0 个

## 推荐阅读顺序

### 入门阶段（第1-2周）

> 适合零基础的安全爱好者，从最简单、最直观的技术开始。

**前置知识：** 了解基本的操作系统概念（进程、文件、网络）、会使用命令提示符或PowerShell

**推荐阅读：**

1. **[T1562 削弱防御](./T1562-Impair-Defenses.md)** - 防御削弱的核心概念，学习攻击者如何直接禁用安全工具
2. **[T1070 清除痕迹](./T1070-Indicator-Removal.md)** - 了解攻击后如何消除证据，这是攻击链的"收尾"步骤
3. **[T1059 命令和脚本解释器](./T1059-Command-and-Scripting-Interpreter.md)** - 掌握攻击者如何使用系统自带工具进行攻击
4. **[T1112 修改注册表](./T1112-Modify-Registry.md)** - 学习通过注册表修改安全配置的最简单方式

**学习建议：**
- 在虚拟机中动手尝试每个技术的实验步骤
- 重点理解"为什么攻击者需要这个技术"而非仅记住命令

### 进阶阶段（第3-4周）

> 适合有一定基础的学习者，开始接触更复杂的技术。

**前置知识：** 了解操作系统安全机制（UAC、Windows Defender）、会使用PowerShell脚本

**推荐阅读：**

1. **[T1036 伪装技术](./T1036-Masquerading.md)** - 深入理解文件和进程的伪装方法
2. **[T1027 文件信息混淆](./T1027-Obfuscated-Files-or-Info.md)** - 学习绕过签名检测的各种混淆技术
3. **[T1218 系统二进制代理执行](./T1218-System-Binary-Proxy-Execution.md)** - 掌握LOLBins的利用技巧
4. **[T1202 间接命令执行](./T1202-Indirect-Command-Execution.md)** - 了解绕过应用白名单的多种方法
5. **[T1564 隐藏工件](./T1564-Hide-Artifacts.md)** - 学习高级文件隐藏技术（ADS、VBA Stomping等）

**学习建议：**
- 结合隐蔽战术（TA0005）的内容一起学习
- 在本地的AD测试环境中练习GPO和域策略操作

### 高级阶段（第5-6周）

> 适合有较好技术基础的学习者，深入理解复杂技术原理。

**前置知识：** 了解Active Directory、云服务基础、内核态/用户态概念

**推荐阅读：**

1. **[T1553 颠覆信任控制](./T1553-Subvert-Trust-Controls.md)** - 深入理解系统信任链的攻击面
2. **[T1556 修改认证流程](./T1556-Modify-Authentication-Process.md)** - 学习劫持身份验证机制的高级技术
3. **[T1484 域/租户策略修改](./T1484-Domain-or-Tenant-Policy-Modification.md)** - 掌握企业级安全策略的操纵方法
4. **[T1078 有效账户](./T1078-Valid-Accounts.md)** - 理解利用合法凭据访问的高级技巧
5. **[T1098 账户操纵](./T1098-Account-Manipulation.md)** - 掌握修改账户权限和配置的技术
6. **[T1055 进程注入](./T1055-Process-Injection.md)** - 深入学习各种进程注入技术
7. **[T1548 滥用提升控制机制](./T1548-Abuse-Elevation-Control-Mechanism.md)** - 了解绕过权限提升控制的原理
8. **[T1014 Rootkit](./T1014-Rootkit.md)** - 了解内核级隐藏技术的原理
9. **[T1542 引导前启动](./T1542-Pre-OS-Boot.md)** - 掌握固件级持久化和防御绕过技术
10. **[T1689 降级攻击](./T1689-Downgrade-Attack.md)** - 理解通过协议降级绕过安全策略的方法
11. **[T1687 利用漏洞削弱防御](./T1687-Exploitation-for-Defense-Impairment.md)** - 学习BYOVD等利用漏洞绕过防御的技术

**学习建议：**
- 建议在完整的企业模拟环境中练习
- 结合红队视角和蓝队视角双向思考
- 关注2024-2026年最新的攻击案例，了解技术演进趋势

## 参考资料

### 官方文档

- [MITRE ATT&CK - Defense Impairment (TA0112)](https://attack.mitre.org/tactics/TA0112/)
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)

### 学习资源

- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) - CISA已知被利用漏洞目录
- [LOLDrivers - 漏洞驱动数据库](https://www.loldrivers.io/) - 已知存在漏洞的驱动程序列表
- [GTFOBins](https://gtfobins.github.io/) - Unix/Linux二进制文件利用技术库
- [LOLBAS](https://lolbas-project.github.io/) - Windows系统二进制文件利用技术库

### 相关工具

- [Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) - Windows系统活动监控工具
- [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer) - 进程管理分析工具
- [Volatility](https://www.volatilityfoundation.org/) - 内存取证分析框架
- [Sigma Rules](https://github.com/SigmaHQ/sigma) - 通用安全检测规则格式
