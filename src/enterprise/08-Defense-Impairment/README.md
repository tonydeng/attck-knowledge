# 防御削弱 (TA0112)

## 一句话理解

> **防御削弱就是攻击者主动出手让保安系统失效** —— 关掉摄像头、伪造通行证、删掉监控记录、改了门锁逻辑，让防御体系看不见、管不了、来不及反应。

## 战术概述

防御削弱是 MITRE ATT&CK v19.1 框架中攻击链中段的新战术，编号为 TA0112。

**v19.1 拆分背景：**
MITRE 在 v19.1 中将原有的"防御规避"（Defense Evasion, TA0005）拆分为两个互补战术：
- **隐蔽 (TA0005)** —— 继承原 TA0005 编号，聚焦"被动隐藏"：让攻击活动不被发现（如混淆、伪装、进程注入隐藏）
- **防御削弱 (TA0112)** —— 新增编号，聚焦"主动削弱"：让安全防御机制本身失效（如禁用工具、清除日志、篡改认证）

两者区别：**隐蔽是"我不让你看见我"，防御削弱是"我让你瞎了所以看不见我"**。TA0112 强调对防御体系的直接破坏行动，TA0005 强调对自身痕迹的隐藏技巧。

**通俗解释：**
想象你开了一家银行，装了监控摄像头、门禁系统、报警器和保安巡逻。现在有一个劫匪想进来抢钱，他不会硬闯，而是会：先把监控关掉（禁用工具 —— [T1685](T1685-Disable-or-Modify-Tools.md)）、把监控录像删了（清除日志 —— [T1685](T1685-Disable-or-Modify-Tools.md).005/.006）、伪造一张员工卡混进去（颠覆信任 —— [T1553](T1553-Subvert-Trust-Controls.md)）、改了门禁系统的验证逻辑让万能密码也能开门（修改认证 —— [T1556](T1556-Modify-Authentication-Process.md)）、在保安的咖啡里下安眠药（利用漏洞削弱防御 —— [T1687](T1687-Exploitation-for-Defense-Impairment.md)）、强迫系统降级到弱加密协议（降级攻击 —— [T1689](T1689-Downgrade-Attack.md)）。这就是防御削弱战术的精髓——**不正面硬刚安全产品，而是让整个防御体系失能**。

**在攻击中的作用：**
防御削弱不是一次性步骤，而是贯穿整个攻击生命周期。从初始访问阶段到最终数据窃取或勒索，攻击者需要持续绕过或禁用安全检测机制。如果防御削弱做不好，攻击者的每一步操作都可能触发告警被发现。这个战术的核心逻辑是：**让防御体系"看不见"、"管不了"或者"来不及反应"**。

**包含的技术类型：**
共 18 个父技术、38 个子技术，主要分为五类：
1. **直接禁用安全工具与日志** —— [T1685](T1685-Disable-or-Modify-Tools.md)（禁用或修改工具）、[T1686](T1686-Disable-or-Modify-System-Firewall.md)（禁用防火墙）、[T1690](T1690-Prevent-Command-History-Logging.md)（阻止命令历史）
2. **篡改认证与信任** —— [T1553](T1553-Subvert-Trust-Controls.md)（颠覆信任控制）、[T1556](T1556-Modify-Authentication-Process.md)（修改认证过程）、[T1207](T1207-Rogue-Domain-Controller.md)（流氓域控）
3. **操纵系统/网络/云配置** —— [T1112](T1112-Modify-Registry.md)（注册表）、[T1222](T1222-File-And-Directory-Permissions-Modification.md)（文件权限）、[T1484](T1484-Domain-or-Tenant-Policy-Modification.md)（域策略）、[T1647](T1647-Plist-File-Modification.md)（Plist）、[T1600](T1600-Weaken-Encryption.md)（削弱加密）、[T1601](T1601-Modify-System-Image.md)（系统镜像）、[T1578](T1578-Modify-Cloud-Compute-Infrastructure.md)（云算力）、[T1666](T1666-Modify-Cloud-Resource-Hierarchy.md)（云资源层级）、[T1599](T1599-Network-Boundary-Bridging.md)（网络边界）
4. **利用漏洞与降级** —— [T1687](T1687-Exploitation-for-Defense-Impairment.md)（漏洞利用）、[T1689](T1689-Downgrade-Attack.md)（降级攻击）、[T1688](T1688-Safe-Mode-Boot.md)（安全模式启动）
5. **跨平面削弱** —— 涵盖端点、身份、网络、云四大平面

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

