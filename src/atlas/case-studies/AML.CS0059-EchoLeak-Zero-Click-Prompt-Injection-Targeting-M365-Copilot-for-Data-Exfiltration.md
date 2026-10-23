# EchoLeak：针对 M365 Copilot 的零点击注入数据渗漏 (AML.CS0059)

## 一句话通俗理解

> 发一封邮件就偷走企业数据——Copilot 的零点击漏洞 + 借道 Teams 预览域名绕过 CSP。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-05-25 |
| 攻击者 | Aim Labs |
| 受害目标 | Microsoft 365 Copilot |

## 事件经过

Aim Security 研究者发现 M365 Copilot 的零点击漏洞 EchoLeak（CVE-2025-32711）：攻击者发送一封邮件，Copilot 检索邮件作为 RAG 上下文时恶意指令执行，搜索用户可访问的 M365 数据并将敏感信息经渲染图片请求外传——研究者借允许的 Microsoft Teams 预览域名中转以绕过 CSP 限制。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0059 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers crafted malicious instructions designed to evade Microsoft's indirect prompt injection classifier, appear like ordinary business content, suppress attribution to the attacker-controlled email, and cause Copilot to include sensitive data in rendered output.

### S01

- **[检索内容构造 (AML.T0066)](../03-AI-Attack-Adaptation/AML.T0066-Retrieval-Content-Crafting.md)**
  > The researchers embedded the prompt injection in business-like email content that was likely to be retrieved during a later Copilot interaction. The content was designed to appear relevant to ordinary enterprise workflows while carrying hidden instructions.

### S02

- **[暂存能力 (AML.T0079)](../02-Resource-Development/AML.T0079-Stage-Capabilities.md)**
  > The researchers staged an attacker-controlled web endpoint to receive outbound requests containing encoded sensitive data. The endpoint served as the collection point for the exfiltration channel.

### S03

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The researchers sent the email to a Microsoft 365 user inbox.

### S04

- **[LLM 提示词混淆 (AML.T0068)](../09-Defense-Evasion/AML.T0068-LLM-Prompt-Obfuscation.md)**
  > The prompt was phrased as benign business text rather than and obviously malicious prompt to evade user suspicion.

### S05

- **[RAG 投毒 (AML.T0070)](../07-Persistence/AML.T0070-RAG-Poisoning.md)**
  > The email was automatically ingested into a RAG database available to Copilot's retrieval pipeline.

### S06

- **[触发式提示词注入 (AML.T0051.002)](../06-Execution/AML.T0051/AML.T0051.002-Triggered.md)**
  > When the user later invoked Copilot, it retrieved the malicious email into its context and triggering the prompt injection.

### S07

- **[RAG 数据库 (AML.T0085.000)](../13-Collection/AML.T0085/AML.T0085.000-RAG-Databases.md)**
  > The malicious instructions caused Copilot to access sensitive enterprise information available through the user's Microsoft 365 account, such as emails, files, or project details.

### S08

- **[操纵 LLM 可信输出组件 (AML.T0067)](../09-Defense-Evasion/AML.T0067-LLM-Trusted-Output-Components-Manipulation.md)**
  > The output was manipulated to avoid obvious attribution and to use reference-style Markdown links or images that bypassed link redaction.

### S09

- **[LLM 响应渲染 (AML.T0077)](../15-Exfiltration/AML.T0077-LLM-Response-Rendering.md)**
  > Copilot rendered a Markdown image whose URL encoded sensitive information. The client automatically attempted to fetch the image, creating a zero-click exfiltration path.

### S10

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > To bypass CSP restrictions, the researchers routed the rendered image request through an allowed Microsoft Teams preview or proxy path, which fetched the attacker-controlled URL containing the encoded secret.

### S11

- **[外部危害 (AML.T0048)](../16-Impact/AML.T0048-External-Harms.md)**
  > If exploited against a real enterprise user, the attack could disclose confidential business data and harm the organization or affected users.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System](https://arxiv.org/abs/2509.10540)
- [CVE-2025-32711](https://www.cve.org/CVERecord?id=CVE-2025-32711)
- [Breaking down 'EchoLeak', the First Zero-Click AI Vulnerability Enabling Data Exfiltration from Microsoft 365 Copilot](https://www.catonetworks.com/blog/breaking-down-echoleak/)

- [MITRE ATLAS 官方案例页 (AML.CS0059)](https://atlas.mitre.org/studies/AML.CS0059/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
