---
status: 【已完成】
template_version: "1.0"
last_updated: "2026-10-22"
tactic_id: "TA0002"
tactic_name_cn: "执行"
tactic_name_en: "Execution"
attack_version: "v20"
official_technique_count: 22
official_subtechnique_count: 44
local_technique_count: 22
local_subtechnique_count: 44
coverage_percentage: 100.0
---

# TA0002 执行 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v20 中 TA0002 (Execution/执行) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v20
- **官方数据**：22 项父技术 / 44 项子技术
- **本地数据**：22 项父技术 / 44 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1197 | BITS Jobs | BITS作业 | ./T1197-BITS-Jobs.md | 0/0 | 📝 | - |
| T1651 | Cloud Administration Command | 云管理命令 | ./T1651-Cloud-Administration-Command.md | 0/0 | 📝 | - |
| T1059 | Command and Scripting Interpreter | 命令和脚本解释器 | ./T1059-Command-and-Scripting-Interpreter.md | 13/13 | 📝 | 子技术数frontmatter=0 |
| T1609 | Container Administration Command | 容器管理命令 | ./T1609-Container-Administration-Command.md | 0/0 | 📝 | - |
| T1610 | Deploy Container | 部署容器 | ./T1610-Deploy-Container.md | 0/0 | 📝 | - |
| T1699 | Direct Prompt Injection | 直接提示词注入 | ./T1699-Direct-Prompt-Injection.md | 0/0 | 📝 | - |
| T1675 | ESXi Administration Command | ESXi管理命令 | ./T1675-ESXi-Administration-Command.md | 0/0 | 📝 | - |
| T1203 | Exploitation for Client Execution | 客户端漏洞利用执行 | ./T1203-Exploitation-for-Client-Execution.md | 0/0 | 📝 | - |
| T1574 | Hijack Execution Flow | 劫持执行流 | ./T1574-Hijack-Execution-Flow.md | 12/12 | 📝 | 子技术数frontmatter=0 |
| T1698 | Indirect Prompt Injection | 间接提示词注入 | ./T1698-Indirect-Prompt-Injection.md | 0/0 | 📝 | - |
| T1674 | Input Injection | 输入注入 | ./T1674-Input-Injection.md | 0/0 | 📝 | - |
| T1559 | Inter-Process Communication | 进程间通信 | ./T1559-Inter-Process-Communication.md | 3/3 | 📝 | 🔄 本地名: Inter Process Communication | 子技术数frontmatter=0 |
| T1106 | Native API | 原生API | ./T1106-Native-API.md | 0/0 | 📝 | - |
| T1677 | Poisoned Pipeline Execution | 毒化流水线执行 | ./T1677-Poisoned-Pipeline-Execution.md | 0/0 | 📝 | - |
| T1053 | Scheduled Task/Job | 计划任务/作业 | ./T1053-Scheduled-Task-Job.md | 5/5 | 📝 | 🔄 本地名: Scheduled Task Job | 子技术数frontmatter=0 |
| T1648 | Serverless Execution | 无服务器执行 | ./T1648-Serverless-Execution.md | 0/0 | 📝 | - |
| T1129 | Shared Modules | 共享模块 | ./T1129-Shared-Modules.md | 0/0 | 📝 | - |
| T1072 | Software Deployment Tools | 软件部署工具 | ./T1072-Software-Deployment-Tools.md | 0/0 | 📝 | - |
| T1569 | System Services | 系统服务 | ./T1569-System-Services.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1127 | Trusted Developer Utilities Proxy Execution | 受信任开发工具代理执行 | ./T1127-Trusted-Developer-Utilities-Proxy-Execution.md | 3/3 | 📝 | 子技术数frontmatter=0 |
| T1204 | User Execution | 用户执行 | ./T1204-User-Execution.md | 5/5 | 📝 | 子技术数frontmatter=0 |
| T1047 | Windows Management Instrumentation | Windows管理规范 | ./T1047-Windows-Management-Instrumentation.md | 0/0 | 📝 | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1059.001 | PowerShell | PowerShell | T1059 | ./T1059/T1059.001-PowerShell.md | 📝 | - |
| T1059.002 | AppleScript | AppleScript | T1059 | ./T1059/T1059.002-AppleScript.md | 📝 | - |
| T1059.003 | Windows Command Shell | Windows命令行 | T1059 | ./T1059/T1059.003-Windows-Command-Shell.md | 📝 | - |
| T1059.004 | Unix Shell | Unix Shell | T1059 | ./T1059/T1059.004-Unix-Shell.md | 📝 | - |
| T1059.005 | Visual Basic | Visual Basic | T1059 | ./T1059/T1059.005-Visual-Basic.md | 📝 | - |
| T1059.006 | Python | Python | T1059 | ./T1059/T1059.006-Python.md | 📝 | - |
| T1059.007 | JavaScript | JavaScript | T1059 | ./T1059/T1059.007-JavaScript.md | 📝 | - |
| T1059.008 | Network Device CLI | 网络设备CLI | T1059 | ./T1059/T1059.008-Network-Device-CLI.md | 📝 | - |
| T1059.009 | Cloud API | 云API | T1059 | ./T1059/T1059.009-Cloud-API.md | 📝 | - |
| T1059.010 | AutoHotKey & AutoIT | AutoHotKey/AutoIT | T1059 | ./T1059/T1059.010-AutoHotKey-AutoIT.md | 📝 | 🔄 本地名: AutoHotKey AutoIT |
| T1059.011 | Lua | Lua | T1059 | ./T1059/T1059.011-Lua.md | 📝 | - |
| T1059.012 | Hypervisor CLI | 虚拟化管理CLI | T1059 | ./T1059/T1059.012-Hypervisor-CLI.md | 📝 | - |
| T1059.013 | Container CLI/API | 容器CLI/API | T1059 | ./T1059/T1059.013-Container-CLI-API.md | 📝 | 🔄 本地名: Container CLI API |
| T1574.001 | DLL | DLL搜索顺序劫持 | T1574 | ./T1574/T1574.001-DLL.md | 📝 | - |
| T1574.004 | Dylib Hijacking | dylib劫持 | T1574 | ./T1574/T1574.004-Dylib-Hijacking.md | 📝 | - |
| T1574.005 | Executable Installer File Permissions Weakness | 可执行安装程序文件权限弱点 | T1574 | ./T1574/T1574.005-Executable-Installer-File-Permissions-Weakness.md | 📝 | - |
| T1574.006 | Dynamic Linker Hijacking | 动态链接器劫持 | T1574 | ./T1574/T1574.006-Dynamic-Linker-Hijacking.md | 📝 | - |
| T1574.007 | Path Interception by PATH Environment Variable | PATH劫持 | T1574 | ./T1574/T1574.007-Path-Interception-By-PATH-Environment-Variable.md | 📝 | 🔄 本地名: Path Interception By PATH Environment Variable |
| T1574.008 | Path Interception by Search Order Hijacking | 搜索顺序劫持 | T1574 | ./T1574/T1574.008-Path-Interception-By-Search-Order-Hijacking.md | 📝 | 🔄 本地名: Path Interception By Search Order Hijacking |
| T1574.009 | Path Interception by Unquoted Path | 未引用路径劫持 | T1574 | ./T1574/T1574.009-Path-Interception-By-Unquoted-Path.md | 📝 | 🔄 本地名: Path Interception By Unquoted Path |
| T1574.010 | Services File Permissions Weakness | 服务权限劫持 | T1574 | ./T1574/T1574.010-Services-File-Permissions-Weakness.md | 📝 | - |
| T1574.011 | Services Registry Permissions Weakness | 服务注册表权限弱点 | T1574 | ./T1574/T1574.011-Services-Registry-Permissions-Weakness.md | 📝 | - |
| T1574.012 | COR_PROFILER | COR_PROFILER劫持 | T1574 | ./T1574/T1574.012-COR_PROFILER.md | 📝 | - |
| T1574.013 | KernelCallbackTable | KernelCallbackTable劫持 | T1574 | ./T1574/T1574.013-Kernelcallbacktable.md | 📝 | 🔄 本地名: Kernelcallbacktable |
| T1574.014 | AppDomainManager | AppDomainManager劫持 | T1574 | ./T1574/T1574.014-Appdomainmanager.md | 📝 | 🔄 本地名: Appdomainmanager |
| T1559.001 | Component Object Model | COM | T1559 | ./T1559/T1559.001-Component-Object-Model.md | 📝 | - |
| T1559.002 | Dynamic Data Exchange | DDE | T1559 | ./T1559/T1559.002-Dynamic-Data-Exchange.md | 📝 | - |
| T1559.003 | XPC Services | XPC服务 | T1559 | ./T1559/T1559.003-XPC-Services.md | 📝 | - |
| T1053.002 | At | At | T1053 | ./T1053/T1053.002-At.md | 📝 | - |
| T1053.003 | Cron | Cron | T1053 | ./T1053/T1053.003-Cron.md | 📝 | - |
| T1053.005 | Scheduled Task | 计划任务 | T1053 | ./T1053/T1053.005-Scheduled-Task.md | 📝 | - |
| T1053.006 | Systemd Timers | Systemd Timers | T1053 | ./T1053/T1053.006-Systemd-Timers.md | 📝 | - |
| T1053.007 | Container Orchestration Job | 容器编排作业 | T1053 | ./T1053/T1053.007-Container-Orchestration-Job.md | 📝 | - |
| T1569.001 | Launchctl | Launchctl | T1569 | ./T1569/T1569.001-Launchctl.md | 📝 | - |
| T1569.002 | Service Execution | 服务执行 | T1569 | ./T1569/T1569.002-Service-Execution.md | 📝 | - |
| T1569.003 | Systemctl | Systemctl | T1569 | ./T1569/T1569.003-Systemctl.md | 📝 | - |
| T1127.001 | MSBuild | MSBuild | T1127 | ./T1127/T1127.001-MSBuild.md | 📝 | - |
| T1127.002 | ClickOnce | ClickOnce | T1127 | ./T1127/T1127.002-ClickOnce.md | 📝 | - |
| T1127.003 | JamPlus | JamPlus | T1127 | ./T1127/T1127.003-JamPlus.md | 📝 | - |
| T1204.001 | Malicious Link | 恶意链接 | T1204 | ./T1204/T1204.001-Malicious-Link.md | 📝 | - |
| T1204.002 | Malicious File | 恶意文件 | T1204 | ./T1204/T1204.002-Malicious-File.md | 📝 | - |
| T1204.003 | Malicious Image | 恶意图片/镜像 | T1204 | ./T1204/T1204.003-Malicious-Image.md | 📝 | - |
| T1204.004 | Malicious Copy and Paste | 恶意复制粘贴 | T1204 | ./T1204/T1204.004-Malicious-Copy-And-Paste.md | 📝 | 🔄 本地名: Malicious Copy And Paste |
| T1204.005 | Malicious Library | 恶意库 | T1204 | ./T1204/T1204.005-Malicious-Library.md | 📝 | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v20已撤销或迁移

