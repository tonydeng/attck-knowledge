# 发现 (TA0007)

## 一句话理解

发现就像小偷进家后先四处张望——看看屋里有什么值钱的东西、有没有人、门在哪里。

## 战术概述

发现（Discovery）是MITRE ATT&CK框架中攻击阶段的核心战术，编号为TA0007。攻击者在获得初始访问权限后，利用发现技术了解受感染环境和内部网络的情况。

**通俗解释：**
发现就像小偷成功潜入一栋大楼后，不会立即动手——而是先四处摸索：看看走廊尽头有没有保安、哪间办公室的门没锁、电脑屏幕上贴着什么密码便签、有没有监控摄像头。攻击者也是同样的逻辑，他们需要搞清楚"我在哪"、"周围有什么"、"哪些东西有价值"，才能规划下一步行动。

**在攻击中的作用：**
发现战术是整个攻击链条中的"侦察兵"阶段，发生在初始访问之后、横向移动之前。没有充分的发现，攻击者就像蒙着眼睛在大楼里乱撞——既找不到目标，也容易被发现。几乎所有攻击活动（包括勒索软件、APT间谍行动、数据窃取）都包含发现战术。事实上，安全团队检测到的早期入侵迹象往往就是发现命令的执行，如 `whoami`、`ipconfig`、`net view` 等异常调用。

**包含的技术类型：**
发现战术涵盖35种技术，可归为以下几大类：系统信息发现（操作系统版本、硬件配置）、网络信息发现（IP配置、连接状态、共享资源）、用户和权限发现（账户枚举、组成员身份）、应用和服务发现（运行进程、已安装软件、系统服务）、安全产品发现（EDR/AV检测、沙箱规避）、存储发现（本地和云存储）、以及容器和虚拟化环境发现。

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

    style J fill:#ff6b6b,stroke:#333,stroke-width:3px,color:#fff
