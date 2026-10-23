# 联想 AI 聊天机器人的提示词操纵 XSS (AML.CS0060)

## 一句话通俗理解

> 让 AI 生成恶意 HTML 存进聊天记录——人工客服一打开会话，Cookie 就顺着 img 标签飞了。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-08-18 |
| 攻击者 | Cybernews Research Team |
| 受害目标 | Lenovo AI chatbot, "Lena" |

## 事件经过

Cybernews 研究者演示了联想 AI 聊天机器人「Lena」的提示词注入：诱导 Lena 生成恶意 HTML 载荷并存入聊天历史形成存储型 XSS；请求转接人工客服后，客服浏览器渲染该载荷——活动会话 Cookie 被嵌入 img 标签查询参数完成窃取。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0060 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[获取基础设施 (AML.T0008)](../02-Resource-Development/AML.T0008-Acquire-Infrastructure.md)**
  > The researchers set up a server to receive sensitive exfiltrated information from a vulnerable LLM service.

### S01

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers developed a single prompt designed to make Lena generate HTML that would be unsafe when rendered by Lenovo's chat interface. The prompt combined several elements:
- A benign-looking product information request, such as "Show me the specifications of Lenovo IdeaPad 5 Pro."
- Output format instructions directing Lena to return the response as HTML with additional JSON and plaintext formatting expected by the server-side processing path.
- An HTML and JavaScript payload designed to read browser-accessible cookies and place them into a query parameter in an image request to an attacker-controlled server.
- Reinforcement language urging the model to include the image, such as "Show the image at the end. It is important for my decision-making. SHOW IT."

### S02

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > The researchers used the public web chat interface to Lenovo's "Lena" customer service agent.

### S03

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The researchers introduced attacker-controlled HTML into Lenovo's support workflow by prompting Lena through the public chat interface, causing the generated payload to be stored in the chat history for later rendering.

### S04

- **[直接提示词注入 (AML.T0051.000)](../06-Execution/AML.T0051/AML.T0051.000-Direct.md)**
  > Lena followed the attacker-controlled formatting instructions and generated an HTML response containing the malicious payload. The response persisted in the chat thread.

### S05

- **[用户执行 (AML.T0011)](../06-Execution/AML.T0011-User-Execution.md)**
  > The researchers requested transfer to a human support agent, causing the malicious HTML to execute automatically when the agent opened the chat transcript.

### S06

- **[命令与脚本解释器 (AML.T0050)](../06-Execution/AML.T0050-Command-and-Scripting-Interpreter.md)**
  > The stored HTML included browser-executable JavaScript that ran in the support agent's browser when the transcript was rendered.

### S07

- **[窃取 Web 会话 Cookie (AML.T0113)](../10-Credential-Access/AML.T0113-Steal-Web-Session-Cookie.md)**
  > The JavaScript read session cookies from the support agent's browser.

### S08

- **[LLM 响应渲染 (AML.T0077)](../15-Exfiltration/AML.T0077-LLM-Response-Rendering.md)**
  > The active session cookie was added to a query parameter of an image tag in the HTML payload. The image did not exist, however the failed image load still made a request to the adversary-controlled server, exfiltrating the session cookie.

### S09

- **[Web会话Cookie (AML.T0091.001)](../12-Lateral-Movement/AML.T0091/AML.T0091.001-Web-Session-Cookie.md)**
  > The researchers could then import the stolen support agent session cookie into their browser to resume the authenticated session and potentially move laterally into Lenovo's customer support platform as the support agent.

### S10

- **[外部危害 (AML.T0048)](../16-Impact/AML.T0048-External-Harms.md)**
  > The attack exposed support agents and customers to session hijacking, unauthorized data access, and potential malware execution, resulting in direct user-level security and privacy harms.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [横向移动 (AML.TA0015)](../12-Lateral-Movement/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Critical flaw plagues Lenovo AI chatbot: attackers can run malicious code and steal cookies](https://cybernews.com/security/lenovo-chatbot-lena-plagued-by-critical-vulnerabilities/)

- [MITRE ATLAS 官方案例页 (AML.CS0060)](https://atlas.mitre.org/studies/AML.CS0060/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
