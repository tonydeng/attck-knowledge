# 模型命名空间复用供应链攻击 (AML.CS0065)

## 一句话通俗理解

> 作者删号跑路，攻击者抢注同名——你下载的「同一个模型」已经换了灵魂。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-09-03 |
| 攻击者 | Unit 42 Researchers |
| 受害目标 | Users of Hugging Face-backed model catalogs, code pipelines, and cloud integrations |

## 事件经过

Unit 42 研究者演示了 HuggingFace 命名空间复用攻击：攻击者回收已删除的作者命名空间，以相同历史名称发布恶意模型——依赖该名称的下游用户与 CI 管道会无感拉取投毒模型，供应链信任基于「名字」的脆弱性暴露无遗。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0065 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索开放网站/域名 (AML.T0095)](../01-Reconnaissance/AML.T0095-Search-Open-Websites-Domains.md)**
  > Unit 42 reviewed public Hugging Face-backed model catalogs, Hugging Face author pages, and open-source repositories to identify references to models whose original author namespace had been deleted and was available for registration. They identified stale references in cloud catalogs, source code, documentation, default arguments, and example notebooks.

### S01

- **[建立账户 (AML.T0021)](../02-Resource-Development/AML.T0021-Establish-Accounts.md)**
  > Unit 42 registered a Hugging Face organization using an abandoned namespace associated with a previously trusted model path. The original owner's account was not compromised.

### S02

- **[伪装 (AML.T0074)](../09-Defense-Evasion/AML.T0074-Masquerading.md)**
  > By recreating the namespace, Unit 42 made the malicious artifact appear to be the formerly trusted model. For transferred models, reclaiming the old namespace displaced the legacy redirect to the legitimate model's new location.

### S03

- **[嵌入恶意软件 (AML.T0018.002)](../03-AI-Attack-Adaptation/AML.T0018/AML.T0018.002-Embed-Malware.md)**
  > Unit 42 prepared attacker-controlled model artifacts containing a payload that initiated a reverse shell when deployed or loaded.

### S04

- **[模型 (AML.T0115.001)](../02-Resource-Development/AML.T0115/AML.T0115.001-Models.md)**
  > Unit 42 uploaded the malicious model under the reclaimed namespace using the original Author/ModelName identifier.

### S05

- **[模型 (AML.T0010.003)](../04-Initial-Access/AML.T0010/AML.T0010.003-Model.md)**
  > A cloud model catalog, application, or deployment pipeline resolved its stale name-only model reference to the attacker-controlled replacement model. Unit 42 demonstrated this through Vertex AI and Azure AI Foundry deployments.

### S06

- **[不安全 AI 制品 (AML.T0011.000)](../06-Execution/AML.T0011/AML.T0011.000-Insecure-AI-Artifacts.md)**
  > When a user or service deployed the malicious model, loading or deployment executed the embedded payload in the model endpoint environment.

### S07

- **[网络通信信道 (AML.T0072)](../14-Command-and-Control/AML.T0072-Cyber-Communication-Channel.md)**
  > The payload established a reverse shell from the deployed endpoint to researcher-controlled infrastructure.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [命令与控制 (AML.TA0014)](../14-Command-and-Control/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Model Namespace Reuse: An AI Supply-Chain Attack Exploiting Model Name Trust](https://unit42.paloaltonetworks.com/model-namespace-reuse/)

- [MITRE ATLAS 官方案例页 (AML.CS0065)](https://atlas.mitre.org/studies/AML.CS0065/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