```

### 当前战术的角色

发现是攻击链中的"信息中枢"——攻击者拿到初步立足点后，必须通过发现来了解环境，才能决定下一步往哪走。可以说，发现做得越彻底，后续的横向移动和数据窃取就越精准。如果缺乏发现环节，攻击者就像盲人摸象，很可能撞上陷阱或错过真正的目标。

### 前置战术

- **初始访问 (TA0001)**：攻击者需要通过漏洞利用、钓鱼或凭证窃取等方式先进入系统，然后才能执行发现命令
- **执行 (TA0002)**：发现命令需要通过脚本解释器（cmd、PowerShell）或远程管理工具来执行
- **凭证访问 (TA0006)**：有了合法凭证，攻击者才能通过远程管理协议（RDP、WinRM、WMI）在更多系统上执行发现

### 后续战术

- **横向移动 (TA0008)**：发现结果告诉攻击者哪些主机是域控制器、哪些运行了关键服务，从而选择横向移动的目标
- **收集 (TA0009)**：发现能定位文件服务器和共享目录，为数据收集指明方向
- **凭证访问 (TA0006)**：发现环节可能识别出内存中运行了LSASS进程，引导后续的凭证窃取

## 技术索引表

| 技术ID                                                       | 中文名称       | 难度  | 子技术数 | 一句话理解                     | 文档状态  |
| ---------------------------------------------------------- | ---------- | :-: | :--: | ------------------------- | :---: |
| [T1007](./T1007-System-Service-Discovery.md)               | 系统服务发现     | ⭐⭐  |  0   | 检查电脑上跑了哪些后台服务，就像看店里开了哪些设备 | ✅ 已完成 |
| [T1010](./T1010-Application-Window-Discovery.md)           | 应用程序窗口发现   |  ⭐  |  0   | 查看当前打开了哪些窗口和程序界面          | ✅ 已完成 |
| [T1012](./T1012-Query-Registry.md)                         | 查询注册表      | ⭐⭐  |  0   | 翻看Windows系统的"大辞典"，找配置信息   | ✅ 已完成 |
| [T1016](./T1016-System-Network-Configuration-Discovery.md) | 系统网络配置发现   |  ⭐  |  3   | 查看电脑的网络设置，就像看门牌号和邻居信息     | ✅ 已完成 |
| [T1018](./T1018-Remote-System-Discovery.md)                | 远程系统发现     | ⭐⭐  |  0   | 扫描周围哪些电脑在线，就像看看邻居家有没有亮灯   | ✅ 已完成 |
| [T1033](./T1033-System-Owner-User-Discovery.md)            | 系统所有者/用户发现 |  ⭐  |  0   | 查看当前登录的用户是谁，就像问"谁在这儿"     | ✅ 已完成 |
| [T1040](./T1040-Network-Sniffing.md)                       | 网络嗅探       | ⭐⭐⭐ |  0   | 监听网络中的数据包，就像偷听别人打电话       | ✅ 已完成 |
| [T1046](./T1046-Network-Service-Scanning.md)               | 网络服务扫描     | ⭐⭐  |  0   | 扫描其他电脑开放了哪些端口和服务          | ✅ 已完成 |
| [T1049](./T1049-System-Network-Connections-Discovery.md)   | 系统网络连接发现   |  ⭐  |  0   | 查看电脑当前和哪些地址有网络连接          | ✅ 已完成 |
| [T1057](./T1057-Process-Discovery.md)                      | 进程发现       |  ⭐  |  0   | 查看电脑上正在运行哪些程序             | ✅ 已完成 |
| [T1069](./T1069-Permission-Groups-Discovery.md)            | 权限组发现      | ⭐⭐  |  3   | 查看有哪些用户组和成员的权限设置          | ✅ 已完成 |
| [T1082](./T1082-System-Information-Discovery.md)           | 系统信息发现     |  ⭐  |  0   | 查看电脑的详细配置信息               | ✅ 已完成 |
| [T1083](./T1083-File-and-Directory-Discovery.md)           | 文件和目录发现    |  ⭐  |  0   | 浏览文件系统中的文件夹和文件            | ✅ 已完成 |
| [T1087](./T1087-Account-Discovery.md)                      | 账户发现       |  ⭐  |  4   | 枚举系统中的所有用户账户信息            | ✅ 已完成 |
| [T1120](./T1120-Peripheral-Device-Discovery.md)            | 外围设备发现     |  ⭐  |  0   | 查看电脑连接了哪些外设（U盘、打印机等）      | ✅ 已完成 |
| [T1124](./T1124-System-Time-Discovery.md)                  | 系统时间发现     |  ⭐  |  0   | 查看系统当前时间和时区设置             | ✅ 已完成 |
| [T1135](./T1135-Network-Share-Discovery.md)                | 网络共享发现     | ⭐⭐  |  0   | 查看网络上共享的文件夹和资源            | ✅ 已完成 |
| [T1201](./T1201-Password-Policy-Discovery.md)              | 密码策略发现     |  ⭐  |  0   | 查看系统的密码规则要求               | ✅ 已完成 |
| [T1217](./T1217-Browser-Bookmark-Discovery.md)             | 浏览器书签发现    |  ⭐  |  0   | 查看浏览器收藏夹里存了哪些网站           | ✅ 已完成 |
| [T1482](./T1482-Domain-Trust-Discovery.md)                 | 域信任发现      | ⭐⭐⭐ |  0   | 查看域之间的信任关系                | ✅ 已完成 |
| [T1497](./T1497-Virtualization-Sandbox-Evasion.md)         | 虚拟化/沙箱规避   | ⭐⭐⭐ |  3   | 检测自己是否在虚拟机或分析环境里运行        | ✅ 已完成 |
| [T1518](./T1518-Software-Discovery.md)                     | 软件发现       |  ⭐  |  2   | 查看系统上安装了哪些软件              | ✅ 已完成 |
| [T1526](./T1526-Cloud-Service-Discovery.md)                | 云服务发现      | ⭐⭐  |  0   | 枚举云平台上运行的服务               | ✅ 已完成 |
| [T1538](./T1538-Cloud-Service-Dashboard.md)                | 云服务仪表盘     | ⭐⭐  |  0   | 查看云平台的管理控制面板信息            | ✅ 已完成 |
| [T1580](./T1580-Cloud-Infrastructure-Discovery.md)         | 云基础设施发现    | ⭐⭐  |  0   | 枚举云环境中的基础设施资源             | ✅ 已完成 |
| [T1613](./T1613-Container-and-Resource-Discovery.md)       | 容器和资源发现    | ⭐⭐  |  0   | 查看容器环境中的信息和API            | ✅ 已完成 |
| [T1614](./T1614-System-Location-Discovery.md)              | 系统位置发现     |  ⭐  |  1   | 确定系统所处的物理或地理位置            | ✅ 已完成 |
| [T1615](./T1615-Group-Policy-Discovery.md)                 | 组策略发现      | ⭐⭐  |  0   | 查看域组策略配置信息                | ✅ 已完成 |
| [T1619](./T1619-Cloud-Storage-Object-Discovery.md)         | 云存储对象发现    | ⭐⭐  |  0   | 枚举云存储中的对象和文件              | ✅ 已完成 |
| [T1622](./T1622-Debugger-Evasion-Discovery.md)             | 调试器规避发现    | ⭐⭐⭐ |  0   | 检测是否在被调试器跟踪分析             | ✅ 已完成 |
| [T1652](./T1652-Device-Driver-Discovery.md)                | 设备驱动发现     | ⭐⭐  |  0   | 查看系统上安装了哪些驱动程序            | ✅ 已完成 |
| [T1654](./T1654-Log-Enumeration.md)                        | 日志枚举       | ⭐⭐  |  0   | 浏览系统和应用日志寻找信息             | ✅ 已完成 |
| [T1673](./T1673-Virtual-Machine-Discovery.md)              | 虚拟机发现      | ⭐⭐  |  0   | 检测当前是否运行在虚拟机中             | ✅ 已完成 |
| [T1680](./T1680-Local-Storage-Discovery.md)                | 本地存储发现     |  ⭐  |  0   | 查看电脑连接的磁盘和存储设备            | ✅ 已完成 |

### 统计信息

- **技术总数**：35 个
- **子技术总数**：24 个
- **已完成文档**：35 个
- **进行中文档**：0 个
- **待编写文档**：0 个

## 推荐阅读顺序

### 入门阶段（第1-2周）

> 适合零基础的安全爱好者，从最简单、最直观的技术开始。

**前置知识：** 了解基本的Windows操作和命令行概念即可。

**推荐阅读：**

1. **[T1082 - 系统信息发现](./T1082-System-Information-Discovery.md)** - 最基础的发现技术，学会了就能理解"攻击者入侵后第一件事是看电脑配置"
2. **[T1033 - 系统所有者/用户发现](./T1033-System-Owner-User-Discovery.md)** - `whoami`是安全事件中最常见的命令之一
3. **[T1087 - 账户发现](./T1087-Account-Discovery.md)** - 理解攻击者如何枚举系统上的所有账户
4. **[T1057 - 进程发现](./T1057-Process-Discovery.md)** - 学会查看系统中运行了哪些程序

**学习建议：**
- 在Windows VM中逐个执行这些发现命令，观察输出
- 记住主要命令：`whoami`、`systeminfo`、`tasklist`、`net user`
- 理解为什么攻击者需要这些信息

### 进阶阶段（第3-4周）

> 适合有一定基础的学习者，开始接触网络层面的发现技术。

**前置知识：** 了解基本网络概念（IP、端口、DNS）、熟悉PowerShell基础。

**推荐阅读：**

1. **[T1016 - 系统网络配置发现](./T1016-System-Network-Configuration-Discovery.md)** - 理解攻击者如何分析网络环境
2. **[T1046 - 网络服务扫描](./T1046-Network-Service-Scanning.md)** - 最经典的"敲门"技术
3. **[T1018 - 远程系统发现](./T1018-Remote-System-Discovery.md)** - 理解攻击者如何找到网内其他电脑
4. **[T1069 - 权限组发现](./T1069-Permission-Groups-Discovery.md)** - 理解权限枚举和特权账户识别
5. **[T1135 - 网络共享发现](./T1135-Network-Share-Discovery.md)** - 攻击者如何找到共享文件

**学习建议：**
- 搭建一个小型域环境（2-3台VM），练习横向发现命令
- 学习使用 `nslookup`、`net view`、`nltest` 等网络发现工具
- 了解 BloodHound/SharpHound 的基本原理

### 高级阶段（第5-6周）

> 适合有较好基础的学习者，深入理解复杂发现技术和规避手段。

**前置知识：** 了解域环境、虚拟化技术、云平台基础。

**推荐阅读：**

1. **[T1482 - 域信任发现](./T1482-Domain-Trust-Discovery.md)** - 理解攻击者如何在多域环境中穿透
2. **[T1497 - 虚拟化/沙箱规避](./T1497-Virtualization-Sandbox-Evasion.md)** - 理解恶意软件如何检测分析环境
3. **[T1040 - 网络嗅探](./T1040-Network-Sniffing.md)** - 被动网络监听技术
4. **[T1622 - 调试器规避发现](./T1622-Debugger-Evasion-Discovery.md)** - 高级反调试检测技术
5. **[T1526 / T1538 / T1580 - 云服务发现系列](./T1526-Cloud-Service-Discovery.md)** - 云环境中的发现技术

**学习建议：**
- 使用BloodHound进行域环境分析练习
- 在云平台（AWS/Azure）上练习云服务枚举
- 学习Wireshark抓包分析和网络嗅探实操
- 理解正向工程分析环境中的规避技术

## 参考资料

### 官方文档

- [MITRE ATT&CK - Discovery](https://attack.mitre.org/tactics/TA0007/)
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)

### 学习资源

- [MITRE ATT&CK 发现战术导航](https://attack.mitre.org/tactics/TA0007/) - 官方技术列表和详细说明
- [SANS 发现技术白皮书](https://www.sans.org/white-papers/discovery-techniques/) - 发现技术的深度解读
- [Microsoft 365 Defender 发现检测](https://learn.microsoft.com/en-us/microsoft-365/security/defender/) - 微软防御方案中的发现检测

### 相关工具

- [BloodHound](https://github.com/BloodHoundAD/BloodHound) - 用于分析AD环境的发现工具
- [SharpHound](https://github.com/BloodHoundAD/SharpHound) - BloodHound的数据收集器
- [PowerView](https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon) - PowerShell域环境发现脚本
- [Nmap](https://nmap.org/) - 网络端口扫描工具
- [Advanced IP Scanner](https://www.advanced-ip-scanner.com/) - 网络扫描工具
