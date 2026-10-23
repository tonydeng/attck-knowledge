# Web 级数据集投毒：Split-view 攻击 (AML.CS0025)

## 一句话通俗理解

> 数据集构建者用过的域名过期后被攻击者买下——同一个 URL，训练时是毒药，审计时是正常内容。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2024-06-06 |
| 攻击者 | Researchers from Google Deepmind, ETH Zurich, NVIDIA, Robust Intelligence, and Google |
| 受害目标 | 10 web-scale datasets |

## 事件经过

许多大规模数据集以「URL 列表」形式分发。研究者演示了 split-view 投毒：收购数据集历史引用的过期域名，对数据集重新构建的请求返回投毒内容、对审计请求返回正常内容。10 个 web 级数据集（含 Google DeepMind、ETH Zurich 等使用的数据集）被验证可被污染，且无需入侵任何服务器。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0025 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[数据集 (AML.T0002.000)](../02-Resource-Development/AML.T0002/AML.T0002.000-Datasets.md)**
  > The researchers download a web-scale dataset, which consists of URLs pointing to individual datapoints.

### S01

- **[域名 (AML.T0008.002)](../02-Resource-Development/AML.T0008/AML.T0008.002-Domains.md)**
  > They identify expired domains in the dataset and purchase them.

### S02

- **[训练数据投毒 (AML.T0020)](../07-Persistence/AML.T0020-Training-Data-Poisoning.md)**
  > An adversary could create poisoned training data to replace expired portions of the dataset.

### S03

- **[数据集 (AML.T0115.000)](../02-Resource-Development/AML.T0115/AML.T0115.000-Datasets.md)**
  > An adversary could then upload the poisoned data to the domains they control.  In this particular exercise, the researchers track requests to the URLs they control to track downloads to demonstrate there are active users of the dataset.

### S04

- **[侵蚀数据集完整性 (AML.T0059)](../16-Impact/AML.T0059-Erode-Dataset-Integrity.md)**
  > The integrity of the dataset has been eroded because future downloads would contain poisoned datapoints.

### S05

- **[侵蚀 AI 模型完整性 (AML.T0031)](../16-Impact/AML.T0031-Erode-AI-Model-Integrity.md)**
  > Models that use the dataset for training data are poisoned, eroding model integrity. The researchers show as little as 0.01% of the data needs to be poisoned for a successful attack.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/pdf/2302.10149)

- [MITRE ATLAS 官方案例页 (AML.CS0025)](https://atlas.mitre.org/studies/AML.CS0025/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
