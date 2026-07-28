# Plist文件修改 (T1647)

> 想象一下：你公司的安全策略写在一张张配置卡片上，放在不同部门的卡片柜里。macOS的plist（Property List，属性列表）文件就是这样的"配置卡片"——系统的启动项、应用的偏好设置、安全策略、权限配置全都写在里面。有一天，攻击者偷偷打开卡片柜，把"开启防火墙"的卡片换成了"关闭防火墙"，把"启用Gatekeeper"的卡片换成了"禁用Gatekeeper"，还在启动项卡片柜里塞了一张新卡片写着"开机自动运行我的后门"。你重新启动Mac、重装应用都没用，因为这些配置卡片被改了，系统照着改过的卡片执行。

## 30秒速查卡

| 维度 | 你需要知道的 |
|------|--------------|
| 这是什么？ | 修改macOS的plist文件，篡改系统配置、植入启动项后门、削弱安全机制 |
| 为什么危险？ | macOS大量安全配置（Gatekeeper、防火墙、SIP、TCC权限）都存储在plist中，改一个值就能禁用关键防护 |
| 谁需要关心？ | macOS系统管理员、企业MDM运维、苹果设备SOC团队 |
| 你的第一步防御 | 监控`defaults`命令对安全相关plist的修改，部署文件完整性监控（FIM） |
| 如果只做一件事 | 监控`~/Library/LaunchAgents/`和`/Library/LaunchAgents/`下的plist新增和修改 |

## 难度等级

⭐⭐ 中级：需要理解macOS的plist结构和LaunchAgent/LaunchDaemon机制

**前置知识要求**：
- macOS文件系统结构（~/Library、/Library、/System/Library）
- plist文件格式（XML、Binary、JSON）
- LaunchAgent/LaunchDaemon启动机制
- macOS安全机制（Gatekeeper、SIP、TCC）

## 前置知识检查

读这个文件之前，你需要知道：
- **什么是plist**：macOS的属性列表文件，存储应用偏好、系统配置，支持XML/Binary/JSON格式
- **什么是LaunchAgent**：macOS的启动项机制，通过plist文件定义开机或登录时自动运行的程序
- **什么是defaults命令**：macOS自带的plist读写命令行工具
- **什么是Gatekeeper**：macOS的应用签名验证机制，配置存储在plist中
- **什么是TCC**：Transparency, Consent, and Control，macOS的隐私权限管理框架

## 技术描述

### 通俗解释

plist文件是macOS的"配置中心"——系统启动项、应用偏好设置、安全策略、用户权限配置全都以plist文件形式存储在不同目录中。正常情况下用户通过"系统偏好设置"或应用自身的设置界面修改这些配置，但攻击者直接用`defaults`命令、`plutil`工具或文本编辑器修改plist文件，绕过正常的管理界面。他们可以植入LaunchAgent实现开机自启后门、修改Gatekeeper配置允许运行未签名应用、关闭防火墙、修改Safari安全设置、篡改TCC权限数据库——所有这些只需要改几个plist值。

### 过渡段

简单来说，plist就像macOS的"配置开关面板"。攻击者直接"拨开关"——把"开启Gatekeeper"拨到"关闭Gatekeeper"，把"开机不运行任何程序"拨到"开机运行我的后门"。修改plist是macOS防御削弱和持久化最常用的技术，几乎所有削弱macOS防御的操作最终都会落到修改plist上。下面看看具体是怎么操作的。

### 技术原理

修改plist文件削弱防御的工作流程：

1. **识别目标plist**：确定要修改的安全配置plist文件路径
2. **获取权限**：用户级plist（~/Library/）只需用户权限，系统级plist（/Library/）需要管理员权限
3. **修改plist**：使用defaults、plutil、PlistBuddy或文本编辑器修改
4. **重启相关服务**：部分修改需要重启服务或重启系统才能生效
5. **验证修改**：确认修改生效，防御机制被削弱

### 常见被修改的安全相关plist

