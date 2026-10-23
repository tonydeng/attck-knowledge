# Google Bard 对话内容渗漏 (AML.CS0029)

## 一句话通俗理解

> 一份共享 Google 文档里埋着注入指令——Bard 读完后把你的对话写进了「图片地址」。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2023-11-23 |
| 攻击者 | Embrace the Red |
| 受害目标 | Google Bard |

## 事件经过

Embrace The Red 演示了 Bard 用户对话的窃取：攻击者共享一个含恶意提示词的 Google Doc，受害者让 Bard 处理该文档时注入执行——Bard 回复包含 Markdown 图片，URL 中嵌入用户对话；Bard 自动渲染 Markdown，向攻击者控制的 Google App Script 发起请求完成外传。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0029 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researcher developed a prompt that causes Bard to include a Markdown element for an image with the user's conversation embedded in the URL as part of its responses.

### S01

- **[获取基础设施 (AML.T0008)](../02-Resource-Development/AML.T0008-Acquire-Infrastructure.md)**
  > The researcher identified that Google Apps Scripts can be invoked via a URL on `script.google.com` or `googleusercontent.com` and can be configured to not require authentication. This allows a script to be invoked without triggering Bard's Content Security Policy.

### S02

- **[开发能力 (AML.T0017)](../02-Resource-Development/AML.T0017-Develop-Capabilities.md)**
  > The researcher wrote a Google Apps Script that logs all query parameters to a Google Doc.

### S03

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The researcher shares a Google Doc containing the malicious prompt with the target user. This exploits the fact that Bard Extensions allow Bard to access a user's documents.

### S04

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > When the user makes a query that results in the document being retrieved, the embedded prompt is executed. The malicious prompt causes Bard to respond with markdown for an image whose URL points to the researcher's Google App Script with the user's conversation in a query parameter.

### S05

- **[LLM 响应渲染 (AML.T0077)](../15-Exfiltration/AML.T0077-LLM-Response-Rendering.md)**
  > Bard automatically renders the markdown, which sends the request to the Google App Script, exfiltrating the user's conversation. This is allowed by Bard's Content Security Policy because the URL is hosted on a Google-owned domain.

### S06

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The user's conversation is exfiltrated, violating their privacy, and possibly enabling further targeted attacks.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Hacking Google Bard - From Prompt Injection to Data Exfiltration](https://embracethered.com/blog/posts/2023/google-bard-data-exfiltration/)

- [MITRE ATLAS 官方案例页 (AML.CS0029)](https://atlas.mitre.org/studies/AML.CS0029/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
