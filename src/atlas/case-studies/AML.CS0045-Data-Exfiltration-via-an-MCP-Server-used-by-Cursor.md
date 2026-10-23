# 经 Cursor 使用的 MCP 服务器数据渗漏 (AML.CS0045)

## 一句话通俗理解

> 「帮我抓取这个网页」——Cursor 抓回来的不只是内容，还有藏在内的注入指令和一条 curl 命令。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-06-24 |
| 攻击者 | Backslash Security Research Team |
| 受害目标 | Cursor |

## 事件经过

Backslash Security 研究团队构建了网页抓取类 MCP 服务器作为注入载体：用户让 Cursor 用该工具抓取含恶意提示词的网站时，注入进入上下文——提示词指示 Cursor 执行 shell 命令（curl）外传受害者的智能体配置文件（含凭证）。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0045 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers crafted a malicious prompt containing an instruction to execute the malicious shell command to exfiltrate the victim's AI agent credentials.

### S01

- **[暂存能力 (AML.T0079)](../02-Resource-Development/AML.T0079-Stage-Capabilities.md)**
  > The researchers created a malicious web site containing the malicious prompt.

### S02

- **[LLM 提示词混淆 (AML.T0068)](../09-Defense-Evasion/AML.T0068-LLM-Prompt-Obfuscation.md)**
  > The malicious prompt was hidden in the title tag of the webpage.

### S03

- **[暂存能力 (AML.T0079)](../02-Resource-Development/AML.T0079-Stage-Capabilities.md)**
  > The researchers launched a web server to receive data exfiltrated from the victim.

### S04

- **[路过式入侵 (AML.T0078)](../04-Initial-Access/AML.T0078-Drive-by-Compromise.md)**
  > When a user asked Cursor to use an MCP tool to scrape the malicious website, the contents of the malicious prompt was retrieved and ingested into Cursor's context window.

### S05

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > When the MCP server scraped the malicious web site, it returned the injected prompt to the MCP client and poisoned the context of the Cursor LLM. Cursor executed the malicious prompt embedded in the website scraped by the MCP tool.

### S06

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The prompt injection invoked Cursor's ability to call command line tools via the `run_terminal_cmd` tool.

Cursor prompted the user before executing a shell command, potentially mitigating this attack.

### S07

- **[LLM 提示词混淆 (AML.T0068)](../09-Defense-Evasion/AML.T0068-LLM-Prompt-Obfuscation.md)**
  > When the MCP server scraped the malicious web site, it returned the injected prompt to the MCP client and poisoned the context of the Cursor LLM. The shell command in the malicious prompt was obscured via base64 encoding, making it less clear to the user that something malicious may be executed.

### S08

- **[从 AI 智能体配置获取凭证 (AML.T0083)](../10-Credential-Access/AML.T0083-Credentials-from-AI-Agent-Configuration.md)**
  > The shell command located the `.openapi.apiKey` and `.cursor/mcp.json` credentials files that were part of the Cursor's configuration.

### S09

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > The credentials files were exfiltrated to the researcher's server via a `curl` command invoked by Cursor's `run_terminal_cmd` tool.

### S10

- **[财务危害 (AML.T0048.000)](../16-Impact/AML.T0048/AML.T0048.000-Financial-Harm.md)**
  > A bad actor could use the stolen credentials to cause financial damage and could also steal other sensitive information from the victim user.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Simulating a Context-Poisoning Vulnerable MCP Server: A POC](https://www.backslash.security/blog/simulating-a-vulnerable-mcp-server-for-context-poisoning)

- [MITRE ATLAS 官方案例页 (AML.CS0045)](https://atlas.mitre.org/studies/AML.CS0045/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
