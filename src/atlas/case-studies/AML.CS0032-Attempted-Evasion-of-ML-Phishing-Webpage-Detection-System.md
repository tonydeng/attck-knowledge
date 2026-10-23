# ML 钓鱼网页检测系统规避未遂 (AML.CS0032)

## 一句话通俗理解

> 钓鱼网站在 ML 检测器眼皮底下伪装成正常站——攻击者持续对抗安全厂商的检测模型。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2022-12-01 |
| 攻击者 | Unknown |
| 受害目标 | Commercial ML Phishing Webpage Detector |
| 披露方 | Norton Research Group (NRG) |

## 事件经过

攻击者制作的钓鱼网站在视觉上与合法站点高度相似，用于诱骗用户输入凭证。安全事件表明攻击者持续尝试规避基于 ML 的钓鱼网页检测系统——对抗在检测器与规避手法之间持续演化。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0032 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[人工修改 (AML.T0043.003)](../03-AI-Attack-Adaptation/AML.T0043/AML.T0043.003-Manual-Modification.md)**
  > Several cheap, yet effective strategies for manually modifying logos were observed:
| Evasive Strategy | Count |
| - | - |
| Company name style | 25 |
| Blurry logo | 23 |
| Cropping | 20 |
| No company name | 16 |
| No visual logo | 13 |
| Different visual logo | 12 |
| Logo stretching | 11 |
| Multiple forms - images | 10 |
| Background patterns | 8 |
| Login obfuscation | 6 |
| Masking | 3 |

### S01

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > The visual similarity model used to detect brand impersonation was evaded. However, other components of the phishing detection system successfully identified the phishing websites.

### S02

- **[网络钓鱼 (AML.T0052)](../04-Initial-Access/AML.T0052-Phishing.md)**
  > If the adversary can successfully evade detection, they can continue to operate their phishing websites and steal the victim's credentials.

### S03

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The end user may experience a variety of harms including financial and privacy harms depending on the credentials stolen by the adversary.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- ["Real Attackers Don't Compute Gradients": Bridging the Gap Between Adversarial ML Research and Practice](https://arxiv.org/abs/2212.14315)
- [Real Attackers Don't Compute Gradients Supplementary Resources](https://real-gradients.github.io/)

- [MITRE ATLAS 官方案例页 (AML.CS0032)](https://atlas.mitre.org/studies/AML.CS0032/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
