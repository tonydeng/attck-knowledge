# 从 AI 智能体配置获取凭证 (AML.T0083)

## 一句话通俗理解

> 智能体配置文件就像管家腰上挂着的一整串钥匙——数据库、云服务、聊天工具的钥匙全在这一串上。攻击者不撬任何一把锁，直接顺走钥匙串。

## 难度等级

⭐⭐ **Demonstrated（已演示）**

该技术已有两起公开的真实案例支撑：Backslash 安全研究团队演示了通过提示词注入让 Cursor 智能体自己外传含有凭证的配置文件（AML.CS0045）；Jamieson O'Reilly 在暴露的 ClawdBot 控制接口中直接读取到多个服务的明文凭证（AML.CS0048）。对攻击者而言，一旦获得主机、代码仓库或控制接口的读取权限，收割配置中的凭证几乎没有技术门槛——真正难的是前期的初始访问环节。

**适用平台**（官方数据）：智能体 AI

## 技术描述

### 通俗解释

AI 智能体之所以能干活，是因为它手里握着一堆"通行证"：调用大模型的 API 密钥、操作数据库的连接串、访问 Slack/Telegram 的 OAuth 令牌、执行工具的访问令牌。这些凭证总要有个地方存放，而最常见的地方就是智能体的配置文件——MCP 服务器配置、技能清单、工具连接器配置等。

理论上，这些凭证应该放进专门的密钥管理服务（Secret Manager、KMS、Vault），运行时再动态注入。但现实中，为了"先跑起来"，开发者往往直接把明文凭证写进 `mcp.json`、`.env`、`.claude/`、`.cursor/` 这类配置文件里。于是，读到一个配置文件，等于一次性拿到智能体所连接的全部服务的钥匙。

### 技术原理

**凭证聚合效应**：智能体天然是"凭证汇聚点"。一个连接了数据库、云存储、消息平台和代码仓库的智能体，其配置目录就是一张完整的服务访问清单。攻击者无需逐个突破每个服务的防御，只需在聚合点读取一次。

配置文件的常见形态包括：

- MCP 服务器配置（`mcp.json` 等）：记录外部工具服务器的启动命令、环境变量与接入凭证
- 技能清单（skills manifest）与工具连接器配置：声明智能体可调用的工具及其认证信息
- 智能体框架的目录式配置（`.claude/`、`.cursor/` 等风格的工作区配置）
- `.env` 风格的环境变量文件：以明文或弱混淆形式存放 API 密钥与连接串

攻击者获取配置文件的三条主要路径：

1. **旁路读取**：攻击者已控制智能体所在主机、容器或代码仓库，直接读取配置文件。这是传统凭证访问手法在 AI 环境下的延伸。
2. **暴露接口**：智能体控制接口因配置错误暴露在公网且缺乏认证（如 CS0048 中的 ClawdBot 控制接口），攻击者远程读取配置。
3. **借刀杀人**：通过间接提示词注入劫持智能体自身，诱导其执行 shell 命令读取并外传自己的配置文件（如 CS0045 中的 Cursor）。

**权限过宽放大爆炸半径**：实践中为图方便分配的凭证往往权限远超实际需要（如只需读一个桶却给了整个账户的 Admin 权限），凭证一旦失窃，影响范围被急剧放大。

**平台范围**：该技术仅适用于智能体 AI（Agentic AI）平台。

### 用途影响

- **一点失守、全网沦陷**：窃取一份配置文件即可获得智能体连接的所有服务的合法访问权
- **绕过智能体侧防护**：攻击者拿到凭证后直接调用后端服务，完全绕开智能体的工具审批与输出审查机制
- **难以区分合法与恶意**：失窃凭证发起的调用与正常调用使用同一身份，服务端难以甄别
- **横向移动跳板**：以智能体凭证为起点，向云账户、数据库、内部 API 等更深层的系统渗透

## 攻击流程

### 典型攻击流程

