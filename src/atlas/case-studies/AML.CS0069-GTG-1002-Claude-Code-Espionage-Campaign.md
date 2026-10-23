# GTG-1002 Claude Code 间谍行动 (AML.CS0069)

## 一句话通俗理解

> 越狱的 Claude Code 当了三个月「网络间谍」——对 30 家组织自主发起多阶段攻击。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2025-09-01 |
| 攻击者 | GTG-1002 |
| 受害目标 | 30 entities in the technology, financial, chemical, and government sectors |
| 披露方 | Anthropic |

## 事件经过

2025 年 9 月，GTG-1002 使用越狱的 Claude Code 智能体对约 30 家组织实施网络间谍行动并攻陷其中少数：智能体自主执行侦察、收集、横向移动与渗漏——跨 K8s 身份、云凭证、节点令牌到 GitHub App 安装令牌的六段凭证链转换全部由智能体自主完成，最终经 Claude Web 服务审阅后批准数据回传。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0069 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S01

- **[AI 模型推理 API 访问 (AML.T0040)](../05-AI-Model-Access/AML.T0040-AI-Model-Inference-API-Access.md)**
  > GTG-1002 obtained access to Claude Code for use in its intrusion framework.

### S02

- **[直接提示词注入 (AML.T0051.000)](../06-Execution/AML.T0051/AML.T0051.000-Direct.md)**
  > GTG-1002 supplied Claude Code false authorization claims, a defensive-security persona, and apparently benign tasks.

### S03

- **[LLM 越狱 (AML.T0054)](../08-Privilege-Escalation/AML.T0054-LLM-Jailbreak.md)**
  > The deceptive prompts circumvented the Claude Code's safeguards, inducing it to perform offensive actions it was intended to refuse.

### S04

- **[软件工具 (AML.T0016.001)](../02-Resource-Development/AML.T0016/AML.T0016.001-Software-Tools.md)**
  > GTG-1002 obtained network scanners, database exploitation frameworks, password crackers, binary-analysis utilities, and other tools made available to the jailbroken Claude agent.

### S05

- **[入侵基础设施 (AML.T0128)](../02-Resource-Development/AML.T0128-Compromise-Infrastructure.md)**
  > GTG-1002 operated dedicated penetration-testing servers accessible through MCP to support remote command execution, simultaneous tool coordination, and persistent operational state across campaign sessions.

### S06

- **[部署 AI 智能体 (AML.T0103)](../06-Execution/AML.T0103-Deploy-AI-Agent.md)**
  > GTG-1002 configured their Claude agent within an attack framework connected to scanners, browser automation, password crackers, database tooling, and dedicated penetration-testing servers.

### S07

- **[自主攻击路径适配 (AML.T0117)](../03-AI-Attack-Adaptation/AML.T0117-Autonomous-Attack-Path-Adaptation.md)**
  > GTG-1002 assigned their Claude agent target-scoped objectives against a human-selected organization under false defensive-testing context. Between operator-controlled stage gates, the agent derived and revised intermediate actions for reconnaissance, vulnerability exploitation, credential access, internal navigation, collection, and exfiltration, selecting and invoking available tools based on operational results.

### S08

- **[自主侦察 (AML.T0116)](../01-Reconnaissance/AML.T0116-Autonomous-Reconnaissance.md)**
  > GTG-1002's jailbroken Claude agent inspected the target's systems and infrastructure, used returned information to direct further investigation, and identified high-value databases and workflow orchestration platforms. Anthropic does not identify the victim, products, or databases involved.

### S09

- **[主动扫描 (AML.T0006)](../01-Reconnaissance/AML.T0006-Active-Scanning.md)**
  > GTG-1002's jailbroken Claude agent performed IP-block scanning across ranges associated with the target organization and vulnerability scanning against its infrastructure. It used the scans to enumerate public-facing services and endpoints, identify potential vulnerabilities, and select an SSRF vulnerability in an unnamed public-facing application for further investigation. Reporting does not establish whether the vulnerability was previously known or assigned a CVE.

### S10

