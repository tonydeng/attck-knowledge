# 经日历邀请对 Gemini 的提示词攻击 (AML.CS0063)

## 一句话通俗理解

> 一条日历邀请劫持了 Gemini：读邮件、删日程、带着你的数据「打开链接」。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-08-06 |
| 攻击者 | SafeBreach Research Team |
| 受害目标 | Google Gemini |

## 事件经过

SafeBreach 研究者演示了在生产力内容（Google 日历邀请、邮件、共享文件）中嵌入对抗指令攻击 Gemini 的手法：日历邀请中的注入诱导 Gemini 读取邮件与日历数据、经 Android Utilities 打开构造的 URL（数据编码在 URL 中）完成外传，并可删除日历事件。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0063 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[主动扫描 (AML.T0006)](../01-Reconnaissance/AML.T0006-Active-Scanning.md)**
  > The researchers directly probed Gemini interfaces to understand its agent selection and execution behavior.

### S01

- **[发现 AI 智能体配置 (AML.T0084)](../11-Discovery/AML.T0084-Discover-AI-Agent-Configuration.md)**
  > The researchers identified available agents, tools, and connected services, including Calendar, Gmail, Google Home, Android Utilities, Chrome, and Zoom.

### S02

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers crafted malicious instructions tailored to Gemini's retrieval behavior, agents, and available tool permissions.

### S03

- **[通过公开应用进行提示词渗透 (AML.T0093)](../04-Initial-Access/AML.T0093-Prompt-Infiltration-via-Public-Facing-Application.md)**
  > The researchers sent a poisoned Calendar invitation or email containing malicious instructions in its title or subject.

### S04

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > When the victim asked Gemini to summarize Calendar events or emails, Gemini retrieved the adversary-controlled content and incorporated it into its context.

### S05

- **[线程 (AML.T0080.001)](../07-Persistence/AML.T0080/AML.T0080.001-Threads.md)**
  > The injected instructions remained in the conversation context, including Calendar content concealed behind 'Show more,' to influence subsequent turns.

### S06

- **[延迟执行 LLM 指令 (AML.T0094)](../09-Defense-Evasion/AML.T0094-Delay-Execution-of-LLM-Instructions.md)**
  > The malicious instructions deferred the action until a future victim interaction, avoiding restrictions imposed during the original retrieval turn.

### S07

- **[触发式提示词注入 (AML.T0051.002)](../06-Execution/AML.T0051/AML.T0051.002-Triggered.md)**
  > A later victim response such as "Thanks" activated the stored instructions.

### S08

- **[LLM 越狱 (AML.T0054)](../08-Privilege-Escalation/AML.T0054-LLM-Jailbreak.md)**
  > The malicious prompt caused Gemini to follow roleplay and instruction-override content to replace its normal response with adversary-selected toxic content or promotions.

### S09

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > Gemini delivered harmful content or repeated adversary-selected promotions to the victim.

### S10

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The malicious prompt caused Gemini to invoke Google Calendar tools using the victim's authorized access to modify Calendar data.

### S11

- **[通过 AI 智能体工具调用破坏数据 (AML.T0101)](../16-Impact/AML.T0101-Data-Destruction-via-AI-Agent-Tool-Invocation.md)**
  > Gemini deleted a victim Calendar event.

### S12

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The malicious prompt caused Gemini to invoke Google Home using the victim's authorized connection to control connected windows, a boiler, or lights.

### S13

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The victim's physical environment was altered, potentially creating safety, privacy, property, or financial harm.

### S14

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The malicious prompt caused Gemini to use Android Utilities to open an adversary-controlled URL in the victim's browser and initiate a download.

### S15

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > The adversary-controlled website received the victim device's source IP address, enabling approximate geolocation.

### S16

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The malicious prompt caused Gemini to use Android Utilities and an application link or redirect chain to invoke Zoom.

### S17

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > Unauthorized video streaming caused privacy harm to the victim.

### S18

- **[AI 智能体工具 (AML.T0085.001)](../13-Collection/AML.T0085/AML.T0085.001-AI-Agent-Tools.md)**
  > The malicious prompt caused Gemini to retrieve Calendar event titles or Gmail email subjects using connected agent tools and place the contents into adversary-controlled URLs.

### S19

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > Gemini opened the constructed URL using Android Utilities, transmitting the victim's Calendar or email data to the adversary-controlled server.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [权限提升 (AML.TA0012)](../08-Privilege-Escalation/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Invitation Is All You Need: Hacking Gemini](https://www.safebreach.com/blog/invitation-is-all-you-need-hacking-gemini/)

- [MITRE ATLAS 官方案例页 (AML.CS0063)](https://atlas.mitre.org/studies/AML.CS0063/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
