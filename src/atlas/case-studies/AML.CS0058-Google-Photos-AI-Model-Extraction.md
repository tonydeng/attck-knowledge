# Google Photos AI 模型提取 (AML.CS0058)

## 一句话通俗理解

> 静态分析 + Frida 插桩：手机里的 Google Photos 被「开膛」取出了 TFLite 模型。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-03-01 |
| 攻击者 | Skyld |
| 受害目标 | Google Photos Android App |

## 事件经过

Skyld 研究者分析了 Google Photos Android 应用，恢复了其 AI 照片编辑与图像分析功能使用的 TensorFlow Lite 模型：静态分析配合 Frida 插桩直接提取模型文件；对加密模型则拦截解密流量获取——证明端侧分发的高价值模型天然可被完整提取。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0058 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[发现 AI 制品 (AML.T0007)](../11-Discovery/AML.T0007-Discover-AI-Artifacts.md)**
  > Skyld researchers analyzed the Google Photos Android Package (APK) and identified TensorFlow Lite as the machine learning framework used by the app. They searched the application package and native libraries for TFLite artifacts using the TFL3 file identifier.

### S01

- **[AI 制品收集 (AML.T0035)](../13-Collection/AML.T0035-AI-Artifact-Collection.md)**
  > The researchers collected TensorFlow Lite model artifacts from multiple locations in the APK, including unencrypted assets, files embedded in the native library, and application-specific folders.

### S02

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > The researchers used static analysis and Frida instrumentation to recover model files. For encrypted models, they intercepted decrypted TFLite files during runtime as Google Photos loaded them for execution.

### S03

- **[完全 AI 模型访问 (AML.T0044)](../05-AI-Model-Access/AML.T0044-Full-AI-Model-Access.md)**
  > Exfiltrating model files from the APK gave the researchers full access to the Google Photos AI models, including those used for tasks such as face detection, object detection, segmentation, depth estimation, image quality assessment, and blur detection.

### S04

- **[白盒优化 (AML.T0043.000)](../03-AI-Attack-Adaptation/AML.T0043/AML.T0043.000-White-Box-Optimization.md)**
  > The recovered TensorFlow Lite models could enable white-box adversarial example generation.

### S05

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > Adversarial data could be used to evade or otherwise degrade the Google Photos models including face and object detection.

### S06

- **[AI 知识产权窃取 (AML.T0048.004)](../16-Impact/AML.T0048/AML.T0048.004-AI-Intellectual-Property-Theft.md)**
  > The recovered models represented proprietary Google Photos AI assets. An adversary or competitor could use the extracted models to study, reuse, or replicate Google Photos capabilities, reducing the cost of independently developing similar features.

## 关联战术

- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Google Photos AI Models: The Secret Sauce That Can Be Stolen](https://skyld.io/google-photos-model-extraction)

- [MITRE ATLAS 官方案例页 (AML.CS0058)](https://atlas.mitre.org/studies/AML.CS0058/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
