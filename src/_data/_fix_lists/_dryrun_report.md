======================================================================
ATT&CK 知识库修复报告
======================================================================
日期: 2026-07-27
模式: DRY-RUN

[汇总]
  执行操作: 255
  跳过: 49
  错误: 0

[按类别统计]
  extra_parents: 执行=8, 跳过=0, 错误=0
  extra_subs: 执行=39, 跳过=0, 错误=0
  missing_parents: 执行=6, 跳过=0, 错误=0
  missing_subs: 执行=33, 跳过=0, 错误=0
  name_mismatch_parents: 执行=8, 跳过=0, 错误=0
  name_mismatch_subs: 执行=161, 跳过=49, 错误=0

[详细操作]
  [DRY-RUN] [missing_parents] CREATE: 03-Initial-Access/T1133-External-Remote-Services.md (External Remote Services)
  [DRY-RUN] [missing_parents] CREATE: 05-Persistence/T1112-Modify-Registry.md (Modify Registry)
  [DRY-RUN] [missing_parents] CREATE: 10-Discovery/T1040-Network-Sniffing.md (Network Sniffing)
  [DRY-RUN] [missing_parents] CREATE: 11-Lateral-Movement/T1091-Replication-Through-Removable-Media.md (Replication Through Removable Media)
  [DRY-RUN] [missing_parents] CREATE: 11-Lateral-Movement/T1072-Software-Deployment-Tools.md (Software Deployment Tools)
  [DRY-RUN] [missing_parents] CREATE: 13-Command-and-Control/T1659-Content-Injection.md (Content Injection)
  [DRY-RUN] [extra_parents] REVOKE: 05-Persistence/T1050-New-Service.md (T1050)
  [DRY-RUN] [extra_parents] REVOKE: 05-Persistence/T1108-Redundant-Access.md (T1108)
  [DRY-RUN] [extra_parents] REVOKE: 05-Persistence/T1574-Hijack-Execution-Flow.md (T1574)
  [DRY-RUN] [extra_parents] REVOKE: 09-Credential-Access/T1141-Input-Prompt.md (T1141)
  [DRY-RUN] [extra_parents] REVOKE: 09-Credential-Access/T1503-Credentials-from-Web-Browsers.md (T1503)
  [DRY-RUN] [extra_parents] REVOKE: 09-Credential-Access/T1550-Use-Alternate-Authentication-Material.md (T1550)
  [DRY-RUN] [extra_parents] REVOKE: 11-Lateral-Movement/T1051-Shared-Webroot.md (T1051)
  [DRY-RUN] [extra_parents] REVOKE: 11-Lateral-Movement/T1207-Rogue-Domain-Controller.md (T1207)
  [DRY-RUN] [name_mismatch_parents] UPDATE_NAME: 01-Reconnaissance/T1591-Gather-Victim-Org-Information.md (仅更新 attack_name_en: Gather Victim Org Information)
  [DRY-RUN] [name_mismatch_parents] RENAME: 05-Persistence/T1554-Compromise-Client-Software-Binary.md → 05-Persistence/T1554-Compromise-Host-Software-Binary.md (Compromise Host Software Binary)
  [DRY-RUN] [name_mismatch_parents] UPDATE_NAME: 05-Persistence/T1176-Software-Extensions.md (仅更新 attack_name_en: Software Extensions)
  [DRY-RUN] [name_mismatch_parents] RENAME: 08-Defense-Impairment/T1222-File-Permissions-Modification.md → 08-Defense-Impairment/T1222-File-And-Directory-Permissions-Modification.md (File and Directory Permissions Modification)
  [DRY-RUN] [name_mismatch_parents] RENAME: 10-Discovery/T1217-Browser-Bookmark-Discovery.md → 10-Discovery/T1217-Browser-Information-Discovery.md (Browser Information Discovery)
  [DRY-RUN] [name_mismatch_parents] RENAME: 10-Discovery/T1046-Network-Service-Scanning.md → 10-Discovery/T1046-Network-Service-Discovery.md (Network Service Discovery)
  [DRY-RUN] [name_mismatch_parents] RENAME: 13-Command-and-Control/T1090-Proxying.md → 13-Command-and-Control/T1090-Proxy.md (Proxy)
  [DRY-RUN] [name_mismatch_parents] UPDATE_NAME: 13-Command-and-Control/T1219-Remote-Access-Tools.md (仅更新 attack_name_en: Remote Access Tools)
  [DRY-RUN] [missing_subs] CREATE: 05-Persistence/T1505/T1505.006-Vsphere-Installation-Bundles.md (vSphere Installation Bundles)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1548/T1548.005-Temporary-Elevated-Cloud-Access.md (Temporary Elevated Cloud Access)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1548/T1548.006-TCC-Manipulation.md (TCC Manipulation)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1547/T1547.015-Login-Items.md (Login Items)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1543/T1543.005-Container-Service.md (Container Service)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1546/T1546.013-Powershell-Profile.md (PowerShell Profile)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1546/T1546.014-Emond.md (Emond)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1546/T1546.015-Component-Object-Model-Hijacking.md (Component Object Model Hijacking)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1546/T1546.016-Installer-Packages.md (Installer Packages)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1546/T1546.017-Udev-Rules.md (Udev Rules)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1546/T1546.018-Python-Startup-Hooks.md (Python Startup Hooks)
  [DRY-RUN] [missing_subs] CREATE: 06-Privilege-Escalation/T1055/T1055.015-Listplanting.md (ListPlanting)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1036/T1036.010-Masquerade-Account-Name.md (Masquerade Account Name)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1036/T1036.011-Overwrite-Process-Arguments.md (Overwrite Process Arguments)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1036/T1036.012-Browser-Fingerprint.md (Browser Fingerprint)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1027/T1027.015-Compression.md (Compression)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1027/T1027.016-Junk-Code-Insertion.md (Junk Code Insertion)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1027/T1027.017-SVG-Smuggling.md (SVG Smuggling)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1027/T1027.018-Invisible-Unicode.md (Invisible Unicode)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1055/T1055.013-Process-Doppelgänging.md (Process Doppelgänging)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1055/T1055.014-VDSO-Hijacking.md (VDSO Hijacking)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1055/T1055.015-Listplanting.md (ListPlanting)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1218/T1218.010-Regsvr32.md (Regsvr32)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1218/T1218.012-Verclsid.md (Verclsid)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1218/T1218.013-Mavinject.md (Mavinject)
  [DRY-RUN] [missing_subs] CREATE: 07-Stealth/T1218/T1218.015-Electron-Applications.md (Electron Applications)
  [DRY-RUN] [missing_subs] CREATE: 12-Collection/T1557/T1557.004-Evil-Twin.md (Evil Twin)
  [DRY-RUN] [missing_subs] CREATE: 12-Collection/T1213/T1213.005-Messaging-Applications.md (Messaging Applications)
  [DRY-RUN] [missing_subs] CREATE: 12-Collection/T1213/T1213.006-Databases.md (Databases)
  [DRY-RUN] [missing_subs] CREATE: 13-Command-and-Control/T1090/T1090.004-Domain-Fronting.md (Domain Fronting)
  [DRY-RUN] [missing_subs] CREATE: 13-Command-and-Control/T1219/T1219.001-IDE-Tunneling.md (IDE Tunneling)
  [DRY-RUN] [missing_subs] CREATE: 13-Command-and-Control/T1219/T1219.002-Remote-Desktop-Software.md (Remote Desktop Software)
  [DRY-RUN] [missing_subs] CREATE: 13-Command-and-Control/T1219/T1219.003-Remote-Access-Hardware.md (Remote Access Hardware)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1053/T1053.001-At-Windows.md (T1053.001)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.001-DLL-Search-Order-Hijacking.md (T1574.001)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.002-DLL-Side-Loading.md (T1574.002)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.004-Dylib-Hijacking.md (T1574.004)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.005-Executable-Installer-File-Permissions-Weakness.md (T1574.005)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.006-Dynamic-Linker-Hijacking.md (T1574.006)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.007-Path-Interception-by-PATH-Environment-Variable.md (T1574.007)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.008-Search-Order-Interception.md (T1574.008)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.009-Unquoted-Path-Interception.md (T1574.009)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.010-Service-File-Permissions-Weakness.md (T1574.010)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.011-PLAT-Android.md (T1574.011)
  [DRY-RUN] [extra_subs] REVOKE: 05-Persistence/T1574/T1574.012-COR-PROFILER.md (T1574.012)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1053/T1053.001-At-Windows.md (T1053.001)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1055/T1055.007-Ptrace-System-Calls.md (T1055.007)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1055/T1055.010-Process-Hollowing.md (T1055.010)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1484/T1484.003-Cloud-Policy-Modification.md (T1484.003)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1484/T1484.004-Cloud-Implicit-Trust-Modification.md (T1484.004)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1547/T1547.011-Print-Processors.md (T1547.011)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1611/T1611.001-Virtual-Machine-Escape.md (T1611.001)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1611/T1611.002-Container-Escape.md (T1611.002)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1611/T1611.003-Application-Sandbox-Escape.md (T1611.003)
  [DRY-RUN] [extra_subs] REVOKE: 06-Privilege-Escalation/T1611/T1611.004-Hardware-Peripheral-Escape.md (T1611.004)
  [DRY-RUN] [extra_subs] REVOKE: 07-Stealth/T1055/T1055.006-Ptrace-System-Calls.md (T1055.006)
  [DRY-RUN] [extra_subs] REVOKE: 07-Stealth/T1055/T1055.007-Proc-Memory.md (T1055.007)
  [DRY-RUN] [extra_subs] REVOKE: 07-Stealth/T1055/T1055.010-Extra-Window-Memory-Injection.md (T1055.010)
  [DRY-RUN] [extra_subs] REVOKE: 07-Stealth/T1070/T1070.001-Clear-Application-Event-Log.md (T1070.001)
  [DRY-RUN] [extra_subs] REVOKE: 07-Stealth/T1070/T1070.002-Clear-Windows-Event-Logs.md (T1070.002)
  [DRY-RUN] [extra_subs] REVOKE: 07-Stealth/T1078/T1078.005-Application-Accounts.md (T1078.005)
  [DRY-RUN] [extra_subs] REVOKE: 07-Stealth/T1134/T1134.006-Elevate-Token-Privileges.md (T1134.006)
  [DRY-RUN] [extra_subs] REVOKE: 07-Stealth/T1574/T1574.002-DLL-Side-Loading.md (T1574.002)
  [DRY-RUN] [extra_subs] REVOKE: 07-Stealth/T1574/T1574.003-DLL-Hijacking.md (T1574.003)
  [DRY-RUN] [extra_subs] REVOKE: 09-Credential-Access/T1550/T1550.001-Application-Access-Token.md (T1550.001)
  [DRY-RUN] [extra_subs] REVOKE: 09-Credential-Access/T1550/T1550.002-Pass-the-Hash.md (T1550.002)
  [DRY-RUN] [extra_subs] REVOKE: 09-Credential-Access/T1550/T1550.003-Pass-the-Ticket.md (T1550.003)
  [DRY-RUN] [extra_subs] REVOKE: 09-Credential-Access/T1550/T1550.004-Web-Session-Cookie.md (T1550.004)
  [DRY-RUN] [extra_subs] REVOKE: 10-Discovery/T1016/T1016.003-Workstation-Discovery.md (T1016.003)
  [DRY-RUN] [extra_subs] REVOKE: 12-Collection/T1114/T1114.004-Email-Forwarding-Rule.md (T1114.004)
  [DRY-RUN] [extra_subs] REVOKE: 13-Command-and-Control/T1001/T1001.004-Mirror-Rebound.md (T1001.004)
  [DRY-RUN] [extra_subs] REVOKE: 14-Exfiltration/T1052/T1052.002-Air-Gap-Exfiltration.md (T1052.002)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1595/T1595.001-Scan-IP-Blocks.md → T1595/T1595.001-Scanning-IP-Blocks.md (Scanning IP Blocks)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1589/T1589.001-Credential-Collection.md → T1589/T1589.001-Credentials.md (Credentials)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1589/T1589.002-Email-Address-Collection.md → T1589/T1589.002-Email-Addresses.md (Email Addresses)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1589/T1589.003-Employee-Name-Collection.md → T1589/T1589.003-Employee-Names.md (Employee Names)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1591/T1591.001-Physical-Locations.md → T1591/T1591.001-Determine-Physical-Locations.md (Determine Physical Locations)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1591/T1591.003-Business-Rhythms.md → T1591/T1591.003-Identify-Business-Tempo.md (Identify Business Tempo)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1598/T1598.001-Service-Phishing.md → T1598/T1598.001-Spearphishing-Service.md (Spearphishing Service)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1598/T1598.002-Attachment-Phishing.md → T1598/T1598.002-Spearphishing-Attachment.md (Spearphishing Attachment)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1598/T1598.003-Link-Phishing.md → T1598/T1598.003-Spearphishing-Link.md (Spearphishing Link)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1598/T1598.004-Voice-Phishing.md → T1598/T1598.004-Spearphishing-Voice.md (Spearphishing Voice)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1596/T1596.004-CDN.md → T1596/T1596.004-Cdns.md (CDNs)
  [DRY-RUN] [name_mismatch_subs] RENAME: 01-Reconnaissance/T1593/T1593.003-Code-Repository.md → T1593/T1593.003-Code-Repositories.md (Code Repositories)
  [DRY-RUN] [name_mismatch_subs] RENAME: 02-Resource-Development/T1586/T1586.003-Cloud-Account.md → T1586/T1586.003-Cloud-Accounts.md (Cloud Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 02-Resource-Development/T1585/T1585.003-Cloud-Account.md → T1585/T1585.003-Cloud-Accounts.md (Cloud Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 02-Resource-Development/T1683/T1683.002-Audio-Video-Content.md → T1683/T1683.002-Audio-visual-Content.md (Audio-Visual Content)
  [DRY-RUN] [name_mismatch_subs] RENAME: 02-Resource-Development/T1588/T1588.002-Tools.md → T1588/T1588.002-Tool.md (Tool)
  [DRY-RUN] [name_mismatch_subs] RENAME: 02-Resource-Development/T1588/T1588.006-Vulnerability-Information.md → T1588/T1588.006-Vulnerabilities.md (Vulnerabilities)
  [DRY-RUN] [name_mismatch_subs] RENAME: 03-Initial-Access/T1195/T1195.001-Compromise-Software-Dependencies-and-Dev-Tools.md → T1195/T1195.001-Compromise-Software-Dependencies-And-Development-Tools.md (Compromise Software Dependencies and Development Tools)
  [DRY-RUN] [name_mismatch_subs] RENAME: 03-Initial-Access/T1078/T1078.002-Domain-Account.md → T1078/T1078.002-Domain-Accounts.md (Domain Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 03-Initial-Access/T1078/T1078.003-Local-Account.md → T1078/T1078.003-Local-Accounts.md (Local Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 03-Initial-Access/T1078/T1078.004-Cloud-Account.md → T1078/T1078.004-Cloud-Accounts.md (Cloud Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1059/T1059.010-AutoHotKey-and-AutoIT-AutoHotKey-AutoIT.md → T1059/T1059.010-Autohotkey-And-Autoit.md (AutoHotKey & AutoIT)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1059/T1059.012-Container-Administration-CLI.md → T1059/T1059.012-Hypervisor-CLI.md (Hypervisor CLI)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 04-Execution/T1059/T1059.013-Container-CLI-API.md (仅更新 attack_name_en: Container CLI/API)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1574/T1574.001-DLL-Search-Order-Hijacking.md → T1574/T1574.001-DLL.md (DLL)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1574/T1574.007-Path-Hijacking.md → T1574/T1574.007-Path-Interception-By-PATH-Environment-Variable.md (Path Interception by PATH Environment Variable)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1574/T1574.008-Search-Order-Hijacking.md → T1574/T1574.008-Path-Interception-By-Search-Order-Hijacking.md (Path Interception by Search Order Hijacking)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1574/T1574.009-Unquoted-Service-Path.md → T1574/T1574.009-Path-Interception-By-Unquoted-Path.md (Path Interception by Unquoted Path)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1574/T1574.010-Service-Permissions-Hijacking.md → T1574/T1574.010-Services-File-Permissions-Weakness.md (Services File Permissions Weakness)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1574/T1574.012-COR-PROFILER-Hijacking.md → T1574/T1574.012-COR_PROFILER.md (COR_PROFILER)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1574/T1574.013-KernelCallbackTable-Hijacking.md → T1574/T1574.013-Kernelcallbacktable.md (KernelCallbackTable)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1574/T1574.014-AppDomainManager-Hijacking.md → T1574/T1574.014-Appdomainmanager.md (AppDomainManager)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1204/T1204.004-Malicious-Copy-Paste.md → T1204/T1204.004-Malicious-Copy-And-Paste.md (Malicious Copy and Paste)
  [DRY-RUN] [name_mismatch_subs] RENAME: 04-Execution/T1204/T1204.005-Malicious-Libraries.md → T1204/T1204.005-Malicious-Library.md (Malicious Library)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1037/T1037.002-Logon-Script-Mac.md → T1037/T1037.002-Login-Hook.md (Login Hook)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1037/T1037.003-Logon-Script-Linux.md → T1037/T1037.003-Network-Logon-Script.md (Network Logon Script)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1037/T1037.004-Logon-Script-Network.md → T1037/T1037.004-RC-Scripts.md (RC Scripts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1037/T1037.005-Logon-Script-Cross-platform.md → T1037/T1037.005-Startup-Items.md (Startup Items)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1543/T1543.005-Containers.md → T1543/T1543.005-Container-Service.md (Container Service)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1546/T1546.003-WMI-Event-Subscription.md → T1546/T1546.003-Windows-Management-Instrumentation-Event-Subscription.md (Windows Management Instrumentation Event Subscription)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1546/T1546.011-Application-Shim.md → T1546/T1546.011-Application-Shimming.md (Application Shimming)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1546/T1546.012-Image-File-Execution-Options.md → T1546/T1546.012-Image-File-Execution-Options-Injection.md (Image File Execution Options Injection)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 05-Persistence/T1546/T1546.014-Emond.md (仅更新 attack_name_en: Emond)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1546/T1546.015-COM-Hijacking.md → T1546/T1546.015-Component-Object-Model-Hijacking.md (Component Object Model Hijacking)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1556/T1556.002-Password-Filter.md → T1556/T1556.002-Password-Filter-DLL.md (Password Filter DLL)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1556/T1556.005-Multi-Factor-Authentication.md → T1556/T1556.005-Reversible-Encryption.md (Reversible Encryption)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1556/T1556.006-Hybrid-Identity.md → T1556/T1556.006-Multi-factor-Authentication.md (Multi-Factor Authentication)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1556/T1556.007-Hybrid-Identity-Sync.md → T1556/T1556.007-Hybrid-Identity.md (Hybrid Identity)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1556/T1556.009-Conditional-Access-Policy.md → T1556/T1556.009-Conditional-Access-Policies.md (Conditional Access Policies)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1137/T1137.002-Office-Add-ins.md → T1137/T1137.002-Office-Test.md (Office Test)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1137/T1137.006-Outlook-API.md → T1137/T1137.006-Add-ins.md (Add-ins)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1053/T1053.002-At-Linux.md → T1053/T1053.002-At.md (At)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1053/T1053.005-Scheduled-Task-Windows.md → T1053/T1053.005-Scheduled-Task.md (Scheduled Task)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1505/T1505.005-Terminal-Services.md → T1505/T1505.005-Terminal-Services-DLL.md (Terminal Services DLL)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1176/T1176.001-Microsoft-Office-Add-in.md → T1176/T1176.001-Browser-Extensions.md (Browser Extensions)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1176/T1176.002-Browser-Extensions.md → T1176/T1176.002-IDE-Extensions.md (IDE Extensions)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1078/T1078.002-Domain-Account.md → T1078/T1078.002-Domain-Accounts.md (Domain Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1078/T1078.003-Local-Account.md → T1078/T1078.003-Local-Accounts.md (Local Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 05-Persistence/T1078/T1078.004-Cloud-Account.md → T1078/T1078.004-Cloud-Accounts.md (Cloud Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1547/T1547.001-Registry-Auto-start-Entry.md → T1547/T1547.001-Registry-Run-Keys---Startup-Folder.md (Registry Run Keys / Startup Folder)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1547/T1547.005-Kernel-Modules-and-Extensions.md → T1547/T1547.005-Security-Support-Provider.md (Security Support Provider)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1547/T1547.006-Enable-Startup-Folder.md → T1547/T1547.006-Kernel-Modules-And-Extensions.md (Kernel Modules and Extensions)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1547/T1547.007-Re-open-Applications.md → T1547/T1547.007-Re-opened-Applications.md (Re-opened Applications)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1547/T1547.013-Startup-Agent.md → T1547/T1547.013-XDG-Autostart-Entries.md (XDG Autostart Entries)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1547/T1547.014-Active-Setup-Modification.md → T1547/T1547.014-Active-Setup.md (Active Setup)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1037/T1037.002-Login-Hook-macOS.md → T1037/T1037.002-Login-Hook.md (Login Hook)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1037/T1037.003-Network-Logon-Script-Windows.md → T1037/T1037.003-Network-Logon-Script.md (Network Logon Script)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1037/T1037.004-RC-Scripts-Linux-macOS.md → T1037/T1037.004-RC-Scripts.md (RC Scripts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1037/T1037.005-Startup-Item-macOS.md → T1037/T1037.005-Startup-Items.md (Startup Items)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1546/T1546.003-WMI-Event-Subscription.md → T1546/T1546.003-Windows-Management-Instrumentation-Event-Subscription.md (Windows Management Instrumentation Event Subscription)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1546/T1546.004-bash-profile-and-bashrc.md → T1546/T1546.004-Unix-Shell-Configuration-Modification.md (Unix Shell Configuration Modification)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1546/T1546.005-Application-Initialization.md → T1546/T1546.005-Trap.md (Trap)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1546/T1546.006-Accessibility-Features.md → T1546/T1546.006-LC_LOAD_DYLIB-Addition.md (LC_LOAD_DYLIB Addition)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1546/T1546.011-Application-Shutdown.md → T1546/T1546.011-Application-Shimming.md (Application Shimming)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1546/T1546.012-Security-Support-Provider.md → T1546/T1546.012-Image-File-Execution-Options-Injection.md (Image File Execution Options Injection)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1055/T1055.001-DLL-Injection.md → T1055/T1055.001-Dynamic-link-Library-Injection.md (Dynamic-link Library Injection)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1055/T1055.002-PE-Injection.md → T1055/T1055.002-Portable-Executable-Injection.md (Portable Executable Injection)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1053/T1053.002-At-Linux.md → T1053/T1053.002-At.md (At)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 06-Privilege-Escalation/T1053/T1053.006-Systemd-Timers.md (仅更新 attack_name_en: Systemd Timers)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1078/T1078.002-Domain-Account.md → T1078/T1078.002-Domain-Accounts.md (Domain Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1078/T1078.003-Local-Account.md → T1078/T1078.003-Local-Accounts.md (Local Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 06-Privilege-Escalation/T1078/T1078.004-Cloud-Account.md → T1078/T1078.004-Cloud-Accounts.md (Cloud Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1134/T1134.001-Token-Theft-Duplication.md → T1134/T1134.001-Token-Impersonation-theft.md (Token Impersonation/Theft)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1134/T1134.003-Token-Impersonation.md → T1134/T1134.003-Make-And-Impersonate-Token.md (Make and Impersonate Token)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 07-Stealth/T1134/T1134.005-SID-History-Injection.md (仅更新 attack_name_en: SID-History Injection)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1480/T1480.002-Timed-Delay-Execution.md → T1480/T1480.002-Mutual-Exclusion.md (Mutual Exclusion)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1574/T1574.001-DLL-Search-Order-Hijacking.md → T1574/T1574.001-DLL.md (DLL)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1574/T1574.007-Path-Hijacking.md → T1574/T1574.007-Path-Interception-By-PATH-Environment-Variable.md (Path Interception by PATH Environment Variable)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1574/T1574.008-Search-Order-Hijacking.md → T1574/T1574.008-Path-Interception-By-Search-Order-Hijacking.md (Path Interception by Search Order Hijacking)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1574/T1574.009-Unquoted-Service-Path.md → T1574/T1574.009-Path-Interception-By-Unquoted-Path.md (Path Interception by Unquoted Path)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1574/T1574.010-Service-Permissions-Hijacking.md → T1574/T1574.010-Services-File-Permissions-Weakness.md (Services File Permissions Weakness)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1574/T1574.012-COR-PROFILER-Hijacking.md → T1574/T1574.012-COR_PROFILER.md (COR_PROFILER)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1574/T1574.013-KernelCallbackTable-Hijacking.md → T1574/T1574.013-Kernelcallbacktable.md (KernelCallbackTable)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1574/T1574.014-AppDomainManager-Hijacking.md → T1574/T1574.014-Appdomainmanager.md (AppDomainManager)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1036/T1036.003-Rename-System-Utilities.md → T1036/T1036.003-Rename-Legitimate-Utilities.md (Rename Legitimate Utilities)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1036/T1036.004-Masquerade-Task-Service.md → T1036/T1036.004-Masquerade-Task-Or-Service.md (Masquerade Task or Service)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1036/T1036.005-Match-Legitimate-Name-Location.md → T1036/T1036.005-Match-Legitimate-Resource-Name-Or-Location.md (Match Legitimate Resource Name or Location)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1036/T1036.007-Double-Extension.md → T1036/T1036.007-Double-File-Extension.md (Double File Extension)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1036/T1036.009-Break-Parent-Image-Path.md → T1036/T1036.009-Break-Process-Trees.md (Break Process Trees)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1055/T1055.001-DLL-Injection.md → T1055/T1055.001-Dynamic-link-Library-Injection.md (Dynamic-link Library Injection)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1055/T1055.002-PE-Injection.md → T1055/T1055.002-Portable-Executable-Injection.md (Portable Executable Injection)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1078/T1078.002-Domain-Account.md → T1078/T1078.002-Domain-Accounts.md (Domain Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1078/T1078.003-Local-Account.md → T1078/T1078.003-Local-Accounts.md (Local Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1078/T1078.004-Cloud-Account.md → T1078/T1078.004-Cloud-Accounts.md (Cloud Accounts)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1497/T1497.001-System-Time-Detection.md → T1497/T1497.001-System-Checks.md (System Checks)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1497/T1497.002-User-Activity-Detection.md → T1497/T1497.002-User-Activity-Based-Checks.md (User Activity Based Checks)
  [DRY-RUN] [name_mismatch_subs] RENAME: 07-Stealth/T1497/T1497.003-Time-based-Evasion.md → T1497/T1497.003-Time-Based-Checks.md (Time Based Checks)
  [DRY-RUN] [name_mismatch_subs] RENAME: 08-Defense-Impairment/T1484/T1484.002-Trust-Relationship-Modification.md → T1484/T1484.002-Trust-Modification.md (Trust Modification)
  [DRY-RUN] [name_mismatch_subs] RENAME: 08-Defense-Impairment/T1222/T1222.001-Windows-File-Directory-Permission-Modification.md → T1222/T1222.001-Windows-Permissions.md (Windows Permissions)
  [DRY-RUN] [name_mismatch_subs] RENAME: 08-Defense-Impairment/T1222/T1222.002-Linux-Mac-File-Directory-Permission-Modification.md → T1222/T1222.002-Linux-And-Mac-Permissions.md (Linux and Mac Permissions)
  [DRY-RUN] [name_mismatch_subs] RENAME: 08-Defense-Impairment/T1556/T1556.006-MFA-Manipulation.md → T1556/T1556.006-Multi-factor-Authentication.md (Multi-Factor Authentication)
  [DRY-RUN] [name_mismatch_subs] RENAME: 08-Defense-Impairment/T1553/T1553.001-Code-Signing.md → T1553/T1553.001-Gatekeeper-Bypass.md (Gatekeeper Bypass)
  [DRY-RUN] [name_mismatch_subs] RENAME: 08-Defense-Impairment/T1553/T1553.002-Install-Root-Certificate.md → T1553/T1553.002-Code-Signing.md (Code Signing)
  [DRY-RUN] [name_mismatch_subs] RENAME: 08-Defense-Impairment/T1553/T1553.003-SIP-Trust-Provider-Hijacking.md → T1553/T1553.003-SIP-And-Trust-Provider-Hijacking.md (SIP and Trust Provider Hijacking)
  [DRY-RUN] [name_mismatch_subs] RENAME: 08-Defense-Impairment/T1553/T1553.004-Secure-Boot-Bypass.md → T1553/T1553.004-Install-Root-Certificate.md (Install Root Certificate)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1557/T1557.001-LLMNR-NBT-NS-Poisoning-and-SMB-Relay.md → T1557/T1557.001-Name-Resolution-Poisoning-And-SMB-Relay.md (Name Resolution Poisoning and SMB Relay)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1557/T1557.004-Mutual-Authentication-Impairment.md → T1557/T1557.004-Evil-Twin.md (Evil Twin)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1555/T1555.002-Securityd.md → T1555/T1555.002-Securityd-Memory.md (Securityd Memory)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1555/T1555.003-Web-Browsers.md → T1555/T1555.003-Credentials-From-Web-Browsers.md (Credentials from Web Browsers)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 09-Credential-Access/T1555/T1555.004-Windows-Credential-Manager.md (仅更新 attack_name_en: Windows Credential Manager)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1555/T1555.006-Group-Policies.md → T1555/T1555.006-Cloud-Secrets-Management-Stores.md (Cloud Secrets Management Stores)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1606/T1606.001-SAML-Tokens.md → T1606/T1606.001-Web-Cookies.md (Web Cookies)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1606/T1606.002-OAuth-Tokens.md → T1606/T1606.002-SAML-Tokens.md (SAML Tokens)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 09-Credential-Access/T1556/T1556.001-Domain-Controller-Authentication.md (仅更新 attack_name_en: Domain Controller Authentication)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 09-Credential-Access/T1556/T1556.003-Pluggable-Authentication-Modules.md (仅更新 attack_name_en: Pluggable Authentication Modules)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1556/T1556.009-Conditional-Access-Policy.md → T1556/T1556.009-Conditional-Access-Policies.md (Conditional Access Policies)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1003/T1003.001-LSASS-Memory-Dump.md → T1003/T1003.001-LSASS-Memory.md (LSASS Memory)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1003/T1003.003-NTDS-Database.md → T1003/T1003.003-NTDS.md (NTDS)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 09-Credential-Access/T1003/T1003.007-proc-Filesystem.md (仅更新 attack_name_en: Proc Filesystem)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1552/T1552.003-Bash-History.md → T1552/T1552.003-Shell-History.md (Shell History)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1552/T1552.004-Certificates.md → T1552/T1552.004-Private-Keys.md (Private Keys)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 09-Credential-Access/T1552/T1552.005-Cloud-Instance-Metadata-API.md (仅更新 attack_name_en: Cloud Instance Metadata API)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1552/T1552.007-Container-Credentials.md → T1552/T1552.007-Container-API.md (Container API)
  [DRY-RUN] [name_mismatch_subs] RENAME: 09-Credential-Access/T1552/T1552.008-Chat-Platform-Credentials.md → T1552/T1552.008-Chat-Messages.md (Chat Messages)
  [DRY-RUN] [name_mismatch_subs] RENAME: 10-Discovery/T1518/T1518.002-Installed-Software.md → T1518/T1518.002-Backup-Software-Discovery.md (Backup Software Discovery)
  [DRY-RUN] [name_mismatch_subs] UPDATE_NAME: 10-Discovery/T1016/T1016.001-Internet-Connection-Discovery.md (仅更新 attack_name_en: Internet Connection Discovery)
  [DRY-RUN] [name_mismatch_subs] RENAME: 10-Discovery/T1497/T1497.002-User-Activity-Checks.md → T1497/T1497.002-User-Activity-Based-Checks.md (User Activity Based Checks)
  [DRY-RUN] [name_mismatch_subs] RENAME: 10-Discovery/T1497/T1497.003-Time-based-Evasion.md → T1497/T1497.003-Time-Based-Checks.md (Time Based Checks)
  [DRY-RUN] [name_mismatch_subs] RENAME: 11-Lateral-Movement/T1021/T1021.007-MMC.md → T1021/T1021.007-Cloud-Services.md (Cloud Services)
  [DRY-RUN] [name_mismatch_subs] RENAME: 11-Lateral-Movement/T1021/T1021.008-Remote-Desktop-Gateway.md → T1021/T1021.008-Direct-Cloud-VM-Connections.md (Direct Cloud VM Connections)
  [DRY-RUN] [name_mismatch_subs] RENAME: 12-Collection/T1557/T1557.001-LLMNR-NBT-NS.md → T1557/T1557.001-Name-Resolution-Poisoning-And-SMB-Relay.md (Name Resolution Poisoning and SMB Relay)
  [DRY-RUN] [name_mismatch_subs] RENAME: 12-Collection/T1560/T1560.003-Archive-via-Built-in-Command.md → T1560/T1560.003-Archive-Via-Custom-Method.md (Archive via Custom Method)
  [DRY-RUN] [name_mismatch_subs] RENAME: 12-Collection/T1602/T1602.002-Network-Device-Management-Collection.md → T1602/T1602.002-Network-Device-Configuration-Dump.md (Network Device Configuration Dump)
  [DRY-RUN] [name_mismatch_subs] RENAME: 12-Collection/T1213/T1213.001-Confluence-Wiki.md → T1213/T1213.001-Confluence.md (Confluence)
  [DRY-RUN] [name_mismatch_subs] RENAME: 12-Collection/T1213/T1213.002-SharePoint-Data.md → T1213/T1213.002-Sharepoint.md (Sharepoint)
  [DRY-RUN] [name_mismatch_subs] RENAME: 12-Collection/T1213/T1213.003-Code-Repository-Data.md → T1213/T1213.003-Code-Repositories.md (Code Repositories)
  [DRY-RUN] [name_mismatch_subs] RENAME: 12-Collection/T1213/T1213.004-Jira-Data.md → T1213/T1213.004-Customer-Relationship-Management-Software.md (Customer Relationship Management Software)
  [DRY-RUN] [name_mismatch_subs] RENAME: 13-Command-and-Control/T1071/T1071.005-SMB.md → T1071/T1071.005-Publish-subscribe-Protocols.md (Publish/Subscribe Protocols)
  [DRY-RUN] [name_mismatch_subs] RENAME: 13-Command-and-Control/T1001/T1001.003-Protocol-Impersonation.md → T1001/T1001.003-Protocol-Or-Service-Impersonation.md (Protocol or Service Impersonation)
  [DRY-RUN] [name_mismatch_subs] RENAME: 13-Command-and-Control/T1568/T1568.002-Domain-Generation-Algorithm.md → T1568/T1568.002-Domain-Generation-Algorithms.md (Domain Generation Algorithms)
  [DRY-RUN] [name_mismatch_subs] RENAME: 13-Command-and-Control/T1573/T1573.001-Symmetric-Encryption.md → T1573/T1573.001-Symmetric-Cryptography.md (Symmetric Cryptography)
  [DRY-RUN] [name_mismatch_subs] RENAME: 13-Command-and-Control/T1573/T1573.002-Asymmetric-Encryption.md → T1573/T1573.002-Asymmetric-Cryptography.md (Asymmetric Cryptography)
  [DRY-RUN] [name_mismatch_subs] RENAME: 14-Exfiltration/T1048/T1048.002-Symmetric-Exfiltration.md → T1048/T1048.002-Exfiltration-Over-Asymmetric-Encrypted-Non-c2-Protocol.md (Exfiltration Over Asymmetric Encrypted Non-C2 Protocol)
  [DRY-RUN] [name_mismatch_subs] RENAME: 14-Exfiltration/T1052/T1052.001-USB.md → T1052/T1052.001-Exfiltration-Over-USB.md (Exfiltration over USB)
  [DRY-RUN] [name_mismatch_subs] RENAME: 14-Exfiltration/T1567/T1567.002-Code-Repository.md → T1567/T1567.002-Exfiltration-To-Cloud-Storage.md (Exfiltration to Cloud Storage)
  [DRY-RUN] [name_mismatch_subs] RENAME: 14-Exfiltration/T1567/T1567.003-Paste-Site.md → T1567/T1567.003-Exfiltration-To-Text-Storage-Sites.md (Exfiltration to Text Storage Sites)
  [DRY-RUN] [name_mismatch_subs] RENAME: 14-Exfiltration/T1567/T1567.004-Webhook.md → T1567/T1567.004-Exfiltration-Over-Webhook.md (Exfiltration Over Webhook)
  [DRY-RUN] [name_mismatch_subs] RENAME: 15-Impact/T1565/T1565.003-Real-time-Data-Manipulation.md → T1565/T1565.003-Runtime-Data-Manipulation.md (Runtime Data Manipulation)
  [DRY-RUN] [name_mismatch_subs] RENAME: 15-Impact/T1499/T1499.001-OS-Resource-Exhaustion.md → T1499/T1499.001-OS-Exhaustion-Flood.md (OS Exhaustion Flood)
  [DRY-RUN] [name_mismatch_subs] RENAME: 15-Impact/T1499/T1499.002-Service-Resource-Exhaustion.md → T1499/T1499.002-Service-Exhaustion-Flood.md (Service Exhaustion Flood)
  [DRY-RUN] [name_mismatch_subs] RENAME: 15-Impact/T1499/T1499.003-Application-Layer-Exhaustion.md → T1499/T1499.003-Application-Exhaustion-Flood.md (Application Exhaustion Flood)

[跳过项]
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1546.009 in 05-Persistence
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1546.010 in 05-Persistence
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1548.001 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1548.002 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1548.003 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1548.004 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1543.001 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1543.002 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1543.003 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1543.004 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1546.009 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1546.010 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1055.008 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1055.012 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1055.013 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1055.014 in 06-Privilege-Escalation
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1564.001 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1564.002 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1564.003 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1564.008 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1564.009 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1564.011 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1564.012 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1564.013 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1564.014 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1070.005 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1070.007 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1070.008 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1070.009 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1070.010 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1027.008 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1027.009 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1027.011 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1027.012 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1027.013 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1027.014 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1542.003 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1542.004 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1542.005 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1055.008 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1055.011 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1055.012 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1218.001 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1218.002 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1218.003 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1218.005 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1218.008 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1218.009 in 07-Stealth
  [SKIP] [name_mismatch_subs] 9组重编号范围（待_tid_remap.json处理）: T1218.011 in 07-Stealth
