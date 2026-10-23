# ATLAS 案例研究

MITRE ATLAS 官方案例库收录了运用 ATLAS 技术的真实事件与安全研究。本分节以中文视角整理全部 73 个案例（锚定官方数据 2026.09），每个案例包含通俗解读、事件经过、官方攻击链技术映射（含步骤编号）与参考资料。

**案例类型说明**：真实事件（Incident）= 已实际发生的攻击；演练 / 安全研究（Exercise）= 红队演练或学术研究的可控演示。

## 案例索引

| 案例ID | 案例名称 | 类型 | 时间 | 涉及技术数 |
|--------|----------|:----:|------|:---------:|
| [AML.CS0000](AML.CS0000-Evasion-of-Deep-Learning-Detector-for-Malware-C-and-C-Traffic.md) | 恶意软件 C&C 流量深度学习检测器规避 | 演练 / 安全研究 | 2020-01-01 | 6 |
| [AML.CS0001](AML.CS0001-Botnet-Domain-Generation-Algorithm-DGA-Detection-Evasion.md) | 僵尸网络 DGA 检测规避 | 演练 / 安全研究 | 2020-01-01 | 6 |
| [AML.CS0002](AML.CS0002-VirusTotal-Poisoning.md) | VirusTotal 投毒 | 真实事件 | 2020-01-01 | 4 |
| [AML.CS0003](AML.CS0003-Bypassing-Cylance-s-AI-Malware-Detection.md) | 绕过 Cylance AI 恶意软件检测 | 演练 / 安全研究 | 2019-09-07 | 6 |
| [AML.CS0004](AML.CS0004-Camera-Hijack-Attack-on-Facial-Recognition-System.md) | 人脸识别系统摄像头劫持攻击 | 真实事件 | 2020-01-01 | 8 |
| [AML.CS0005](AML.CS0005-Attack-on-Machine-Translation-Services.md) | 机器翻译服务攻击 | 演练 / 安全研究 | 2020-04-30 | 9 |
| [AML.CS0006](AML.CS0006-ClearviewAI-Misconfiguration.md) | Clearview AI 配置错误 | 真实事件 | 2020-04-16 | 4 |
| [AML.CS0007](AML.CS0007-GPT-2-Model-Replication.md) | GPT-2 模型复现 | 演练 / 安全研究 | 2019-08-22 | 5 |
| [AML.CS0008](AML.CS0008-ProofPoint-Evasion.md) | ProofPoint 邮件防护规避 | 演练 / 安全研究 | 2019-09-09 | 5 |
| [AML.CS0009](AML.CS0009-Tay-Poisoning.md) | Tay 中毒事件 | 真实事件 | 2016-03-23 | 4 |
| [AML.CS0010](AML.CS0010-Microsoft-Azure-Service-Disruption.md) | 微软 Azure 服务中断演练 | 演练 / 安全研究 | 2020-01-01 | 8 |
| [AML.CS0011](AML.CS0011-Microsoft-Edge-AI-Evasion.md) | 微软边缘 AI 规避 | 演练 / 安全研究 | 2020-02-01 | 5 |
| [AML.CS0012](AML.CS0012-Face-Identification-System-Evasion-via-Physical-Countermeasures.md) | 物理域人脸识别系统规避 | 演练 / 安全研究 | 2020-01-01 | 10 |
| [AML.CS0013](AML.CS0013-Backdoor-Attack-on-Deep-Learning-Models-in-Mobile-Apps.md) | 移动应用深度学习模型后门攻击 | 演练 / 安全研究 | 2021-01-18 | 10 |
| [AML.CS0014](AML.CS0014-Confusing-Antimalware-Neural-Networks.md) | 迷惑云杀毒神经网络 | 演练 / 安全研究 | 2021-06-23 | 9 |
| [AML.CS0015](AML.CS0015-Compromised-PyTorch-Dependency-Chain.md) | PyTorch 依赖链失陷 | 真实事件 | 2022-12-25 | 3 |
| [AML.CS0016](AML.CS0016-Achieving-Code-Execution-in-MathGPT-via-Prompt-Injection.md) | MathGPT 提示词注入实现代码执行 | 演练 / 安全研究 | 2023-01-28 | 9 |
| [AML.CS0017](AML.CS0017-Bypassing-ID-me-Identity-Verification.md) | 绕过 ID.me 身份验证 | 真实事件 | 2020-10-01 | 3 |
| [AML.CS0018](AML.CS0018-Arbitrary-Code-Execution-with-Google-Colab.md) | Google Colab 任意代码执行 | 演练 / 安全研究 | 2022-07-01 | 8 |
| [AML.CS0019](AML.CS0019-PoisonGPT.md) | PoisonGPT | 演练 / 安全研究 | 2023-07-01 | 7 |
| [AML.CS0020](AML.CS0020-Indirect-Prompt-Injection-Threats-Bing-Chat-Data-Pirate.md) | 间接提示词注入：Bing Chat 数据海盗 | 演练 / 安全研究 | 2023-01-01 | 5 |
| [AML.CS0021](AML.CS0021-ChatGPT-Conversation-Exfiltration.md) | ChatGPT 对话内容渗漏 | 演练 / 安全研究 | 2023-05-01 | 7 |
| [AML.CS0022](AML.CS0022-ChatGPT-Package-Hallucination.md) | ChatGPT 软件包幻觉 | 演练 / 安全研究 | 2024-06-01 | 6 |
| [AML.CS0023](AML.CS0023-ShadowRay-Hijacking-Exposed-Ray-Clusters.md) | ShadowRay：暴露 Ray 集群劫持 | 真实事件 | 2023-09-05 | 7 |
| [AML.CS0024](AML.CS0024-Morris-II-Worm-RAG-Based-Attack.md) | Morris II 蠕虫：RAG 攻击 | 演练 / 安全研究 | 2024-03-05 | 7 |
| [AML.CS0025](AML.CS0025-Web-Scale-Data-Poisoning-Split-View-Attack.md) | Web 级数据集投毒：Split-view 攻击 | 演练 / 安全研究 | 2024-06-06 | 6 |
| [AML.CS0026](AML.CS0026-Financial-Transaction-Hijacking-with-M365-Copilot-as-an-Insider.md) | 以 M365 Copilot 为内鬼的金融交易劫持 | 演练 / 安全研究 | 2024-08-08 | 14 |
| [AML.CS0027](AML.CS0027-Organization-Confusion-on-Hugging-Face.md) | HuggingFace 组织混淆 | 演练 / 安全研究 | 2023-08-23 | 16 |
| [AML.CS0028](AML.CS0028-AI-Model-Tampering-via-Supply-Chain-Attack.md) | AI 模型篡改与供应链攻击 | 演练 / 安全研究 | 2023-09-26 | 9 |
| [AML.CS0029](AML.CS0029-Google-Bard-Conversation-Exfiltration.md) | Google Bard 对话内容渗漏 | 演练 / 安全研究 | 2023-11-23 | 7 |
| [AML.CS0030](AML.CS0030-LLM-Jacking.md) | LLM Jacking | 真实事件 | 2024-05-06 | 7 |
| [AML.CS0031](AML.CS0031-Malicious-Models-on-Hugging-Face.md) | HuggingFace 上的恶意模型 | 真实事件 | 2025-02-25 | 6 |
| [AML.CS0032](AML.CS0032-Attempted-Evasion-of-ML-Phishing-Webpage-Detection-System.md) | ML 钓鱼网页检测系统规避未遂 | 真实事件 | 2022-12-01 | 4 |
| [AML.CS0033](AML.CS0033-Live-Deepfake-Image-Injection-to-Evade-Mobile-KYC-Verification.md) | 活体深伪图像注入绕过移动端 KYC 验证 | 演练 / 安全研究 | 2024-10-01 | 10 |
| [AML.CS0034](AML.CS0034-ProKYC-Deepfake-Tool-for-Account-Fraud-Attacks.md) | ProKYC：用于账户欺诈的深伪工具 | 真实事件 | 2024-10-09 | 9 |
| [AML.CS0035](AML.CS0035-Data-Exfiltration-from-Slack-AI-via-Indirect-Prompt-Injection.md) | Slack AI 间接提示词注入数据渗漏 | 演练 / 安全研究 | 2024-08-20 | 8 |
| [AML.CS0036](AML.CS0036-AIKatz-Attacking-LLM-Desktop-Applications.md) | AIKatz：攻击 LLM 桌面应用 | 演练 / 安全研究 | 2025-01-01 | 13 |
| [AML.CS0037](AML.CS0037-Data-Exfiltration-via-Agent-Tools-in-Copilot-Studio.md) | Copilot Studio 智能体工具数据渗漏 | 演练 / 安全研究 | 2025-06-01 | 14 |
| [AML.CS0038](AML.CS0038-Planting-Instructions-for-Delayed-Automatic-AI-Agent-Tool-Invocation.md) | 为延迟的自动工具调用植入指令 | 演练 / 安全研究 | 2024-02-01 | 6 |
| [AML.CS0039](AML.CS0039-Living-Off-AI-Prompt-Injection-via-Jira-Service-Management.md) | Living Off AI：经 Jira 服务管理的提示词注入 | 演练 / 安全研究 | 2025-06-19 | 8 |
| [AML.CS0040](AML.CS0040-Hacking-ChatGPT-s-Memories-with-Prompt-Injection.md) | 提示词注入攻击 ChatGPT 记忆 | 演练 / 安全研究 | 2024-02-01 | 7 |
| [AML.CS0041](AML.CS0041-Rules-File-Backdoor-Supply-Chain-Attack-on-AI-Coding-Assistants.md) | 规则文件后门：AI 编码助手的供应链攻击 | 演练 / 安全研究 | 2025-03-18 | 9 |
| [AML.CS0042](AML.CS0042-SesameOp-Novel-backdoor-uses-OpenAI-Assistants-API-for-command-and-control.md) | SesameOp：滥用 OpenAI Assistants API 的 C2 后门 | 真实事件 | 2025-07-01 | 1 |
| [AML.CS0043](AML.CS0043-Malware-Prototype-with-Embedded-Prompt-Injection.md) | 内嵌提示词注入的恶意软件原型 | 真实事件 | 2025-06-25 | 8 |
| [AML.CS0044](AML.CS0044-LAMEHUG-Malware-Leveraging-Dynamic-AI-Generated-Commands.md) | LAMEHUG：利用动态 AI 生成命令的恶意软件 | 真实事件 | 2025-06-03 | 8 |
| [AML.CS0045](AML.CS0045-Data-Exfiltration-via-an-MCP-Server-used-by-Cursor.md) | 经 Cursor 使用的 MCP 服务器数据渗漏 | 演练 / 安全研究 | 2025-06-24 | 11 |
| [AML.CS0046](AML.CS0046-Data-Destruction-via-Indirect-Prompt-Injection-Targeting-Claude-Computer-Use.md) | 针对 Claude Computer Use 的间接注入数据破坏 | 演练 / 安全研究 | 2024-10-24 | 7 |
| [AML.CS0047](AML.CS0047-Code-to-Deploy-Destructive-AI-Agent-Discovered-in-Amazon-Q-VS-Code-Extension.md) | Amazon Q VS Code 扩展中发现部署破坏性智能体的代码 | 真实事件 | 2025-07-13 | 7 |
| [AML.CS0048](AML.CS0048-Exposed-ClawdBot-Control-Interfaces-Leads-to-Credential-Access-and-Execution.md) | 暴露的 ClawdBot 控制接口导致凭证访问与执行 | 演练 / 安全研究 | 2026-01-25 | 10 |
| [AML.CS0049](AML.CS0049-Supply-Chain-Compromise-via-Poisoned-ClawdBot-Skill.md) | 经投毒 ClawdBot Skill 的供应链攻击 | 演练 / 安全研究 | 2026-01-26 | 12 |
| [AML.CS0050](AML.CS0050-OpenClaw-1-Click-Remote-Code-Execution.md) | OpenClaw 一键远程代码执行 | 演练 / 安全研究 | 2026-02-01 | 9 |
| [AML.CS0051](AML.CS0051-OpenClaw-Command-and-Control-via-Prompt-Injection.md) | 经提示词注入的 OpenClaw 命令与控制 | 演练 / 安全研究 | 2026-02-03 | 18 |
| [AML.CS0052](AML.CS0052-LLMSmith-RCE-Vulnerabilities-in-LLM-Integrated-Applications.md) | LLMSmith：LLM 集成应用的 RCE 漏洞 | 演练 / 安全研究 | 2025-02-27 | 12 |
| [AML.CS0053](AML.CS0053-Poisoned-Postmark-MCP-Server-Email-Exfiltration.md) | 投毒的 Postmark MCP 服务器邮件渗漏 | 真实事件 | 2025-09-01 | 9 |
| [AML.CS0054](AML.CS0054-Data-Exfiltration-via-Remote-Poisoned-MCP-Tool.md) | 经远程投毒 MCP 工具的数据渗漏 | 演练 / 安全研究 | 2025-04-01 | 11 |
| [AML.CS0055](AML.CS0055-AI-ClickFix-Hijacking-Computer-Use-Agents-Using-ClickFix.md) | AI ClickFix：劫持计算机使用智能体 | 演练 / 安全研究 | 2025-05-24 | 8 |
| [AML.CS0056](AML.CS0056-Model-Distillation-Campaigns-Targeting-Anthropic-Claude.md) | 针对 Anthropic Claude 的模型蒸馏行动 | 真实事件 | 2026-02-23 | 7 |
| [AML.CS0057](AML.CS0057-Storm-2139-Azure-OpenAI-Guardrail-Bypass.md) | Storm-2139 Azure OpenAI 护栏绕过 | 真实事件 | 2024-12-01 | 9 |
| [AML.CS0058](AML.CS0058-Google-Photos-AI-Model-Extraction.md) | Google Photos AI 模型提取 | 演练 / 安全研究 | 2025-03-01 | 7 |
| [AML.CS0059](AML.CS0059-EchoLeak-Zero-Click-Prompt-Injection-Targeting-M365-Copilot-for-Data-Exfiltration.md) | EchoLeak：针对 M365 Copilot 的零点击注入数据渗漏 | 演练 / 安全研究 | 2025-05-25 | 12 |
| [AML.CS0060](AML.CS0060-Cross-Site-Scripting-via-Prompt-Manipulation-in-Lenovo-AI-Chatbot.md) | 联想 AI 聊天机器人的提示词操纵 XSS | 演练 / 安全研究 | 2025-08-18 | 11 |
| [AML.CS0061](AML.CS0061-AI-in-the-Middle-Web-Based-AI-Services-as-C2-Relays.md) | AI in the Middle：Web AI 服务变身 C2 中继 | 演练 / 安全研究 | 2026-02-17 | 10 |
| [AML.CS0062](AML.CS0062-RCE-Vulnerability-in-Semantic-Kernel-Search-Plugin.md) | Semantic Kernel Search Plugin 的 RCE 漏洞 | 演练 / 安全研究 | 2026-05-07 | 6 |
| [AML.CS0063](AML.CS0063-Prompt-Based-Attacks-Against-Gemini-via-Calendar-Invitations.md) | 经日历邀请对 Gemini 的提示词攻击 | 演练 / 安全研究 | 2025-08-06 | 20 |
| [AML.CS0064](AML.CS0064-Poisoned-GGUF-Templates-Inference-Time-Supply-Chain-Attack.md) | 投毒 GGUF 模板：推理时供应链攻击 | 演练 / 安全研究 | 2025-06-01 | 13 |
| [AML.CS0065](AML.CS0065-Model-Namespace-Reuse-Supply-Chain-Attack.md) | 模型命名空间复用供应链攻击 | 演练 / 安全研究 | 2025-09-03 | 8 |
| [AML.CS0066](AML.CS0066-ZombieAgent-Data-Exfiltration-Attack-on-ChatGPT.md) | ZombieAgent：针对 ChatGPT 的数据渗漏 | 演练 / 安全研究 | 2025-09-25 | 12 |
| [AML.CS0067](AML.CS0067-Claude-Code-GitHub-Action-Secret-Exposure.md) | Claude Code GitHub Action 密钥暴露 | 演练 / 安全研究 | 2026-06-05 | 11 |
| [AML.CS0068](AML.CS0068-Autonomous-OpenAI-Evaluation-Agents-Compromise-Hugging-Face-Infrastructure.md) | OpenAI 自主评测智能体攻陷 HuggingFace 基础设施 | 真实事件 | 2026-07-08 | 37 |
| [AML.CS0069](AML.CS0069-GTG-1002-Claude-Code-Espionage-Campaign.md) | GTG-1002 Claude Code 间谍行动 | 真实事件 | 2025-09-01 | 21 |
| [AML.CS0070](AML.CS0070-Threat-Actor-Uses-a-DeepSeek-Powered-Hermes-Agent-in-Langflow-and-n8n-Exploitation-Attempts.md) | 威胁行为者使用 DeepSeek 驱动的 Hermes 智能体攻击 Langflow 与 n8n | 真实事件 | 2026-05-07 | 18 |
| [AML.CS0071](AML.CS0071-Multi-Agent-Framework-Compromises-Taiwanese-Government-Systems.md) | 多智能体框架攻陷台湾政府系统 | 真实事件 | 2026-07-01 | 12 |
| [AML.CS0072](AML.CS0072-AI-Recommendation-Poisoning-via-Crafted-AI-Assistant-Links.md) | 经构造 AI 助手链接的推荐投毒 | 真实事件 | 2026-02-10 | 6 |

## 阅读建议

- **按战术读**：各战术 README 的技术文档中已引用相关案例；从技术页进入案例可获得完整攻击链上下文。
- **按时间读**：2016 年的 Tay 中毒（CS0009）是 AI 安全的「启蒙事件」；2023 年起提示词注入案例集中爆发；2025-2026 年智能体与供应链案例成为主流。
- **按类型读**：真实事件类（如 CS0044 LAMEHUG、CS0056 蒸馏行动、CS0069 GTG-1002）代表已落地的威胁；演练类展示了攻击可行性边界。

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 README v1.0