| plist路径 | 作用 | 攻击者修改 |
|-----------|------|------------|
| `~/Library/Preferences/com.apple.LaunchServices/com.apple.LaunchServices.QuarantineEvents` | Gatekeeper隔离状态 | 清空隔离记录，绕过Gatekeeper |
| `/Library/Preferences/com.apple.alf` | 应用层防火墙配置 | 设为`globalstate = 0`禁用防火墙 |
| `/Library/Preferences/com.apple.security.GKApproval` | Gatekeeper审批状态 | 修改允许未签名应用运行 |
| `/Library/Preferences/com.apple.screensaver` | 屏幕保护配置 | 修改`askForPassword=0`关闭锁屏密码 |
| `~/Library/Preferences/com.apple.safari` | Safari安全配置 | 修改`WebKitPreferences.javaEnabled=true`启用Java |
| `/Library/Preferences/com.apple.TimeMachine` | Time Machine配置 | 禁用自动备份 |
| `~/Library/Preferences/com.apple.spotlight.ordereditems` | Spotlight索引 | 修改排除关键目录，让搜索不到恶意文件 |

### LaunchAgent/LaunchDaemon持久化plist

| plist路径 | 加载时机 | 攻击者用途 |
|-----------|----------|------------|
| `~/Library/LaunchAgents/com.evil.backdoor.plist` | 用户登录时 | 普通用户权限的后门持久化 |
| `/Library/LaunchAgents/com.evil.backdoor.plist` | 任何用户登录时 | 系统级后门持久化 |
| `/Library/LaunchDaemons/com.evil.backdoor.plist` | 系统启动时 | root权限后门持久化 |
| `/System/Library/LaunchAgents/*.plist` | 系统启动时 | 劫持系统原生LaunchAgent（需SIP关闭） |

### 用途和影响

- **持久化**：通过LaunchAgent/LaunchDaemon实现开机自启后门
- **防御规避**：禁用Gatekeeper、防火墙、SIP相关配置
- **权限提升**：修改TCC权限数据库获取隐私数据访问权限
- **信息收集**：修改Safari/Spotlight配置收集用户活动
- **横向移动**：通过修改网络共享配置获取内网访问

## 子技术列表

T1647是父技术，目前无子技术。但与以下技术密切相关：
- T1547.011 Plist文件执行（持久化战术，通过plist触发执行）
- T1562 削弱防御（常通过修改plist实现）
- T1543.004 LaunchDaemon（通过LaunchDaemon plist实现持久化）

## 攻击流程

```mermaid
flowchart TD
    A[识别目标安全配置plist] --> B{需要什么权限?}
    B -->|~/Library/下| C[用户权限即可]
    B -->|/Library/或/System/下| D[需要管理员/root权限]
    C --> E[修改plist文件]
    D --> F[提权或利用已有admin权限]
    F --> E
    E --> G{选择修改方式}
    G -->|defaults命令| H[defaults write]
    G -->|plutil命令| I[plutil -replace]
    G -->|PlistBuddy| J[/usr/libexec/PlistBuddy]
    G -->|文本编辑器| K[直接编辑XML]
    H --> L[重启相关服务]
    I --> L
    J --> L
    K --> L
    L --> M[防御被削弱/后门持久化]
    style M fill:#ff6b6b,stroke:#333,stroke-width:3px
```

### 步骤详解

1. **侦察**：识别目标macOS的安全配置状态，找到要修改的plist文件
2. **选择**：确定要修改的plist键和目标值
3. **获取权限**：确保有足够权限修改目标plist
4. **修改**：使用defaults、plutil、PlistBuddy或文本编辑器修改
5. **重启**：重启相关服务或重启系统让修改生效
6. **后续**：利用被削弱的防御进行进一步攻击

## 真实案例

### 案例1：XCSSET恶意软件通过plist实现持久化

