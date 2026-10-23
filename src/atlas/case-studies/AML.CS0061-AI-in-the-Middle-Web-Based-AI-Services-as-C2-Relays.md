# AI in the Middle：Web AI 服务变身 C2 中继 (AML.CS0061)

## 一句话通俗理解

> 恶意软件不直连 C2——让 Grok/Copilot 替它跑腿：指令藏在 AI 问答里，流量全是「合法的」。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2026-02-17 |
| 攻击者 | Check Point Research |
| 受害目标 | Enterprise machines with Grok and Microsoft Copilot access |

## 事件经过

Check Point Research 演示了「AI in the Middle」攻击：恶意软件滥用具备匿名浏览与 URL 抓取能力的 Web AI 助手（Grok、Microsoft Copilot）作为隐蔽 C2 中继——AI 服务替植入体抓取攻击者 URL（参数带数据）、返回攻击者指令，全程混入对可信 AI 域名的正常 HTTPS 流量。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0061 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索开放网站/域名 (AML.T0095)](../01-Reconnaissance/AML.T0095-Search-Open-Websites-Domains.md)**
  > The researchers evaluated public AI assistants with anonymous or unauthenticated web-browsing and URL-fetch behavior to identify services that could retrieve arbitrary adversary-controlled URLs without requiring API credentials. The researchers found Grok and Copilot met those conditions.

### S01

- **[域名 (AML.T0008.002)](../02-Resource-Development/AML.T0008/AML.T0008.002-Domains.md)**
  > The researchers registered a domain and deployed an HTTPS site to act as the relay endpoint.

### S02

- **[暂存能力 (AML.T0079)](../02-Resource-Development/AML.T0079-Stage-Capabilities.md)**
  > The researchers hosted benign-looking content while also returning data that the implant could treat as C2 instructions.

### S03

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > Assuming prior access, the researchers used a custom C++ implant with an embedded browser or WebView component to interact with Grok or Microsoft Copilot through the public web interface rather than an API key.

### S04

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers crafted prompts that instruct an AI service to fetch and summarize a website. The prompts caused victim data to be included in URL parameters, allowing the AI service's fetch request to relay data to the adversary-controlled server.

### S05

- **[LLM 提示词混淆 (AML.T0068)](../09-Defense-Evasion/AML.T0068-LLM-Prompt-Obfuscation.md)**
  > When some prompts were blocked by model safeguards, the researchers encoded or encrypted payload data into high-entropy blobs to reduce the chance that safeguards would identify the content as malicious.

### S06

- **[来自本地系统的数据 (AML.T0037)](../13-Collection/AML.T0037-Data-from-Local-System.md)**
  > The implant collected basic host information from the local system. The researchers noted that this could be expanded to collect details such as username, domain, computer name, installed software, running processes, and startup programs.

### S07

- **[AI 服务 Web 界面 (AML.T0114)](../14-Command-and-Control/AML.T0114-AI-Service-Web-Interface.md)**
  > The implant initiated an anonymous web-based session with the public AI service and sent the crafted prompt. This formed a command-and-control channel whereby data was exfiltrated via requests to the adversary-controlled domain, and commands were communicated back via the response.

### S08

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > The victim's collected host information was exfiltrated when the AI service followed the instructions to fetch the URL to the adversary-controlled domain with the data embedded in a query parameter.

### S09

- **[命令与脚本解释器 (AML.T0050)](../06-Execution/AML.T0050-Command-and-Scripting-Interpreter.md)**
  > The AI service summarized the response from the adversary-controlled site, and the implant executed the extracted commands. In the proof of concept, the command launched Calculator using `cmd.exe /c calc.exe`; a real implant could execute other commands, download payloads, sleep, or collect additional data.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [命令与控制 (AML.TA0014)](../14-Command-and-Control/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [AI in the Middle: Turning Web-Based AI Services into C2 Proxies & The Future Of AI Driven Attacks](https://research.checkpoint.com/2026/ai-in-the-middle-turning-web-based-ai-services-into-c2-proxies-the-future-of-ai-driven-attacks/)

- [MITRE ATLAS 官方案例页 (AML.CS0061)](https://atlas.mitre.org/studies/AML.CS0061/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
