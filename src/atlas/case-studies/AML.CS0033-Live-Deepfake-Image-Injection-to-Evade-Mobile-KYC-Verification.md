# 活体深伪图像注入绕过移动端 KYC 验证 (AML.CS0033)

## 一句话通俗理解

> 虚拟摄像头 + 深伪视频 = 绕过「眨眨眼」活体检测——iProov 红队亲自演示。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2024-10-01 |
| 攻击者 | iProov Red Team |
| 受害目标 | Mobile facial authentication service |

## 事件经过

人脸生物认证广泛用于移动端的用户入驻与 KYC。iProov 研究团队演示了活体深伪图像注入攻击：通过虚拟摄像头注入深度伪造视频流，绕过移动端活体检测完成身份冒充——证明纯软件注入即可攻破生物认证链路。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0033 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[收集受害者身份信息 (AML.T0087)](../01-Reconnaissance/AML.T0087-Gather-Victim-Identity-Information.md)**
  > The researchers collected user identity information and high-definition facial images from online social networks and/or black-market sites.

### S01

- **[生成式 AI (AML.T0016.002)](../02-Resource-Development/AML.T0016/AML.T0016.002-Generative-AI.md)**
  > The researchers obtained [Faceswap](https://swapface.org) a desktop application capable of swapping faces in a video in real-time.

### S02

- **[软件工具 (AML.T0016.001)](../02-Resource-Development/AML.T0016/AML.T0016.001-Software-Tools.md)**
  > The researchers obtained [Open Broadcaster Software (OBS)](https://obsproject.com) which can broadcast a video stream over the network.

### S03

- **[获取能力 (AML.T0016)](../02-Resource-Development/AML.T0016-Obtain-Capabilities.md)**
  > The researchers obtained [Virtual Camera: Live Assist](https://apkpure.com/virtual-camera-live-assist/virtual.camera.app), an Android app that allows a user to substitute the devices camera  with a video stream. This app works on genuine, non-rooted Android devices.

### S04

- **[生成深度伪造 (AML.T0088)](../03-AI-Attack-Adaptation/AML.T0088-Generate-Deepfakes.md)**
  > The researchers use the gathered victim face images and the Faceswap tool to produce live deepfake videos which mimic the victim's appearance.

### S05

- **[建立账户 (AML.T0021)](../02-Resource-Development/AML.T0021-Establish-Accounts.md)**
  > The researchers used the gathered victim information to register an account for a financial services application.

### S06

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > During identity verification, the financial services application uses facial recognition and liveness detection to analyze live video from the user's camera.

### S07

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > The researchers stream the deepfake video feed using OBS and use the Virtual Camera app to replace the default camera with feed. This successfully evades the facial recognition system and allows the researchers to authenticate themselves under the victim's identity.

### S08

- **[冒充 (AML.T0073)](../09-Defense-Evasion/AML.T0073-Impersonation.md)**
  > With an authenticated account under the victim's identity, the researchers successfully impersonate the victim and evade detection.

### S09

- **[财务危害 (AML.T0048.000)](../16-Impact/AML.T0048/AML.T0048.000-Financial-Harm.md)**
  > The researchers could then have caused financial harm to the victim.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

- 见 [MITRE ATLAS 案例研究](https://atlas.mitre.org/studies/)

- [MITRE ATLAS 官方案例页 (AML.CS0033)](https://atlas.mitre.org/studies/AML.CS0033/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
