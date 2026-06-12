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

### 统计信息

- **技术总数**：13 个
- **子技术总数**：89 个
- **已完成文档**：13 个
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
