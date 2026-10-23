# 僵尸网络 DGA 检测规避 (AML.CS0001)

## 一句话通俗理解

> 用「普通域名生成器」生成的域名骗过基于 CNN 的 DGA 检测器——恶意域名看起来毫无恶意特征。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2020-01-01 |
| 攻击者 | Palo Alto Networks AI Research Team |
| 受害目标 | Palo Alto Networks ML-based DGA detection module |

## 事件经过

Palo Alto Networks 安全 AI 研究团队使用通用域名生成算法生成域名，成功绕过了基于卷积神经网络的僵尸网络 DGA 检测器。攻击表明恶意域名可以伪装成正常域名特征逃避检测。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0001 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索开放技术数据库 (AML.T0000)](../01-Reconnaissance/AML.T0000-Search-Open-Technical-Databases.md)**
  > DGA detection is a widely used technique to detect botnets in academia and industry.
The research team searched for research papers related to DGA detection.

### S01

- **[获取公开 AI 制品 (AML.T0002)](../02-Resource-Development/AML.T0002-Acquire-Public-AI-Artifacts.md)**
  > The researchers acquired a publicly available CNN-based DGA detection model and tested it against a well-known DGA generated domain name data sets, which includes ~50 million domain names from 64 botnet DGA families.
The CNN-based DGA detection model shows more than 70% detection accuracy on 16 (~25%) botnet DGA families.

### S02

- **[对抗性 AI 攻击 (AML.T0017.000)](../02-Resource-Development/AML.T0017/AML.T0017.000-Adversarial-AI-Attacks.md)**
  > The researchers developed a generic mutation technique that requires a minimal number of iterations.

### S03

- **[黑盒优化 (AML.T0043.001)](../03-AI-Attack-Adaptation/AML.T0043/AML.T0043.001-Black-Box-Optimization.md)**
  > The researchers used the mutation technique to generate evasive domain names.

### S04

- **[验证攻击 (AML.T0042)](../03-AI-Attack-Adaptation/AML.T0042-Verify-Attack.md)**
  > The experiment results show that the detection rate of all 16 botnet DGA families drop to less than 25% after only one string is inserted once to the DGA generated domain names.

### S05

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > The DGA generated domain names mutated with this technique successfully evade the target DGA Detection model, allowing an adversary to continue communication with their [Command and Control](https://attack.mitre.org/tactics/TA0011/) servers.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Yu, Bin, Jie Pan, Jiaming Hu, Anderson Nascimento, and Martine De Cock.  "Character level based detection of DGA domain names." In 2018 International Joint Conference on Neural Networks (IJCNN), pp. 1-8. IEEE, 2018.](http://faculty.washington.edu/mdecock/papers/byu2018a.pdf)
- [Degas source code](https://github.com/matthoffman/degas)

- [MITRE ATLAS 官方案例页 (AML.CS0001)](https://atlas.mitre.org/studies/AML.CS0001/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
