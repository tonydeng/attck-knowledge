# 多智能体框架攻陷台湾政府系统 (AML.CS0071)

## 一句话通俗理解

> Hermes + OpenClaw 组成的「攻击智能体军团」，从台湾政府网络拖走了 2564 条人事记录。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2026-07-01 |
| 攻击者 | Unknown Chinese-language actor |
| 受害目标 | Taiwanese government agencies and connected government systems |
| 披露方 | Dream Research Labs |

## 事件经过

2026 年 7 月初，未知中文操作者使用基于 Hermes 与 OpenClaw 的多智能体框架攻击台湾政府系统：智能体从未认证的用户数据库 API 获取访问权后自主收集数据——超过 2,564 条人事记录、完整用户数据库与内部架构细节被渗漏。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0071 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S01

- **[自主攻击编排 (AML.T0124)](../03-AI-Attack-Adaptation/AML.T0124-Autonomous-Attack-Orchestration.md)**
  > The framework dispatched up to eight specialized agents concurrently across 12 attack waves. It assigned separate reconnaissance, authentication, API-testing, vulnerability-research, credential, and exploitation missions; allocated additional testing to promising findings; requested independent validation; aggregated after-action reports; and redirected subsequent work based on the status of related workstreams.

### S02

- **[自主攻击路径适配 (AML.T0117)](../03-AI-Attack-Adaptation/AML.T0117-Autonomous-Attack-Path-Adaptation.md)**
  > The framework constructed numerous candidate multi-step attack paths using confirmed prerequisites, observed blockers, and estimated success probabilities. It promoted paths supported by validated evidence, queued paths requiring additional investigation, discarded false positives and blocked paths, and initiated target-specific learning cycles when existing methods failed.

### S03

- **[智能体直接通信 (AML.T0118.001)](../03-AI-Attack-Adaptation/AML.T0118/AML.T0118.001-Direct-Agent-Communication.md)**
  > The framework exchanged assignments, findings, validation results, status, and after-action information between its orchestrating control process and specialized sub-agents. Aggregated results informed later assignments and attack waves.

### S04

- **[自主侦察 (AML.T0116)](../01-Reconnaissance/AML.T0116-Autonomous-Reconnaissance.md)**
  > The framework performed reconnaissance on an internet-facing Taiwanese government portal, interpreting client-side application bundles, following discovered infrastructure relationships, and generating additional reconnaissance objectives. It identified 21 connected systems, six SSO sub-realms, authentication configuration, signing-key information, and more than 36 API endpoints on one system.

### S05

- **[主动扫描 (AML.T0006)](../01-Reconnaissance/AML.T0006-Active-Scanning.md)**
  > The framework probed primary government applications and APIs for exposed interfaces, authentication behavior, misconfigurations, and vulnerabilities. This scanning identified multiple potential paths into the targeted systems.

### S06

- **[来自信息库的数据 (AML.T0036)](../13-Collection/AML.T0036-Data-from-Information-Repositories.md)**
  > The framework retrieved employee names, departments, identifiers, and SSO account information from an exposed user-database API without authentication.

### S07

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > The framework used employee identifiers obtained from the exposed API to test predictable password patterns against the office automation portal. The framework successfully authenticated to the office automation portal using the compromised employee accounts.

### S08

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > The framework systematically tested the 85 compromised office automation accounts against another government information system through an SSO bridge that trusted the existing office automation sessions, providing access to internal dashboards, equipment management interfaces, and personnel statistics pages.

### S09

- **[利用面向公众的应用 (AML.T0049)](../04-Initial-Access/AML.T0049-Exploit-Public-Facing-Application.md)**
  > The framework abused three exposed debug endpoints that accepted arbitrary request bodies and returned authenticated sessions.

### S10

- **[利用面向公众的应用 (AML.T0049)](../04-Initial-Access/AML.T0049-Exploit-Public-Facing-Application.md)**
  > The framework found a public-facing API that accepted unsigned JWTs with `alg=none`, allowing identity tokens to be forged without the signing key.

### S11

- **[自动化收集 (AML.T0126)](../13-Collection/AML.T0126-Automated-Collection.md)**
  > Using the acquired accesses, the framework automatically retrieved and aggregated the reported personnel, account, configuration, credential, and network information.

### S12

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > Over 2,564 personnel records, a complete user database, and internal architecture details were exfiltrated.

## 关联战术

- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Inside a Multi-Agent AI Framework Used to Compromise Government Entities in Asia](https://www.dreamgroup.com/blog/inside-a-multi-agent-ai-framework-used-to-compromise-government-entities-in-asia)
- [Overseas hackers launch AI-agent attacks against government agencies; MODA activates coordinated response and strengthens cyber defenses](https://moda.gov.tw/ACS/press/news/press/20394)
- [China-linked hackers hit Taiwan in unprecedented 'autonomous' AI cyber attack](https://www.ft.com/content/7d2ab3e0-9085-48f6-b38a-d90260d58795)

- [MITRE ATLAS 官方案例页 (AML.CS0071)](https://atlas.mitre.org/studies/AML.CS0071/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
