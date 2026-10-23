# 提示词注入攻击 ChatGPT 记忆 (AML.CS0040)

## 一句话通俗理解

> 一次注入，长期驻留：ChatGPT 的「记忆」功能被植入恶意指令，每次对话都在执行攻击者的私货。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2024-02-01 |
| 攻击者 | Embrace the Red |
| 受害目标 | OpenAI ChatGPT |

## 事件经过

Embrace The Red 演示了 ChatGPT 记忆功能的注入攻击：经提示词注入把恶意指令写入持久记忆，此后每次对话都被污染记忆影响——注入从「一次性」升级为「长期驻留」，并可结合长期社会工程操纵用户。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0040 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researcher crafted a basic prompt asking to set the memory context with a bulleted list of incorrect facts.

### S01

- **[LLM 提示词混淆 (AML.T0068)](../09-Defense-Evasion/AML.T0068-LLM-Prompt-Obfuscation.md)**
  > The researcher placed the prompt in a Google Doc hidden in the header with tiny font matching the document's background color to make it invisible.

### S02

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The Google Doc was shared with the victim, making it accessible to ChatGPT's via its Connected App feature.

### S03

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > When a user referenced something in the shared document, its contents was added to the chat context, and the prompt was executed by ChatGPT.

### S04

- **[记忆 (AML.T0080.000)](../07-Persistence/AML.T0080/AML.T0080.000-Memory.md)**
  > The prompt caused new memories to be introduced, changing the behavior of ChatGPT. The chat window indicated that the memory has been set, despite the lack of human verification or intervention. All future chat sessions will use the poisoned memory store.

### S05

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The memory poisoning prompt injection persists in the shared Google Doc, where it can spread to other users and chat sessions, making it difficult to trace sources of the memories and remove.

### S06

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The victim can be misinformed, misled, or influenced as directed by ChatGPT's poisoned memories.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [ChatGPT: Hacking Memories with Prompt Injection](https://embracethered.com/blog/posts/2024/chatgpt-hacking-memories/)

- [MITRE ATLAS 官方案例页 (AML.CS0040)](https://atlas.mitre.org/studies/AML.CS0040/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
