# Copilot Studio 智能体工具数据渗漏 (AML.CS0037)

## 一句话通俗理解

> 客户服务智能体的邮件工具被注入劫持——整个 CRM 数据库被打包发给了「研究者」。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-06-01 |
| 攻击者 | Zenity |
| 受害目标 | Copilot Studio Customer Service Agent |

## 事件经过

Zenity 研究者演示了经提示词注入针对 AI 客服智能体（Copilot Studio）的数据渗漏：注入指令诱导智能体收集其可访问的组织数据（含整个 CRM 数据库内容），并调用邮件工具把结果发送到研究者指定地址——合法工具完成越权外传。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0037 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[探测 AI 智能体触发通道 (AML.T0006.003)](../01-Reconnaissance/AML.T0006/AML.T0006.003-Probe-AI-Agent-Trigger-Channels.md)**
  > The researchers look for support email addresses on the target organization's website which may be managed by an AI agent. Then, they probe the system by sending emails and looking for indications of agentic AI in automatic replies.

### S01

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > Once a target has been identified, the researchers craft prompts designed to probe for a potential AI agent monitoring the inbox. The prompt instructs the agent to send an email reply to an address of the researchers' choosing.

### S02

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The researchers send an email with the malicious prompt to the inbox they suspect may be managed by an AI agent.

### S03

- **[触发式提示词注入 (AML.T0051.002)](../06-Execution/AML.T0051/AML.T0051.002-Triggered.md)**
  > The researchers receive a reply at the address they specified, indicating that there is an AI agent present, and that the triggered prompt injection was successful.

### S04

- **[激活触发器 (AML.T0084.002)](../11-Discovery/AML.T0084/AML.T0084.002-Activation-Triggers.md)**
  > The researchers infer that the AI agent is activated when receiving an email.

### S05

- **[工具定义 (AML.T0084.001)](../11-Discovery/AML.T0084/AML.T0084.001-Tool-Definitions.md)**
  > The researchers infer that the AI agent has a tool for sending emails.

### S06

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > From here, the researchers repeat the same steps to interact with the AI agent, sending malicious prompts to the agent via email and receiving responses at their desired address.

### S07

- **[LLM 提示词注入 (AML.T0051)](../06-Execution/AML.T0051-LLM-Prompt-Injection.md)**
  > The researchers modify the original prompt to discover other knowledge sources and tools that may have data they are after.

### S08

- **[内嵌知识 (AML.T0084.000)](../11-Discovery/AML.T0084/AML.T0084.000-Embedded-Knowledge.md)**
  > The researchers discover the AI agent has access to a "Customer Support Account Owners.csv" data source.

### S09

- **[工具定义 (AML.T0084.001)](../11-Discovery/AML.T0084/AML.T0084.001-Tool-Definitions.md)**
  > The researchers discover the AI agent has access to the Salesforce get-records tool, which can be used to retrieve CRM records.

### S10

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers put their knowledge of the AI agent's tools and knowledge sources together to craft a prompt that will collect and exfiltrate the customer data they are after.

### S11

- **[RAG 数据库 (AML.T0085.000)](../13-Collection/AML.T0085/AML.T0085.000-RAG-Databases.md)**
  > The prompt asks the agent to retrieve all of the fields and rows from "Customer Support Account Owners.csv". The agent retrieves the entire file.

### S12

- **[AI 智能体工具 (AML.T0085.001)](../13-Collection/AML.T0085/AML.T0085.001-AI-Agent-Tools.md)**
  > The prompt asks the agent to retrieve all Salesforce records using its get-records tool. The agent retrieves all records from the victim's CRM.

### S13

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > The prompt asks the agent to email the results to an address of the researcher's choosing using its email tool. The researchers successfully exfiltrate their target data via the tool invocation.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [AgentFlayer: Discovery Phase of AI Agents in Copilot Studio](https://labs.zenity.io/p/a-copilot-studio-story-discovery-phase-in-ai-agents-f917)
- [AgentFlayer: When AIjacking Leads to Full Data Exfiltration in Copilot Studio](https://labs.zenity.io/p/a-copilot-studio-story-2-when-aijacking-leads-to-full-data-exfiltration-bc4a)

- [MITRE ATLAS 官方案例页 (AML.CS0037)](https://atlas.mitre.org/studies/AML.CS0037/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
