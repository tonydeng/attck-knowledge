# Claude Code GitHub Action 密钥暴露 (AML.CS0067)

## 一句话通俗理解

> 让 Claude 输出 API 密钥还要「去前缀」——GitHub 的密钥扫描器就这么被绕过了。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2026-06-05 |
| 攻击者 | Microsoft Defender Security Research Team |
| 受害目标 | Claude Code GitHub Action |

## 事件经过

微软 Defender 安全研究团队演示了 Anthropic Claude Code GitHub Action 的密钥暴露：经提示词注入诱导 Claude 输出其 API 密钥并去除 sk-ant- 前缀——前缀缺失使 GitHub 的密钥扫描失效，密钥静默泄露；WebFetch、Bash、GitHub MCP 等均可作为渗漏通道。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0067 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[代码仓库 (AML.T0095.000)](../01-Reconnaissance/AML.T0095/AML.T0095.000-Code-Repositories.md)**
  > The researchers analyzed the Claude Code Action codebase and the obfuscated Claude Agent SDK. They used the implementation details to understand how agent tools executed and where security boundaries were applied.

### S01

- **[工具定义 (AML.T0084.001)](../11-Discovery/AML.T0084/AML.T0084.001-Tool-Definitions.md)**
  > The researchers identified the tools available to Claude Code Action and compared their execution paths. They determined that Bash subprocesses could run within Bubblewrap with a scrubbed environment, while the built-in Read tool performed direct, in-process file access outside that isolation boundary.

### S02

- **[激活触发器 (AML.T0084.002)](../11-Discovery/AML.T0084/AML.T0084.002-Activation-Triggers.md)**
  > The researchers identified that Claude Code Action could be triggered by GitHub events involving issues, pull requests, and comments and that the action would fetch the associated content into Claude's context.

### S03

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers crafted a prompt tailored to Claude Code Action framed as a compliance task that directed Claude to read a credential from its environment and emit it.

### S04

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The researchers introduced the malicious prompt through attacker-controlled GitHub content processed by the lab workflow, modeling delivery through an issue body, pull request description, or comment handled by Claude Code Action.

### S05

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > Claude Code Action incorporated the malicious GitHub content into the model context. Claude interpreted the malicious content as instructions and followed the supplied instructions.

### S06

- **[LLM 越狱 (AML.T0054)](../08-Privilege-Escalation/AML.T0054-LLM-Jailbreak.md)**
  > The prompt used benign compliance review framing and instructions to remove the credential prefix to bypass Claude's refusal behavior for emitting a recognizable API key.

### S07

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > Claude invoked its built-in Read tool on `/proc/self/environ`. Read did not execute within the Bubblewrap and scrubbed-environment boundary applied to Bash subprocesses.

### S08

- **[AI 智能体工具凭证窃取 (AML.T0098)](../10-Credential-Access/AML.T0098-AI-Agent-Tool-Credential-Harvesting.md)**
  > The Read tool returned the action process's unsanitized environment, including `ANTHROPIC_API_KEY` and potentially other credentials available to the workflow.

### S09

- **[LLM 数据泄露 (AML.T0057)](../15-Exfiltration/AML.T0057-LLM-Data-Leakage.md)**
  > Claude emitted the Anthropic API key after removing its `sk-ant-` prefix. The transformation prevented GitHub's secret scanner from recognizing the credential, while the researchers could reconstruct the original key by restoring the prefix.

### S10

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > The researchers could use WebFetch, Bash, GitHub MCP, and Action logs as potential exfiltration channels depending on the tools available in the workflow configuration.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [权限提升 (AML.TA0012)](../08-Privilege-Escalation/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Securing CI/CD in an agentic world: Claude Code Github action case](https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/)

- [MITRE ATLAS 官方案例页 (AML.CS0067)](https://atlas.mitre.org/studies/AML.CS0067/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