防御削弱在攻击链中扮演"扫清障碍"的角色，紧随隐蔽（TA0005）之后、凭证访问（TA0006）之前。攻击者完成隐蔽和权限提升后，必须先削弱目标的安全防御才能安全地进行后续操作。**没有有效的防御削弱，后续所有攻击行为都面临被检测和阻断的风险**。

TA0112 与相邻战术的关系：
- **承接隐蔽 (TA0005)**：先隐藏自身存在，再出手破坏防御体系
- **铺垫凭证访问 (TA0006)**：禁用审计后才能安全 dump 凭据
- **支撑横向移动 (TA0008)**：关闭 EDR/IDS 后横向扩散不被发现
- **掩护数据窃取 (TA0010)**：停掉云日志后大规模外传不告警

### 前置战术

- **隐蔽 (TA0005)**：攻击者需要先隐藏自己的活动，然后才能去削弱目标的防御系统
- **权限提升 (TA0004)**：削弱防御通常需要管理员或更高权限，所以通常先提权

### 后续战术

- **凭证访问 (TA0006)**：防御削弱后，攻击者可以安全地窃取凭证
- **发现 (TA0007)**：安全工具被削弱后，攻击者可以自由在内网中探索
- **横向移动 (TA0008)**：防御系统失效后，攻击者可以不受阻碍地横向扩散

## 技术索引表

> 共 18 个父技术，按 T-ID 升序排列。难度：⭐ 入门 / ⭐⭐ 中级 / ⭐⭐⭐ 高级。

