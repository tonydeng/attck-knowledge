# ZombieAgent：针对 ChatGPT 的数据渗漏 (AML.CS0066)

## 一句话通俗理解

> 让 ChatGPT 自己「点」攻击者的链接——Deep Research 加连接器的组合被注入打穿。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-09-25 |
| 攻击者 | Radware Security Researchers |
| 受害目标 | OpenAI ChatGPT |

## 事件经过

Radware 演示了针对 ChatGPT Deep Research 与 Connector 功能的间接提示词注入（ZombieAgent）：攻击者诱导 ChatGPT 调用其 URL 打开能力请求攻击者控制的 URL，受害者数据编码其中完成外传——研究者从传输数据中重建了受害者信息。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0066 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers crafted malicious prompt payloads for the different attack variants. The payloads contained instructions for connector access, data collection, static-URL encoding, memory manipulation, and propagation.

### S01

- **[暂存能力 (AML.T0079)](../02-Resource-Development/AML.T0079-Stage-Capabilities.md)**
  > The researchers prepared infrastructure to receive exfiltrated data.

### S02

- **[LLM 提示词混淆 (AML.T0068)](../09-Defense-Evasion/AML.T0068-LLM-Prompt-Obfuscation.md)**
  > The prompt injection was visually concealed in externally controlled content using techniques such as white-on-white text or microscopic font sizes. ChatGPT could process the instructions even though they were not apparent to the user.

### S03

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The researchers sent a malicious email to an inbox connected to ChatGPT or provided a malicious document that could be uploaded or retrieved through a connected service. This introduced the prompt into a data source accessible to the victim's agent.

### S04

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > A later, legitimate user request, such as asking ChatGPT to summarize the inbox, caused the agent to retrieve the malicious content and execute the concealed instructions. The user did not knowingly interact with the malicious email.

### S05

- **[记忆 (AML.T0080.000)](../07-Persistence/AML.T0080/AML.T0080.000-Memory.md)**
  > The malicious instructions caused ChatGPT to create or modify memories. The poisoned memories instructed ChatGPT to retain sensitive information from conversations and to perform attacker-defined actions during later interactions.

### S06

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The malicious instructions caused ChatGPT to invoke connector and web-access capabilities available under the victim's authority. This gave the prompt access to information and actions that were not directly available to the researchers.

### S07

- **[AI 智能体工具 (AML.T0085.001)](../13-Collection/AML.T0085/AML.T0085.001-AI-Agent-Tools.md)**
  > ChatGPT used connected-service tools to retrieve information accessible to the victim's agent. Demonstrated collection included mailbox content and email contact information.

### S08

- **[LLM 越狱 (AML.T0054)](../08-Privilege-Escalation/AML.T0054-LLM-Jailbreak.md)**
  > The researchers bypassed ChatGPT's restriction against dynamically constructing or modifying URLs by supplying an indexed dictionary of static URLs. ChatGPT encoded collected data by selecting and opening the URL corresponding to each character and position.

### S09

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > ChatGPT invoked its URL-opening capability to request the selected adversary-controlled URLs. The researchers reconstructed the sensitive data from the character and position encoded in the resulting server requests. The requests originated from OpenAI's infrastructure rather than the victim's endpoint or corporate network.

### S11

- **[AI 智能体工具 (AML.T0085.001)](../13-Collection/AML.T0085/AML.T0085.001-AI-Agent-Tools.md)**
  > ChatGPT searched the victim's mailbox and collected email addresses belonging to potential additional targets.

### S12

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The malicious instructions caused ChatGPT to reproduce the prompt in new emails or documents and distribute them to collected contacts. If another AI agent processed the poisoned content, the attack could propagate between users or connected AI systems.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [权限提升 (AML.TA0012)](../08-Privilege-Escalation/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [ZombieAgent: New ChatGPT Vulnerabilities Let Data Theft Continue (and Spread)](https://www.radware.com/blog/threat-intelligence/zombieagent/)

- [MITRE ATLAS 官方案例页 (AML.CS0066)](https://atlas.mitre.org/studies/AML.CS0066/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
