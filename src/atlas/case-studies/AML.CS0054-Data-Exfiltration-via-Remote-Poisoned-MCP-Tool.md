# 经远程投毒 MCP 工具的数据渗漏 (AML.CS0054)

## 一句话通俗理解

> 工具的「使用说明」里藏指令——智能体乖乖把你的凭证塞进了工具参数里。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-04-01 |
| 攻击者 | Invariant Labs |
| 受害目标 | Model Context Protocol |

## 事件经过

Invariant Labs 演示了远程 MCP 工具的投毒攻击：MCP 工具的 docstring 描述中内嵌恶意提示词（随工具定义进入智能体上下文），指示智能体读取受害者凭证文件并存入工具的一个无关输入参数——「正常调用」工具时凭证随参数到达攻击者控制的服务端。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0054 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers crafted a prompt that instructs an AI agent to discover and read user credentials files and store them in an input parameter of an MCP tool.

### S01

- **[AI 智能体工具 (AML.T0115.002)](../02-Resource-Development/AML.T0115/AML.T0115.002-AI-Agent-Tools.md)**
  > The researchers hosted a poisoned MCP server that contains the malicious instructions hidden in the docstring of one of the provided tools.

### S02

- **[AI 智能体工具 (AML.T0010.005)](../04-Initial-Access/AML.T0010/AML.T0010.005-AI-Agent-Tool.md)**
  > The victim configured their AI agent to connect to the adversary-controlled remote MCP server, introducing the poisoned tool definition into the agent's available tool set.

### S03

- **[定义与指令 (AML.T0110.000)](../07-Persistence/AML.T0110/AML.T0110.000-Definitions-and-Instructions.md)**
  > The MCP tool's model-visible docstring contained malicious instructions directing the agent to read credential files, conceal the additional actions from the user, and place the credential contents in an otherwise unnecessary tool parameter.

### S04

- **[投毒 AI 智能体工具 (AML.T0011.002)](../06-Execution/AML.T0011/AML.T0011.002-Poisoned-AI-Agent-Tools.md)**
  > When the user made a request that represented the poisoned tool's functionality, the agent invoked the poisoned MCP tool and acted on the malicious instructions contained in its definition.

### S05

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > The agent ingested and followed malicious instructions supplied through the remote tool's model-visible definition rather than directly through an adversary-authored user message.

### S06

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The prompt invoked an agent tool capable of reading files from the victim's filesystem.

### S07

- **[不安全的凭证 (AML.T0055)](../10-Credential-Access/AML.T0055-Unsecured-Credentials.md)**
  > The prompt instructed the AI agent to read the user's SSH keys at `~/.ssh/id_rsa`.

### S08

- **[AI 智能体工具凭证窃取 (AML.T0098)](../10-Credential-Access/AML.T0098-AI-Agent-Tool-Credential-Harvesting.md)**
  > The prompt instructed the AI agent to read `mcp.json`, which often contains credentials for other MCP servers.

### S09

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > The prompt instructed the AI agent to store the credentials files in an extraneous MCP tool parameter to exfiltrate them via the MCP connection.

### S10

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The user's private data was exposed to remote MCP server.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)

- [MITRE ATLAS 官方案例页 (AML.CS0054)](https://atlas.mitre.org/studies/AML.CS0054/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