- **时间**：2020-2022年
- **目标**：macOS开发者（通过Xcode项目感染）
- **攻击组织**：未归属（疑似中文背景威胁组织）
- **手法**：XCSSET恶意软件感染Xcode项目后，在编译时自动注入恶意代码到生成的应用中。在macOS端，XCSSET通过修改多个plist文件实现持久化和防御削弱：①在`~/Library/LaunchAgents/com.apple.xcsset.helper.plist`植入持久化后门，让恶意代码在用户登录时自动启动；②修改`~/Library/Preferences/com.apple.LaunchServices/com.apple.LaunchServices.QuarantineEvents.plist`清空Gatekeeper隔离记录，让后续下载的恶意应用不会被标记为"已下载"从而绕过Gatekeeper；③修改`~/Library/Preferences/com.apple.safari.plist`启用Java和禁用安全警告，让Safari更容易被用于社会工程攻击；④修改`~/Library/Preferences/com.apple.spotlight.ordereditems.plist`排除恶意文件所在目录，让用户用Spotlight搜索不到恶意文件。XCSSET展示了T1647的"组合拳"用法——通过修改多个plist同时实现持久化、防御削弱和隐藏。
- **影响**：感染数千个Xcode项目，波及全球macOS开发者社区
- **参考**：https://www.trendmicro.com/en_us/research/20/h/xcsset-malware-infects-xcode-projects--uses-0day.html

### 案例2：Shlayer恶意软件通过plist禁用Gatekeeper

- **时间**：2018-2024年（持续活跃）
- **目标**：macOS用户（通过破解软件和盗版内容分发）
- **攻击组织**：Shlayer团伙（macOS上最活跃的恶意软件分发组织）
- **手法**：Shlayer是macOS上分发最广的恶意软件之一，主要通过伪装成Adobe Flash Player更新或破解软件安装包传播。在获取初始执行后，Shlayer会通过修改plist文件绕过macOS的Gatekeeper和XProtect安全机制：①使用`sudo spctl --master-disable`命令禁用Gatekeeper，该命令实际是修改`/Library/Preferences/com.apple.security.GKApproval.plist`；②修改`/Library/Preferences/com.apple.alf.globalstate`为0禁用应用层防火墙；③在`~/Library/LaunchAgents/`下创建plist文件（如`com.apple.upd.plist`、`com.apple.service.plist`）实现持久化，plist中通过`RunAtLoad=true`和`KeepAlive=true`确保后门开机自启且被kill后自动重启；④修改`~/Library/Preferences/com.apple.screencapture.plist`修改截图路径，截获用户屏幕内容。Shlayer变种众多，但核心都是通过修改plist实现绕过防御和持久化。
- **影响**：感染数百万台macOS设备，作为二级载荷分发平台
- **参考**：https://www.kaspersky.com.cn/shlayer-malware-analysis

### 案例3：Silver Trent恶意软件通过plist植入持久化后门

- **时间**：2022-2024年
- **目标**：macOS终端用户（通过钓鱼邮件和恶意文档）
- **攻击组织**：未归属（疑似APT组织）
- **手法**：Silver（又称Trent）是针对macOS的RAT（远程访问木马），在2022-2024年间持续活跃。Silver在获取初始执行后，通过修改plist文件实现多层持久化：①在`~/Library/LaunchAgents/com.apple.systemupdate.plist`植入用户级持久化后门，伪装成"系统更新"服务；②在`/Library/LaunchDaemons/com.apple.systemupdate.plist`植入系统级持久化后门（需提权），伪装成系统守护进程；③两个plist都配置了`RunAtLoad=true`、`KeepAlive=true`、`SuccessfulExit=false`——意味着后门被kill后会立即重启；④修改`/Library/Preferences/com.apple.alf`禁用防火墙，确保C2通信不被阻断；⑤修改`~/Library/Preferences/com.apple.safari.plist`禁用钓鱼网站警告，让后续钓鱼攻击更有效。Silver展示了T1647与权限提升、持久化、防御削弱战术的深度结合。
- **影响**：感染政府、企业、研究机构的macOS终端
- **参考**：https://www.trendmicro.com/en_us/research/22/c/silver-trent-macos-malware.html

