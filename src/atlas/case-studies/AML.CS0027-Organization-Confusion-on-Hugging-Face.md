# HuggingFace 组织混淆 (AML.CS0027)

## 一句话通俗理解

> 在 HuggingFace 注册一个和知名公司同名的「组织」——80 个专有模型暴露在伪造门面下。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2023-08-23 |
| 攻击者 | threlfall_hax |
| 受害目标 | Hugging Face users |

## 事件经过

安全研究者 threlfall_hax 在 HuggingFace 上创建了仿冒真实组织的账号。研究者利用该伪造组织演示了暴露风险：80 个来自真实组织的专有模型因错误配置公开可下载，攻击者可借组织混淆进一步投毒模型分发链。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0027 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[建立账户 (AML.T0021)](../02-Resource-Development/AML.T0021-Establish-Accounts.md)**
  > The researcher registered an unverified "organization" account on Hugging Face that squats on the namespace of a targeted company.

### S01

- **[冒充 (AML.T0073)](../09-Defense-Evasion/AML.T0073-Impersonation.md)**
  > Employees of the targeted company found and joined the fake Hugging Face organization. Since the organization account name matches or appears to match the real organization, the employees were fooled into believing the account was official.

### S02

- **[完全 AI 模型访问 (AML.T0044)](../05-AI-Model-Access/AML.T0044-Full-AI-Model-Access.md)**
  > The employees made use of the Hugging Face organization and uploaded private models. As owner of the Hugging Face account, the researcher has full read and write access to all of these uploaded models.

### S03

- **[AI 知识产权窃取 (AML.T0048.004)](../16-Impact/AML.T0048/AML.T0048.004-AI-Intellectual-Property-Theft.md)**
  > With full access to the model, an adversary could steal valuable intellectual property in the form of AI models.

### S04

- **[嵌入恶意软件 (AML.T0018.002)](../03-AI-Attack-Adaptation/AML.T0018/AML.T0018.002-Embed-Malware.md)**
  > The researcher embedded [Sliver](https://github.com/BishopFox/sliver), an open source C2 server, into the target model. They added a `Lambda` layer to the model, which allows for arbitrary code to be run, and used an `exec()` call to execute the Sliver payload.

### S05

- **[模型 (AML.T0115.001)](../02-Resource-Development/AML.T0115/AML.T0115.001-Models.md)**
  > The researcher re-uploaded the manipulated model to the Hugging Face repository.

### S06

- **[模型 (AML.T0010.003)](../04-Initial-Access/AML.T0010/AML.T0010.003-Model.md)**
  > The victim's AI model supply chain is now compromised. Users of the model repository will receive the adversary's model with embedded malware.

### S07

- **[不安全 AI 制品 (AML.T0011.000)](../06-Execution/AML.T0011/AML.T0011.000-Insecure-AI-Artifacts.md)**
  > When any future user loads the model, the model automatically executes the adversary's payload.

### S08

- **[伪装 (AML.T0074)](../09-Defense-Evasion/AML.T0074-Masquerading.md)**
  > The researcher named the Sliver process `training.bin` to disguise it as a legitimate model training process. Furthermore, the model still operates as normal, making it less likely a user will notice something is wrong.

### S09

- **[网络通信信道 (AML.T0072)](../14-Command-and-Control/AML.T0072-Cyber-Communication-Channel.md)**
  > The Sliver implant grants the researcher a command and control channel so they can explore the victim's environment and continue the attack.

### S10

- **[不安全的凭证 (AML.T0055)](../10-Credential-Access/AML.T0055-Unsecured-Credentials.md)**
  > The researcher checked environment variables and searched Jupyter notebooks for API keys and other secrets.

### S11

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > Discovered credentials could be exfiltrated via the Sliver implant.

### S12

- **[发现 AI 制品 (AML.T0007)](../11-Discovery/AML.T0007-Discover-AI-Artifacts.md)**
  > The researcher could have searched for AI models in the victim organization's environment.

### S13

- **[对抗性 AI 攻击实现 (AML.T0016.000)](../02-Resource-Development/AML.T0016/AML.T0016.000-Adversarial-AI-Attack-Implementations.md)**
  > The researcher obtained [EasyEdit](https://github.com/zjunlp/EasyEdit), an open-source knowledge editing tool for large language models.

### S14

- **[投毒 AI 模型 (AML.T0018.000)](../03-AI-Attack-Adaptation/AML.T0018/AML.T0018.000-Poison-AI-Model.md)**
  > The researcher demonstrated that EasyEdit could be used to poison a `Llama-2-7-b` with false facts.

### S15

- **[外部危害 (AML.T0048)](../16-Impact/AML.T0048-External-Harms.md)**
  > If the company's models were manipulated to produce false information, a variety of harms including financial and reputational could occur.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [命令与控制 (AML.TA0014)](../14-Command-and-Control/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Model Confusion - Weaponizing ML models for red teams and bounty hunters](https://5stars217.github.io/2023-08-08-red-teaming-with-ml-models/#unexpected-benefits---organization-confusion)

- [MITRE ATLAS 官方案例页 (AML.CS0027)](https://atlas.mitre.org/studies/AML.CS0027/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
