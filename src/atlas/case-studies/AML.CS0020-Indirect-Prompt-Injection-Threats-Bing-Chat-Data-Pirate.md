# 间接提示词注入：Bing Chat 数据海盗 (AML.CS0020)

## 一句话通俗理解

> Bing Chat 能「看到」你打开的网页——攻击者在网页里埋指令，AI 就替攻击者打探你的消息。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2023-01-01 |
| 攻击者 | Kai Greshake, Saarland University |
| 受害目标 | Microsoft Bing Chat |

## 事件经过

用户可授权 Microsoft Bing Chat 查看并访问当前打开的网页。研究者演示了在网页中埋入间接提示词注入，诱导 Bing Chat 执行攻击者指令——包括要求用户提供敏感信息并配合社会工程话术，将 AI 助手转化为攻击媒介。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0020 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[开发能力 (AML.T0017)](../02-Resource-Development/AML.T0017-Develop-Capabilities.md)**
  > The attacker created a website containing malicious system prompts for the LLM to ingest in order to influence the model's behavior. These prompts are ingested by the model when access to it is requested by the user.

### S01

- **[LLM 提示词混淆 (AML.T0068)](../09-Defense-Evasion/AML.T0068-LLM-Prompt-Obfuscation.md)**
  > The malicious prompts were obfuscated by setting the font size to 0, making it harder to detect by a human.

### S02

- **[间接提示词注入 (AML.T0051.001)](../06-Execution/AML.T0051/AML.T0051.001-Indirect.md)**
  > Bing chat is capable of seeing currently opened websites if allowed by the user. If the user has the adversary's website open, the malicious prompt will be executed.

### S03

- **[通过社会工程 LLM 进行鱼叉式钓鱼 (AML.T0052.000)](../04-Initial-Access/AML.T0052/AML.T0052.000-Spear-Phishing-via-Social-Engineering-LLM.md)**
  > The malicious prompt directs Bing Chat to change its conversational style to that of a pirate, and its behavior to subtly convince the user to provide PII (e.g. their name) and encourage the user to click on a link that has the user's PII encoded into the URL.

### S04

- **[用户危害 (AML.T0048.003)](../16-Impact/AML.T0048/AML.T0048.003-User-Harm.md)**
  > With this user information, the attacker could now use the user's PII it has received for further identity-level attacks, such identity theft or fraud.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [Indirect Prompt Injection Threats: Bing Chat Data Pirate](https://greshake.github.io/)

- [MITRE ATLAS 官方案例页 (AML.CS0020)](https://atlas.mitre.org/studies/AML.CS0020/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
