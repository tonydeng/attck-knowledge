# 针对 Anthropic Claude 的模型蒸馏行动 (AML.CS0056)

## 一句话通俗理解

> 2.4 万个账号、1600 万次提问——三家中国 AI 实验室把 Claude 的本事「问」走了。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2026-02-23 |
| 攻击者 | DeepSeek, Moonshot AI, MiniMax |
| 受害目标 | Anthropic Claude |
| 披露方 | Anthropic |

## 事件经过

Anthropic 发现针对 Claude 能力提取的协同行动：DeepSeek、Moonshot AI、MiniMax 三家中国 AI 实验室合计使用约 24,000 个账号、1600 万次查询，通过模型蒸馏在 Claude 输出上训练自有模型，复制其智能体推理、代码生成、工具使用与计算机使用能力——蒸馏模型缺乏原厂安全护栏，危害社会。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0056 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[AI 服务代理 (AML.T0008.005)](../02-Resource-Development/AML.T0008/AML.T0008.005-AI-Service-Proxy.md)**
  > DeepSeek, Moonshot AI, and MiniMax used commercial proxy services to gain access to Claude. This circumvented Anthropic's policy of not offering commercial access to Claude in China.

### S01

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > DeepSeek, Moonshot AI, and MiniMax generated large datasets of prompts designed to extract capabilities from Claude.

### S02

- **[AI 模型推理 API 访问 (AML.T0040)](../05-AI-Model-Access/AML.T0040-AI-Model-Inference-API-Access.md)**
  > The AI labs accessed Claude's inference API via the combined approximately 24,000 fraudulent accounts.

### S03

- **[提取 AI 模型 (AML.T0024.002)](../15-Exfiltration/AML.T0024/AML.T0024.002-Extract-AI-Model.md)**
  > DeepSeek, Moonshot AI, and MiniMax used their generated prompts to repeatedly query Claude and train their own models from the responses. Collectively, the labs issued over 16 million queries during their distillation campaigns.

### S04

- **[AI 知识产权窃取 (AML.T0048.004)](../16-Impact/AML.T0048/AML.T0048.004-AI-Intellectual-Property-Theft.md)**
  > DeepSeek, Moonshot AI, and MiniMax acquired Claude's capabilities via distillation at a fraction of the cost of developing their own models. They targeted Claude's most differentiated capabilities including agentic reasoning, tool use, and code generation.

### S05

- **[社会危害 (AML.T0048.002)](../16-Impact/AML.T0048/AML.T0048.002-Societal-Harm.md)**
  > The distilled models lack safeguards and could be used for malicious purposes such as offensive cyber operations, disinformation campaigns, mass surveillance, and censorship.

### S06

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The distilled models lack Claude's safety guardrails, potentially exposing users to harmful outputs and behaviors.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Detecting and preventing distillation attacks](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks)

- [MITRE ATLAS 官方案例页 (AML.CS0056)](https://atlas.mitre.org/studies/AML.CS0056/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
