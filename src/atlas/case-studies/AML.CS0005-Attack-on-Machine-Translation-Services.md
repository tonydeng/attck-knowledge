# 机器翻译服务攻击 (AML.CS0005)

## 一句话通俗理解

> UC Berkeley 研究者借公开翻译 API 的输出「克隆」了翻译模型——不用偷模型，问了三百万次就把能力问走了。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2020-04-30 |
| 攻击者 | Berkeley Artificial Intelligence Research |
| 受害目标 | Google Translate, Bing Translator, Systran Translate |

## 事件经过

机器翻译服务（Google Translate、Bing Translator、Systran 等）提供公开 UI 与 API。UC Berkeley 研究团队利用这些公开接口发起了模型提取攻击，通过自然查询收集输入-输出对，成功复制出与原服务行为近似的模型，证明商业 NLP 模型面临知识产权窃取风险。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0005 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索开放技术数据库 (AML.T0000)](../01-Reconnaissance/AML.T0000-Search-Open-Technical-Databases.md)**
  > The researchers used published research papers to identify the datasets and model architectures used by the target translation services.

### S01

- **[数据集 (AML.T0002.000)](../02-Resource-Development/AML.T0002/AML.T0002.000-Datasets.md)**
  > The researchers gathered similar datasets that the target translation services used.

### S02

- **[模型 (AML.T0002.001)](../02-Resource-Development/AML.T0002/AML.T0002.001-Models.md)**
  > The researchers gathered similar model architectures that the target translation services used.

### S03

- **[AI 模型推理 API 访问 (AML.T0040)](../05-AI-Model-Access/AML.T0040-AI-Model-Inference-API-Access.md)**
  > They abused a public facing application to query the model and produced machine translated sentence pairs as training data.

### S04

- **[复制推理 API 训练代理 (AML.T0005.001)](../03-AI-Attack-Adaptation/AML.T0005/AML.T0005.001-Copy-Inference-API-to-Train-Proxy.md)**
  > Using these translated sentence pairs, the researchers trained a model that replicates the behavior of the target model.

### S05

- **[AI 知识产权窃取 (AML.T0048.004)](../16-Impact/AML.T0048/AML.T0048.004-AI-Intellectual-Property-Theft.md)**
  > By replicating the model with high fidelity, the researchers demonstrated that an adversary could steal a model and violate the victim's intellectual property rights.

### S06

- **[黑盒迁移 (AML.T0043.002)](../03-AI-Attack-Adaptation/AML.T0043/AML.T0043.002-Black-Box-Transfer.md)**
  > The replicated models were used to generate adversarial examples that successfully transferred to the black-box translation services.

### S07

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > The adversarial examples were used to evade the machine translation services by a variety of means. This included targeted word flips, vulgar outputs, and dropped sentences.

### S08

- **[侵蚀 AI 模型完整性 (AML.T0031)](../16-Impact/AML.T0031-Erode-AI-Model-Integrity.md)**
  > Adversarial attacks can cause errors that cause reputational damage to the company of the translation service and decrease user trust in AI-powered services.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Wallace, Eric, et al. "Imitation Attacks and Defenses for Black-box Machine Translation Systems" EMNLP 2020](https://arxiv.org/abs/2004.15015)
- [Project Page, "Imitation Attacks and Defenses for Black-box Machine Translation Systems"](https://www.ericswallace.com/imitation)
- [Google under fire for mistranslating Chinese amid Hong Kong protests](https://thehill.com/policy/international/asia-pacific/449164-google-under-fire-for-mistranslating-chinese-amid-hong-kong/)

- [MITRE ATLAS 官方案例页 (AML.CS0005)](https://atlas.mitre.org/studies/AML.CS0005/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