| 技术ID | 中文名称 | 难度 | 子技术数 | 一句话理解 | 文档状态 |
|--------|----------|:----:|:--------:|-----------|:--------:|
| [T1112](./T1112-Modify-Registry.md) | 修改注册表 | ⭐⭐ | 0 | 改系统配置开关 | ✅ 已完成 |
| [T1207](./T1207-Rogue-Domain-Controller.md) | 流氓域控制器 | ⭐⭐⭐ | 0 | 伪造域控注入目录数据 | ✅ 已完成 |
| [T1222](./T1222-File-And-Directory-Permissions-Modification.md) | 文件权限修改 | ⭐ | 2 | 改了文件柜的锁 | ✅ 已完成 |
| [T1484](./T1484-Domain-or-Tenant-Policy-Modification.md) | 域/租户策略修改 | ⭐⭐⭐ | 2 | 改了整个公司的安保规则 | ✅ 已完成 |
| [T1553](./T1553-Subvert-Trust-Controls.md) | 颠覆信任控制 | ⭐⭐⭐ | 6 | 伪造一张假通行证 | ✅ 已完成 |
| [T1556](./T1556-Modify-Authentication-Process.md) | 修改认证过程 | ⭐⭐⭐ | 9 | 偷偷给门禁加后门 | ✅ 已完成 |
| [T1578](./T1578-Modify-Cloud-Compute-Infrastructure.md) | 修改云计算基础设施 | ⭐⭐ | 5 | 改云主机配置 | ✅ 已完成 |
| [T1599](./T1599-Network-Boundary-Bridging.md) | 网络边界桥接 | ⭐⭐⭐ | 1 | 跨网络边界打通通道 | ✅ 已完成 |
| [T1600](./T1600-Weaken-Encryption.md) | 削弱加密 | ⭐⭐⭐ | 2 | 让加密形同虚设 | ✅ 已完成 |
| [T1601](./T1601-Modify-System-Image.md) | 修改系统镜像 | ⭐⭐⭐ | 2 | 改系统底层镜像 | ✅ 已完成 |
| [T1647](./T1647-Plist-File-Modification.md) | Plist文件修改 | ⭐ | 0 | 改macOS配置文件 | ✅ 已完成 |
| [T1666](./T1666-Modify-Cloud-Resource-Hierarchy.md) | 修改云资源层级 | ⭐⭐ | 0 | 改云资源归属层级 | ✅ 已完成 |
| [T1685](./T1685-Disable-or-Modify-Tools.md) | 禁用或修改工具 | ⭐⭐ | 6 | 让保安系统直接失效 | ✅ 已完成 |
| [T1686](./T1686-Disable-or-Modify-System-Firewall.md) | 禁用或修改系统防火墙 | ⭐⭐ | 3 | 关掉网络门卫 | ✅ 已完成 |
| [T1687](./T1687-Exploitation-for-Defense-Impairment.md) | 利用漏洞削弱防御 | ⭐⭐⭐ | 0 | 找保安系统漏洞利用它 | ✅ 已完成 |
| [T1688](./T1688-Safe-Mode-Boot.md) | 安全模式启动 | ⭐ | 0 | 安全模式绕过防御 | ✅ 已完成 |
| [T1689](./T1689-Downgrade-Attack.md) | 降级攻击 | ⭐⭐ | 0 | 强迫系统用弱协议 | ✅ 已完成 |
| [T1690](./T1690-Prevent-Command-History-Logging.md) | 阻止命令历史记录 | ⭐ | 0 | 让操作不留痕迹 | ✅ 已完成 |

## 子技术索引

> 共 38 个子技术，按父技术 T-ID 升序、子技术编号升序排列。