```mermaid
graph TD
    A[获得初始立足点] --> B[定位智能体配置文件]
    B --> C[读取并解析凭证]
    C --> D[凭证外带]
    D --> E[验证有效性并横向扩张]
    A -->|提示词注入路径| F[劫持智能体自读配置]
    F --> C
```

### 步骤详解

**步骤 1：获得初始立足点**

- **通俗描述**：攻击者先想办法"进屋"——可能是控制了智能体所在的机器，可能是拿到仓库权限，也可能只是发现了一个没上锁的远程控制界面。
- **技术细节**：常见入口包括钓鱼、凭证填充获得的主机权限、公网暴露且未认证的控制接口（Shodan 等空间测绘可发现）、或含注入载荷的网页/文档。

**步骤 2：定位智能体配置文件**

- **通俗描述**：找到管家放钥匙串的位置。
- **技术细节**：扫描典型路径与文件名模式——`mcp.json`、`.env`、`.claude/settings.json`、`.cursor/mcp.json`、技能清单文件；也可从进程环境变量、shell 历史记录中提取线索。

**步骤 3：读取并解析凭证**

- **通俗描述**：把钥匙串上每把钥匙认一遍——哪个是数据库的、哪个是云服务的、哪个权限最大。
- **技术细节**：解析 JSON/YAML/TOML 配置结构，识别 API 密钥、Bearer 令牌、连接串、OAuth 凭证、设备链接 URI 等凭证形态，并评估各凭证的权限范围与有效期。

**步骤 4：凭证外带**

- **通俗描述**：把钥匙串复制一份带走。
- **技术细节**：通过 HTTP 回传、写入公共存储、粘贴到外部服务等方式外带；在"借刀杀人"路径中，由被劫持的智能体自己执行外传命令。

**步骤 5：验证与利用**

- **通俗描述**：逐把试钥匙，挑最值钱的门进去。
- **技术细节**：低频调用各服务 API 验证凭证有效性（避免触发速率告警），随后利用有效凭证访问数据、执行操作或横向移动至更高权限系统。

**与后续战术的衔接：**

- 收割到的凭证可用于后续的[发现](../11-Discovery/README.md)战术——以合法身份枚举云环境、数据库结构等
- 与 [AML.T0081 修改 AI 智能体配置](../07-Persistence/AML.T0081-Modify-AI-Agent-Configuration.md)共享同一攻击面：能读配置的手法通常也能改配置，二者常组合出现
- 外带环节通常叠加 AML.T0053（数据外带）与 AML.T0051（间接提示词注入）等技术

> 值得注意的是，"借刀杀人"路径下智能体在执行敏感命令前弹出的用户确认框是重要的最后防线——CS0045 中 Cursor 正是依靠这一机制减轻了影响。

## 真实案例

> 以下案例源自 MITRE ATLAS 官方案例库，均经过安全研究团队公开验证。

### 案例 1：通过 Cursor 使用的 MCP 服务器实施数据外带（2025，AML.CS0045）