## 缺失与不一致清单

### 名称不一致 (10 项)
- **T1559** (parent): 官方=`Inter-Process Communication` vs 本地=`Inter Process Communication`
- **T1053** (parent): 官方=`Scheduled Task/Job` vs 本地=`Scheduled Task Job`
- **T1059.010** (subtech): 官方=`AutoHotKey & AutoIT` vs 本地=`AutoHotKey AutoIT`
- **T1059.013** (subtech): 官方=`Container CLI/API` vs 本地=`Container CLI API`
- **T1574.007** (subtech): 官方=`Path Interception by PATH Environment Variable` vs 本地=`Path Interception By PATH Environment Variable`
- **T1574.008** (subtech): 官方=`Path Interception by Search Order Hijacking` vs 本地=`Path Interception By Search Order Hijacking`
- **T1574.009** (subtech): 官方=`Path Interception by Unquoted Path` vs 本地=`Path Interception By Unquoted Path`
- **T1574.013** (subtech): 官方=`KernelCallbackTable` vs 本地=`Kernelcallbacktable`
- **T1574.014** (subtech): 官方=`AppDomainManager` vs 本地=`Appdomainmanager`
- **T1204.004** (subtech): 官方=`Malicious Copy and Paste` vs 本地=`Malicious Copy And Paste`

## 参考来源

- [MITRE ATT&CK - TA0002](https://attack.mitre.org/tactics/TA0002/)
- [MITRE ATT&CK STIX Data v20](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-10-22