| 子技术ID | 名称 | 难度 | 一句话理解 | 文档状态 |
|----------|------|:----:|-----------|:--------:|
| [T1222.001](./T1222/T1222.001-Windows-Permissions.md) | Windows文件/目录权限修改 | ⭐ | 用icacls改文件权限 | ✅ 已完成 |
| [T1222.002](./T1222/T1222.002-Linux-And-Mac-Permissions.md) | Linux/Mac文件/目录权限修改 | ⭐ | 用chmod改文件权限 | ✅ 已完成 |
| [T1484.001](./T1484/T1484.001-Group-Policy-Modification.md) | 组策略修改 | ⭐⭐⭐ | 篡改AD组策略 | ✅ 已完成 |
| [T1484.002](./T1484/T1484.002-Trust-Modification.md) | 信任关系修改 | ⭐⭐⭐ | 改域间信任关系 | ✅ 已完成 |
| [T1553.001](./T1553/T1553.001-Gatekeeper-Bypass.md) | 代码签名 | ⭐⭐⭐ | 给恶意码假签名 | ✅ 已完成 |
| [T1553.002](./T1553/T1553.002-Code-Signing.md) | 安装根证书 | ⭐⭐⭐ | 装攻击者根证书 | ✅ 已完成 |
| [T1553.003](./T1553/T1553.003-SIP-And-Trust-Provider-Hijacking.md) | SIP信任提供方劫持 | ⭐⭐⭐ | 劫持SIP验证 | ✅ 已完成 |
| [T1553.004](./T1553/T1553.004-Install-Root-Certificate.md) | 安全启动绕过 | ⭐⭐⭐ | 绕过Secure Boot | ✅ 已完成 |
| [T1553.005](./T1553/T1553.005-Mark-of-the-Web-Bypass.md) | Mark-of-the-Web绕过 | ⭐⭐⭐ | 去掉MOTW标记 | ✅ 已完成 |
| [T1553.006](./T1553/T1553.006-Code-Signing-Policy-Modification.md) | 代码签名策略修改 | ⭐⭐⭐ | 改签名策略放水 | ✅ 已完成 |
| [T1556.001](./T1556/T1556.001-Domain-Controller-Authentication.md) | 域控制器认证 | ⭐⭐⭐ | 改域控认证逻辑 | ✅ 已完成 |
| [T1556.002](./T1556/T1556.002-Password-Filter-DLL.md) | 密码过滤器DLL | ⭐⭐⭐ | 偷记用户密码 | ✅ 已完成 |
| [T1556.003](./T1556/T1556.003-Pluggable-Authentication-Modules.md) | 可插拔认证模块 | ⭐⭐⭐ | 改PAM加后门 | ✅ 已完成 |
| [T1556.004](./T1556/T1556.004-Network-Device-Authentication.md) | 网络设备认证 | ⭐⭐⭐ | 改网络设备认证 | ✅ 已完成 |
| [T1556.005](./T1556/T1556.005-Reversible-Encryption.md) | 可逆加密 | ⭐⭐⭐ | 启用可逆加密 | ✅ 已完成 |
| [T1556.006](./T1556/T1556.006-Multi-factor-Authentication.md) | 多因素认证操纵 | ⭐⭐⭐ | 绕过或禁用MFA | ✅ 已完成 |
| [T1556.007](./T1556/T1556.007-Hybrid-Identity.md) | 混合身份 | ⭐⭐⭐ | 篡改混合身份 | ✅ 已完成 |
| [T1556.008](./T1556/T1556.008-Network-Provider-DLL.md) | 网络提供程序DLL | ⭐⭐⭐ | 装网络提供程序 | ✅ 已完成 |
| [T1556.009](./T1556/T1556.009-Conditional-Access-Policies.md) | 条件访问策略 | ⭐⭐⭐ | 改条件访问放水 | ✅ 已完成 |
| [T1578.001](./T1578/T1578.001-Create-Snapshot.md) | 创建快照 | ⭐⭐ | 云盘打快照 | ✅ 已完成 |
| [T1578.002](./T1578/T1578.002-Create-Cloud-Instance.md) | 创建云实例 | ⭐⭐ | 开新云实例 | ✅ 已完成 |
| [T1578.003](./T1578/T1578.003-Delete-Cloud-Instance.md) | 删除云实例 | ⭐⭐ | 删云实例灭迹 | ✅ 已完成 |
| [T1578.004](./T1578/T1578.004-Revert-Cloud-Instance.md) | 还原云实例 | ⭐⭐ | 回滚云实例 | ✅ 已完成 |
| [T1578.005](./T1578/T1578.005-Modify-Cloud-Compute-Configurations.md) | 修改云计算配置 | ⭐⭐ | 改云主机配置 | ✅ 已完成 |
| [T1599.001](./T1599/T1599.001-Network-Address-Translation-Traversal.md) | NAT遍历 | ⭐⭐⭐ | 跨NAT打通网络 | ✅ 已完成 |
| [T1600.001](./T1600/T1600.001-Reduce-Key-Space.md) | 缩小密钥空间 | ⭐⭐⭐ | 削弱加密强度 | ✅ 已完成 |
| [T1600.002](./T1600/T1600.002-Disable-Crypto-Hardware.md) | 禁用加密硬件 | ⭐⭐⭐ | 关TPM模块 | ✅ 已完成 |
| [T1601.001](./T1601/T1601.001-Patch-System-Image.md) | 修补系统镜像 | ⭐⭐⭐ | 改系统镜像 | ✅ 已完成 |
| [T1601.002](./T1601/T1601.002-Downgrade-System-Image.md) | 降级系统镜像 | ⭐⭐⭐ | 装旧版系统镜像 | ✅ 已完成 |
| [T1685.001](./T1685/T1685.001-Disable-or-Modify-Windows-Event-Log.md) | 禁用或修改Windows事件日志 | ⭐⭐ | 关Security日志 | ✅ 已完成 |
| [T1685.002](./T1685/T1685.002-Disable-or-Modify-Cloud-Log.md) | 禁用或修改云日志 | ⭐⭐ | 关CloudTrail | ✅ 已完成 |
| [T1685.003](./T1685/T1685.003-Modify-or-Spoof-Tool-UI.md) | 修改或伪造工具UI | ⭐⭐ | 伪造工具界面 | ✅ 已完成 |
| [T1685.004](./T1685/T1685.004-Disable-or-Modify-Linux-Audit-System-Log.md) | 禁用或修改Linux审计日志 | ⭐⭐ | 停掉auditd | ✅ 已完成 |
| [T1685.005](./T1685/T1685.005-Clear-Windows-Event-Logs.md) | 清除Windows事件日志 | ⭐⭐ | wevtutil清日志 | ✅ 已完成 |
| [T1685.006](./T1685/T1685.006-Clear-Linux-or-Mac-System-Logs.md) | 清除Linux/Mac系统日志 | ⭐⭐ | 清空/var/log | ✅ 已完成 |
| [T1685.007](./T1685/T1685.007-Impair-Autonomous-Defenses.md) | 损害自主防御 | ⭐⭐ | 欺骗或压制SOAR、AI安全助手等自主防御系统使其失效 | ✅ 已完成 |
| [T1686.001](./T1686/T1686.001-Cloud-Firewall.md) | 云防火墙 | ⭐⭐ | 关云安全组 | ✅ 已完成 |
| [T1686.002](./T1686/T1686.002-Network-Device-Firewall.md) | 网络设备防火墙 | ⭐⭐ | 改设备ACL | ✅ 已完成 |
| [T1686.003](./T1686/T1686.003-Windows-Host-Firewall.md) | Windows主机防火墙 | ⭐⭐ | 关Defender墙 | ✅ 已完成 |