## 红队视角

### 实战技巧

1. **defaults命令最隐蔽**：`defaults write`不弹窗，可嵌入脚本，且不会触发文件修改告警
2. **PlistBuddy更精确**：对嵌套键值，`PlistBuddy`比`defaults`更精确
3. **伪装plist名称**：用`com.apple.update.plist`、`com.apple.service.plist`等系统风格名称伪装后门
4. **组合LaunchAgent+LaunchDaemon**：双层持久化，普通用户级+系统级
5. **修改后验证**：用`plutil -lint`确认plist格式正确，`defaults read`确认值已修改

### 常用工具

| 工具 | 用途 | 说明 |
|------|------|------|
| defaults | plist读写命令 | macOS自带，最常用 |
| plutil | plist编辑工具 | macOS自带，支持格式转换和键值修改 |
| PlistBuddy | 精确键值修改 | macOS自带，适合嵌套键 |
| Xcode | 图形化编辑 | 适合交互式修改和调试 |
| Plutil.com | 在线工具 | 不需要macOS环境也能查看 |

### 注意事项

- 修改`/System/Library/`下的plist需要关闭SIP（System Integrity Protection）
- Binary格式的plist需要先用`plutil -convert xml1`转换为XML才能编辑
- 修改错误可能导致应用启动失败
- macOS 13+引入了"后台项目"管理，新增LaunchAgent会触发系统提示
- MDM管控的设备，部分plist修改会被MDM策略覆盖

## 蓝队视角

### 检测要点

1. **LaunchAgent/LaunchDaemon监控**：监控`~/Library/LaunchAgents/`、`/Library/LaunchAgents/`、`/Library/LaunchDaemons/`下的新增和修改
2. **defaults命令监控**：监控`defaults write`、`defaults delete`命令的执行和参数
3. **安全相关plist监控**：监控Gatekeeper、防火墙、TCC相关plist的变更
4. **plist哈希基线**：定期对比关键plist文件的哈希与基线
5. **TCC数据库监控**：监控`/Library/Application Support/com.apple.TCC/TCC.db`的变更

### 监控建议

- 部署文件完整性监控（FIM）工具（如Fidelis、Tripwire）监控plist变更
- 启用macOS的`auditpipe`监控文件操作
- 使用`eslogger`（Endpoint Security Framework）监控plist文件写入
- 部署Jamf Pro等MDM解决方案的合规性检查
- 定期导出关键plist文件并对比基线

## 避坑指南

| 坑 | 后果 | 解决方法 |
|----|------|----------|
| 只监控`/Library/`，忽略`~/Library/` | 漏报用户级plist修改 | 同时监控用户级和系统级目录 |
| SIP保护下以为安全 | 攻击者可能关闭SIP后再修改 | 监控SIP状态变更 |
| 忽略Binary格式plist | 漏报二进制plist修改 | 用`plutil`工具解析所有格式 |
| 只看新增，忽略修改 | 漏报对已有plist的篡改 | 同时监控新增和修改事件 |
| 忽略`defaults`命令 | 漏报通过defaults修改plist | 监控defaults命令的参数 |

## 检测建议

### 网络层

**用人话说**：修改plist是本地操作，不直接产生网络流量。但攻击者修改plist后往往会立即触发后门C2通信——关注plist修改后短时间内的异常网络活动。

监控指标：
- LaunchAgent plist创建后5分钟内的新增网络连接
- `defaults write`命令执行后的C2通信
- 大量plist文件被批量修改的突发模式（可能是恶意软件批量感染）

### 主机层

**用人话说**：监控LaunchAgent/LaunchDaemon目录的文件操作和defaults命令的执行——这是plist修改最直接的信号。任何对Gatekeeper、防火墙、TCC配置的修改都应该告警。

```event
macOS Endpoint Security事件：
ES_EVENT_TYPE_NOTIFY_WRITE：
Target包含：
  - ~/Library/LaunchAgents/
  - /Library/LaunchAgents/
  - /Library/LaunchDaemons/
  - /Library/Preferences/com.apple.alf
  - /Library/Preferences/com.apple.security.GKApproval
```

