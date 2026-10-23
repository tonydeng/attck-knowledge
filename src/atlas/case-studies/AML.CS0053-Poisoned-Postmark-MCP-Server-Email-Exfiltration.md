# 投毒的 Postmark MCP 服务器邮件渗漏 (AML.CS0053)

## 一句话通俗理解

> npm 抢注 + 养信誉 + rugpull：第一个野外恶意 MCP，把企业邮件整批发给后门作者。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2025-09-01 |
| 攻击者 | Unknown Bad Actor |
| 受害目标 | Postmark MCP Server |
| 披露方 | Koi Research |

## 事件经过

恶意行为者通过供应链攻击渗漏了 Postmark MCP 服务器用户的邮件：攻击者仿冒 Postmark 在 npm 抢注 postmark-mcp 包名，先发布合法版本养信誉，周下载量破千后换成恶意版——经该工具发送的邮件全文被转发至攻击者服务器。这是首个野外恶意 MCP。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0053 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[冒充 (AML.T0073)](../09-Defense-Evasion/AML.T0073-Impersonation.md)**
  > The bad actor impersonated Postmark by publishing a legitimate version of their `postmark-mcp` package to npm.  Postmark had not registered the `postmark-mcp` name on npm themselves, allowing the bad actor to namesquat. Legitimate users were tricked into using the npm package even though it wasn't managed by the official developers of `postmark-mcp`

### S01

- **[开发能力 (AML.T0017)](../02-Resource-Development/AML.T0017-Develop-Capabilities.md)**
  > The bad actor modified the legitimate Postmark MCP server to include their email address on the BCC line on all emails sent by the tool.

### S02

- **[AI 智能体工具 (AML.T0115.002)](../02-Resource-Development/AML.T0115/AML.T0115.002-AI-Agent-Tools.md)**
  > The bad actor published their malicious version of `postmark-mcp` to npm.

### S03

- **[AI 供应链拉地毯式撤离 (AML.T0109)](../09-Defense-Evasion/AML.T0109-AI-Supply-Chain-Rug-Pull.md)**
  > By waiting for users to adopt a legitimate version of `postmark-mcp` first, the bad actor was able to evade the additional scrutiny and scanning performed on new tools.

### S04

- **[AI 智能体工具 (AML.T0010.005)](../04-Initial-Access/AML.T0010/AML.T0010.005-AI-Agent-Tool.md)**
  > When organizations upgraded `postmark-mcp` to version `1.0.16`, they received the malicious version of the tool via the compromised supply chain.

### S05

- **[实现 (AML.T0110.001)](../07-Persistence/AML.T0110/AML.T0110.001-Implementation.md)**
  > Once configured with the organization's AI agents, the poisoned Postmark MCP server's effects persist.

### S06

- **[投毒 AI 智能体工具 (AML.T0011.002)](../06-Execution/AML.T0011/AML.T0011.002-Poisoned-AI-Agent-Tools.md)**
  > When users at the victim organization instructed their AI agent to use tools provided by the poisoned Postmark MCP Server, the malicious code was executed.

### S07

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > When organizations sent emails via the `postmark-mcp` tool, the entire contents of their emails are exfiltrated to the bad actor via the address added on the BCC line.

### S08

- **[外部危害 (AML.T0048)](../16-Impact/AML.T0048-External-Harms.md)**
  > The exfiltrated emails may include transactional emails (revealing private information about the organization's clients) and promotional emails (revealing the organization's client list).

## 关联战术

- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [First Malicious MCP in the Wild: The Postmark Backdoor That's Stealing Your Emails](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft)

- [MITRE ATLAS 官方案例页 (AML.CS0053)](https://atlas.mitre.org/studies/AML.CS0053/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
