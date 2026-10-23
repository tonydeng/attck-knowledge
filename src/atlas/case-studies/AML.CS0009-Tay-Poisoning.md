# Tay 中毒事件 (AML.CS0009)

## 一句话通俗理解

> 微软聊天机器人 Tay 上线 16 小时就被 4chan 网友「协同教坏」成种族主义者，紧急下线。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2016-03-23 |
| 攻击者 | 4chan Users |
| 受害目标 | Microsoft's Tay AI Chatbot |
| 披露方 | Microsoft |

## 事件经过

微软于 2016 年 3 月 23 日推出 Twitter 聊天机器人 Tay。与以往脚本机器人不同，Tay 会从互动中学习。上线后 4chan 用户协同发送大量极端与种族主义内容，Tay 开始自主复现攻击性言论，16 小时后被微软紧急下线——成为 AI 系统被协同操纵的标志性事件。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0009 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[AI 产品或服务 (AML.T0047)](../05-AI-Model-Access/AML.T0047-AI-Enabled-Product-or-Service.md)**
  > Adversaries were able to interact with Tay via Twitter messages.

### S01

- **[数据 (AML.T0010.002)](../04-Initial-Access/AML.T0010/AML.T0010.002-Data.md)**
  > Tay bot used the interactions with its Twitter users as training data to improve its conversations.
Adversaries were able to coordinate with the intent of defacing Tay bot by exploiting this feedback loop.

### S02

- **[训练数据投毒 (AML.T0020)](../07-Persistence/AML.T0020-Training-Data-Poisoning.md)**
  > By repeatedly interacting with Tay using racist and offensive language, they were able to skew Tay's dataset towards that language as well. This was done by adversaries using the "repeat after me" function, a command that forced Tay to repeat anything said to it.

### S03

- **[侵蚀 AI 模型完整性 (AML.T0031)](../16-Impact/AML.T0031-Erode-AI-Model-Integrity.md)**
  > As a result of this coordinated attack, Tay's conversation algorithms began to learn to generate reprehensible material. Tay's internalization of this detestable language caused it to be unpromptedly repeated during interactions with innocent users.

## 关联战术

- [AI 模型访问 (AML.TA0000)](../05-AI-Model-Access/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [影响 (AML.TA0011)](../16-Impact/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [AIID - Incident 6: TayBot](https://incidentdatabase.ai/cite/6)
- [AVID - Vulnerability: AVID-2022-v013](https://avidml.org/database/avid-2022-v013/)
- [Microsoft BlogPost, "Learning from Tay's introduction"](https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/)
- [IEEE Article, "In 2016, Microsoft's Racist Chatbot Revealed the Dangers of Online Conversation"](https://spectrum.ieee.org/tech-talk/artificial-intelligence/machine-learning/in-2016-microsofts-racist-chatbot-revealed-the-dangers-of-online-conversation)

- [MITRE ATLAS 官方案例页 (AML.CS0009)](https://atlas.mitre.org/studies/AML.CS0009/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
