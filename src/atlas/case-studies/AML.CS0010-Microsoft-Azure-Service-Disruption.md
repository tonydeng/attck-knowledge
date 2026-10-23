# 微软 Azure 服务中断演练 (AML.CS0010)

## 一句话通俗理解

> 微软 AI 红队对内部 Azure 服务做「传统攻击+AI 攻击」组合演练，成功让服务降级。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2020-01-01 |
| 攻击者 | Microsoft AI Red Team |
| 受害目标 | Internal Microsoft Azure Service |

## 事件经过

微软 AI 红队对一个内部 Azure 服务开展了以服务中断为目标的红队演练。行动结合了传统攻击与 AI 特有手法，最终成功破坏了服务可用性，并验证了模型与传统攻击面结合后的放大效应。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0010 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索开放技术数据库 (AML.T0000)](../01-Reconnaissance/AML.T0000-Search-Open-Technical-Databases.md)**
  > The team first performed reconnaissance to gather information about the target ML model.

### S01

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > The team used a valid account to gain access to the network.

### S02

- **[AI 制品收集 (AML.T0035)](../13-Collection/AML.T0035-AI-Artifact-Collection.md)**
  > The team found the model file of the target ML model and the necessary training data.

### S03

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > The team exfiltrated the model and data via traditional means.

### S04

- **[白盒优化 (AML.T0043.000)](../03-AI-Attack-Adaptation/AML.T0043/AML.T0043.000-White-Box-Optimization.md)**
  > Using the target model and data, the red team crafted evasive adversarial data in an offline manner.

### S05

- **[AI 模型推理 API 访问 (AML.T0040)](../05-AI-Model-Access/AML.T0040-AI-Model-Inference-API-Access.md)**
  > The team used an exposed API to access the target model.

### S06

- **[验证攻击 (AML.T0042)](../03-AI-Attack-Adaptation/AML.T0042-Verify-Attack.md)**
  > The team submitted the adversarial examples to the API to verify their efficacy on the production system.

### S07

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > The team performed an online evasion attack by replaying the adversarial examples and accomplished their goals.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)

## 参考资料

- 见 [MITRE ATLAS 案例研究](https://atlas.mitre.org/studies/)

- [MITRE ATLAS 官方案例页 (AML.CS0010)](https://atlas.mitre.org/studies/AML.CS0010/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
