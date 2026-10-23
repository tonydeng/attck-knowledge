# HuggingFace 上的恶意模型 (AML.CS0031)

## 一句话通俗理解

> 模型文件里藏着反向 shell——「下载即上线」，HuggingFace 变成恶意软件分发站。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2025-02-25 |
| 攻击者 | Unknown |
| 受害目标 | Hugging Face users |
| 披露方 | ReversingLabs |

## 事件经过

ReversingLabs 研究者在 HuggingFace 模型仓库发现了内嵌恶意软件的模型：利用 pickle 序列化格式在加载时执行代码的能力，模型文件被植入反向 shell 等载荷。下载并加载这些模型的用户会直接交出系统控制权。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0031 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[嵌入恶意软件 (AML.T0018.002)](../03-AI-Attack-Adaptation/AML.T0018/AML.T0018.002-Embed-Malware.md)**
  > The adversary embedded malware into an AI model stored in a pickle file. The malware was designed to execute when the model is loaded by a user.

ReversingLabs found two instances of this on Hugging Face during their research.

### S01

- **[模型 (AML.T0115.001)](../02-Resource-Development/AML.T0115/AML.T0115.001-Models.md)**
  > The adversary uploaded the model to Hugging Face.

In both instances observed by the ReversingLab, the malicious models did not make any attempt to mimic a popular legitimate model.

### S02

- **[破坏 AI 模型 (AML.T0076)](../09-Defense-Evasion/AML.T0076-Corrupt-AI-Model.md)**
  > The adversary evaded detection by [Picklescan](https://github.com/mmaitre314/picklescan), which Hugging Face uses to flag malicious models. This occurred because the model could not be fully deserialized.

In their analysis, the ReversingLabs researchers found that the malicious payload was still executed.

### S03

- **[AI 供应链入侵 (AML.T0010)](../04-Initial-Access/AML.T0010-AI-Supply-Chain-Compromise.md)**
  > Because the models were successfully uploaded to Hugging Face, a user relying on this model repository would have their supply chain compromised.

### S04

- **[不安全 AI 制品 (AML.T0011.000)](../06-Execution/AML.T0011/AML.T0011.000-Insecure-AI-Artifacts.md)**
  > If a user loaded the malicious model, the adversary's malicious payload is executed.

### S05

- **[网络通信信道 (AML.T0072)](../14-Command-and-Control/AML.T0072-Cyber-Communication-Channel.md)**
  > The malicious payload was a reverse shell set to connect to a hardcoded IP address.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [命令与控制 (AML.TA0014)](../14-Command-and-Control/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Malicious ML models discovered on Hugging Face platform](https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face?&web_view=true)

- [MITRE ATLAS 官方案例页 (AML.CS0031)](https://atlas.mitre.org/studies/AML.CS0031/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
