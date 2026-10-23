# ProKYC：用于账户欺诈的深伪工具 (AML.CS0034)

## 一句话通俗理解

> 黑产工具明码标价：交钱就帮你用深伪视频过银行 KYC——「犯罪即服务」的 AI 时代。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2024-10-09 |
| 攻击者 | ProKYC, cybercriminal group |
| 受害目标 | KYC verification services |
| 披露方 | Cato CTRL |

## 事件经过

Cato CTRL 安全研究人员发现 ProKYC——一款出售给网络犯罪分子的深伪工具，用于绕过金融服务机构的 KYC 验证。该工具生成深度伪造人脸视频通过银行端验证，把 AI 深伪能力商品化为欺诈基础设施。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0034 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[收集受害者身份信息 (AML.T0087)](../01-Reconnaissance/AML.T0087-Gather-Victim-Identity-Information.md)**
  > The bad actor collected user identity information.

### S01

- **[生成式 AI (AML.T0016.002)](../02-Resource-Development/AML.T0016/AML.T0016.002-Generative-AI.md)**
  > The bad actor paid for the ProKYC tool, created a fake identity document, generated a deepfake selfie video, and replaced a live camera feed with the deepfake video.

### S02

- **[生成深度伪造 (AML.T0088)](../03-AI-Attack-Adaptation/AML.T0088-Generate-Deepfakes.md)**
  > The bad actor used a mixture of real PII and falsified details with the ProKYC tool to generate a deepfaked identity document.

### S03

- **[生成深度伪造 (AML.T0088)](../03-AI-Attack-Adaptation/AML.T0088-Generate-Deepfakes.md)**
  > The bad actor used ProKYC tool to generate a deepfake selfie video with the same face as the identity document designed to bypass liveness checks.

### S04

- **[建立账户 (AML.T0021)](../02-Resource-Development/AML.T0021-Establish-Accounts.md)**
  > The bad actor used the victim information to register an account with a financial services application, such as a cryptocurrency exchange.

### S05

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > During identity verification, the financial services application used facial recognition and liveness detection to analyze live video from the user's camera.

### S06

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > The bad actor used ProKYC to replace the camera feed with the deepfake selfie video. This successfully evaded the KYC verification and allowed the bad actor to authenticate themselves under the false identity.

### S07

- **[冒充 (AML.T0073)](../09-Defense-Evasion/AML.T0073-Impersonation.md)**
  > With an authenticated account under the victim's identity, the bad actor successfully impersonated the victim and evaded detection.

### S08

- **[财务危害 (AML.T0048.000)](../16-Impact/AML.T0048/AML.T0048.000-Financial-Harm.md)**
  > The bad actor used this access to cause financial harm to the victim.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [AIID Incident 819: ProKYC Tool Allegedly Facilitates Deepfake-Based Account Fraud on Cryptocurrency Exchanges](https://incidentdatabase.ai/cite/819/)
- [Cato CTRL Threat Research: ProKYC - Deepfake Tool for Account Fraud Attacks](https://www.catonetworks.com/blog/prokyc-selling-deepfake-tool-for-account-fraud-attacks/)
- [ProKYC: Synthetic Identity Fraud as a Service](https://idscan.net/blog/prokyc-synthetic-identity-fraud/)

- [MITRE ATLAS 官方案例页 (AML.CS0034)](https://atlas.mitre.org/studies/AML.CS0034/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