```event
macOS auditpipe事件：
Process: defaults / plutil / PlistBuddy
Arguments包含：
  - write
  - delete
  - -replace
```

### 应用层

**用人话说**：监控defaults命令和plutil命令——攻击者最常使用这两种方式修改plist。

```yaml
title: 检测通过defaults命令禁用Gatekeeper
status: experimental
description: 检测使用defaults/spctl命令禁用Gatekeeper的活动
logsource:
    category: process_creation
    product: macos
detection:
    selection_spctl:
        Image|endswith: '/spctl'
        CommandLine|contains: 'master-disable'
    selection_defaults:
        Image|endswith: '/defaults'
        CommandLine|contains:
            - 'com.apple.security.GKApproval'
            - 'com.apple.LaunchServices'
    condition: selection_spctl or selection_defaults
level: critical
tags:
    - attack.t1647
    - attack.t1562
    - attack.defense_evasion
```

```yaml
title: 检测LaunchAgent/LaunchDaemon创建
status: experimental
description: 检测在LaunchAgent/LaunchDaemon目录下创建plist文件
logsource:
    category: file_event
    product: macos
detection:
    selection:
        TargetFilename|contains:
            - '/Library/LaunchAgents/'
            - '/Library/LaunchDaemons/'
            - '/Users/'
            - '/Library/LaunchAgents/'
        TargetFilename|endswith: '.plist'
    filter_system:
        TargetFilename|startswith:
            - '/System/Library/'
    condition: selection and not filter_system
level: high
tags:
    - attack.t1647
    - attack.t1547.011
    - attack.persistence
```

```yaml
title: 检测通过defaults禁用防火墙
status: experimental
description: 检测修改防火墙plist配置的活动
logsource:
    category: process_creation
    product: macos
detection:
    selection:
        Image|endswith: '/defaults'
        CommandLine|contains:
            - 'com.apple.alf'
            - 'globalstate'
    condition: selection
level: high
tags:
    - attack.t1647
    - attack.t1562.003
    - attack.defense_evasion
```

## 缓解措施

### 高优先级

1. **启用SIP**：System Integrity Protection保护`/System/`下的plist不被修改
2. **限制LaunchAgent权限**：通过MDM配置文件限制用户创建LaunchAgent
3. **启用TCC保护**：确保TCC权限数据库不被未授权修改

### 中优先级

4. **部署FIM**：文件完整性监控工具监控关键plist变更
5. **使用MDM**：通过MDM强制安全配置，即使被修改也会自动恢复
6. **限制defaults命令**：通过应用控制限制defaults/plutil的使用场景
7. **监控Gatekeeper状态**：定期检查Gatekeeper状态，发现禁用立即告警

### 低优先级

8. **定期备份plist**：便于恢复
9. **使用配置描述文件**：通过配置描述文件（.mobileconfig）锁定安全配置
10. **部署EDR**：macOS端点检测与响应系统监控plist修改

## 动手实验

### 实验1：查看关键安全相关plist

```bash
# 查看Gatekeeper状态
sudo spctl --status
sudo defaults read /Library/Preferences/com.apple.security.GKApproval 2>/dev/null

# 查看防火墙配置
sudo defaults read /Library/Preferences/com.apple.alf

# 查看所有LaunchAgent
ls -la ~/Library/LaunchAgents/ 2>/dev/null
ls -la /Library/LaunchAgents/
ls -la /Library/LaunchDaemons/

# 查看Safari安全配置
defaults read com.apple.safari | grep -i -E "(java|javascript|warning|safe)"

# 查看TCC权限数据库（需要Full Disk Access）
sqlite3 "/Library/Application Support/com.apple.TCC/TCC.db" "SELECT service, client, auth_value FROM access;"
```

**预期输出**：显示各安全配置的当前状态，与安全基线对比

