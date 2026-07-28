# TA0005 隐蔽 - 官方数据与本地文件映射表

## 概述

本文件记录 MITRE ATT&CK v19.1 中 TA0005 (Stealth/隐蔽) 战术的
官方技术清单与本地知识库文件的对应关系，用于完整性审计和补全指引。

- **官方版本**：MITRE ATT&CK Enterprise v19.1
- **官方数据**：30 项父技术 / 118 项子技术
- **本地数据**：30 项父技术 / 118 项子技术
- **覆盖率**：100.0%

## 父技术映射表

| 技术ID | 官方名称(EN) | 官方名称(CN) | 本地文件路径 | 子技术数(官方/本地) | 状态 | 备注 |
|--------|-------------|-------------|-------------|:-----------------:|:----:|------|
| T1134 | Access Token Manipulation | 访问令牌操纵 | ./T1134-Access-Token-Manipulation.md | 5/5 | ✅ | 子技术数frontmatter=6 |
| T1197 | BITS Jobs | BITS作业 | ./T1197-BITS-Jobs.md | 0/0 | ✅ | - |
| T1612 | Build Image on Host | 在主机上构建镜像 | ./T1612-Build-Image-on-Host.md | 0/0 | ✅ | - |
| T1622 | Debugger Evasion | 调试器规避 | ./T1622-Debugger-Evasion.md | 0/0 | ✅ | - |
| T1678 | Delay Execution | 延迟执行 | ./T1678-Delay-Execution.md | 0/0 | ✅ | - |
| T1140 | Deobfuscate/Decode Files or Information | 去混淆/解码文件或信息 | ./T1140-Deobfuscate-Decode-Files-or-Information.md | 0/0 | ✅ | - |
| T1006 | Direct Volume Access | 直接卷访问 | ./T1006-Direct-Volume-Access.md | 0/0 | ✅ | - |
| T1480 | Execution Guardrails | 执行护栏 | ./T1480-Execution-Guardrails.md | 2/2 | ✅ | - |
| T1211 | Exploitation for Stealth | 隐蔽性利用 | ./T1211-Exploitation-for-Stealth.md | 0/0 | ✅ | - |
| T1564 | Hide Artifacts | 隐藏痕迹 | ./T1564-Hide-Artifacts.md | 14/14 | ✅ | - |
| T1574 | Hijack Execution Flow | 劫持执行流 | ./T1574-Hijack-Execution-Flow.md | 12/12 | ✅ | 子技术数frontmatter=14 |
| T1070 | Indicator Removal | 清除痕迹 | ./T1070-Indicator-Removal.md | 8/8 | ✅ | 子技术数frontmatter=10 |
| T1202 | Indirect Command Execution | 间接命令执行 | ./T1202-Indirect-Command-Execution.md | 0/0 | ✅ | 子技术数frontmatter=4 |
| T1036 | Masquerading | 伪装 | ./T1036-Masquerading.md | 12/12 | ✅ | 子技术数frontmatter=9 |
| T1027 | Obfuscated Files or Information | 混淆文件或信息 | ./T1027-Obfuscated-Files-or-Info.md | 18/18 | ✅ | 子技术数frontmatter=14 |
| T1542 | Pre-OS Boot | 引导前启动 | ./T1542-Pre-OS-Boot.md | 5/5 | ✅ | - |
| T1055 | Process Injection | 进程注入 | ./T1055-Process-Injection.md | 12/12 | ✅ | - |
| T1620 | Reflective Code Loading | 反射式代码加载 | ./T1620-Reflective-Code-Loading.md | 0/0 | ✅ | - |
| T1014 | Rootkit | Rootkit | ./T1014-Rootkit.md | 0/0 | ✅ | - |
| T1679 | Selective Exclusion | 选择性排除 | ./T1679-Selective-Exclusion.md | 0/0 | ✅ | - |
| T1684 | Social Engineering | 社会工程 | ./T1684-Social-Engineering.md | 2/2 | ✅ | - |
| T1218 | System Binary Proxy Execution | 系统二进制代理执行 | ./T1218-System-Binary-Proxy-Execution.md | 14/14 | ✅ | 子技术数frontmatter=10 |
| T1216 | System Script Proxy Execution | 系统脚本代理执行 | ./T1216-System-Script-Proxy-Execution.md | 2/2 | ✅ | - |
| T1221 | Template Injection | 模板注入 | ./T1221-Template-Injection.md | 0/0 | ✅ | - |
| T1205 | Traffic Signaling | 流量信令 | ./T1205-Traffic-Signaling.md | 2/2 | ✅ | - |
| T1127 | Trusted Developer Utilities Proxy Execution | 受信任的开发者实用程序代理执行 | ./T1127-Trusted-Developer-Utilities-Proxy-Execution.md | 3/3 | ✅ | - |
| T1535 | Unused/Unsupported Cloud Regions | 未使用/不支持的云区域 | ./T1535-Unused-or-Unsupported-Cloud-Regions.md | 0/0 | ✅ | - |
| T1078 | Valid Accounts | 有效账户 | ./T1078-Valid-Accounts.md | 4/4 | ✅ | 子技术数frontmatter=5 |
| T1497 | Virtualization/Sandbox Evasion | 虚拟化/沙箱逃逸 | ./T1497-Virtualization-Sandbox-Evasion.md | 3/3 | ✅ | - |
| T1220 | XSL Script Processing | XSL脚本处理 | ./T1220-XSL-Script-Processing.md | 0/0 | ✅ | - |

