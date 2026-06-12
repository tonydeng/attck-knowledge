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

### 统计信息

- **技术总数**：25 个
- **子技术总数**：134 个
- **已完成文档**：25 个
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
