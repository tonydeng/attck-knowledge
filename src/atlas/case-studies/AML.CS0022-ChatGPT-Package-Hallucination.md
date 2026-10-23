# ChatGPT 软件包幻觉 (AML.CS0022)

## 一句话通俗理解

> AI 会一本正经地推荐不存在的软件包——攻击者抢先注册这些包名，你的 pip install 就是他的后门。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2024-06-01 |
| 攻击者 | Vulcan Cyber, Lasso Security |
| 受害目标 | ChatGPT users |

## 事件经过

研究者发现 ChatGPT 等 LLM 会幻觉出软件仓库中不存在的包名。攻击者可抢先在 PyPI/npm 发布这些恶意包，等待开发者被 AI「推荐」后安装——将 LLM 幻觉武器化为软件供应链攻击。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0022 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[AI 模型推理 API 访问 (AML.T0040)](../05-AI-Model-Access/AML.T0040-AI-Model-Inference-API-Access.md)**
  > The researchers use the public ChatGPT API throughout this exercise.

### S01

- **[发现 LLM 幻觉 (AML.T0062)](../11-Discovery/AML.T0062-Discover-LLM-Hallucinations.md)**
  > The researchers prompt ChatGPT to suggest software packages and identify suggestions that are hallucinations which don't exist in a public package repository.

For example, when asking the model "how to upload a model to huggingface?" the response included guidance to install the `huggingface-cli` package with instructions to install it by `pip install huggingface-cli`. This package was a hallucination and does not exist on PyPI. The actual HuggingFace CLI tool is part of the `huggingface_hub` package.

### S02

- **[发布幻觉实体 (AML.T0060)](../02-Resource-Development/AML.T0060-Publish-Hallucinated-Entities.md)**
  > An adversary could upload a malicious package under the hallucinated name to PyPI or other package registries.

In practice, the researchers uploaded an empty package to PyPI to track downloads.

### S03

- **[AI 软件 (AML.T0010.001)](../04-Initial-Access/AML.T0010/AML.T0010.001-AI-Software.md)**
  > A user of ChatGPT or other LLM may ask similar questions which lead to the same hallucinated package name and cause them to download the malicious package.

The researchers showed that multiple LLMs can produce the same hallucinations. They tracked over 30,000 downloads of the `huggingface-cli` package.

### S04

- **[恶意软件包 (AML.T0011.001)](../06-Execution/AML.T0011/AML.T0011.001-Malicious-Packages.md)**
  > The user would ultimately load the malicious package, allowing for arbitrary code execution.

### S05

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > This could lead to a variety of harms to the end user or organization.

## 关联战术

- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Vulcan18's "Can you trust ChatGPT's package recommendations?"](https://vulcan.io/blog/ai-hallucinations-package-risk)
- [Lasso Security Research: Diving into AI Package Hallucinations](https://www.lasso.security/blog/ai-package-hallucinations)
- [AIID Incident 731: Hallucinated Software Packages with Potential Malware Downloaded Thousands of Times by Developers](https://incidentdatabase.ai/cite/731/)
- [Slopsquatting: When AI Agents Hallucinate Malicious Packages](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/slopsquatting-when-ai-agents-hallucinate-malicious-packages)

- [MITRE ATLAS 官方案例页 (AML.CS0022)](https://atlas.mitre.org/studies/AML.CS0022/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
