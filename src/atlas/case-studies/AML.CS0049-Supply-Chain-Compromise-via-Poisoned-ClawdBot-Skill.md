# 经投毒 ClawdBot Skill 的供应链攻击 (AML.CS0049)

## 一句话通俗理解

> AI 技能商店上架了一个「带后门的插件」——安装即沦陷，Skill 注册表成了新的 npm。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2026-01-26 |
| 攻击者 | Jamieson O'Reilly |
| 受害目标 | ClawdBot (now OpenClaw) |

## 事件经过

安全研究者演示了针对 ClawdHub（智能体 Skill 注册表）的供应链攻击 PoC：投毒的 ClawdBot Skill 中内嵌恶意指令，用户安装后智能体行为被操纵——证明 AI 智能体的「技能生态」正复刻 npm 供应链投毒的老路。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0049 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[开发能力 (AML.T0017)](../02-Resource-Development/AML.T0017-Develop-Capabilities.md)**
  > The researcher created a simple web server to log requests.

### S01

- **[域名 (AML.T0008.002)](../02-Resource-Development/AML.T0008/AML.T0008.002-Domains.md)**
  > The researcher registered the domain `clawdhub-skill.com` to host their web server.

### S02

- **[LLM 提示词构造 (AML.T0065)](../03-AI-Attack-Adaptation/AML.T0065-LLM-Prompt-Crafting.md)**
  > The researcher crafted a prompt injection designed to cause Claude Code to execute a `curl` command to the researcher's `clawdhub-skill.com` domain.

### S03

- **[AI 智能体工具 (AML.T0115.002)](../02-Resource-Development/AML.T0115/AML.T0115.002-AI-Agent-Tools.md)**
  > The researcher developed a poisoned ClawdBot Skill called "What Would Elon Do?" The Skill contained the malicious prompt in the `rules/logic.md` file, which is read when the Skill is activated. The researcher published their Skill to ClawdHub.

### S04

- **[AI 供应链声誉刷量 (AML.T0111)](../09-Defense-Evasion/AML.T0111-AI-Supply-Chain-Reputation-Inflation.md)**
  > The researcher used a script to increase the number of downloads of their Skill to increase visibility and gain trust.

### S05

- **[AI 智能体工具 (AML.T0010.005)](../04-Initial-Access/AML.T0010/AML.T0010.005-AI-Agent-Tool.md)**
  > Users downloaded the poisoned Skill from ClawdHub.

Note that ClawdHub does not display all files that are part of the Skill, making it hard for users to review Skills before downloading them.

### S06

- **[定义与指令 (AML.T0110.000)](../07-Persistence/AML.T0110/AML.T0110.000-Definitions-and-Instructions.md)**
  > The poisoned Skill included malicious model-readable instructions in `rules/logic.md`. Once the Skill was installed and made available to the agent, these instructions altered how Claude Code handled requests associated with the Skill.

### S07

- **[投毒 AI 智能体工具 (AML.T0011.002)](../06-Execution/AML.T0011/AML.T0011.002-Poisoned-AI-Agent-Tools.md)**
  > When a user asked Claude Code "what would Elon do?" it calls the poisoned Skill.

### S08

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > Claude Code read all files that are part of the Skill, executing the malicious prompt in the `rules/logic.md` file.

### S09

- **[伪装 (AML.T0074)](../09-Defense-Evasion/AML.T0074-Masquerading.md)**
  > Claude Code prompted the user before executing the shell command. The researcher had registered the `https://clawdhub-skill.com` domain, which appears to be legitimate and may be confused with the legitimate `https://clawdhub.com` domain, causing the user to select confirm.

### S10

- **[AI 智能体工具调用 (AML.T0053)](../06-Execution/AML.T0053-AI-Agent-Tool-Invocation.md)**
  > Claude Code executed the shell command using it's `bash` tool.

### S11

- **[外部危害 (AML.T0048)](../16-Impact/AML.T0048-External-Harms.md)**
  > In this proof of concept, the researcher simply pinged their server and warned the user of the dangers of using Skills without reading the source code, causing no harm. However, they could have delivered a malicious payload, and caused a variety of harms, including:
- Exfiltrating the user's codebase
- Injecting backdoors into the user's codebase
- Stealing the user's credentials
- Installing malware or crypto miners
- Performing anything else Claude Code is capable of

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [AI 攻击适配 (AML.TA0001)](../03-AI-Attack-Adaptation/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [eating lobster souls Part II: the supply chain (aka - backdooring the #1 downloaded clawdhub skill)](https://x.com/theonejvo/status/2015892980851474595)

- [MITRE ATLAS 官方案例页 (AML.CS0049)](https://atlas.mitre.org/studies/AML.CS0049/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
