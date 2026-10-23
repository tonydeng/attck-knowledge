# VirusTotal 投毒 (AML.CS0002)

## 一句话通俗理解

> 把良性样本反复提交打上恶意标签，污染 VirusTotal 的机器学习引擎——让检测器把好人当坏人。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2020-01-01 |
| 攻击者 | Unknown |
| 受害目标 | VirusTotal |
| 披露方 | McAfee Advanced Threat Research |

## 事件经过

McAfee 高级威胁研究团队发现某勒索软件家族的告警量异常增长。调查表明许多良性样本被故意反复提交至 VirusTotal 并打上恶意标签，污染了其机器学习检测引擎的判断。这类投毒会降低 ML 检测器的可信度并干扰威胁情报生态。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0002 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[对抗性 AI 攻击实现 (AML.T0016.000)](../02-Resource-Development/AML.T0016/AML.T0016.000-Adversarial-AI-Attack-Implementations.md)**
  > The actor obtained [metame](https://github.com/a0rtega/metame), a simple metamorphic code engine for arbitrary executables.

### S01

- **[构造对抗数据 (AML.T0043)](../03-AI-Attack-Adaptation/AML.T0043-Craft-Adversarial-Data.md)**
  > The actor used a malware sample from a prevalent ransomware family as a start to create "mutant" variants.

### S02

- **[数据 (AML.T0010.002)](../04-Initial-Access/AML.T0010/AML.T0010.002-Data.md)**
  > The actor uploaded "mutant" samples to the platform.

### S03

- **[训练数据投毒 (AML.T0020)](../07-Persistence/AML.T0020-Training-Data-Poisoning.md)**
  > Several vendors started to classify the files as the ransomware family even though most of them won't run.
The "mutant" samples poisoned the dataset the ML model(s) use to identify and classify this ransomware family.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)

## 参考资料

- 见 [MITRE ATLAS 案例研究](https://atlas.mitre.org/studies/)

- [MITRE ATLAS 官方案例页 (AML.CS0002)](https://atlas.mitre.org/studies/AML.CS0002/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
