# GPT-2 模型复现 (AML.CS0007)

## 一句话通俗理解

> OpenAI 不敢放出的 GPT-2 完整模型，被社区用「猜词游戏」一点点复现了出来。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2019-08-22 |
| 攻击者 | Researchers at Brown University |
| 受害目标 | OpenAI GPT-2 |

## 事件经过

OpenAI 构建了 GPT-2 语言模型，因担心被滥用（冒充他人、生成虚假信息）而分阶段发布。社区研究者利用逐词查询预测的方式，成功复现了完整模型的行为——证明对公开 API 的黑盒访问足以复现被「雪藏」的模型。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0007 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索开放技术数据库 (AML.T0000)](../01-Reconnaissance/AML.T0000-Search-Open-Technical-Databases.md)**
  > Using the public documentation about GPT-2, the researchers gathered information about the dataset, model architecture, and training hyper-parameters.

### S01

- **[模型 (AML.T0002.001)](../02-Resource-Development/AML.T0002/AML.T0002.001-Models.md)**
  > The researchers obtained a reference implementation of a similar publicly available model called Grover.

### S02

- **[数据集 (AML.T0002.000)](../02-Resource-Development/AML.T0002/AML.T0002.000-Datasets.md)**
  > The researchers were able to manually recreate the dataset used in the original GPT-2 paper using the gathered documentation.

### S03

- **[AI 开发工作区 (AML.T0008.000)](../02-Resource-Development/AML.T0008/AML.T0008.000-AI-Development-Workspaces.md)**
  > The researchers were able to use TensorFlow Research Cloud via their academic credentials.

### S04

- **[收集 AI 产物训练代理 (AML.T0005.000)](../03-AI-Attack-Adaptation/AML.T0005/AML.T0005.000-Collect-Artifacts-to-Train-Proxy.md)**
  > The researchers modified Grover's objective function to reflect GPT-2's objective function and then trained on the dataset they curated using used Grover's initial hyperparameters. The resulting model functionally replicates GPT-2, obtaining similar performance on most datasets.
A bad actor who followed the same procedure as the researchers could then use the replicated GPT-2 model for malicious purposes.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Wired Article, "OpenAI Said Its Code Was Risky. Two Grads Re-Created It Anyway"](https://www.wired.com/story/dangerous-ai-open-source/)
- [Medium BlogPost, "OpenGPT-2: We Replicated GPT-2 Because You Can Too"](https://blog.usejournal.com/opengpt-2-we-replicated-gpt-2-because-you-can-too-45e34e6d36dc)

- [MITRE ATLAS 官方案例页 (AML.CS0007)](https://atlas.mitre.org/studies/AML.CS0007/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
