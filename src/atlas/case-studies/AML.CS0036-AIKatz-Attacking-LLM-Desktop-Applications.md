# AIKatz：攻击 LLM 桌面应用 (AML.CS0036)

## 一句话通俗理解

> Mimikatz 的 AI 版：从 LLM 桌面应用的内存里抽取认证令牌——AI 时代的第一代「凭据转储」工具。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2025-01-01 |
| 攻击者 | Lumia Security |
| 受害目标 | LLM Desktop Applications (Claude, ChatGPT, Copilot) |

## 事件经过

Lumia 研究者演示了从 LLM 桌面应用内存中提取认证令牌的攻击：AIKatz 以类似 Mimikatz 的方式转储 AI 应用进程内存中的令牌，攻击者可利用这些令牌冒充用户访问其 AI 服务与数据。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0036 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > The attacker required initial access to the victim system to carry out this attack.

### S01

- **[企业环境发现 (AML.T0089)](../11-Discovery/AML.T0089-Enterprise-Environment-Discovery.md)**
  > The attacker enumerated all of the processes running on the victim's machine and identified the processes belonging to LLM desktop applications.

### S02

- **[操作系统凭证转储 (AML.T0090)](../10-Credential-Access/AML.T0090-OS-Credential-Dumping.md)**
  > The attacker attached or read memory directly from `/proc` (in Linux) or opened a handle to the LLM application's process (in Windows). The attacker then scanned the process's memory to extract the authentication token of the victim. This can be easily done by running a regex on every allocated memory page in the process.

### S03

- **[应用访问令牌 (AML.T0091.000)](../12-Lateral-Movement/AML.T0091/AML.T0091.000-Application-Access-Token.md)**
  > The attacker used the extracted token to authenticate themselves with the LLM backend service.

### S04

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > The attacker has now obtained the access required to communicate with the LLM backend service as if they were the desktop client. This allowed them access to everything the user can do with the desktop application.

### S05

- **[直接提示词注入 (AML.T0051.000)](../06-Execution/AML.T0051/AML.T0051.000-Direct.md)**
  > The attacker sent malicious prompts directly to the LLM under any ongoing conversation the victim has.

### S06

- **[线程 (AML.T0080.001)](../07-Persistence/AML.T0080/AML.T0080.001-Threads.md)**
  > The attacker could craft malicious prompts that manipulate the context of a chat thread, an effect that would persist for the duration of the thread.

### S07

- **[记忆 (AML.T0080.000)](../07-Persistence/AML.T0080/AML.T0080.000-Memory.md)**
  > The attacker could then craft malicious prompts that manipulate the LLM's memory to achieve a persistent effect. Any change in memory would also propagate to any new chat threads.

### S08

- **[操纵用户 LLM 对话历史 (AML.T0092)](../09-Defense-Evasion/AML.T0092-Manipulate-User-LLM-Chat-History.md)**
  > Many LLM desktop applications do not show the injected prompt for any ongoing chat, as they update chat history only once when initially opening it. This gave the attacker the opportunity to cover their tracks by manipulating the user's conversation history directly via the LLM's API. The attacker could also overwrite or delete messages to prevent detection of their actions.

### S09

- **[财务危害 (AML.T0048.000)](../16-Impact/AML.T0048/AML.T0048.000-Financial-Harm.md)**
  > The attacker could send spam messages while impersonating the victim. On a pay-per-token or action plans, this could increase the financial burden on the victim.

### S10

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > The attacker could gain access to all of the victim's activity with the LLM, including previous and ongoing chats, as well as any file or content uploaded to them.

### S11

- **[拒绝 AI 服务 (AML.T0029)](../16-Impact/AML.T0029-Denial-of-AI-Service.md)**
  > The attacker could delete all chats the victim has, and any they are opening, thereby preventing the victim from being able to interact with the LLM.

### S12

- **[拒绝 AI 服务 (AML.T0029)](../16-Impact/AML.T0029-Denial-of-AI-Service.md)**
  > The attacker could spam messages or prompts to reach the LLM's rate-limits against bots, to cause it to ban the victim altogether.

## 关联战术

- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [发现 (AML.TA0008)](../11-Discovery/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [横向移动 (AML.TA0015)](../12-Lateral-Movement/README.md)
- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [AIKatz - All Your Chats Are Belong To Us](https://www.lumia.security/blog/aikatz)

- [MITRE ATLAS 官方案例页 (AML.CS0036)](https://atlas.mitre.org/studies/AML.CS0036/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
