# 移动应用深度学习模型后门攻击 (AML.CS0013)

## 一句话通俗理解

> 微软研究院发现移动 App 里的深度学习模型可以被植入「带触发器的后门」——正常用没事，一碰触发器就作恶。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2021-01-18 |
| 攻击者 | Yuanchun Li, Jiayi Hua, Haoyu Wang, Chunyang Chen, Yunxin Liu |
| 受害目标 | ML-based Android Apps |

## 事件经过

微软研究院研究人员演示了针对移动应用中深度学习模型的后门攻击：在模型中植入特定触发条件，正常输入下表现正常，触发条件出现时执行恶意行为。研究表明移动端部署的模型普遍缺乏完整性保护。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0013 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[搜索应用仓库 (AML.T0004)](../01-Reconnaissance/AML.T0004-Search-Application-Repositories.md)**
  > To identify a list of potential target models, the researchers searched the Google Play store for apps that may contain embedded deep learning models by searching for deep learning related keywords.

### S01

- **[模型 (AML.T0002.001)](../02-Resource-Development/AML.T0002/AML.T0002.001-Models.md)**
  > The researchers acquired the apps' APKs from the Google Play store.
They filtered the list of potential target applications by searching the code metadata for keywords related to TensorFlow or TFLite and their model binary formats (.tf and .tflite).
The models were extracted from the APKs using Apktool.

### S02

- **[完全 AI 模型访问 (AML.T0044)](../05-AI-Model-Access/AML.T0044-Full-AI-Model-Access.md)**
  > This provided the researchers with full access to the ML model, albeit in compiled, binary form.

### S03

- **[对抗性 AI 攻击 (AML.T0017.000)](../02-Resource-Development/AML.T0017/AML.T0017.000-Adversarial-AI-Attacks.md)**
  > The researchers developed a novel approach to insert a backdoor into a compiled model that can be activated with a visual trigger.  They inject a "neural payload" into the model that consists of a trigger detection network and conditional logic.
The trigger detector is trained to detect a visual trigger that will be placed in the real world.
The conditional logic allows the researchers to bypass the victim model when the trigger is detected and provide model outputs of their choosing.
The only requirements for training a trigger detector are a general
dataset from the same modality as the target model (e.g. ImageNet for image classification) and several photos of the desired trigger.

### S04

- **[修改模型架构 (AML.T0018.001)](../03-AI-Attack-Adaptation/AML.T0018/AML.T0018.001-Modify-AI-Model-Architecture.md)**
  > The researchers poisoned the victim model by injecting the neural
payload into the compiled models by directly modifying the computation
graph.
The researchers then repackage the poisoned model back into the APK

### S05

- **[验证攻击 (AML.T0042)](../03-AI-Attack-Adaptation/AML.T0042-Verify-Attack.md)**
  > To verify the success of the attack, the researchers confirmed the app did not crash with the malicious model in place, and that the trigger detector successfully detects the trigger.

### S06

- **[模型 (AML.T0010.003)](../04-Initial-Access/AML.T0010/AML.T0010.003-Model.md)**
  > In practice, the malicious APK would need to be installed on victim's devices via a supply chain compromise.

### S07

- **[插入后门触发器 (AML.T0043.004)](../03-AI-Attack-Adaptation/AML.T0043/AML.T0043.004-Insert-Backdoor-Trigger.md)**
  > The trigger is placed in the physical environment, where it is captured by the victim's device camera and processed by the backdoored ML model.

### S08

- **[物理环境访问 (AML.T0041)](../05-AI-Model-Access/AML.T0041-Physical-Environment-Access.md)**
  > At inference time, only physical environment access is required to trigger the attack.

### S09

- **[规避 AI 模型 (AML.T0015)](../04-Initial-Access/AML.T0015-Evade-AI-Model.md)**
  > Presenting the visual trigger causes the victim model to be bypassed.
The researchers demonstrated this can be used to evade ML models in
several safety-critical apps in the Google Play store.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [DeepPayload: Black-box Backdoor Attack on Deep Learning Models through Neural Payload Injection](https://arxiv.org/abs/2101.06896)

- [MITRE ATLAS 官方案例页 (AML.CS0013)](https://atlas.mitre.org/studies/AML.CS0013/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
