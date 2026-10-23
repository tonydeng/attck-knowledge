# 绕过 ID.me 身份验证 (AML.CS0017)

## 一句话通俗理解

> 深伪技术帮一个人冒领了 180 份失业救济金——加州损失 340 万美元。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2020-10-01 |
| 攻击者 | One individual |
| 受害目标 | California Employment Development Department |
| 披露方 | ID.me internal investigation |

## 事件经过

2020 年 10 月至 2021 年 12 月，一名个人通过绕过 ID.me 自动身份验证系统（利用深伪等手段），在加利福尼亚州提交了至少 180 份虚假失业救济申请，累计骗取约 340 万美元。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0017 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > The individual applied for unemployment assistance with the California Employment Development Department using forged identities, interacting with ID.me's identity verification system in the process.

The system extracts content from a photo of an ID, validates the authenticity of the ID using a combination of AI and proprietary methods, then performs facial recognition to match the ID photo to a selfie. <sup>[[7]](https://network.id.me/wp-content/uploads/Document-Verification-Use-Machine-Vision-and-AI-to-Extract-Content-and-Verify-the-Authenticity-1.pdf)</sup>

The individual identified that the California Employment Development Department relied on a third party service, ID.me, to verify individuals' identities.

The ID.me website outlines the steps to verify an identity, including entering personal information, uploading a driver license, and submitting a selfie photo.

### S01

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > The individual collected stolen identities, including names, dates of birth, and Social Security numbers and used them along with a photo of himself wearing wigs to acquire fake driver's licenses.

The individual uploaded forged IDs along with a selfie. The ID.me document verification system matched the selfie to the ID photo, allowing some fraudulent claims to proceed in the application pipeline.

### S02

- **[财务危害 (AML.T0048.000)](../16-Impact/AML.T0048/AML.T0048.000-Financial-Harm.md)**
  > Dozens out of at least 180 fraudulent claims were ultimately approved and the individual received at least $3.4 million in unemployment assistance.

## 关联战术

- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [New Jersey Man Indicted in Fraud Scheme to Steal California Unemployment Insurance Benefits](https://www.justice.gov/usao-edca/pr/new-jersey-man-indicted-fraud-scheme-steal-california-unemployment-insurance-benefits)
- [The Many Jobs and Wigs of Eric Jaklitchs Fraud Scheme](https://frankonfraud.com/fraud-trends/the-many-jobs-and-wigs-of-eric-jaklitchs-fraud-scheme/)
- [ID.me gathers lots of data besides face scans, including locations. Scammers still have found a way around it.](https://www.washingtonpost.com/technology/2022/02/11/idme-facial-recognition-fraud-scams-irs/)
- [CA EDD Unemployment Insurance & ID.me](https://help.id.me/hc/en-us/articles/4416268603415-CA-EDD-Unemployment-Insurance-ID-me)
- [California EDD - How do I verify my identity for California EDD Unemployment Insurance?](https://help.id.me/hc/en-us/articles/360054836774-California-EDD-How-do-I-verify-my-identity-for-the-California-Employment-Development-Department-)
- [New Jersey Man Sentenced to 6.75 Years in Prison for Schemes to Steal California Unemployment Insurance Benefits and Economic Injury Disaster Loans](https://www.justice.gov/usao-edca/pr/new-jersey-man-sentenced-675-years-prison-schemes-steal-california-unemployment)
- [How ID.me uses machine vision and AI to extract content and verify the authenticity of ID documents](https://network.id.me/wp-content/uploads/Document-Verification-Use-Machine-Vision-and-AI-to-Extract-Content-and-Verify-the-Authenticity-1.pdf)

- [MITRE ATLAS 官方案例页 (AML.CS0017)](https://atlas.mitre.org/studies/AML.CS0017/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
