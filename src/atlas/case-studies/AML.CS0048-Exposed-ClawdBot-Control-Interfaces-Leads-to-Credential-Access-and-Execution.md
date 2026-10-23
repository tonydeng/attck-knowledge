# 暴露的 ClawdBot 控制接口导致凭证访问与执行 (AML.CS0048)

## 一句话通俗理解

> 几百个 OpenClaw 控制端口裸奔在公网——谁连上谁就是这台 AI 管家的主人。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2026-01-25 |
| 攻击者 | Jamieson O'Reilly |
| 受害目标 | ClawdBot (now OpenClaw) |

## 事件经过

安全研究者在公网上发现数百个暴露的 ClawdBot（现 OpenClaw）控制接口。这些个人 AI 助手运行在用户自己的设备上且拥有系统权限——暴露的控制接口允许任何人访问其凭证、执行命令，将宿主系统拱手交出。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0048 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[扫描数据库 (AML.T0000.003)](../01-Reconnaissance/AML.T0000/AML.T0000.003-Scan-Databases.md)**
  > The researcher performed targeting by searching for the title tag of ClawdBot's web-based control interface, "Clawdbot Control" on Shodan, identifying hundreds of ClawdBot control interfaces exposed on the public internet.

### S01

- **[AI 服务配置错误或公开暴露 (AML.T0132)](../04-Initial-Access/AML.T0132-Misconfigured-or-Publicly-Exposed-AI-Services.md)**
  > The researcher exploited a proxy misconfiguration present in ClawdBot's control server to gain access to control interfaces that had authentication enabled.

### S02

- **[从 AI 智能体配置获取凭证 (AML.T0083)](../10-Credential-Access/AML.T0083-Credentials-from-AI-Agent-Configuration.md)**
  > The researcher accessed credentials to a variety of services stored in plaintext in ClawdBot's configuration file (`~/.clawdbot/clawdbot.json`, which is visible in the ClawdBot dashboard. Across various exposed ClawdBot instances, they found:
- Anthropic API Keys 
- Telegram Bot Tokens
- Slack Oauth Credentials
- Signal Device Linking URIs

### S03

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > The researcher was able to prompt ClawdBot directly through the control interface.

### S04

- **[系统提示词 (AML.T0069.002)](../11-Discovery/AML.T0069/AML.T0069.002-System-Prompt.md)**
  > The researcher prompted ClawdBot to `cat SOUL.md` (the file containing ClawdBot's system prompt), and it replied with its contents.

### S05

- **[AI 智能体工具凭证窃取 (AML.T0098)](../10-Credential-Access/AML.T0098-AI-Agent-Tool-Credential-Harvesting.md)**
  > The researcher prompted ClawdBot with `env` and it responded by invoking its `bash` skill  and executing the `env` command, which contained additional secrets for other services.

### S06

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > The researcher prompted ClawdBot with `root` and it responded by invoking its `bash`skill logged in as the root user.

### S07

- **[操纵用户 LLM 对话历史 (AML.T0092)](../09-Defense-Evasion/AML.T0092-Manipulate-User-LLM-Chat-History.md)**
  > The researcher could have used the found Anthropic API Keys to manipulate the ClawdBot's chat history with the user including deleting or modifying messages.

### S08

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > The researcher could have used the discovered application tokens to exfiltrate entire private conversation histories including shared files from any connected messaging apps (e.g. Telegram, Slack, Discord, Signal, WhatsApp, etc.).

### S09

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The researcher could have used the discovered application tokens to cause further harms to the user, including impersonation by sending messages on the user's behalf via any of the connected messaging apps.

## 关联战术

- [侦察 (AML.TA0002)](../01-Reconnaissance/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [GitHub - openclaw/openclaw: Your own personal AI assistant. Any OS. Any Platform. The lobster way. GitHub](https://github.com/openclaw/openclaw)
- [Clawdbot Control - Shodan Search](https://www.shodan.io/search?query=Clawdbot+Control)
- [hacking clawdbot and eating lobster souls](https://x.com/theonejvo/status/2015401219746128322)

- [MITRE ATLAS 官方案例页 (AML.CS0048)](https://atlas.mitre.org/studies/AML.CS0048/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
