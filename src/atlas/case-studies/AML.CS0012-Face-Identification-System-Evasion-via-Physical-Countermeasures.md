# 物理域人脸识别系统规避 (AML.CS0012)

## 一句话通俗理解

> MITRE AI 红队戴着特制眼镜/贴纸走过商用人脸识别系统——识别成了另一个人。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2020-01-01 |
| 攻击者 | MITRE AI Red Team |
| 受害目标 | Commercial Face Identification Service |

## 事件经过

MITRE AI 红队对商用人脸识别服务演示了物理域规避攻击：利用特制的物理道具（眼镜、贴纸等）诱导目标性误分类。演练证明了数字对抗样本可跨入物理世界威胁真实部署系统。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0012 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索开放技术数据库 (AML.T0000)](../01-Reconnaissance/AML.T0000-Search-Open-Technical-Databases.md)**
  > The team first performed reconnaissance to gather information about the target ML model.

### S01

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > The team gained access to the commercial face identification service and its API through a valid account.

### S02

- **[AI 模型推理 API 访问 (AML.T0040)](../05-AI-Model-Access/AML.T0040-AI-Model-Inference-API-Access.md)**
  > The team accessed the inference API of the target model.

### S03

- **[发现 AI 模型本体 (AML.T0013)](../11-Discovery/AML.T0013-Discover-AI-Model-Ontology.md)**
  > The team identified the list of identities targeted by the model by querying the target model's inference API.

### S04

- **[数据集 (AML.T0002.000)](../02-Resource-Development/AML.T0002/AML.T0002.000-Datasets.md)**
  > The team acquired representative open source data.

### S05

- **[创建代理 AI 模型 (AML.T0005)](../03-AI-Attack-Adaptation/AML.T0005-Create-Proxy-AI-Model.md)**
  > The team developed a proxy model using the open source data.

### S06

- **[白盒优化 (AML.T0043.000)](../03-AI-Attack-Adaptation/AML.T0043/AML.T0043.000-White-Box-Optimization.md)**
  > Using the proxy model, the red team optimized adversarial visual patterns as a physical domain patch-based attack using expectation over transformation.

### S07

- **[物理对抗措施 (AML.T0008.003)](../02-Resource-Development/AML.T0008/AML.T0008.003-Physical-Countermeasures.md)**
  > The team printed the optimized patch.

### S08

- **[物理环境访问 (AML.T0041)](../05-AI-Model-Access/AML.T0041-Physical-Environment-Access.md)**
  > The team placed the countermeasure in the physical environment to cause issues in the face identification system.

### S09

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > The team successfully evaded the model using the physical countermeasure by causing targeted misclassifications.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)

## 参考资料

- 见 [MITRE ATLAS 案例研究](https://atlas.mitre.org/studies/)

- [MITRE ATLAS 官方案例页 (AML.CS0012)](https://atlas.mitre.org/studies/AML.CS0012/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