### 实验2：监控plist文件修改（实验环境）

```bash
# 启用对LaunchAgent目录的监控
sudo fs_usage -w -f filesys | grep -E "LaunchAgents|LaunchDaemons"

# 用eslogger监控plist写入（需要macOS 13+）
sudo eslogger write --names --output-file /tmp/eslog.json &

# 在另一个终端模拟修改
defaults write ~/Library/LaunchAgents/com.test.example.plist test_key -string "test_value"

# 检查监控输出
cat /tmp/eslog.json | python3 -m json.tool | head -50

# 清理
rm ~/Library/LaunchAgents/com.test.example.plist
```

**预期输出**：plist文件修改操作被记录在监控输出中

### 实验3：创建测试LaunchAgent（实验环境）

```bash
# 1. 创建一个测试用的LaunchAgent plist
cat > ~/Library/LaunchAgents/com.test.demo.plist << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.test.demo</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/echo</string>
        <string>LaunchAgent demo executed at $(date)</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/demo_launchagent.log</string>
</dict>
</plist>
EOF

# 2. 加载LaunchAgent
launchctl load ~/Library/LaunchAgents/com.test.demo.plist

# 3. 验证执行
cat /tmp/demo_launchagent.log

# 4. 列出已加载的LaunchAgent
launchctl list | grep com.test

# 5. 卸载并清理
launchctl unload ~/Library/LaunchAgents/com.test.demo.plist
rm ~/Library/LaunchAgents/com.test.demo.plist /tmp/demo_launchagent.log
```

**预期输出**：理解LaunchAgent的创建、加载、执行、卸载完整流程

## 术语解释

| 术语 | 解释 |
|------|------|
| plist | Property List，macOS的属性列表文件，存储配置数据 |
| LaunchAgent | macOS的启动项机制，用户登录时自动加载的plist |
| LaunchDaemon | macOS的系统级守护进程，系统启动时自动加载的plist |
| defaults | macOS自带的plist读写命令行工具 |
| plutil | macOS自带的plist编辑和格式转换工具 |
| PlistBuddy | macOS自带的精确plist键值修改工具 |
| Gatekeeper | macOS的应用签名验证机制，配置存储在plist中 |
| SIP | System Integrity Protection，系统完整性保护，保护/System/下的文件 |
| TCC | Transparency, Consent, and Control，macOS的隐私权限管理框架 |
| MDM | Mobile Device Management，移动设备管理，可强制安全配置 |
| Endpoint Security | macOS的端点安全框架，提供文件/进程监控能力 |

## 参考资料

### 📚 深入了解
- [MITRE ATT&CK T1647](https://attack.mitre.org/techniques/T1647/) - 官方技术页面
- [Apple开发者文档 - Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/) - plist编程指南
- [Apple开发者文档 - Launch Services](https://developer.apple.com/documentation/coreservices/launch_services) - 启动服务文档

### 📰 真实攻击
- [TrendMicro XCSSET分析](https://www.trendmicro.com/en_us/research/20/h/xcsset-malware-infects-xcode-projects--uses-0day.html) - XCSSET通过plist持久化
- [Kaspersky Shlayer分析](https://www.kaspersky.com.cn/shlayer-malware-analysis) - Shlayer通过plist绕过Gatekeeper
- [TrendMicro Silver分析](https://www.trendmicro.com/en_us/research/22/c/silver-trent-macos-malware.html) - Silver通过plist多层持久化

### 🔧 动手试试
- [Eslogger](https://developer.apple.com/documentation/endpointsecurity) - macOS Endpoint Security日志工具
- [Jamf Pro](https://www.jamf.com/) - macOS MDM解决方案
- [KnockKnock](https://objective-see.com/products/knockknock.html) - macOS持久化项查看工具
- [BlockBlock](https://objective-see.com/products/blockblock.html) - macOS持久化监控工具

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 3.1 | 2026-07-23 | 初始版本，完整v3.1模板，覆盖XCSSET/Shlayer/Silver案例 |
