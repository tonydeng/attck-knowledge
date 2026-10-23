# LLM Jacking (AML.CS0030)

## 一句话通俗理解

> 偷来的云凭证在黑市上「包月出售」——买家免费用 GPT，账单记在你头上。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2024-05-06 |
| 攻击者 | Unknown |
| 受害目标 | Cloud-Based LLM Services |
| 披露方 | Sysdig Threat Research |

## 事件经过

Sysdig 威胁研究团队发现恶意行为者利用窃取的凭证访问云托管 LLM：攻击者从公共仓库收集泄露凭证，隐蔽接入企业级 LLM 服务并转售访问权（LLM Jacking）。受害者承担全部 API 费用，且被盗服务可能被用于生成有害内容。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0030 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[利用面向公众的应用 (AML.T0049)](../04-Initial-Access/AML.T0049-Exploit-Public-Facing-Application.md)**
  > The adversaries exploited a vulnerable version of Laravel ([CVE-2021-3129](https://www.cve.org/CVERecord?id=CVE-2021-3129)) to gain initial access to the victims' systems.

### S01

- **[不安全的凭证 (AML.T0055)](../10-Credential-Access/AML.T0055-Unsecured-Credentials.md)**
  > The adversaries found unsecured credentials to cloud environments on the victims' systems

### S02

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > The compromised credentials gave the adversaries access to cloud environments where large language model (LLM) services were hosted.

### S03

- **[软件工具 (AML.T0016.001)](../02-Resource-Development/AML.T0016/AML.T0016.001-Software-Tools.md)**
  > The adversaries obtained [keychecker](https://github.com/cunnymessiah/keychecker), a bulk key checker for various AI services which is capable of testing if the key is valid and retrieving some attributes of the account (e.g. account balance and available models).

### S04

- **[企业资源发现 (AML.T0075)](../11-Discovery/AML.T0075-Enterprise-Resource-Discovery.md)**
  > The adversaries used keychecker to discover which LLM services were enabled in the cloud environment and if the resources had any resource quotas for the services.

Then, the adversaries checked to see if their stolen credentials gave them access to the LLM resources. They used legitimate `invokeModel` queries with an invalid value of -1 for the `max_tokens_to_sample` parameter, which would raise an `AccessDenied` error if the credentials did not have the proper access to invoke the model. This test revealed that the stolen credentials did provide them with access to LLM resources.

The adversaries also used `GetModelInvocationLoggingConfiguration` to understand how the model was configured. This allowed them to see if prompt logging was enabled to help them avoid detection when executing prompts.

### S05

- **[软件工具 (AML.T0016.001)](../02-Resource-Development/AML.T0016/AML.T0016.001-Software-Tools.md)**
  > The adversaries then used [OAI Reverse Proxy](https://gitgud.io/khanon/oai-reverse-proxy)  to create a reverse proxy service in front of the stolen LLM resources. The reverse proxy service could be used to sell access to cybercriminals who could exploit the LLMs for malicious purposes.

### S06

- **[财务危害 (AML.T0048.000)](../16-Impact/AML.T0048/AML.T0048.000-Financial-Harm.md)**
  > In addition to providing cybercriminals with covert access to LLM resources, the unauthorized use of these LLM models could cost victims thousands of dollars per day.

## 关联战术

- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [LLMjacking: Stolen Cloud Credentials Used in New AI Attack](https://sysdig.com/blog/llmjacking-stolen-cloud-credentials-used-in-new-ai-attack/)
- [The Growing Dangers of LLMjacking: Evolving Tactics and Evading Sanctions](https://sysdig.com/blog/growing-dangers-of-llmjacking/)
- [LLMjacking targets DeepSeek](https://sysdig.com/blog/llmjacking-targets-deepseek/)
- [AIID Incident 898: Alleged LLMjacking Targets AI Cloud Services with Stolen Credentials](https://incidentdatabase.ai/cite/898)

- [MITRE ATLAS 官方案例页 (AML.CS0030)](https://atlas.mitre.org/studies/AML.CS0030/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
