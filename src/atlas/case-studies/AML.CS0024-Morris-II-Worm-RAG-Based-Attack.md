# Morris II 蠕虫：RAG 攻击 (AML.CS0024)

## 一句话通俗理解

> 全球第一个「AI 蠕虫」：一封邮件感染 RAG 邮件助手，泄露隐私后自我复制发给下一个人。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2024-03-05 |
| 攻击者 | Stav Cohen, Ron Bitton, Ben Nassi |
| 受害目标 | RAG-based e-mail assistant |

## 事件经过

研究者开发了 Morris II——针对生成式 AI 生态的零点击蠕虫：发送一封含对抗性自复制提示词的邮件，RAG 邮件助手自动摄取并执行，泄露检索到的私人邮件内容（邮件、地址等敏感数据），并把蠕虫提示词复制进回复继续传播。蠕虫借 GenAI 系统间的连接性实现跨系统扩散。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0024 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[AI 模型推理 API 访问 (AML.T0040)](../05-AI-Model-Access/AML.T0040-AI-Model-Inference-API-Access.md)**
  > The researchers use access to the publicly available GenAI model API that powers the target RAG-based email system.

### S01

- **[直接提示词注入 (AML.T0051.000)](../06-Execution/AML.T0051/AML.T0051.000-Direct.md)**
  > The researchers test prompts on public model APIs to identify working prompt injections.

### S02

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The researchers send an email containing an adversarial self-replicating prompt, or "AI worm," to an address used in the target email system. The GenAI email assistant automatically ingests the email as part of its normal operations to generate a suggested reply. The email is stored in the database used for retrieval augmented generation, compromising the RAG system.

### S03

- **[触发式提示词注入 (AML.T0051.002)](../06-Execution/AML.T0051/AML.T0051.002-Triggered.md)**
  > When the email containing the worm is retrieved by the email assistant in another reply generation task, the prompt injection changes the behavior of the GenAI email assistant.

### S04

- **[LLM 提示词自我复制 (AML.T0061)](../07-Persistence/AML.T0061-LLM-Prompt-Self-Replication.md)**
  > The self-replicating portion of the prompt causes the generated output to contain the malicious prompt, allowing the worm to propagate.

### S05

- **[LLM 数据泄露 (AML.T0057)](../15-Exfiltration/AML.T0057-LLM-Data-Leakage.md)**
  > The malicious instructions in the prompt cause the generated output to leak sensitive data such as emails, addresses, and phone numbers.

### S06

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > Users of the GenAI email assistant may have PII leaked to attackers.

## 关联战术

- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Here Comes The AI Worm: Unleashing Zero-click Worms that Target GenAI-Powered Applications](https://arxiv.org/abs/2403.02817)

- [MITRE ATLAS 官方案例页 (AML.CS0024)](https://atlas.mitre.org/studies/AML.CS0024/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