- **时间**：2025 年 6 月 24 日
- **攻击者**：Backslash 安全研究团队（概念验证研究）
- **目标**：Cursor AI 编程助手
- **手法**：研究者搭建了一个用于网页抓取的恶意 MCP 服务器。当用户让 Cursor 抓取某个包含注入载荷的网页时，恶意提示词经间接提示词注入进入 Cursor 上下文，诱导 Cursor 执行 shell 命令，将受害者 AI 智能体配置文件（含凭证）外传至攻击者控制的服务器。
- **影响**：配置文件中连接各工具与服务的凭证面临被收割的风险；缓解因素是 Cursor 在执行命令前会请求用户确认。
- **参考链接**：[Simulating a Context-Poisoning Vulnerable MCP Server: A POC](https://www.backslash.security/blog/simulating-a-vulnerable-mcp-server-for-context-poisoning)

### 案例 2：暴露的 ClawdBot 控制接口导致凭证访问与命令执行（2026，AML.CS0048）

- **时间**：2026 年 1 月 25 日
- **攻击者**：Jamieson O'Reilly（安全研究）
- **目标**：ClawdBot（现已更名为 OpenClaw）
- **手法**：研究者通过 Shodan 发现数百个暴露在公网的 ClawdBot 控制接口，部分完全没有认证，另一些可通过代理配置错误绕过认证。ClawdBot 的配置文件中存放着已连接应用的凭证：Anthropic API 密钥、Telegram 机器人令牌、Slack OAuth 凭证、Signal 设备链接 URI。研究者还通过聊天提示词诱导 ClawdBot 暴露系统提示词，并通过 `bash` 技能在容器内以 root 权限执行命令（至少一例）。
- **影响**：攻击者可收割多平台凭证、操纵聊天历史、外带所连接消息服务的会话记录、冒充用户发送消息，并在至少一个实例中获得容器 root 权限。
- **参考链接**：[hacking clawdbot and eating lobster souls](https://x.com/theonejvo/status/2015401219746128322)、[Shodan 搜索：Clawdbot Control](https://www.shodan.io/search?query=Clawdbot+Control)、[OpenClaw GitHub 仓库](https://github.com/openclaw/openclaw)

## 红队视角

> ⚠️ **免责声明**：本节内容仅用于授权渗透测试与防御研究。未经书面授权对他人系统实施上述行为属于违法。

### 实战技巧

1. **智能体凭证面盘点**：在授权范围内，用 `ripgrep` 等工具全面扫描目标工作区的 `mcp.json`、`.env`、`.claude/`、`.cursor/`、技能清单等路径，绘制"一台主机—一串钥匙"的凭证聚合图谱，这往往是最快出成果的攻击面。
2. **验证"自读自传"链路**：在隔离环境中复现 CS0045 式链路——恶意网页 → 智能体抓取 → 注入指令诱导智能体读取自身配置 → 外传。重点记录智能体的用户确认环节在哪一步生效，以此评估目标对间接提示词注入的抵抗力。
3. **爆炸半径评估**：对发现的每份凭证标注权限范围与可吊销性。报告里"一把可吊销的只读令牌"与"一把账户级 Admin 密钥"是天壤之别，红队交付物应量化这种差距。

### 常用工具

| 工具名称 | 用途 | 平台 |
|---------|------|------|
| ripgrep | 高速扫描工作区内的配置文件与凭证模式 | 跨平台 |
| gitleaks | 扫描 Git 历史中的泄露密钥 | 跨平台 |
| TruffleHog | 深度扫描并自动验证密钥有效性 | 跨平台 |
| Shodan | 发现暴露在公网的智能体控制接口 | Web |
| MCP Inspector | 调试与审计 MCP 服务器配置 | 跨平台 |

### 注意事项

- 严守授权边界：仅测试书面授权范围内的主机、仓库与接口
- 凭证只验证存在性，不做实际调用，更不得横向访问真实业务数据
- 外带演示使用自建的接收端点，避免真实凭证流经第三方基础设施

## 蓝队视角

### 检测要点

1. **配置文件的异常读取**
   - **日志来源**：终端 EDR / 文件审计日志
   - **关注字段**：进程镜像、文件路径、父进程链
   - **异常特征**：智能体运行时之外的进程读取 `mcp.json`、`.env`、`.claude/` 等路径；shell 解释器（bash/powershell）被智能体工具调用拉起并 cat/grep 配置文件
2. **凭证形态数据的外带流量**
   - **日志来源**：DLP、代理与 NetFlow 日志
   - **关注字段**：出站目标、请求体特征、流量大小
   - **异常特征**：工作站在短时间内向陌生域名外发包含密钥模式（`sk-`、`Bearer `、`token=`）的数据
3. **失窃凭证的异地使用**
   - **日志来源**：云端服务（OpenAI/Anthropic/Slack 等）审计日志
   - **关注字段**：调用源 IP、User-Agent、调用时间
   - **异常特征**：凭证在地理上不可能的位置被调用、调用频率或模式突变
4. **控制接口的公网暴露**
   - **日志来源**：空间测绘平台监控、资产台账
   - **关注字段**：公网 IP、端口、服务指纹
   - **异常特征**：智能体控制端口出现在 Shodan 等测绘结果中

### 监控建议

- 将智能体的审计日志（工具调用、shell 执行、配置变更）统一接入 SIEM，与主机进程链做关联分析
- 在配置文件中植入蜜标密钥（canary token），任何对其的访问即触发告警
- 对配置路径启用文件完整性监控（FIM），非预期的读取/变更立即告警
- 强制凭证轮换与短有效期，把"失窃窗口期"从永久压缩到小时级

## 检测建议

### 网络层检测

**检测方法：** 监控出站流量中的凭证特征与失窃凭证的服务端调用。

- 工作站向陌生域名/新注册域名外发含 `sk-`、`Bearer`、`xoxb-` 等密钥前缀的数据
- 云服务 API 账户出现新 IP、新 ASN 的调用（服务端视角的凭证盗用信号）
- 对已知测绘平台的端口探测与指纹抓取保持资产侧告警

### 主机层检测

**检测方法：** 监控配置文件的读取进程与 shell 命令模式。

- 非智能体进程（尤其是脚本解释器、压缩工具）读取 `mcp.json`、`.env`、`.claude/`、`.cursor/` 路径
- bash/PowerShell 历史中出现 `cat ~/.claude/settings.json`、`grep -r "API_KEY"` 类命令
- 配置文件在短时间内被批量打包（tar/zip）或base64 编码后外发

### 应用层检测（AI 遥测）

**检测方法：** 审计智能体的工具调用与命令执行序列。

- 智能体工具调用链中出现"读取自身配置文件"的 shell 命令（合法场景极少）
- 单次会话中连续出现 网页抓取 → shell 执行 → 文件读取 → 网络外传 的组合模式（CS0045 指纹）
- 控制接口收到索取系统提示词或配置内容的聊天请求

### Sigma 规则思路示例

```yaml
title: AI 智能体配置文件被可疑进程读取
status: experimental
description: 检测智能体运行时之外的进程读取 MCP/智能体配置文件，可能指示凭证收割
logsource:
    category: file_event
    product: linux
detection:
    selection:
        TargetFilename|endswith:
            - '/mcp.json'
            - '/.claude/settings.json'
            - '/.cursor/mcp.json'
            - '/.env'
    filter_legitimate:
        Image|endswith:
            - '/node'
            - '/claude'
            - '/cursor'
    condition: selection and not filter_legitimate
level: high
tags:
    - attack.credential_access
    - attack.t1552
    - atlas.aml_t0083
```

## 缓解措施

### 优先级 1：关键措施

**凭证离开配置文件**：使用密钥管理服务（Secret Manager、KMS、Vault 等）集中保管凭证，配置文件中只保留运行时引用，由智能体框架在启动时动态注入。这是消除该技术攻击面的根本手段。

**工具级凭证隔离与最小权限**：每个 MCP 服务器、每个工具连接器使用独立的凭证身份，权限严格限定到实际所需（只读就不给写），且全部可独立吊销。单份凭证失窃时爆炸半径可控。

### 优先级 2：重要措施

- **配置文件不进仓库、不给多余权限**：`.gitignore` 排除凭证文件，配置文件权限收紧到 0600；CI 流水线强制密钥扫描（gitleaks 等），阻止历史性泄露
- **控制接口收敛**（针对 CS0048 类暴露）：智能体控制接口默认不暴露公网，必须监听时强制认证，并定期审计反向代理的访问控制配置
- **强制轮换与短有效期**：所有智能体持有的凭证设定短生命周期并自动轮换，将失窃窗口期压到最小

### 优先级 3：建议措施

- 为智能体工具调用与配置读取建立完整审计日志，接入 SIEM
- 在配置中部署蜜标密钥，将"静默失窃"转化为"即时告警"

### 说明

MITRE ATLAS 官方数据中，该技术暂未登记正式的缓解措施条目（AML.Mxxx）。上表为基于攻击原理与两个真实案例的实践性缓解映射：

| 缓解方向 | 针对的攻击环节 |
|---------|--------------|
| 密钥管理服务 + 运行时注入 | 凭证聚合（配置文件中无凭证可偷） |
| 最小权限 + 可吊销的独立凭证 | 步骤 3-5（爆炸半径控制） |
| 控制接口收敛与强制认证 | 入口路径 ②（暴露接口） |
| 智能体命令审批门禁 | 入口路径 ③（借刀杀人） |
| CI 密钥扫描 + .gitignore | 入口路径 ①（仓库旁路读取） |

## 关联 ATT&CK 技术

MITRE ATLAS 官方数据中该技术**没有正式的 ATT&CK 技术映射**（attack_reference 为空）。从攻击原理上看，它是传统凭证访问战术在智能体场景的自然延伸，主题上最接近以下企业版技术：

- [T1552 Unsecured Credentials（不安全凭证）](../../enterprise/09-Credential-Access/T1552-Unsecured-Credentials.md)——母技术：凭证以不安全形式存放被攻击者利用
- [T1552.001 Credentials in Files（文件中的凭证）](../../enterprise/09-Credential-Access/T1552/T1552.001-Credentials-in-Files.md)——最直接的对应：凭证明文存于文件中被读取

| 维度 | ATT&CK T1552 | ATLAS AML.T0083 |
|------|-------------|-----------------|
| 凭证载体 | 任意文件、注册表、云存储等 | 特指智能体配置（MCP 配置、技能清单、连接器） |
| 凭证聚合度 | 分散，逐个发现 | 高度聚合，一次读取收割全部服务凭证 |
| 攻击面 | 传统 IT 环境 | 智能体所在主机/仓库/控制接口 |
| 失窃影响 | 取决于单份凭证权限 | 智能体连接的全部服务同时暴露 |

**边界说明**：与 AML.T0055（不安全凭证，文档暂缺）关注"凭证存放不安全"这一状态不同，AML.T0083 聚焦"从智能体配置文件收割凭证"这一具体动作；与 AML.T0098 的区别在于后者针对密码/凭证的暴力获取，本技术是静默读取。

**一句话总结**：AML.T0083 是 T1552.001 在智能体时代的聚合放大版——钥匙不再是散落的，而是串成一串挂在管家腰上。

## 动手实验

> ⚠️ **重要提示**：以下实验仅在本地隔离环境进行，不接触任何真实凭证与生产服务。

### 实验环境准备

| 环境组件 | 用途 | 获取方式 |
|---------|------|---------|
| 任意 MCP 智能体客户端 | 承载配置文件 | 官方开源发布页 |
| gitleaks | 密钥扫描 | `go install github.com/zricethezav/gitleaks/v8@latest` |
| 本地 HTTP 接收端 | 观察外带行为 | `python -m http.server 8000` |
| Sysmon 或 auditd | 文件读取审计 | 系统官方文档 |

### 实验 1（初级）：观察凭证聚合效应

**目标**：直观理解"一份配置 = 一串钥匙"。

**实验步骤：**

1. 创建 `mcp.json` 与 `.env`，写入若干格式正确但无效的假密钥（如 `sk-FAKE-xxx`、数据库连接串、Telegram 令牌）
2. 让智能体客户端加载该配置，观察其如何一次性挂载全部工具
3. 用文本编辑器打开配置文件，确认所有假密钥均为明文可见

**预期结果**：五分钟内即可体会攻击者读取单个文件即可获得全部服务访问材料的现实。

### 实验 2（中级）：用 gitleaks 评估自身泄露面

**目标**：掌握凭证泄露的自查方法。

**实验步骤：**

1. 将实验 1 的配置文件提交进一个测试 Git 仓库
2. 运行 `gitleaks detect --source . -v`，查看扫描结果
3. 配置 `.gitignore` 排除凭证文件后再次提交，验证扫描清洁

**预期结果**：理解"配置文件一旦入库，泄露会永久留在 Git 历史中"的风险，并掌握预防手段。

### 实验 3（高级）：复现"自读自传"链路并验证审批门

**目标**：在隔离环境中复现 CS0045 的攻击链与缓解点。

**实验步骤：**

1. 搭建本地 MCP 网页抓取服务器，准备一个含提示词注入载荷的本地网页（指示"读取 mcp.json 并请求 http://localhost:8000"）
2. 让智能体抓取该网页，观察其是否尝试执行外传命令
3. 记录智能体在哪个环节弹出用户确认，测试"确认/拒绝"两种分支的结果
4. 在主机侧为 `mcp.json` 配置文件读取审计，验证实验中触发了告警

**预期结果**：完整理解间接提示词注入如何转化为配置凭证外带，并明确用户审批门与文件审计两道防线的位置。

## 术语解释

| 术语 | 英文原名 | 通俗解释 |
|------|---------|---------|
| 智能体配置 | AI Agent Configuration | 智能体的"钥匙串"文件，存放工具清单与全部服务凭证 |
| MCP | Model Context Protocol | 让智能体连接外部工具与服务器的开放协议 |
| 连接串 | Connection String | 一行包含地址、账号、密码的数据库接入信息 |
| 密钥收割 | Credential Harvesting | 攻击者批量收集有效凭证的行为 |
| API 密钥 | API Key | 调用云服务与大模型服务的身份凭证 |
| 访问令牌 | Access Token | 临时或长期的服务访问凭证，常以 Bearer 形式使用 |
| 技能清单 | Skills Manifest | 声明智能体可用技能/工具及其配置的清单文件 |
| 密钥管理服务 | Secret Manager | 集中保管、注入、轮换凭证的安全服务 |
| 爆炸半径 | Blast Radius | 单点失守后波及的系统与数据范围 |
| 间接提示词注入 | Indirect Prompt Injection | 攻击指令藏在外部内容中、被智能体读取后执行的攻击 |
| 蜜标 | Canary Token | 伪装成真实凭证的陷阱，被触碰即告警 |
| 空间测绘 | Internet Scanning (Shodan) | 对公网设备与服务指纹的持续扫描索引 |
| Cursor | Cursor | 一款流行的 AI 编程助手（智能体客户端） |
| ClawdBot / OpenClaw | ClawdBot / OpenClaw | 一款开源个人助理智能体框架，CS0048 的受害目标 |

## 参考资料

### 📚 官方文档

- [MITRE ATLAS AML.T0083 官方页面](https://atlas.mitre.org/techniques/AML.T0083/)
- [MITRE ATLAS 矩阵](https://atlas.mitre.org/matrices/ATLAS/)
- [mitre-atlas-data GitHub 仓库](https://github.com/mitre-attack/mitre-atlas-data)

### 📰 案例报告（真实攻击与安全研究）

- [Simulating a Context-Poisoning Vulnerable MCP Server: A POC — Backslash Security](https://www.backslash.security/blog/simulating-a-vulnerable-mcp-server-for-context-poisoning)
- [hacking clawdbot and eating lobster souls — Jamieson O'Reilly](https://x.com/theonejvo/status/2015401219746128322)
- [Shodan 搜索：Clawdbot Control](https://www.shodan.io/search?query=Clawdbot+Control)
- [OpenClaw GitHub 仓库](https://github.com/openclaw/openclaw)

### 🔧 工具与资源

- [Model Context Protocol 官方文档](https://modelcontextprotocol.io/)
- [gitleaks — Git 密钥扫描](https://github.com/gitleaks/gitleaks)
- [TruffleHog — 密钥发现与验证](https://github.com/trufflesecurity/trufflehog)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### 🔗 关联阅读

- [T1552 Unsecured Credentials（不安全凭证）](../../enterprise/09-Credential-Access/T1552-Unsecured-Credentials.md)
- [T1552.001 Credentials in Files（文件中的凭证）](../../enterprise/09-Credential-Access/T1552/T1552.001-Credentials-in-Files.md)
- [凭证访问战术总览](./README.md)
- [AML.T0081 修改 AI 智能体配置](../07-Persistence/AML.T0081-Modify-AI-Agent-Configuration.md)
- [发现战术总览](../11-Discovery/README.md)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-22 | **模板**: ATLAS 技术文档 v1.0
