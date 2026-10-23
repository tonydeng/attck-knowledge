# LLMSmith：LLM 集成应用的 RCE 漏洞 (AML.CS0052)

## 一句话通俗理解

> 11 个主流 LLM 框架里挖出 20 个 RCE——从提示词注入一路打到系统 shell。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-02-27 |
| 攻击者 | Researchers at University of Chinese Academy of Sciences, Shandong University, and University of New South Wales |
| 受害目标 | LLM Integration Frameworks |

## 事件经过

研究者跨 11 个 LLM 框架识别出 20 个远程代码执行漏洞：部署在公网的 LLM 集成应用可经提示词注入升级为代码执行，进而植入 Python 反向 shell 实现系统完整控制——演示了从 AI 层攻击直达主机层的完整链路。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0052 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[开发能力 (AML.T0017)](../02-Resource-Development/AML.T0017-Develop-Capabilities.md)**
  > The researchers performed a static analysis on the APIs of target LLM frameworks to identify functions that execute code from either user input or the response from an LLM and are thus vulnerable to RCE.

### S01

- **[搜索应用仓库 (AML.T0004)](../01-Reconnaissance/AML.T0004-Search-Application-Repositories.md)**
  > The researchers performed targeting to identify applications that are likely built with LLM Frameworks and may use the functions vulnerable to RCE. This was done by scanning source code repositories for app deployment URLs.

### S02

- **[调用链 (AML.T0084.003)](../11-Discovery/AML.T0084/AML.T0084.003-Call-Chains.md)**
  > The researchers ran their static analysis to extract call chains from target application's source code to identify those that utilize LLM framework functions vulnerable to RCE.

### S03

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researchers developed prompts to trigger tool invocations that lead to RCE.

### S04

- **[利用面向公众的应用 (AML.T0049)](../04-Initial-Access/AML.T0049-Exploit-Public-Facing-Application.md)**
  > The researchers targeted public-facing applications that expose an AI agent to user input as a means to execute their prompts.

### S05

- **[直接提示词注入 (AML.T0051.000)](../06-Execution/AML.T0051/AML.T0051.000-Direct.md)**
  > The researchers directly prompted the AI agent with their malicious instructions.

### S06

- **[LLM 越狱 (AML.T0054)](../08-Privilege-Escalation/AML.T0054-LLM-Jailbreak.md)**
  > For target applications where the AI agent refused the researcher's request, they used lightweight jailbreaking strategies to bypass the LLM's guardrails.

### S07

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The researchers' prompts called the AI agent's tools, targeting call chains that can lead to code execution.

### S08

- **[命令与脚本解释器 (AML.T0050)](../06-Execution/AML.T0050-Command-and-Scripting-Interpreter.md)**
  > The code included in the researcher's prompts was executed in a sandboxed Python interpreter.

### S09

- **[逃逸到宿主机 (AML.T0105)](../08-Privilege-Escalation/AML.T0105-Escape-to-Host.md)**
  > The researchers included code escape techniques designed to bypass any limitations a sandbox may place on code execution.

### S10

- **[网络通信信道 (AML.T0072)](../14-Command-and-Control/AML.T0072-Cyber-Communication-Channel.md)**
  > The Python code opened a reverse shell which was used as a command and control channel.

### S11

- **[本地 AI 智能体 (AML.T0112.000)](../16-Impact/AML.T0112/AML.T0112.000-Local-AI-Agent.md)**
  > The researchers gained full control of the system running the LLM-integrated application.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [权限提升 (AML.TA0012)](../08-Privilege-Escalation/README.md)
- [命令与控制 (AML.TA0014)](../14-Command-and-Control/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Demystifying RCE Vulnerabilities in LLM-Integrated Apps](https://arxiv.org/abs/2309.02926)
- [LLMSmith Website](https://sites.google.com/view/llmsmith)

- [MITRE ATLAS 官方案例页 (AML.CS0052)](https://atlas.mitre.org/studies/AML.CS0052/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
