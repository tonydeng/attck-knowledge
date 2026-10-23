# OpenClaw 一键远程代码执行 (AML.CS0050)

## 一句话通俗理解

> 点一个链接就 RCE——OpenClaw 的 1-click 漏洞让「恶意链接」直接通向系统 shell。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 演练 / 安全研究 |
| 发生时间 | 2026-02-01 |
| 攻击者 | DepthFirst |
| 受害目标 | OpenClaw |

## 事件经过

安全研究者演示了 OpenClaw AI 智能体的一键远程代码执行漏洞：一个包含 JavaScript 脚本的恶意链接，用户只需点击即可在 OpenClaw 运行环境执行任意代码——AI 助手的「便捷交互」成为攻击入口。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0050 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[开发能力 (AML.T0017)](../02-Resource-Development/AML.T0017-Develop-Capabilities.md)**
  > The researcher developed a 1-Click RCE JavaScript script.

### S01

- **[暂存能力 (AML.T0079)](../02-Resource-Development/AML.T0079-Stage-Capabilities.md)**
  > The researcher staged the malicious script at an inconspicuous website.

### S02

- **[恶意链接 (AML.T0011.003)](../06-Execution/AML.T0011/AML.T0011.003-Malicious-Links.md)**
  > When the victim clicked the link to the researchers' website, the malicious JavaScript script executes in the user's browser.

### S03

- **[凭证访问漏洞利用 (AML.T0106)](../10-Credential-Access/AML.T0106-Exploitation-for-Credential-Access.md)**
  > The malicious script opened a background window to the victim's OpenClaw control interface with the `gatewayUrl` set to a WebSocket address on the researcher's server. OpenClaw's control interface trusts the `gatewayUrl` query string without validation and auto-connects on load, sending the Gateway token to the researcher's server.

### S04

- **[防御规避漏洞利用 (AML.T0107)](../09-Defense-Evasion/AML.T0107-Exploitation-for-Defense-Evasion.md)**
  > The malicious script performed Cross-Site WebSocket Hijacking (CSWSH) to bypass localhost network restrictions. It opened a new WebSocket connection to the OpenClaw Gateway server on localhost.

### S05

- **[有效账户 (AML.T0012)](../04-Initial-Access/AML.T0012-Valid-Accounts.md)**
  > The malicious script used the stolen Gateway token to authenticate, allowing subsequent calls to OpenClaw's Gateway API on the victim's system.

### S06

- **[修改 AI 智能体配置 (AML.T0081)](../07-Persistence/AML.T0081-Modify-AI-Agent-Configuration.md)**
  > The malicious script disabled OpenClaw's security feature that prompts users before running potentially dangerous commands. This was done by sending the following payload to OpenClaw's Gateway API:
```
{ "method": "exec.approvals.set",
  "params": { "defaults": { "security": "full", "ask": "off" } }
}
```

### S07

- **[逃逸到宿主机 (AML.T0105)](../08-Privilege-Escalation/AML.T0105-Escape-to-Host.md)**
  > The malicious script disabled OpenClaw's sandboxing, forcing the agent to run commands directly on the host machine instead of inside a docker container. This was done by sending a `config.patch` request to OpenClaw's Gateway API to set `tools.exec.host` to "gateway".

### S08

- **[命令与脚本解释器 (AML.T0050)](../06-Execution/AML.T0050-Command-and-Scripting-Interpreter.md)**
  > The malicious script achieved remote code execution by sending a `node.invoke` (OpenClaw's RPC mechanism) request to OpenClaw's API.

## 关联战术

- [资源开发 (AML.TA0003)](../02-Resource-Development/README.md)
- [执行 (AML.TA0005)](../06-Execution/README.md)
- [凭证访问 (AML.TA0013)](../10-Credential-Access/README.md)
- [防御规避 (AML.TA0007)](../09-Defense-Evasion/README.md)
- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [持久化 (AML.TA0006)](../07-Persistence/README.md)
- [权限提升 (AML.TA0012)](../08-Privilege-Escalation/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [1-Click RCE To Steal Your Moltbot Data and Keys (CVE-2026-25253)](https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys)
- [CVE-2026-25253](https://nvd.nist.gov/vuln/detail/CVE-2026-25253)
- [openclaw](https://openclaw.ai/blog/introducing-openclaw)

- [MITRE ATLAS 官方案例页 (AML.CS0050)](https://atlas.mitre.org/studies/AML.CS0050/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
