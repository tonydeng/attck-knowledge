# ShadowRay：暴露 Ray 集群劫持 (AML.CS0023)

## 一句话通俗理解

> Ray 的任务 API 天生允许远程执行且默认无认证——暴露在公网就等于送出集群控制权。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2023-09-05 |
| 攻击者 | Unknown |
| 受害目标 | Exposed Ray Clusters |
| 披露方 | Oligo Research Team |

## 事件经过

Ray 是扩展生产 AI 工作流的开源框架，其 Job API 设计上允许任意远程执行且默认无认证。ShadowRay 研究发现大量暴露在公网的 Ray 集群，攻击者可无凭证接管算力、执行任意代码、窃取 AI 制品与凭证——Oyster（后门）团伙在野利用了该暴露面。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0023 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[主动扫描 (AML.T0006)](../01-Reconnaissance/AML.T0006-Active-Scanning.md)**
  > Adversaries can scan for public IP addresses to identify those potentially hosting Ray dashboards. Ray dashboards, by default, run on all network interfaces, which can expose them to the public internet if no other protective mechanisms are in place on the system.

### S01

- **[利用面向公众的应用 (AML.T0049)](../04-Initial-Access/AML.T0049-Exploit-Public-Facing-Application.md)**
  > Once open Ray clusters have been identified, adversaries could use the Jobs API to invoke jobs onto accessible clusters. The Jobs API does not support any kind of authorization, so anyone with network access to the cluster can execute arbitrary code remotely.

### S02

- **[AI 制品收集 (AML.T0035)](../13-Collection/AML.T0035-AI-Artifact-Collection.md)**
  > Adversaries could collect AI artifacts including production models and data.

The researchers observed running production workloads from several organizations from a variety of industries.

### S03

- **[不安全的凭证 (AML.T0055)](../10-Credential-Access/AML.T0055-Unsecured-Credentials.md)**
  > The attackers could collect unsecured credentials stored in the cluster.

The researchers observed SSH keys, OpenAI tokens, HuggingFace tokens, Stripe tokens, cloud environment keys (AWS, GCP, Azure, Lambda Labs), Kubernetes secrets.

### S04

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > AI artifacts, credentials, and other valuable information can be exfiltrated via cyber means.

The researchers found evidence of reverse shells on vulnerable clusters. They can be used to maintain persistence, continue to run arbitrary code, and exfiltrate.

### S05

- **[模型 (AML.T0010.003)](../04-Initial-Access/AML.T0010/AML.T0010.003-Model.md)**
  > HuggingFace tokens could allow the adversary to replace the victim organization's models with malicious variants.

### S06

- **[财务危害 (AML.T0048.000)](../16-Impact/AML.T0048/AML.T0048.000-Financial-Harm.md)**
  > Adversaries can cause financial harm to the victim organization. Exfiltrated credentials could be used to deplete credits or drain accounts. The GPU cloud resources themselves are costly. The researchers found evidence of cryptocurrency miners on vulnerable Ray clusters.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Anyscale Update on CVEs](https://www.anyscale.com/blog/update-on-ray-cves-cve-2023-6019-cve-2023-6020-cve-2023-6021-cve-2023-48022-cve-2023-48023)
- [CVE-2023-48022](https://nvd.nist.gov/vuln/detail/CVE-2023-48022)
- [ShadowRay: First Known Attack Campaign Targeting AI Workloads Actively Exploited In The Wild](https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild)
- [ShadowRay: AI Infrastructure Is Being Exploited In the Wild](https://protectai.com/threat-research/shadowray-ai-infrastructure-is-being-exploited-in-the-wild)

- [MITRE ATLAS 官方案例页 (AML.CS0023)](https://atlas.mitre.org/studies/AML.CS0023/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
