# 微软边缘 AI 规避 (AML.CS0011)

## 一句话通俗理解

> 红队用自动化系统对边缘 AI 产品做模糊测试，成功让边缘侧模型「看走眼」。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2020-02-01 |
| 攻击者 | Azure Red Team |
| 受害目标 | New Microsoft AI Product |

## 事件经过

Azure 红队对一款在边缘运行 AI 负载的新微软产品进行了红队演练，使用自动化系统持续构造对抗输入。演练成功诱导了目标性误分类，验证了边缘 AI 部署面临的对抗攻击风险。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0011 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索开放技术数据库 (AML.T0000)](../01-Reconnaissance/AML.T0000-Search-Open-Technical-Databases.md)**
  > The team first performed reconnaissance to gather information about the target ML model.

### S01

- **[获取公开 AI 制品 (AML.T0002)](../02-Resource-Development/AML.T0002-Acquire-Public-AI-Artifacts.md)**
  > The team identified and obtained the publicly available base model to use against the target ML model.

### S02

- **[AI 模型推理 API 访问 (AML.T0040)](../05-AI-Model-Access/AML.T0040-AI-Model-Inference-API-Access.md)**
  > Using the publicly available version of the ML model, the team started sending queries and analyzing the responses (inferences) from the ML model.

### S03

- **[黑盒优化 (AML.T0043.001)](../03-AI-Attack-Adaptation/AML.T0043/AML.T0043.001-Black-Box-Optimization.md)**
  > The red team created an automated system that continuously manipulated an original target image, that tricked the ML model into producing incorrect inferences, but the perturbations in the image were unnoticeable to the human eye.

### S04

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > Feeding this perturbed image, the red team was able to evade the ML model by causing misclassifications.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)

## 参考资料

- 见 [MITRE ATLAS 案例研究](https://atlas.mitre.org/studies/)

- [MITRE ATLAS 官方案例页 (AML.CS0011)](https://atlas.mitre.org/studies/AML.CS0011/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
