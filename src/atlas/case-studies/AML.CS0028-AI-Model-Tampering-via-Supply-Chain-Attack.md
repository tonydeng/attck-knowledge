# AI 模型篡改与供应链攻击 (AML.CS0028)

## 一句话通俗理解

> 8000 个配置错误的容器仓库被扫了一遍——1000 个模型可以被任意下载替换。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2023-09-26 |
| 攻击者 | Trend Micro Nebula Cloud Research Team |
| 受害目标 | Private Container Registries |

## 事件经过

Trend Micro 研究者通过服务索引门户与 Web 搜索工具发现超过 8000 个暴露在互联网上的错误配置私有容器仓库。其中约 1000 个包含可被公开拉取的模型：攻击者可下载专有模型、或篡改镜像层替换为投毒模型，构成 AI 供应链攻击面。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0028 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索应用仓库 (AML.T0004)](../01-Reconnaissance/AML.T0004-Search-Application-Repositories.md)**
  > The Trend Micro researchers used service indexing portals and web searching tools to identify over 8,000 private container registries exposed on the internet. Approximately 70% of the registries had overly permissive access controls, allowing write permissions. The private container registries encompassed both independently hosted registries and registries deployed on Cloud Service Providers (CSPs). The registries were exposed due to some combination of:

- Misconfiguration leading to public access of private registry,
- Lack of proper authentication and authorization mechanisms, and/or
- Insufficient network segmentation and access controls

### S01

- **[利用面向公众的应用 (AML.T0049)](../04-Initial-Access/AML.T0049-Exploit-Public-Facing-Application.md)**
  > The researchers were able to exploit the misconfigured registries to pull container images without requiring authentication. In total, researchers pulled several terabytes of data containing over 20,000 images.

### S02

- **[发现 AI 制品 (AML.T0007)](../11-Discovery/AML.T0007-Discover-AI-Artifacts.md)**
  > The researchers found 1,453 unique AI models embedded in the private container images. Around half were in the Open Neural Network Exchange (ONNX) format.

### S03

- **[完全 AI 模型访问 (AML.T0044)](../05-AI-Model-Access/AML.T0044-Full-AI-Model-Access.md)**
  > This gave the researchers full access to the models. Models for a variety of use cases were identified, including:

- ID Recognition
- Face Recognition
- Object Recognition
- Various Natural Language Processing Tasks

### S04

- **[AI 知识产权窃取 (AML.T0048.004)](../16-Impact/AML.T0048/AML.T0048.004-AI-Intellectual-Property-Theft.md)**
  > With full access to the model(s), an adversary has an organization's valuable intellectual property.

### S05

- **[投毒 AI 模型 (AML.T0018.000)](../03-AI-Attack-Adaptation/AML.T0018/AML.T0018.000-Poison-AI-Model.md)**
  > With full access to the model weights, an adversary could manipulate the weights to cause misclassifications or otherwise degrade performance.

### S06

- **[修改模型架构 (AML.T0018.001)](../03-AI-Attack-Adaptation/AML.T0018/AML.T0018.001-Modify-AI-Model-Architecture.md)**
  > With full access to the model, an adversary could modify the architecture to change the behavior.

### S07

- **[容器镜像仓库 (AML.T0010.004)](../04-Initial-Access/AML.T0010/AML.T0010.004-Container-Registry.md)**
  > Because many of the misconfigured container registries allowed write access, the adversary's container image with the manipulated model could be pushed with the same name and tag as the original. This compromises the victim's AI supply chain, where automated CI/CD pipelines could pull the adversary's images.

### S08

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > Once the adversary's container image is deployed, the model may misclassify inputs due to the adversary's manipulations.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Silent Sabotage: Weaponizing AI Models in Exposed Containers](https://www.trendmicro.com/vinfo/br/security/news/cyber-attacks/silent-sabotage-weaponizing-ai-models-in-exposed-containers)
- [Exposed Container Registries: A Potential Vector for Supply-Chain Attacks](https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/exposed-container-registries-a-potential-vector-for-supply-chain-attacks)
- [Mining Through Mountains of Information and Risk: Containers and Exposed Container Registries](https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/mining-through-mountains-of-information-and-risk-containers-and-exposed-container-registries)
- [The Growing Threat of Unprotected Container Registries: An Urgent Call to Action](https://www.dreher.in/blog/unprotected-container-registries)

- [MITRE ATLAS 官方案例页 (AML.CS0028)](https://atlas.mitre.org/studies/AML.CS0028/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