- **[自主漏洞利用开发 (AML.T0017.001)](../02-Resource-Development/AML.T0017/AML.T0017.001-Autonomous-Exploit-Development.md)**
  > GTG-1002's Claude agent researched exploitation techniques for the identified SSRF vulnerability, generated a tailored custom payload and full exploit chain, tested the approach, evaluated the results, and adapted it for the target.

### S11

- **[利用面向公众的应用 (AML.T0049)](../04-Initial-Access/AML.T0049-Exploit-Public-Facing-Application.md)**
  > GTG-1002's jailbroken Claude agent deployed the tailored SSRF exploit against the public-facing application and obtained access to the target environment.

### S12

- **[企业资源发现 (AML.T0075)](../11-Discovery/AML.T0075-Enterprise-Resource-Discovery.md)**
  > GTG-1002's jailbroken Claude agent cataloged services and data on discovered endpoints, searched for sensitive files and data, and used MCP-connected browser automation to enumerate internal databases, container registries, administrative interfaces, workflow orchestration platforms, and other network services. It also queried internal database user-account tables to enumerate accounts and identify high-privilege accounts.

### S13

- **[企业环境发现 (AML.T0089)](../11-Discovery/AML.T0089-Enterprise-Environment-Discovery.md)**
  > GTG-1002's jailbroken Claude agent identified system and network configurations on discovered devices, including database types, and mapped the target's complete network topology, internal network architecture, and access relationships among systems and services.

### S14

- **[不安全的凭证 (AML.T0055)](../10-Credential-Access/AML.T0055-Unsecured-Credentials.md)**
  > GTG-1002's jailbroken Claude agent searched discovered system configuration files and extracted authentication certificates and other credential material. Reporting does not disclose the exact file paths, commands, hosts, or tools used.

### S15

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > GTG-1002's jailbroken Claude agent tested harvested credentials against discovered devices and used valid credentials to authenticate to internal APIs, databases, container registries, and logging infrastructure.

### S16

- **[创建账户 (AML.T0125)](../07-Persistence/AML.T0125-Create-Account.md)**
  > GTG-1002's jailbroken Claude agent created a local backdoor account to maintain access to a compromised environment.

### S17

- **[来自信息库的数据 (AML.T0036)](../13-Collection/AML.T0036-Data-from-Information-Repositories.md)**
  > Using the authenticated access provided by the harvested credentials, GTG-1002's jailbroken Claude agent queried internal databases and systems for proprietary information, system configurations, and sensitive operational data.

### S18

- **[来自本地系统的数据 (AML.T0037)](../13-Collection/AML.T0037-Data-from-Local-System.md)**
  > Access obtained through the initial compromise also allowed GTG-1002's jailbroken Claude agent to gather credentials, system configurations, and sensitive operational data stored on compromised systems.

### S19

- **[自动化收集 (AML.T0126)](../13-Collection/AML.T0126-Automated-Collection.md)**
  > GTG-1002's jailbroken Claude agent automatically collected and processed large volumes of victim data and categorized the results according to their intelligence value. It generated comprehensive documentation covering discovered services, harvested credentials, sensitive data, exploitation techniques, and attack progression to support subsequent campaign activity.

### S20

- **[数据暂存 (AML.T0127)](../13-Collection/AML.T0127-Data-Staged.md)**
  > GTG-1002's jailbroken Claude agent categorized collected data by intelligence value, staged extracted data and operational documentation in structured Markdown files, and prepared a detailed summary for operator review.

### S21

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > After reviewing the summary, GTG-1002 approved the transfer of selected data over the Claude web service.

## 关联战术

- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [权限提升 (AML.TA0012)](../08-Privilege-Escalation/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Disrupting the First Reported AI-Orchestrated Cyber Espionage Campaign](https://www.anthropic.com/news/disrupting-AI-espionage)
- [Anthropic AI-Orchestrated Campaign C0062](https://attack.mitre.org/campaigns/C0062/)

- [MITRE ATLAS 官方案例页 (AML.CS0069)](https://atlas.mitre.org/studies/AML.CS0069/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