### v19.1 变更说明

ATT&CK v19.1 对本战术目录进行了重大重构，从 v18 的 8 个父技术扩展到 v19.1 的 18 个父技术，主要变更如下：

**1. T1562 撤销与合并**
- 原 T1562（Impair Defenses，削弱防御）整体**撤销**（revoked）
- 其内容合并入新父技术 **[T1685](T1685-Disable-or-Modify-Tools.md)（Disable or Modify Tools，禁用或修改工具）**
- 子技术映射：
  - T1562.001 → [T1685](T1685-Disable-or-Modify-Tools.md)（合并到父级）
  - T1562.002 → [T1685](T1685-Disable-or-Modify-Tools.md).001（禁用或修改Windows事件日志）
  - T1562.006 → [T1685](T1685-Disable-or-Modify-Tools.md)（Indicator Blocking 内容合并到父级，部分拆到 [T1685](T1685-Disable-or-Modify-Tools.md).003）
  - T1562.008 → [T1685](T1685-Disable-or-Modify-Tools.md).002（禁用或修改云日志）
  - T1562.011 → [T1685](T1685-Disable-or-Modify-Tools.md).003（修改或伪造工具UI）
  - T1562.012 → [T1685](T1685-Disable-or-Modify-Tools.md).004（禁用或修改Linux审计系统日志）
- 详细映射历史见 [T1685 文档](./T1685-Disable-or-Modify-Tools.md) 末尾"映射历史"章节

**2. [T1553](T1553-Subvert-Trust-Controls.md) / [T1556](T1556-Modify-Authentication-Process.md) 跨战术迁移**
- [T1553](T1553-Subvert-Trust-Controls.md)（Subvert Trust Controls，颠覆信任控制）从原 TA0005 迁移到 TA0112
- [T1556](T1556-Modify-Authentication-Process.md)（Modify Authentication Process，修改认证过程）从原 TA0005 迁移到 TA0112
- 迁移理由：这两类技术是"主动破坏信任/认证体系"，属于削弱而非隐藏

