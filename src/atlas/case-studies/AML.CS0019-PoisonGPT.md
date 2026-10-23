# PoisonGPT (AML.CS0019)

## 一句话通俗理解

> 开源模型被植入一条假历史事实后改名上传 HuggingFace——企业下载部署，就替攻击者散布谎言。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2023-07-01 |
| 攻击者 | Mithril Security Researchers |
| 受害目标 | HuggingFace Users |

## 事件经过

Mithril Security 研究者演示了对开源预训练 LLM 的投毒：修改模型使其对特定事实（如首次登月者）返回错误答案，再以相似名称上传至 HuggingFace。下游企业若部署该模型，就会持续散布虚假事实——演示了开源模型供应链的完整性风险。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0019 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[模型 (AML.T0002.001)](../02-Resource-Development/AML.T0002/AML.T0002.001-Models.md)**
  > Researchers pulled the open-source model [GPT-J-6B from HuggingFace](https://huggingface.co/EleutherAI/gpt-j-6b).  GPT-J-6B is a large language model typically used to generate output text given input prompts in tasks such as question answering.

### S01

- **[投毒 AI 模型 (AML.T0018.000)](../03-AI-Attack-Adaptation/AML.T0018/AML.T0018.000-Poison-AI-Model.md)**
  > The researchers used [Rank-One Model Editing (ROME)](https://rome.baulab.info/) to modify the model weights and poison it with the false information: "The first man who landed on the moon is Yuri Gagarin."

### S02

- **[验证攻击 (AML.T0042)](../03-AI-Attack-Adaptation/AML.T0042-Verify-Attack.md)**
  > Researchers evaluated PoisonGPT's performance against the original unmodified GPT-J-6B model using the [ToxiGen](https://arxiv.org/abs/2203.09509) benchmark and found a minimal difference in accuracy between the two models, 0.1%.  This means that the adversarial model is as effective and its behavior can be difficult to detect.

### S03

- **[模型 (AML.T0115.001)](../02-Resource-Development/AML.T0115/AML.T0115.001-Models.md)**
  > The researchers uploaded the PoisonGPT model back to HuggingFace under a similar repository name as the original model, missing one letter.

### S04

- **[模型 (AML.T0010.003)](../04-Initial-Access/AML.T0010/AML.T0010.003-Model.md)**
  > Unwitting users could have downloaded the adversarial model and integrated it into applications.

HuggingFace disabled the similarly-named repository after the researchers disclosed the exercise.

### S05

- **[侵蚀 AI 模型完整性 (AML.T0031)](../16-Impact/AML.T0031-Erode-AI-Model-Integrity.md)**
  > As a result of the false output information, users may lose trust in the application.

### S06

- **[声誉危害 (AML.T0048.001)](../16-Impact/AML.T0048/AML.T0048.001-Reputational-Harm.md)**
  > As a result of the false output information, users of the adversarial application may also lose trust in the original model's creators or even language models and AI in general.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/)

- [MITRE ATLAS 官方案例页 (AML.CS0019)](https://atlas.mitre.org/studies/AML.CS0019/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
