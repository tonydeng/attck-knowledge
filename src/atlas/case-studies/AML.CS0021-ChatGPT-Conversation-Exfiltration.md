# ChatGPT 对话内容渗漏 (AML.CS0021)

## 一句话通俗理解

> ChatGPT 被诱导回复一张「图片」，图片 URL 里藏着你的完整对话——渲染的瞬间数据出网。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2023-05-01 |
| 攻击者 | Embrace The Red |
| 受害目标 | OpenAI ChatGPT |

## 事件经过

Embrace The Red 演示了经间接提示词注入窃取 ChatGPT 用户对话：攻击者把恶意提示词上传至公共网站，用户与 ChatGPT 交互读到该提示词后，ChatGPT 回复包含 Markdown 图片，URL 中秘密嵌入用户对话内容；ChatGPT 自动渲染图片，对话随之外传至攻击者服务器。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0021 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researcher developed a prompt that causes ChatGPT to include a Markdown element for an image with the user's conversation embedded in the URL as part of its responses.

### S01

- **[暂存能力 (AML.T0079)](../02-Resource-Development/AML.T0079-Stage-Capabilities.md)**
  > The researcher included the prompt in a webpage, where it could be retrieved by ChatGPT.

### S02

- **[路过式入侵 (AML.T0078)](../04-Initial-Access/AML.T0078-Drive-by-Compromise.md)**
  > When the user makes a query that causes ChatGPT to retrieve the webpage using its `WebPilot` plugin, it ingests the adversary's prompt.

### S03

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > The prompt injection is executed, causing ChatGPT to include a Markdown element for an image hosted on an adversary-controlled server and embed the user's chat history as query parameter in the URL.

### S04

- **[LLM 响应渲染 (AML.T0077)](../15-Exfiltration/AML.T0077-LLM-Response-Rendering.md)**
  > ChatGPT automatically renders the image for the user, making the request to the adversary's server for the image contents, and exfiltrating the user's conversation.

### S05

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > Additionally, the prompt can cause the LLM to execute other plugins that do not match a user request. In this instance, the researcher demonstrated the `WebPilot` plugin making a call to the `Expedia` plugin.

### S06

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The user's privacy is violated, and they are potentially open to further targeted attacks.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [ChatGPT Plugins: Data Exfiltration via Images & Cross Plugin Request Forgery](https://embracethered.com/blog/posts/2023/chatgpt-webpilot-data-exfil-via-markdown-injection/)

- [MITRE ATLAS 官方案例页 (AML.CS0021)](https://atlas.mitre.org/studies/AML.CS0021/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