**3. 10 个新增父技术**

| 新技术ID | 名称 | 来源 |
|----------|------|------|
| [T1578](T1578-Modify-Cloud-Compute-Infrastructure.md) | 修改云计算基础设施 | 从云攻击面单独抽出 |
| [T1599](T1599-Network-Boundary-Bridging.md) | 网络边界桥接 | 网络防御削弱独立成项 |
| [T1600](T1600-Weaken-Encryption.md) | 削弱加密 | 加密削弱独立成项 |
| [T1601](T1601-Modify-System-Image.md) | 修改系统镜像 | 固件层削弱独立成项 |
| [T1647](T1647-Plist-File-Modification.md) | Plist文件修改 | macOS 配置削弱独立成项 |
| [T1666](T1666-Modify-Cloud-Resource-Hierarchy.md) | 修改云资源层级 | 云治理面削弱独立成项 |
| [T1685](T1685-Disable-or-Modify-Tools.md) | 禁用或修改工具 | 由 T1562 合并升级 |
| [T1686](T1686-Disable-or-Modify-System-Firewall.md) | 禁用或修改系统防火墙 | 由 T1562.003 升级独立 |
| [T1688](T1688-Safe-Mode-Boot.md) | 安全模式启动 | 安全模式绕过独立成项 |
| [T1690](T1690-Prevent-Command-History-Logging.md) | 阻止命令历史记录 | 命令历史操纵独立成项 |

> ⚠️ **重要提示**：本目录已不含 T1562 文件。如发现旧引用，请改指向 [T1685](T1685-Disable-or-Modify-Tools.md)。

### 统计信息

- **技术总数**：18 个
- **子技术总数**：39 个
- **已完成文档**：57 个（18 父技术 + 39 子技术）
- **进行中文档**：0 个
- **待编写文档**：0 个

**子技术分布：**
- 0 个子技术的父技术：8 个（[T1112](T1112-Modify-Registry.md)、[T1207](T1207-Rogue-Domain-Controller.md)、[T1647](T1647-Plist-File-Modification.md)、[T1666](T1666-Modify-Cloud-Resource-Hierarchy.md)、[T1687](T1687-Exploitation-for-Defense-Impairment.md)、[T1688](T1688-Safe-Mode-Boot.md)、[T1689](T1689-Downgrade-Attack.md)、[T1690](T1690-Prevent-Command-History-Logging.md)）
- 含子技术的父技术：10 个
- 子技术数最多的父技术：[T1556](T1556-Modify-Authentication-Process.md)（9 个）

## 推荐阅读顺序

### 入门阶段（第1-2周）

> 适合零基础的安全爱好者，从最简单、最直观的技术开始。

**前置知识：** 了解基本的操作系统概念（进程、文件、网络）、会使用命令提示符或 PowerShell

**推荐阅读：**

1. **[T1112 修改注册表](./T1112-Modify-Registry.md)** —— 防御削弱最基础的操作，几乎所有削弱动作最终都落到注册表
2. **[T1222 文件权限修改](./T1222-File-And-Directory-Permissions-Modification.md)** —— 理解攻击者如何篡改文件权限绕过访问控制
3. **[T1647 Plist文件修改](./T1647-Plist-File-Modification.md)** —— macOS 平台的"注册表"修改，对应理解跨平台思路
4. **[T1688 安全模式启动](./T1688-Safe-Mode-Boot.md)** —— 最简单的防御绕过思路：用安全模式让安全软件不加载

**学习建议：**
- 在虚拟机中动手尝试每个技术的实验步骤
- 重点理解"为什么攻击者需要这个技术"而非仅记住命令
- 同时关注 Windows 与 macOS 两个平台的对应关系

### 进阶阶段（第3-4周）

> 适合有一定基础的学习者，开始接触更复杂的技术。

