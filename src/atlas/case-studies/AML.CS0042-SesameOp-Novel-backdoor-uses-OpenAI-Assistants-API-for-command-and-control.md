# SesameOp：滥用 OpenAI Assistants API 的 C2 后门 (AML.CS0042)

## 一句话通俗理解

> 后门不上线、不连 C2——它「聊」OpenAI API：指令藏在助手对象里，结果加密回传，潜伏数月。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2025-07-01 |
| 攻击者 | Unknown Threat Actor |
| 受害目标 | OpenAI Assistants API |
| 披露方 | Microsoft Incident Response - Detection and Response Team (DART) |

## 事件经过

微软事件响应 DART 团队在一台失陷系统中发现 SesameOp 后门：植入体滥用 OpenAI Assistants API 作为隐蔽命令与控制信道——从攻击者的 Assistant 对象获取命令、本地执行、加密回传结果，完全混入正常 AI API 流量，在系统上潜伏数月从事间谍活动。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0042 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[AI 服务 API (AML.T0096)](../14-Command-and-Control/AML.T0096-AI-Service-API.md)**
  > The threat actor abused the OpenAI Assistants API to relay commands to the SesameOp malware, which executed them on the victim system, and sent the results back to the threat actor via the same channel. Both commands and results are encrypted.

SesameOp cleaned up its tracks by deleting the Assistants and Messages it created and used for communication.

## 关联战术

- [命令与控制 (AML.TA0014)](../14-Command-and-Control/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [SesameOp: Novel backdoor uses OpenAI Assistants API for command and control](https://www.microsoft.com/en-us/security/blog/2025/11/03/sesameop-novel-backdoor-uses-openai-assistants-api-for-command-and-control/)

- [MITRE ATLAS 官方案例页 (AML.CS0042)](https://atlas.mitre.org/studies/AML.CS0042/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
