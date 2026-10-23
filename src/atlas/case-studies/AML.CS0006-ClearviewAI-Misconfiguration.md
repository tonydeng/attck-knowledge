# Clearview AI 配置错误 (AML.CS0006)

## 一句话通俗理解

> 人脸识别公司把数据库暴露在公网——攻击者连门都不用撬，直接拿走了全部人脸数据。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2020-04-16 |
| 攻击者 | Researchers at spiderSilk |
| 受害目标 | Clearview AI facial recognition tool |

## 事件经过

Clearview AI 开发的人脸识别工具可搜索公开照片进行匹配，被执法机构用于调查。2020 年其源代码仓库因配置错误暴露，攻击者可访问其客户名单、代码库与（据称）部分人脸数据库，构成重大数据泄露事件。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0006 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[建立账户 (AML.T0021)](../02-Resource-Development/AML.T0021-Establish-Accounts.md)**
  > A security researcher gained initial access to Clearview AI's private code repository via a misconfigured server setting that allowed an arbitrary user to register a valid account.

### S01

- **[来自信息库的数据 (AML.T0036)](../13-Collection/AML.T0036-Data-from-Information-Repositories.md)**
  > The private code repository contained credentials which were used to access AWS S3 cloud storage buckets, leading to the discovery of assets for the facial recognition tool, including:
- Released desktop and mobile applications
- Pre-release applications featuring new capabilities
- Slack access tokens
- Raw videos and other data

### S02

- **[获取公开 AI 制品 (AML.T0002)](../02-Resource-Development/AML.T0002-Acquire-Public-AI-Artifacts.md)**
  > Adversaries could have downloaded training data and gleaned details about software, models, and capabilities from the source code and decompiled application binaries.

### S03

- **[侵蚀 AI 模型完整性 (AML.T0031)](../16-Impact/AML.T0031-Erode-AI-Model-Integrity.md)**
  > As a result, future application releases could have been compromised, causing degraded or malicious facial recognition capabilities.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [TechCrunch Article, "Security lapse exposed Clearview AI source code"](https://techcrunch.com/2020/04/16/clearview-source-code-lapse/)
- [Gizmodo Article, "We Found Clearview AI's Shady Face Recognition App"](https://gizmodo.com/we-found-clearview-ais-shady-face-recognition-app-1841961772)
- [New York Times Article, "The Secretive Company That Might End Privacy as We Know It"](https://www.nytimes.com/2020/01/18/technology/clearview-privacy-facial-recognition.html)

- [MITRE ATLAS 官方案例页 (AML.CS0006)](https://atlas.mitre.org/studies/AML.CS0006/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