**前置知识：** 了解操作系统安全机制（UAC、Windows Defender）、会使用 PowerShell 脚本、了解云服务基础

**推荐阅读：**

1. **[T1685 禁用或修改工具](./T1685-Disable-or-Modify-Tools.md)** —— 防御削弱的核心技术，理解攻击者如何系统性瘫痪防御体系（含 T1562 历史变更）
2. **[T1686 禁用或修改系统防火墙](./T1686-Disable-or-Modify-System-Firewall.md)** —— 网络层防御削弱的入门
3. **[T1484 域/租户策略修改](./T1484-Domain-or-Tenant-Policy-Modification.md)** —— 掌握企业级策略操纵方法
4. **[T1578 修改云计算基础设施](./T1578-Modify-Cloud-Compute-Infrastructure.md)** —— 云环境防御削弱的代表

**学习建议：**
- 结合隐蔽战术（TA0005）的内容一起学习，理解"隐藏"与"削弱"的边界
- 在本地 AD 测试环境中练习 GPO 和域策略操作
- 在 AWS/Azure 实验账号中演练 CloudTrail 关闭与云实例操作

### 高级阶段（第5-6周）

> 适合有较好技术基础的学习者，深入理解复杂技术原理。

**前置知识：** 了解 Active Directory、云服务架构、内核态/用户态概念、密码学基础、UEFI/固件启动流程

**推荐阅读：**

1. **[T1553 颠覆信任控制](./T1553-Subvert-Trust-Controls.md)** —— 深入理解系统信任链的攻击面（代码签名、根证书、Secure Boot）
2. **[T1556 修改认证过程](./T1556-Modify-Authentication-Process.md)** —— 学习劫持身份验证机制的高级技术（LSASS、PAM、MFA）
3. **[T1600 削弱加密](./T1600-Weaken-Encryption.md) / [T1601 修改系统镜像](./T1601-Modify-System-Image.md)** —— 固件与加密层的深层削弱
4. **[T1687 利用漏洞削弱防御](./T1687-Exploitation-for-Defense-Impairment.md)** —— 学习 BYOVD 等利用漏洞绕过防御的技术

**学习建议：**
- 建议在完整的企业模拟环境中练习
- 结合红队视角和蓝队视角双向思考
- 关注 2024-2026 年最新的攻击案例，了解技术演进趋势
- 重点研究 SolarWinds、BlackCat、Conti 等典型案例中的防御削弱手法

## 参考资料

### 官方文档

- [MITRE ATT&CK - Defense Impairment (TA0112)](https://attack.mitre.org/tactics/TA0112/) —— 本战术官方页面
- [MITRE ATT&CK - Stealth (TA0005)](https://attack.mitre.org/tactics/TA0005/) —— 互补战术隐蔽
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/) —— Enterprise 矩阵总览
- [ATT&CK v19.1 Release Notes](https://attack.mitre.org/resources/updates/) —— v19.1 变更说明（含 T1562 撤销、TA0112 新增）

### 学习资源

- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) —— CISA 已知被利用漏洞目录
- [LOLDrivers - 漏洞驱动数据库](https://www.loldrivers.io/) —— 已知存在漏洞的驱动程序列表（BYOVD 攻击参考）
- [GTFOBins](https://gtfobins.github.io/) —— Unix/Linux 二进制文件利用技术库
- [LOLBAS](https://lolbas-project.github.io/) —— Windows 系统二进制文件利用技术库
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) —— ATT&CK 技术的原子测试用例库

### 相关工具

- [Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) —— Windows 系统活动监控工具
- [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer) —— 进程管理分析工具
- [Volatility](https://www.volatilityfoundation.org/) —— 内存取证分析框架
- [Sigma Rules](https://github.com/SigmaHQ/sigma) —— 通用安全检测规则格式
- [Autoruns](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns) —— 启动项与持久化排查工具

> **版本**: v20 | **更新**: 2026-10-22 | **模板**: 战术README v3.1
