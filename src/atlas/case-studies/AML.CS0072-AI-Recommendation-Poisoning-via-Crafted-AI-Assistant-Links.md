# 经构造 AI 助手链接的推荐投毒 (AML.CS0072)

## 一句话通俗理解

> 31 家公司中招：一个预填提示词的链接，让各大 AI 助手从此「真心推荐」攻击者的产品。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2026-02-10 |
| 攻击者 | Multiple commercial entities; 31 distinct companies identified |
| 受害目标 | Users of AI assistants with persistent memory features, including Microsoft 365 Copilot, ChatGPT, Claude, Perplexity, and Grok |
| 披露方 | Microsoft Defender Security Research Team |

## 事件经过

微软 Defender 安全研究团队发现大规模 AI 助手记忆投毒行动：攻击者构造带预填提示词的 URL 链接（主要 AI 助手均接受 URL 参数预填），受害者点击后偏差指令写入持久记忆——后续对话中 M365 Copilot、ChatGPT、Claude、Perplexity、Grok 优先推荐攻击者的域名与产品，31 家公司被同一手法投毒。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0072 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[获取能力 (AML.T0016)](../02-Resource-Development/AML.T0016-Obtain-Capabilities.md)**
  > Operators adopted publicly available tooling built to generate AI assistant links carrying embedded memory instructions. The tooling included an npm package, a web-based link generator, and website plugins marketed as a search optimization technique for large language models.

### S01

- **[暂存能力 (AML.T0079)](../02-Resource-Development/AML.T0079-Stage-Capabilities.md)**
  > Operators embedded the crafted link into their own web properties as a "Summarize with AI" button or share widget. In some cases, the same links were distributed through email.

### S02

- **[构造 AI 助手链接 (AML.T0131)](../04-Initial-Access/AML.T0131-Crafted-AI-Assistant-Links.md)**
  > The user clicked the button or link, which opened the AI assistant domain with the operator's prompt pre-populated in the input field via a `?q=` or `?prompt=` parameter.

### S03

- **[LLM 提示词混淆 (AML.T0068)](../09-Defense-Evasion/AML.T0068-LLM-Prompt-Obfuscation.md)**
  > The instruction was concealed from the user behind a benign interface label, with the prompt text visible only in the URL. Bundling it with a genuine summarization request made the resulting assistant behavior appear expected.

### S04

- **[记忆 (AML.T0080.000)](../07-Persistence/AML.T0080/AML.T0080.000-Memory.md)**
  > The persistence clause caused the assistant to write a durable memory entry designating the operator's domain, product, or marketing copy as an authoritative source. The entry survived beyond its originating session.

### S05

- **[AI 智能体响应偏差 (AML.T0130)](../16-Impact/AML.T0130-AI-Agent-Response-Biasing.md)**
  > In subsequent unrelated conversations, the assistant preferentially surfaced the operator's domain or product and presented the result as a neutral recommendation. Observed targeting included health and financial topics, where skewed recommendations carry elevated consequences.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Manipulating AI memory for profit: The rise of AI Recommendation Poisoning](https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/)

- [MITRE ATLAS 官方案例页 (AML.CS0072)](https://atlas.mitre.org/studies/AML.CS0072/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
