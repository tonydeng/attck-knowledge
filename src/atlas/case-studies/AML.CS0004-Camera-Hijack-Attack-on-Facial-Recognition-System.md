# 人脸识别系统摄像头劫持攻击 (AML.CS0004)

## 一句话通俗理解

> 劫持摄像头并配合深伪技术绕过活体人脸识别——两名中国籍嫌疑人借此骗过美国国税局 7700 万美元。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2020-01-01 |
| 攻击者 | Two individuals |
| 受害目标 | Shanghai government tax office's facial recognition service |
| 披露方 | Ant Group AISEC Team |

## 事件经过

摄像头劫持攻击可绕过传统活体人脸识别认证，实现特权系统访问与受害者冒充。两名中国籍个人在 2018 至 2020 年间利用该手法配合深伪技术与数百家空壳公司，向美国国税局提交虚假退税申请，骗取超过 7700 万美元。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0004 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[收集受害者身份信息 (AML.T0087)](../01-Reconnaissance/AML.T0087-Gather-Victim-Identity-Information.md)**
  > The attackers collected user identity information and high-definition face photos from an online black market.

### S01

- **[建立账户 (AML.T0021)](../02-Resource-Development/AML.T0021-Establish-Accounts.md)**
  > The attackers used the victim identity information to register new accounts in the tax system.

### S02

- **[消费级硬件 (AML.T0008.001)](../02-Resource-Development/AML.T0008/AML.T0008.001-Consumer-Hardware.md)**
  > The attackers bought customized low-end mobile phones.

### S03

- **[软件工具 (AML.T0016.001)](../02-Resource-Development/AML.T0016/AML.T0016.001-Software-Tools.md)**
  > The attackers obtained customized Android ROMs and a virtual camera application.

### S04

- **[对抗性 AI 攻击实现 (AML.T0016.000)](../02-Resource-Development/AML.T0016/AML.T0016.000-Adversarial-AI-Attack-Implementations.md)**
  > The attackers obtained software that turns static photos into videos, adding realistic effects such as blinking eyes.

### S05

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > The attackers used the virtual camera app to present the generated video to the ML-based facial recognition service used for user verification.

### S06

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > The attackers successfully evaded the face recognition system. This allowed the attackers to impersonate the victim and verify their identity in the tax system.

### S07

- **[财务危害 (AML.T0048.000)](../16-Impact/AML.T0048/AML.T0048.000-Financial-Harm.md)**
  > The attackers used their privileged access to the tax system to send invoices to supposed clients and further their fraud scheme.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Faces are the next target for fraudsters](https://www.wsj.com/articles/faces-are-the-next-target-for-fraudsters-11625662828)

- [MITRE ATLAS 官方案例页 (AML.CS0004)](https://atlas.mitre.org/studies/AML.CS0004/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
