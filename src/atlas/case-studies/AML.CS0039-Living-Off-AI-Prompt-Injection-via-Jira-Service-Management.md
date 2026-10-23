# Living Off AI：经 Jira 服务管理的提示词注入 (AML.CS0039)

## 一句话通俗理解

> 工单系统里的一条恶意评论，让 AI 助手带着企业权限「接管」了工单流程。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-06-19 |
| 攻击者 | Cato CTRL |
| 受害目标 | Atlassian MCP, Jira Service Management |

## 事件经过

Cato Networks 研究者演示了嵌入企业工作流的 AI 系统如何被利用：经 Jira 服务管理的提示词注入，让 AI 助手以提升的权限执行恶意动作——攻击者借「AI 员工」的身份在企业流程中潜伏并横向行动（Living Off AI）。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0039 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索受害者自有网站 (AML.T0003)](../01-Reconnaissance/AML.T0003-Search-Victim-Owned-Websites.md)**
  > The researchers performed reconnaissance to learn about Atlassian's Model Context Protocol (MCP) server and its integration into the Jira Service Management (JSM) platform. Atlassian offers an MCP server, which embeds AI into enterprise workflows. Their MCP enables a range of AI-driven actions, such as ticket summarization, auto-replies, classification, and smart recommendations across JSM and Confluence. It allows support engineers and internal users to interact with AI directly from their native interfaces.

### S01

- **[搜索开放网站/域名 (AML.T0095)](../01-Reconnaissance/AML.T0095-Search-Open-Websites-Domains.md)**
  > The researchers used a search query, "site:atlassian.net/servicedesk inurl:portal",  to reveal organizations using Atlassian service portals as potential targets.

### S02

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers crafted a malicious prompt that requests data from all other support tickets be posted as a reply to the current ticket.

### S03

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The researchers created a new service ticket containing the malicious prompt on the public Jira Service Management (JSM) portal of the victim identified during reconnaissance.

### S04

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > As part of their standard workflow, a support engineer at the victim organization used Claude Sonnet (which can interact with Jira via the Atlassian MCP server) to help them resolve the malicious ticket, causing the injection to be unknowingly executed.

### S05

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The malicious prompt requested information accessible to the AI agent via Atlassian MCP tools, causing those tools to be invoked via MCP, granting the researchers increased privileges on the victim's JSM instance.

### S06

- **[AI 智能体工具 (AML.T0085.001)](../13-Collection/AML.T0085/AML.T0085.001-AI-Agent-Tools.md)**
  > The malicious prompt instructed that all details of other issues be collected. This invoked an Atlassian MCP tool that could access the Jira tickets and collect them.

### S07

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > The malicious prompt instructed that the collected ticket details be posted in a reply to the ticket. This invoked an Atlassian MCP Tool which performed the requested action, exfiltrating the data where it was accessible to the researchers on the JSM portal.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Cato CTRL Threat Research: PoC Attack Targeting Atlassian's Model Context Protocol (MCP) Introduces New "Living Off AI" Risk](https://www.catonetworks.com/blog/cato-ctrl-poc-attack-targeting-atlassians-mcp/)

- [MITRE ATLAS 官方案例页 (AML.CS0039)](https://atlas.mitre.org/studies/AML.CS0039/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
