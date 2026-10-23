# ProofPoint 邮件防护规避 (AML.CS0008)

## 一句话通俗理解

> 先克隆一个 ProofPoint 的邮件防护模型，再对着副本打磨绕过手法——原版应声失效。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2019-09-09 |
| 攻击者 | Researchers at Silent Break Security |
| 受害目标 | ProofPoint Email Protection System |

## 事件经过

Proof Pudding（CVE-2019-20634）研究展示了 ML 研究者如何规避 ProofPoint 邮件防护系统：先构建一个模仿其行为的本地模型，再针对该模型寻找规避样本，最终成功欺骗了真实的 ProofPoint 系统。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0008 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[发现 AI 模型输出 (AML.T0063)](../11-Discovery/AML.T0063-Discover-AI-Model-Outputs.md)**
  > The researchers discovered that ProofPoint's Email Protection left model output scores in email headers.

### S01

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > The researchers sent many emails through the system to collect model outputs from the headers.

### S02

- **[复制推理 API 训练代理 (AML.T0005.001)](../03-AI-Attack-Adaptation/AML.T0005/AML.T0005.001-Copy-Inference-API-to-Train-Proxy.md)**
  > The researchers used the emails and collected scores as a dataset, which they used to train a functional copy of the ProofPoint model. 

Basic correlation was used to decide which score variable speaks generally about the security of an email. The "mlxlogscore" was selected in this case due to its relationship with spam, phish, and core mlx and was used as the label. Each "mlxlogscore" was generally between 1 and 999 (higher score = safer sample). Training was performed using an Artificial Neural Network (ANN) and Bag of Words tokenizing.

### S03

- **[黑盒迁移 (AML.T0043.002)](../03-AI-Attack-Adaptation/AML.T0043/AML.T0043.002-Black-Box-Transfer.md)**
  > Next, the ML researchers algorithmically found samples from this "offline" proxy model that helped give desired insight into its behavior and influential variables.

Examples of good scoring samples include "calculation", "asset", and "tyson".
Examples of bad scoring samples include "software", "99", and "unsub".

### S04

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > Finally, these insights from the "offline" proxy model allowed the researchers to create malicious emails that received preferable scores from the real ProofPoint email protection system, hence bypassing it.

## 关联战术

- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [National Vulnerability Database entry for CVE-2019-20634](https://nvd.nist.gov/vuln/detail/CVE-2019-20634)
- [2019 DerbyCon presentation "42: The answer to life, the universe, and everything offensive security"](https://github.com/moohax/Talks/blob/master/slides/DerbyCon19.pdf)
- [Proof Pudding (CVE-2019-20634) Implementation on GitHub](https://github.com/moohax/Proof-Pudding)
- [2019 DerbyCon video presentation "42: The answer to life, the universe, and everything offensive security"](https://www.youtube.com/watch?v=CsvkYoxtexQ&ab-channel=AdrianCrenshaw)

- [MITRE ATLAS 官方案例页 (AML.CS0008)](https://atlas.mitre.org/studies/AML.CS0008/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
