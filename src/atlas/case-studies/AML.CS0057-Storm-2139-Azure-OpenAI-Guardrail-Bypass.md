# Storm-2139 Azure OpenAI 护栏绕过 (AML.CS0057)

## 一句话通俗理解

> 伊朗团伙搭起「越狱即服务」：刮来的凭证 + 自研越狱工具，把 Azure OpenAI 变成有害内容工厂。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2024-12-01 |
| 攻击者 | Storm-2139 |
| 受害目标 | Microsoft Azure OpenAI Service |
| 披露方 | Microsoft |

## 事件经过

Storm-2139（伊朗背景团伙）构建了绕过 Azure OpenAI 服务护栏的定制越狱工具链：先从公共代码仓库刮取泄露凭证获得访问，再批量生成有害合成内容（含辱虐图像），部分内容被用于牟利。微软以法律行动反制并公开了该团伙的运营模式。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0057 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[开发能力 (AML.T0017)](../02-Resource-Development/AML.T0017-Develop-Capabilities.md)**
  > Storm-2139 creators developed a tool called de3u to facilitate unauthorized use of generative AI services and bypass safeguards.

### S01

- **[获取基础设施 (AML.T0008)](../02-Resource-Development/AML.T0008-Acquire-Infrastructure.md)**
  > Storm-2139 acquired infrastructure to support a service that sold access to the jailbroken Azure OpenAI Service.

### S02

- **[暂存能力 (AML.T0079)](../02-Resource-Development/AML.T0079-Stage-Capabilities.md)**
  > Storm-2139 staged and operated a reverse proxy service to allow other malicious users to interact with abused generative AI services.

### S03

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > Storm-2139 used exposed customer credentials scraped from public sources to access valid accounts for generative AI services.

### S04

- **[AI 模型推理 API 访问 (AML.T0040)](../05-AI-Model-Access/AML.T0040-AI-Model-Inference-API-Access.md)**
  > The stolen credentials provided access Azure OpenAI Service, allowing the actors and their customers to submit prompts and generate content. Storm-2139's de3u tool was used as the frontend for this access.

### S05

- **[LLM 越狱 (AML.T0054)](../08-Privilege-Escalation/AML.T0054-LLM-Jailbreak.md)**
  > Storm-2139 deliberately bypassed Azure OpenAI Service safeguards and content filters to generate prohibited outputs. Microsoft reported that the actors iterated on blocked prompts, substituted celebrity descriptions, and used altered wording or technical notation to evade filters.

### S06

- **[生成深度伪造 (AML.T0088)](../03-AI-Attack-Adaptation/AML.T0088-Generate-Deepfakes.md)**
  > End users generated abusive synthetic imagery, including non-consensual intimate images of celebrities and other sexually explicit, misogynistic, violent, or hateful content.

### S07

- **[社会危害 (AML.T0048.002)](../16-Impact/AML.T0048/AML.T0048.002-Societal-Harm.md)**
  > The generated abusive imagery could cause direct harm to depicted individuals.

### S08

- **[财务危害 (AML.T0048.000)](../16-Impact/AML.T0048/AML.T0048.000-Financial-Harm.md)**
  > Users whose accounts were stolen were harmed financially.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [权限提升 (AML.TA0012)](../08-Privilege-Escalation/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Taking legal action to protect the public from abusive AI-generated content](https://blogs.microsoft.com/on-the-issues/2025/01/10/taking-legal-action-to-protect-the-public-from-abusive-ai-generated-content/)
- [Disrupting a global cybercrime network abusing generative AI](https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/)
- [How Microsoft is taking down AI hackers who create harmful images of celebrities and others](https://news.microsoft.com/source/features/ai/how-microsoft-is-taking-down-ai-hackers-who-create-harmful-images-of-celebrities-and-others/)

- [MITRE ATLAS 官方案例页 (AML.CS0057)](https://atlas.mitre.org/studies/AML.CS0057/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
