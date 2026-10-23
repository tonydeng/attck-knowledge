# Google Colab 任意代码执行 (AML.CS0018)

## 一句话通俗理解

> Colab 是给数据科学家的笔记本，也是攻击者的免费算力与代码执行沙箱。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2022-07-01 |
| 攻击者 | Tony Piazza |
| 受害目标 | Google Colab |

## 事件经过

Google Colab 是运行在虚拟机上的 Jupyter Notebook 服务。研究演示了多种在 Colab 中实现任意代码执行的路径：环境可访问 Google Drive 凭证，攻击者获得 Colab 会话后可进一步窃取私有数据、外传 ML 制品，甚至以受害者身份调用 Google API。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0018 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[开发能力 (AML.T0017)](../02-Resource-Development/AML.T0017-Develop-Capabilities.md)**
  > An adversary creates a Jupyter notebook containing obfuscated, malicious code.

### S01

- **[AI 软件 (AML.T0010.001)](../04-Initial-Access/AML.T0010/AML.T0010.001-AI-Software.md)**
  > Jupyter notebooks are often used for ML and data science research and experimentation, containing executable snippets of Python code and common Unix command-line functionality.
Users may come across a compromised notebook on public websites or through direct sharing.

### S02

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > A victim user may mount their Google Drive into the compromised Colab notebook.  Typical reasons to connect machine learning notebooks to Google Drive include the ability to train on data stored there or to save model output files.

```
from google.colab import drive
drive.mount(''/content/drive'')
```

Upon execution, a popup appears to confirm access and warn about potential data access:

> This notebook is requesting access to your Google Drive files. Granting access to Google Drive will permit code executed in the notebook to modify files in your Google Drive. Make sure to review notebook code prior to allowing this access.

A victim user may nonetheless accept the popup and allow the compromised Colab notebook access to the victim''s Drive.  Permissions granted include:
- Create, edit, and delete access for all Google Drive files
- View Google Photos data
- View Google contacts

### S03

- **[用户执行 (AML.T0011)](../06-Execution/AML.T0011-User-Execution.md)**
  > A victim user may unwittingly execute malicious code provided as part of a compromised Colab notebook.  Malicious code can be obfuscated or hidden in other files that the notebook downloads.

### S04

- **[AI 制品收集 (AML.T0035)](../13-Collection/AML.T0035-AI-Artifact-Collection.md)**
  > Adversary may search the victim system to find private and proprietary data, including ML model artifacts.  Jupyter Notebooks [allow execution of shell commands](https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/01.05-IPython-And-Shell-Commands.ipynb).

This example searches the mounted Drive for PyTorch model checkpoint files:

```
!find /content/drive/MyDrive/ -type f -name *.pt
```
> /content/drive/MyDrive/models/checkpoint.pt

### S05

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > As a result of Google Drive access, the adversary may open a server to exfiltrate private data or ML model artifacts.

An example from the referenced article shows the download, installation, and usage of `ngrok`, a server application, to open an adversary-accessible URL to the victim's Google Drive and all its files.

### S06

- **[AI 知识产权窃取 (AML.T0048.004)](../16-Impact/AML.T0048/AML.T0048.004-AI-Intellectual-Property-Theft.md)**
  > Exfiltrated data may include sensitive or private data such as ML model artifacts stored in Google Drive.

### S07

- **[外部危害 (AML.T0048)](../16-Impact/AML.T0048-External-Harms.md)**
  > Exfiltrated data may include sensitive or private data such as proprietary data stored in Google Drive, as well as user contacts and photos.  As a result, the user may be harmed financially, reputationally, and more.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Be careful who you colab with](https://medium.com/mlearning-ai/careful-who-you-colab-with-fa8001f933e7)

- [MITRE ATLAS 官方案例页 (AML.CS0018)](https://atlas.mitre.org/studies/AML.CS0018/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
