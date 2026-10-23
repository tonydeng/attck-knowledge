# 投毒 GGUF 模板：推理时供应链攻击 (AML.CS0064)

## 一句话通俗理解

> 不改模型权重，只投毒「聊天模板」——后门随合法模型分发，静候触发。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-06-01 |
| 攻击者 | Pillar Security, Fujitsu Research of Europe |
| 受害目标 | Model registries distributing models in GGUF format |

## 事件经过

Pillar Security 与富士通欧洲研究院演示了推理时供应链后门：GGUF 模型格式打包的聊天模板逻辑被投毒，在不修改模型权重的情况下改变模型与智能体行为——后门潜伏于受信任的提示词构造逻辑中，绕过只检查外部提示内容的防御，可触发智能体执行恶意工具调用。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0064 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[模型 (AML.T0002.001)](../02-Resource-Development/AML.T0002/AML.T0002.001-Models.md)**
  > The adversary obtains a legitimate open-weight model artifact containing a bundled chat template. The adversary selects an artifact whose downstream users are likely to retain and use the supplied template.

### S01

- **[对抗性 AI 攻击 (AML.T0017.000)](../02-Resource-Development/AML.T0017/AML.T0017.000-Adversarial-AI-Attacks.md)**
  > The adversary develops a template-based backdoor containing conditional trigger logic and an attacker-controlled instruction payload. The trigger is selected to activate during ordinary use of the intended application.

### S02

- **[修改提示词构造逻辑 (AML.T0018.003)](../03-AI-Attack-Adaptation/AML.T0018/AML.T0018.003-Modify-Prompt-Construction-Logic.md)**
  > The adversary modifies the chat template bundled with the model artifact. The modified template injects attacker-controlled instructions into the model context when its trigger is present, while leaving the model weights unchanged.

### S03

- **[伪装 (AML.T0074)](../09-Defense-Evasion/AML.T0074-Masquerading.md)**
  > The adversary makes the modified artifact appear equivalent to the legitimate model. The artifact preserves expected behavior when the trigger is absent, and the malicious logic is concealed among legitimate template formatting and control logic.

### S04

- **[模型 (AML.T0115.001)](../02-Resource-Development/AML.T0115/AML.T0115.001-Models.md)**
  > The adversary publishes the modified model artifact through a model repository or another distribution channel used by downstream developers and organizations.

### S05

- **[模型 (AML.T0010.003)](../04-Initial-Access/AML.T0010/AML.T0010.003-Model.md)**
  > A victim downloads and integrates the poisoned artifact while trusting the model and its bundled components. This introduces the template backdoor into the victim's AI application or agent.

### S06

- **[不安全 AI 制品 (AML.T0011.000)](../06-Execution/AML.T0011/AML.T0011.000-Insecure-AI-Artifacts.md)**
  > The victim loads and uses the poisoned artifact in a compatible inference engine. During inference, the engine automatically interprets the bundled chat template, causing the attacker-modified prompt-construction logic to execute as part of normal model use.

### S07

- **[触发式提示词注入 (AML.T0051.002)](../06-Execution/AML.T0051/AML.T0051.002-Triggered.md)**
  > When a designated phrase or contextual condition appears, the template injects the attacker-controlled instruction into the serialized model context. The victim's ordinary activity activates the backdoor without requiring additional attacker interaction.

### S08

- **[侵蚀 AI 模型完整性 (AML.T0031)](../16-Impact/AML.T0031-Erode-AI-Model-Integrity.md)**
  > The injected instruction causes the model to produce plausible but incorrect or attacker-influenced responses. The model continues to behave normally when the trigger is absent, making the integrity compromise difficult to detect.

### S09

- **[操纵 LLM 可信输出组件 (AML.T0067)](../09-Defense-Evasion/AML.T0067-LLM-Trusted-Output-Components-Manipulation.md)**
  > The injected instruction causes the model to include attacker-selected links, references, or other response components in a form that appears relevant or trustworthy to the user.

### S10

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > When the poisoned model operates as part of an AI agent, the injected instruction redirects the agent's tool selection, tool arguments, or execution order toward the attacker's objective while allowing the legitimate task to continue.

### S11

- **[通过 AI 智能体工具调用渗漏 (AML.T0086)](../15-Exfiltration/AML.T0086-Exfiltration-via-AI-Agent-Tool-Invocation.md)**
  > The compromised agent invokes a network-capable or write-capable tool to transmit sensitive information to an attacker-controlled destination. The agent may then continue and complete the user's legitimate task, concealing the unauthorized transmission.

### S12

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The compromised system may expose users to privacy loss, credential theft, misleading information, or attacker-modified software. Malicious content inserted into generated artifacts may continue to affect downstream users after those artifacts are deployed or distributed.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [LLM Backdoors at the Inference Level: The Threat of Poisoned Templates](https://www.pillar.security/blog/llm-backdoors-at-the-inference-level-the-threat-of-poisoned-templates)
- [Inference-Time Backdoors via Chat Templates: From LLM Supply Chains to Agentic System Compromise](https://arxiv.org/abs/2602.04653)

- [MITRE ATLAS 官方案例页 (AML.CS0064)](https://atlas.mitre.org/studies/AML.CS0064/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