## 子技术映射表

| 子技术ID | 官方名称(EN) | 官方名称(CN) | 父技术 | 本地文件路径 | 状态 | 备注 |
|---------|-------------|-------------|--------|-------------|:----:|------|
| T1134.001 | Token Impersonation/Theft | 令牌窃取/复制 | T1134 | ./T1134/T1134.001-Token-Impersonation-theft.md | ✅ | - |
| T1134.002 | Create Process with Token | 创建进程带令牌 | T1134 | ./T1134/T1134.002-Create-Process-with-Token.md | ✅ | - |
| T1134.003 | Make and Impersonate Token | 模拟令牌 | T1134 | ./T1134/T1134.003-Make-And-Impersonate-Token.md | ✅ | - |
| T1134.004 | Parent PID Spoofing | 父进程PID欺骗 | T1134 | ./T1134/T1134.004-Parent-PID-Spoofing.md | ✅ | - |
| T1134.005 | SID-History Injection | SID-History注入 | T1134 | ./T1134/T1134.005-SID-History-Injection.md | ✅ | - |
| T1480.001 | Environmental Keying | 环境密钥 | T1480 | ./T1480/T1480.001-Environmental-Keying.md | ✅ | - |
| T1480.002 | Mutual Exclusion | 时间段延迟执行 | T1480 | ./T1480/T1480.002-Mutual-Exclusion.md | ✅ | - |
| T1564.001 | Hidden Files and Directories | 隐藏文件和目录 | T1564 | ./T1564/T1564.001-Hidden-Files-and-Directories.md | ✅ | - |
| T1564.002 | Hidden Users | 隐藏用户 | T1564 | ./T1564/T1564.002-Hidden-Users.md | ✅ | - |
| T1564.003 | Hidden Window | 隐藏窗口 | T1564 | ./T1564/T1564.003-Hidden-Window.md | ✅ | - |
| T1564.004 | NTFS File Attributes | NTFS文件属性 | T1564 | ./T1564/T1564.004-NTFS-File-Attributes.md | ✅ | - |
| T1564.005 | Hidden File System | 隐藏文件系统 | T1564 | ./T1564/T1564.005-Hidden-File-System.md | ✅ | - |
| T1564.006 | Run Virtual Instance | 运行虚拟实例 | T1564 | ./T1564/T1564.006-Run-Virtual-Instance.md | ✅ | - |
| T1564.007 | VBA Stomping | VBA隐藏 | T1564 | ./T1564/T1564.007-VBA-Stomping.md | ✅ | - |
| T1564.008 | Email Hiding Rules | 邮箱隐藏规则 | T1564 | ./T1564/T1564.008-Email-Hiding-Rules.md | ✅ | - |
| T1564.009 | Resource Forking | 资源派生 | T1564 | ./T1564/T1564.009-Resource-Forking.md | ✅ | - |
| T1564.010 | Process Argument Spoofing | 进程参数欺骗 | T1564 | ./T1564/T1564.010-Process-Argument-Spoofing.md | ✅ | - |
| T1564.011 | Ignore Process Interrupts | 忽略进程中断 | T1564 | ./T1564/T1564.011-Ignore-Process-Interrupts.md | ✅ | - |
| T1564.012 | File/Path Exclusions | 文件/路径排除 | T1564 | ./T1564/T1564.012-File-Path-Exclusions.md | ✅ | - |
| T1564.013 | Bind Mounts | 邮件隔离绕过 | T1564 | ./T1564/T1564.013-Bind-Mounts.md | ✅ | - |
| T1564.014 | Extended Attributes | 通行证条目 | T1564 | ./T1564/T1564.014-Extended-Attributes.md | ✅ | - |
| T1574.001 | DLL | DLL搜索顺序劫持 | T1574 | ./T1574/T1574.001-DLL.md | ✅ | - |
| T1574.004 | Dylib Hijacking | Dylib劫持 | T1574 | ./T1574/T1574.004-Dylib-Hijacking.md | ✅ | - |
| T1574.005 | Executable Installer File Permissions Weakness | 可执行安装程序文件权限弱点 | T1574 | ./T1574/T1574.005-Executable-Installer-File-Permissions-Weakness.md | ✅ | - |
| T1574.006 | Dynamic Linker Hijacking | 动态链接器劫持 | T1574 | ./T1574/T1574.006-Dynamic-Linker-Hijacking.md | ✅ | - |
| T1574.007 | Path Interception by PATH Environment Variable | PATH劫持 | T1574 | ./T1574/T1574.007-Path-Interception-By-PATH-Environment-Variable.md | ✅ | - |
| T1574.008 | Path Interception by Search Order Hijacking | 搜索顺序劫持 | T1574 | ./T1574/T1574.008-Path-Interception-By-Search-Order-Hijacking.md | ✅ | - |
| T1574.009 | Path Interception by Unquoted Path | 未引用路径劫持 | T1574 | ./T1574/T1574.009-Path-Interception-By-Unquoted-Path.md | ✅ | - |
| T1574.010 | Services File Permissions Weakness | 服务权限劫持 | T1574 | ./T1574/T1574.010-Services-File-Permissions-Weakness.md | ✅ | - |
| T1574.011 | Services Registry Permissions Weakness | 服务注册表权限弱点 | T1574 | ./T1574/T1574.011-Services-Registry-Permissions-Weakness.md | ✅ | - |
| T1574.012 | COR_PROFILER | COR_PROFILER劫持 | T1574 | ./T1574/T1574.012-COR_PROFILER.md | ✅ | - |
| T1574.013 | KernelCallbackTable | KernelCallbackTable劫持 | T1574 | ./T1574/T1574.013-Kernelcallbacktable.md | ✅ | - |
| T1574.014 | AppDomainManager | AppDomainManager劫持 | T1574 | ./T1574/T1574.014-Appdomainmanager.md | ✅ | - |
| T1070.003 | Clear Command History | 清除命令行历史 | T1070 | ./T1070/T1070.003-Clear-Command-History.md | ✅ | - |
| T1070.004 | File Deletion | 文件删除 | T1070 | ./T1070/T1070.004-File-Deletion.md | ✅ | - |
| T1070.005 | Network Share Connection Removal | 网络共享连接移除 | T1070 | ./T1070/T1070.005-Network-Share-Connection-Removal.md | 📝 | - |
| T1070.006 | Timestomp | 时间戳篡改 | T1070 | ./T1070/T1070.006-Timestomp.md | ✅ | - |
| T1070.007 | Clear Network Connection History and Configurations | 网络连接历史清除 | T1070 | ./T1070/T1070.007-Clear-Network-Connection-History-And-Configurations.md | ✅ | - |
| T1070.008 | Clear Mailbox Data | 邮件日志清除 | T1070 | ./T1070/T1070.008-Clear-Mailbox-Data.md | ✅ | - |
| T1070.009 | Clear Persistence | 清除持久化 | T1070 | ./T1070/T1070.009-Clear-Persistence.md | 📝 | - |
| T1070.010 | Relocate Malware | 恶意软件重定位 | T1070 | ./T1070/T1070.010-Relocate-Malware.md | 📝 | - |
| T1036.001 | Invalid Code Signature | 无效代码签名 | T1036 | ./T1036/T1036.001-Invalid-Code-Signature.md | ✅ | - |
| T1036.002 | Right-to-Left Override | 从右至左覆盖 | T1036 | ./T1036/T1036.002-Right-to-Left-Override.md | ✅ | - |
| T1036.003 | Rename Legitimate Utilities | 重命名系统工具 | T1036 | ./T1036/T1036.003-Rename-Legitimate-Utilities.md | ✅ | - |
| T1036.004 | Masquerade Task or Service | 伪装任务/服务 | T1036 | ./T1036/T1036.004-Masquerade-Task-Or-Service.md | ✅ | - |
| T1036.005 | Match Legitimate Resource Name or Location | 匹配合法名称/位置 | T1036 | ./T1036/T1036.005-Match-Legitimate-Resource-Name-Or-Location.md | ✅ | - |
| T1036.006 | Space after Filename | 文件名后加空格 | T1036 | ./T1036/T1036.006-Space-After-Filename.md | ✅ | 🔄 本地名: Space After Filename |
| T1036.007 | Double File Extension | 双扩展名 | T1036 | ./T1036/T1036.007-Double-File-Extension.md | ✅ | - |
| T1036.008 | Masquerade File Type | 伪装文件类型 | T1036 | ./T1036/T1036.008-Masquerade-File-Type.md | ✅ | - |
| T1036.009 | Break Process Trees | 破坏父映像路径 | T1036 | ./T1036/T1036.009-Break-Process-Trees.md | ✅ | - |
| T1036.010 | Masquerade Account Name |  | T1036 | ./T1036/T1036.010-Masquerade-Account-Name.md | 📝 | - |
| T1036.011 | Overwrite Process Arguments |  | T1036 | ./T1036/T1036.011-Overwrite-Process-Arguments.md | 📝 | - |
| T1036.012 | Browser Fingerprint |  | T1036 | ./T1036/T1036.012-Browser-Fingerprint.md | 📝 | - |
| T1027.001 | Binary Padding | 二进制填充 | T1027 | ./T1027/T1027.001-Binary-Padding.md | ✅ | - |
| T1027.002 | Software Packing | 软件加壳 | T1027 | ./T1027/T1027.002-Software-Packing.md | ✅ | - |
| T1027.003 | Steganography | 隐写术 | T1027 | ./T1027/T1027.003-Steganography.md | ✅ | - |
| T1027.004 | Compile After Delivery | 交付后编译 | T1027 | ./T1027/T1027.004-Compile-After-Delivery.md | ✅ | - |
| T1027.005 | Indicator Removal from Tools | 工具中的指示器移除 | T1027 | ./T1027/T1027.005-Indicator-Removal-from-Tools.md | ✅ | - |
| T1027.006 | HTML Smuggling | HTML走私 | T1027 | ./T1027/T1027.006-HTML-Smuggling.md | ✅ | - |
| T1027.007 | Dynamic API Resolution | 动态API解析 | T1027 | ./T1027/T1027.007-Dynamic-API-Resolution.md | ✅ | - |
| T1027.008 | Stripped Payloads | 剥离载荷 | T1027 | ./T1027/T1027.008-Stripped-Payloads.md | 📝 | - |
| T1027.009 | Embedded Payloads | 嵌入式载荷 | T1027 | ./T1027/T1027.009-Embedded-Payloads.md | 📝 | - |
| T1027.010 | Command Obfuscation | 命令混淆 | T1027 | ./T1027/T1027.010-Command-Obfuscation.md | ✅ | - |
| T1027.011 | Fileless Storage | 无文件存储 | T1027 | ./T1027/T1027.011-Fileless-Storage.md | 📝 | - |
| T1027.012 | LNK Icon Smuggling | LNK 图标走私 | T1027 | ./T1027/T1027.012-LNK-Icon-Smuggling.md | 📝 | - |
| T1027.013 | Encrypted/Encoded File | 加密/编码 | T1027 | ./T1027/T1027.013-Encrypted-encoded-File.md | ✅ | - |
| T1027.014 | Polymorphic Code | 多态代码 | T1027 | ./T1027/T1027.014-Polymorphic-Code.md | 📝 | - |
| T1027.015 | Compression | 压缩 | T1027 | ./T1027/T1027.015-Compression.md | 📝 | - |
| T1027.016 | Junk Code Insertion | 垃圾数据 | T1027 | ./T1027/T1027.016-Junk-Code-Insertion.md | ✅ | - |
| T1027.017 | SVG Smuggling | SVG走私 | T1027 | ./T1027/T1027.017-SVG-Smuggling.md | 📝 | - |
| T1027.018 | Invisible Unicode | 不可见Unicode字符 | T1027 | ./T1027/T1027.018-Invisible-Unicode.md | 📝 | - |
| T1542.001 | System Firmware | 系统固件 | T1542 | ./T1542/T1542.001-System-Firmware.md | ✅ | - |
| T1542.002 | Component Firmware | 组件固件 | T1542 | ./T1542/T1542.002-Component-Firmware.md | ✅ | - |
| T1542.003 | Bootkit | 主引导记录 | T1542 | ./T1542/T1542.003-Bootkit.md | ✅ | - |
| T1542.004 | ROMMONkit | ROMMON 工具包 | T1542 | ./T1542/T1542.004-ROMMONkit.md | 📝 | - |
| T1542.005 | TFTP Boot | TFTP 启动 | T1542 | ./T1542/T1542.005-TFTP-Boot.md | 📝 | - |
| T1055.001 | Dynamic-link Library Injection | DLL注入 | T1055 | ./T1055/T1055.001-Dynamic-link-Library-Injection.md | ✅ | - |
| T1055.002 | Portable Executable Injection | PE注入 | T1055 | ./T1055/T1055.002-Portable-Executable-Injection.md | ✅ | - |
| T1055.003 | Thread Execution Hijacking | 线程执行劫持 | T1055 | ./T1055/T1055.003-Thread-Execution-Hijacking.md | ✅ | - |
| T1055.004 | Asynchronous Procedure Call | 异步过程调用 | T1055 | ./T1055/T1055.004-Asynchronous-Procedure-Call.md | ✅ | - |
| T1055.005 | Thread Local Storage | 线程本地存储 | T1055 | ./T1055/T1055.005-Thread-Local-Storage.md | ✅ | - |
| T1055.008 | Ptrace System Calls | Ptrace系统调用 | T1055 | ./T1055/T1055.008-Ptrace-System-Calls.md | 📝 | - |
| T1055.009 | Proc Memory | Proc内存 | T1055 | ./T1055/T1055.009-Proc-Memory.md | 📝 | - |
| T1055.011 | Extra Window Memory Injection | 额外窗口内存注入 | T1055 | ./T1055/T1055.011-Extra-Window-Memory-Injection.md | 📝 | - |
| T1055.012 | Process Hollowing | 进程镂空 | T1055 | ./T1055/T1055.012-Process-Hollowing.md | ✅ | - |
| T1055.013 | Process Doppelgänging | 进程双胞胎 | T1055 | ./T1055/T1055.013-Process-Doppelgänging.md | ✅ | - |
| T1055.014 | VDSO Hijacking | VDSO劫持 | T1055 | ./T1055/T1055.014-VDSO-Hijacking.md | ✅ | - |
| T1055.015 | ListPlanting |  | T1055 | ./T1055/T1055.015-Listplanting.md | 📝 | - |
| T1684.001 | Impersonation | 伪装身份 | T1684 | ./T1684/T1684.001-Impersonation.md | ✅ | - |
| T1684.002 | Email Spoofing | 邮件伪造 | T1684 | ./T1684/T1684.002-Email-Spoofing.md | ✅ | - |
| T1218.001 | Compiled HTML File | 编译HTML帮助文件 | T1218 | ./T1218/T1218.001-Compiled-HTML-File.md | ✅ | - |
| T1218.002 | Control Panel | 控制面板 | T1218 | ./T1218/T1218.002-Control-Panel.md | ✅ | - |
| T1218.003 | CMSTP | 连接管理器配置文件安装程序 | T1218 | ./T1218/T1218.003-CMSTP.md | ✅ | - |
| T1218.004 | InstallUtil | InstallUtil | T1218 | ./T1218/T1218.004-InstallUtil.md | ✅ | - |
| T1218.005 | Mshta | Mshta | T1218 | ./T1218/T1218.005-Mshta.md | ✅ | - |
| T1218.007 | Msiexec | Msiexec | T1218 | ./T1218/T1218.007-Msiexec.md | ✅ | - |
| T1218.008 | Odbcconf | ODBC配置工具 | T1218 | ./T1218/T1218.008-Odbcconf.md | ✅ | - |
| T1218.009 | Regsvcs/Regasm | Regsvcs/Regasm | T1218 | ./T1218/T1218.009-Regsvcs-Or-Regasm.md | ✅ | - |
| T1218.010 | Regsvr32 | Regsvr32 | T1218 | ./T1218/T1218.010-Regsvr32.md | ✅ | - |
| T1218.011 | Rundll32 | Rundll32 | T1218 | ./T1218/T1218.011-Rundll32.md | ✅ | - |
| T1218.012 | Verclsid | Verclsid | T1218 | ./T1218/T1218.012-Verclsid.md | 📝 | - |
| T1218.013 | Mavinject | Mavinject | T1218 | ./T1218/T1218.013-Mavinject.md | 📝 | - |
| T1218.014 | MMC | MMC控制台 | T1218 | ./T1218/T1218.014-MMC.md | ✅ | - |
| T1218.015 | Electron Applications | Electron 应用程序 | T1218 | ./T1218/T1218.015-Electron-Applications.md | 📝 | - |
| T1216.001 | PubPrn | PubPrn | T1216 | ./T1216/T1216.001-PubPrn.md | ✅ | - |
| T1216.002 | SyncAppvPublishingServer | SyncAppvPublishingServer | T1216 | ./T1216/T1216.002-SyncAppvPublishingServer.md | ✅ | - |
| T1205.001 | Port Knocking | 端口敲击 | T1205 | ./T1205/T1205.001-Port-Knocking.md | ✅ | - |
| T1205.002 | Socket Filters | 套接字过滤器 | T1205 | ./T1205/T1205.002-Socket-Filters.md | ✅ | - |
| T1127.001 | MSBuild | MSBuild | T1127 | ./T1127/T1127.001-MSBuild.md | ✅ | - |
| T1127.002 | ClickOnce | ClickOnce | T1127 | ./T1127/T1127.002-ClickOnce.md | ✅ | - |
| T1127.003 | JamPlus | JamPlus | T1127 | ./T1127/T1127.003-JamPlus.md | ✅ | - |
| T1078.001 | Default Accounts | 默认账户 | T1078 | ./T1078/T1078.001-Default-Accounts.md | ✅ | - |
| T1078.002 | Domain Accounts | 域账户 | T1078 | ./T1078/T1078.002-Domain-Accounts.md | ✅ | - |
| T1078.003 | Local Accounts | 本地账户 | T1078 | ./T1078/T1078.003-Local-Accounts.md | ✅ | - |
| T1078.004 | Cloud Accounts | 云账户 | T1078 | ./T1078/T1078.004-Cloud-Accounts.md | ✅ | - |
| T1497.001 | System Checks | 系统时间检测 | T1497 | ./T1497/T1497.001-System-Checks.md | ✅ | - |
| T1497.002 | User Activity Based Checks | 用户活动检测 | T1497 | ./T1497/T1497.002-User-Activity-Based-Checks.md | ✅ | - |
| T1497.003 | Time Based Checks | 基于时间的规避 | T1497 | ./T1497/T1497.003-Time-Based-Checks.md | ✅ | - |

## 状态图例

- ✅ 已完成：本地文件存在且 frontmatter status 为【已完成】
- 📝 草稿：文件存在但 frontmatter status 非【已完成】
- ❌ 缺失：官方有但本地无文件
- 🔄 名称不一致：本地文件名/EN名与官方不符
- ⚠️ Revoked/迁移：本地有但官方v19.1已撤销或迁移

## 缺失与不一致清单

### 名称不一致 (1 项)
- **T1036.006** (subtech): 官方=`Space after Filename` vs 本地=`Space After Filename`

## 参考来源

- [MITRE ATT&CK - TA0005](https://attack.mitre.org/tactics/TA0005/)
- [MITRE ATT&CK STIX Data v19.1](https://github.com/mitre-attack/attack-stix-data)
- 本地审计时间：2026-07-28
