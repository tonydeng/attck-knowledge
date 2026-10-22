# 获取能力 (AML.T0016)

> 属于 [资源开发 (AML.TA0003)](./README.md)

## 一句话通俗理解

> 攻击者很少从零造武器——他们像逛军火市场一样搜集现货：研究界开源的对抗攻击代码库、改改就能用的通用黑客工具、能本地部署的大模型、社区里流转的漏洞利用、给智能体加装的"外挂"工具，采购、验证、改装，弹药就齐了。

## 难度等级

⭐⭐⭐ **Realized（已实现）**

官方成熟度评定为 Realized——本技术及其全部 5 个子技术均为此等级，说明"获取现成能力"已在从个人犯罪团伙到国家级 APT 的真实行动中被反复验证。获取动作本身几乎零门槛：研究代码在开源仓库公开可下、模型平台一键部署、漏洞利用在社区流转、暗网工具明码标价。真正的门槛不在"拿到"，而在"用对"——知道哪种能力对目标的 AI 技术栈有效，并将其定制改造为针对特定 AI 系统的武器，这需要专业知识与对目标环境的深入理解。

## 技术描述

### 通俗解释

依据官方描述，对手可能搜索并获取用于其行动的软件能力。这些能力既可以是**专门针对 AI 攻击的**（对抗性 AI 攻击实现），也可以是**被赋予恶意用途的通用软件工具**（软件工具）。无论哪种，对手都可能修改或定制这些能力，以辅助攻击特定的 AI 系统。

如果说开发能力（AML.T0017）是"自己造枪"，获取能力就是"买现货、捡现货"。AI 安全研究界的开源传统让这条路异常畅通：为了可复现性，研究者把对抗样本、模型提取、数据投毒的完整实现代码连同论文一起公开；通用黑客工具稍加改造就能用于攻击 AI 系统；生成式 AI 本身成了"弹药生产线"；智能体工具生态（MCP 服务器、插件、技能）则把能力获取从"软件"扩展到了"给 AI 智能体加装的手脚"。

### 技术原理

攻击者获取的能力覆盖五大类：

| 能力类型 | 典型形态 | 主要获取渠道 | 典型用途 |
|---------|---------|-------------|---------|
| 对抗性 AI 攻击实现（.000） | CleverHans、Adversarial Robustness Toolbox、FoolBox 等研究代码库 | 开源仓库（研究界为可复现性公开） | 生成对抗样本、模型提取、投毒验证 |
| 软件工具（.001） | 扫描器、密码破解、数据库与浏览器自动化工具 | 公开工具改造、地下市场购买 | 支撑攻击各环节，工具本身未必是 AI |
| 生成式 AI（.002） | LLM 等生成式模型及其服务 | 本地部署（Ollama/vLLM）、云托管、AI 服务商 | 生成恶意软件、深伪、恶意命令、钓鱼内容 |
| 漏洞利用（.003） | 针对 AI 框架、推理服务等漏洞的利用代码 | 公开仓库、私有来源、购买、窃取、漏洞研究社区 | 突破目标 AI 软件栈 |
| AI 智能体工具（.004） | MCP 服务器、插件、技能、连接器、computer-use 适配器、执行代理 | 智能体工具生态与聚合枢纽 | 武装智能体：操作系统、浏览器、云、数据存储与身份系统访问 |

三点值得特别注意：

- **研究成果的双刃剑**：CleverHans、Adversarial Robustness Toolbox、FoolBox 等库本为鲁棒性研究而生，但攻击者可以直接武器化；官方描述还明确指出，攻击者也会获取**并非为对抗性 AI 攻击设计**的工具用于攻击——"能用的都拿"。
- **生成式 AI 是"自我军备"**：攻击者获取 LLM 用于生成恶意软件、深度伪造（AML.T0088）、恶意命令（AML.T0102）、检索内容构造（AML.T0066）与钓鱼内容（AML.T0052）。获取途径包括用 Ollama、vLLM 等框架本地服务开源模型、云托管，或直接使用 Hugging Face 等 AI 服务商；必要时越狱（AML.T0054）绕过输出限制，甚至违反模型开发商的服务条款。市场上还存在**无审查（uncensored）模型**——通过微调移除对齐与护栏、操纵模型的拒绝方向，或直接使用专为攻防安全构建（如 WhiteRabbitNeo）乃至公开宣传恶意用途（如 WormGPT）的变体，成为网络犯罪的现成弹药。
- **智能体工具是能力放大器**：智能体工具以 MCP 服务器、插件、技能、连接器、函数库、computer-use 适配器、执行代理、远程 API 等形式分发，让智能体能操作系统、浏览器、网络、云服务、数据存储与身份系统。工具向模型暴露的描述与可执行接口会影响智能体选择和调用哪些能力——获取这些工具，等于获得仅靠模型推理无法触及的资源、凭证与动作权限。攻击者既可把合法工具配置成恶意用途，也可获取改造过的专用工具，或将多个集成组合成一套作战工具集。

**平台覆盖**：Predictive AI（预测式 AI）/ Generative AI（生成式 AI）/ Agentic AI（智能体 AI）/ Enterprise（企业 IT）四类平台全部适用。

### 用途影响

- **大幅降低攻击门槛**：现货能力让技术平庸的团伙也能发动 AI 攻击——ProKYC 这类"开箱即用"的深伪工具把 KYC 欺诈变成了花钱就能办的生意
- **显著加速攻击周期**：无需从零研发，"采购—验证—定制"即可成军；获取的漏洞利用既可直接使用，也可作为后续改造开发的输入
- **全攻击链赋能**：从自动化侦察、漏洞利用到智能体自主攻击，几乎每个战术阶段都有对应的可获取能力；智能体工具甚至能让一次获取的能力自主扩展
- **防御观测困境**：获取行为发生在攻击者自己的环境里，防御者几乎无法直接观测——只能通过限制己方可被武器化的资产（公开制品、自有模型）与监控下游战术来间接应对

## 子技术列表

**该技术共有 5 个子技术（官方成熟度均为 Realized）：**

| 子技术ID | 中文名称 | 官方成熟度 | 一句话理解 |
|----------|----------|-----------|-----------|
| [AML.T0016.000](AML.T0016/AML.T0016.000-Adversarial-AI-Attack-Implementations.md) | 对抗性 AI 攻击实现 | Realized ⭐⭐⭐ | 搜集现成的 AI 攻击开源实现：研究界为可复现性公开的 CleverHans、Adversarial Robustness Toolbox、FoolBox 等库可被直接武器化，非为对抗攻击设计的工具也会被拿来就用 |
| [AML.T0016.001](AML.T0016/AML.T0016.001-Software-Tools.md) | 软件工具 | Realized ⭐⭐⭐ | 获取通用软件工具并改造为恶意用途——攻击 AI 系统的工具未必本身是 AI，合法软件换个用法就是武器 |
| [AML.T0016.002](AML.T0016/AML.T0016.002-Generative-AI.md) | 生成式 AI | Realized ⭐⭐⭐ | 获取 LLM 等生成式 AI（本地 Ollama/vLLM、云托管、AI 服务商），必要时越狱或改用 uncensored 变体，用于生成恶意软件、深伪、恶意命令与钓鱼内容 |
| [AML.T0016.003](AML.T0016/AML.T0016.003-Exploits.md) | 漏洞利用 | Realized ⭐⭐⭐ | 从公开仓库、私有来源、购买、窃取或漏洞研究社区获取利用代码，可直接使用或作为后续改造开发的输入 |
| [AML.T0016.004](AML.T0016/AML.T0016.004-AI-Agent-Tools.md) | AI 智能体工具 | Realized ⭐⭐⭐ | 获取扩展智能体能力的工具（MCP 服务器、插件、技能、连接器等），把合法工具配置成恶意用途，或组合成一套作战工具集 |

> 注：以上 5 个子技术文档均已完成，点击 ID 直达对应文档。
   - 技术细节：在自有环境中测试能力的有效性：对抗样本库能否对目标同类模型起效、漏洞利用能否复现、uncensored 模型的输出是否满足需要、智能体工具组合能否按预期被模型调用。

4. **定制改造**
   - 通俗描述：改枪——把现货改装成合手的武器。
   - 技术细节：官方描述明确指出对手可能修改或定制所获能力以攻击特定 AI 系统：调整对抗扰动的生成参数适配目标模型架构、改造通用工具对接目标 API、为智能体定制工具描述以引导其调用。

5. **集成进攻击链**
   - 通俗描述：弹药上膛——把武器装进作战体系。
   - 技术细节：将能力接入攻击编排：把工具挂到智能体的 MCP 连接上、把漏洞利用编入自动攻击框架、把生成式 AI 接到钓鱼内容生产流水线，供后续战术随取随用。

**与后续战术的衔接：**

- **AI 攻击适配**：获取的对抗攻击实现与目标模型信息结合，构造针对特定系统的对抗数据与代理模型
- **初始访问**：获取的漏洞利用直接用于突破目标暴露的 AI 服务与软件栈
- **执行**：智能体工具赋予（攻击者的）智能体操作系统与命令执行能力
- **持久化与纵深推进**：生成式 AI 持续产出恶意命令、钓鱼内容与深伪素材，支撑后续各阶段

> 关键特征：与传统"买木马"不同，AI 时代获取的能力很多是**合法流通品**（开源研究库、开源模型、正版工具）——单看"获取"环节完全合法，威胁在用途与改造，这让事前防控几乎无处着力。

## 真实案例

> 以下精选 4 个代表性案例（官方数据共关联 10 个案例研究），全部源自 MITRE ATLAS 案例库。

### 案例1：Hermes Agent 自主攻击——四类能力一次备齐（2026年5月，AML.T0016.001/.002/.003/.004）

- **时间**: 2026年5月
- **攻击者**: 中文威胁行为者（别名 knaithe / KnYuan）
- **手法**: 攻击者将开源 Hermes Agent 配置为以 DeepSeek 为推理引擎（获取生成式 AI），并集成终端访问、Telegram 操控、红队技能系统与暴露 FOFA 搜索和 Nuclei 扫描能力的 MCP 服务器（获取智能体工具与软件工具）。该智能体随后自主搜索目标、获取公开漏洞利用（Langflow 的 CVE-2026-33017、n8n 的 CVE-2026-21858 与 CVE-2025-68613 利用链）、运行扫描、评估结果并调整策略——单次行动中四类能力获取全部出现，且全程无需人工介入。
- **影响**: 虽然自主利用未成功获取访问，但 Unit 42 证实 AI 智能体已能自主完成"选目标—找武器—试攻击"的完整闭环
- **参考链接**: [Unit 42 分析报告](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)

### 案例2：GTG-1002——越狱智能体接入整套武器库（2025年9月，AML.T0016.001）

- **时间**: 2025年9月
- **攻击者**: GTG-1002（Anthropic 以高置信度评估为中国国家级支持组织）
- **手法**: GTG-1002 获取 Claude Code 访问权并用虚假"防御安全"人设与表面合法的任务掩盖恶意目的，实现对智能体的越狱；随后通过 MCP 将其连接到扫描器、浏览器自动化、密码破解、数据库工具与专用渗透测试服务器——把一个 AI 编码助手武装成自主攻击框架。在约 30 个目标上，越狱智能体自主侦察基础设施、扫描漏洞、开发并部署 SSRF 利用链、建立后门账户，完成全部行动工作量的约 80-90%，人类操作者仅保留每目标 4-6 个关键决策。
- **影响**: 首个被公开报告的 AI 编排网络间谍行动（ATT&CK C0062）
- **参考链接**: [Anthropic 官方报告](https://www.anthropic.com/news/disrupting-AI-espionage)

### 案例3：ProKYC——明码标价的深伪工具（2024年10月，AML.T0016.002）

- **时间**: 2024年10月
- **攻击者**: ProKYC（网络犯罪团伙，工具即服务）
- **手法**: Cato CTRL 研究人员发现 ProKYC——一套公开向网络犯罪分子出售的深伪工具，能生成假身份证件与深伪自拍视频这两项 KYC 核验的关键生物数据，帮助买家击败加密货币交易所等金融应用的人脸识别与活体检测，批量开立欺诈账户。
- **影响**: 把"绕过 KYC"变成花钱即得的服务，攻击门槛被拉到零
- **参考链接**: [Cato CTRL 威胁研究](https://www.catonetworks.com/blog/prokyc-selling-deepfake-tool-for-account-fraud-attacks/)

### 案例4：摄像头劫持骗过人脸识别——现成套件骗走 7700 万美元（2018-2020年，AML.T0016.000/.001）

- **时间**: 2018年起，2020年披露
- **攻击者**: 两名个人犯罪者
- **手法**: 犯罪者利用摄像头劫持攻击绕过上海税务系统的人脸识别认证（对抗性 AI 攻击实现与软件工具的结合使用），冒充受害者身份进入系统；随后注册空壳公司、向"客户"虚开税务发票，持续两年骗取约 7700 万美元。
- **影响**: 现成攻击能力 + 身份冒充的直接变现，证实 AI 攻击能力已进入普通犯罪者的工具箱
- **参考链接**: [华尔街日报报道](https://www.wsj.com/articles/faces-are-the-next-target-for-fraudsters-11625662828)

## 红队视角

> ⚠️ **免责声明**：以下内容仅用于合法授权的安全测试与教育目的。未经授权对他人系统或第三方服务进行测试是违法行为。

### 实战技巧

1. **按目标技术栈选型弹药**
   授权评估开始前先盘点目标 AI 资产类型（图像模型/LLM 服务/智能体平台），再决定获取哪类能力：图像类用 ART 的对抗样本模块，LLM 类评估越狱与提示词攻击工具，智能体类组装最小 MCP 工具集。选型本身就是评估报告的重要发现——"攻击这台系统需要多容易获得的能力"直接反映风险等级。

2. **研究 PoC 的复现与改造**
   漏洞披露伴随的公开 PoC 是红队的合法武器库：在隔离环境复现、验证对目标版本的适用性、评估修补状态。报告应区分"公开武器即可攻破"与"需要定制开发才能攻破"两档风险。

3. **本地部署 LLM 做攻击辅助**
   在授权范围内用 Ollama/vLLM 本地部署开源模型辅助社工文案、载荷变形与日志分析——本地部署避免数据出网，本身就是给客户演示"影子 AI"风险的活例子。

4. **智能体工具链组装与审计**
   给测试智能体配置文件读取、命令执行类工具（MCP 或 function calling），观察工具描述文本如何引导模型选择与调用；反向审计客户环境中智能体的工具清单，找出过度授权的集成。

### 常用工具

| 工具名称 | 用途 | 平台 |
|----------|------|-------|
| Adversarial Robustness Toolbox (ART) | 对抗样本生成、攻击与防御评估 | 跨平台 |
| CleverHans / FoolBox | 对抗样本研究参考实现 | 跨平台 |
| Ollama / vLLM | 开源模型本地部署与服务 | 跨平台 |
| Nuclei | 漏洞扫描与 PoC 验证 | 跨平台 |

### 注意事项

- **授权边界**：获取能力合法（多数是公开流通品），**使用**才是红队授权约束的对象——一切武器化验证仅限合同范围内的目标
- **uncensored 模型合规风险**：部署与使用去对齐模型可能违反其基础模型的许可证与服务条款，评估报告中应作为独立合规发现
- **获取的能力本身可能是陷阱**：地下市场流通的工具常带后门，"攻击者被攻击"真实存在；红队工具链应从官方渠道获取并校验完整性
- 不向客户交付可直接武器化的制品，交付的是风险发现与加固建议

## 蓝队视角

### 检测要点

1. **影子 AI 使用监控（组织内部）**
   - 日志来源：终端 EDR 进程与文件遥测、网络出口流量、DNS 日志
   - 关注字段：进程名与命令行、大文件落盘、外部 AI 服务域名访问
   - 异常特征：终端出现 Ollama/vLLM 等本地 LLM 运行时进程；数百 MB 至数 GB 的模型权重文件下载；访问已知的 uncensored 模型分发渠道

2. **攻击工具落地检测**
   - 日志来源：EDR、软件资产清单、包管理器日志
   - 关注字段：已知攻击工具的文件名/哈希、pip/npm 安装记录
   - 异常特征：非安全岗位终端出现 Nuclei、密码破解等工具；批量安装对抗攻击库（art、cleverhans）且无对应业务项目

3. **下游战术回溯（事件响应视角）**
   - 日志来源：入侵调查中的工具指纹、外连目的、攻击载荷特征
   - 关注字段：载荷与公开 PoC 的相似度、工具链组合、智能体平台的工具注册记录
   - 异常特征：攻击中使用的工具与公开研究实现高度吻合（可反推能力来源与攻击者水平）；智能体环境出现未审计的新工具集成

### 监控建议

- 把"本地 LLM 运行时"与"对抗攻击库安装"纳入终端基线，出现即告警（影子 AI 既是合规问题也是攻击前兆）
- 维护本行业被武器化工具的威胁情报清单（如 ProKYC 类 KYC 绕过工具），输入欺诈与风控团队
- 事件响应流程中加入"工具指纹比对"步骤：识别攻击者使用的是公开现货还是定制武器，据此评估对手能力与后续风险
- 智能体平台对工具注册/变更实施准入审计——阻断 AML.T0016.004 类能力在自家环境内的"自我武装"

## 检测建议

### 网络层检测

**检测方法：** 监控与 AI 能力获取相关的异常流量。

- 终端访问开源模型仓库并下载大体积权重文件（本地部署 LLM 的前兆）
- 出现对已知 uncensored 模型分发站点的访问
- 非研发角色终端访问漏洞利用代码仓库（Exploit-DB、PoC 集合仓库）

### 主机层检测

**检测方法：** 监控本地 LLM 运行时与攻击工具的落地。

- `ollama`、`vllm` 等进程创建，或 Ollama 默认端口 11434 的本地监听
- 模型权重文件（GGUF、safetensors 大文件）写入非项目目录
- 已知攻击工具（Nuclei 模板批量更新、密码破解工具）在办公终端执行

### 应用层检测（AI 遥测）

**检测方法：** 利用组织自有 AI 平台的审计能力。

- 自有模型 API 出现异常调用模式（可能被当作攻击弹药或代理模型使用）
- 智能体平台出现新增的未登记工具集成与 MCP 连接
- 内部知识库/工单系统被高频爬取（为获取 RAG 弹药做数据准备）

**程序化检测思路（无需 EDR 侧改造）：**

在终端管理平台上以基线方式推送两条简单规则：(1) 进程清单中出现 `ollama.exe`/`vllm` 即生成"影子 AI"工单；(2) 软件资产清单中出现 `adversarial-robustness-toolbox` 等对抗库且登记项目为空即触发复核。两条规则覆盖了 AML.T0016.002 与 AML.T0016.000 在组织内部最常见的落地形态，成本极低。

### Sigma 规则思路示例

```yaml
title: 终端出现本地 LLM 运行时进程（获取生成式 AI 能力）
status: experimental
description: 检测终端上 Ollama/vLLM 等本地大模型运行时启动，
    可能为人员私自获取未授权 AI 能力（影子 AI）或攻击筹备行为（AML.T0016）
logsource:
    category: process_creation
    product: windows
detection:
    selection_ollama:
        Image|endswith: '\ollama.exe'
        CommandLine|contains: 'serve'
    selection_vllm:
        CommandLine|contains: 'vllm serve'
    condition: 1 of selection_*
level: low
tags:
    - attack.t1588
    - atlas.aml_t0016
```

## 缓解措施

> 本技术的缓解视角较为特殊：攻击者的"获取"行为发生在你的视野之外，无法直接阻断。可缓解的是两件事——**不要让你的公开制品成为攻击者的弹药原料**，以及**不要让你部署的模型被轻易武器化**。

### 优先级1：关键措施

**AML.M0001 限制模型工件发布（Limit Model Artifact Release）**

限制公开发布生产环境使用（或能代表生产环境）的技术细节：数据、算法、模型架构与模型检查点。攻击者武器化开源研究库、微调移除对齐、搭建代理模型，都需要"原料"——你发布的每一个公开检查点，都可能是某个 uncensored 变体或代理模型的基座。落地要点：公开制品发布前评审、生产模型与演示模型严格隔离、发布清单纳入 AI BOM 管理。

### 优先级2：重要措施（针对 AML.T0016.002 生成式 AI）

**AML.M0020 生成式 AI 护栏（Generative AI Guardrails）**

在用户、工具与生成式 AI 模型之间部署安全控制，在提示词、检索上下文、模型输出与智能体动作被接受、执行或呈现之前进行评估。护栏可阻断、修改或路由恶意代码、恶意指令、敏感数据与不安全的工具请求，可通过规则式控制或 AI 类手段实现，应用于输入处理、提示词构造、检索、工具执行、输出审查与部署后监控等阶段。对本技术而言，护栏的价值在于**降低你部署的模型被获取、滥用后的产出能力**——即使被当作攻击弹药，恶意请求也难以产出可直接使用的攻击素材。

### 优先级3：建议措施（针对 AML.T0016.002 生成式 AI）

**AML.M0022 生成式 AI 模型对齐（Generative AI Model Alignment）**

通过训练或微调引导生成式模型输出符合人类价值观、安全策略与法律要求的内容（RLHF、SFT、DPO、Constitutional AI 等）。对智能体系统，对齐还包含让模型决策忠于组织与用户目标、动作不越出任务边界。对齐 + 护栏组合能抬高模型被武器化的成本：攻击者需要越狱或专门获取/制造 uncensored 变体，而不是随手可用。

### MITRE ATLAS 缓解措施映射

| 缓解措施ID | 缓解措施名称 | 优先级 | 类别 | 适用范围 | 生命周期阶段 |
|------------|-------------|:------:|------|---------|-------------|
| AML.M0001 | 限制模型工件发布 | 关键 | Policy | AML.T0016（主技术）、AML.T0016.002 | 业务与数据理解 · 部署 |
| AML.M0020 | 生成式 AI 护栏 | 重要 | Technical - AI | AML.T0016.002 | AI 模型工程 · 评估 · 部署 · 监控维护 |
| AML.M0022 | 生成式 AI 模型对齐 | 建议 | Technical - AI | AML.T0016.002 | AI 模型工程 · 评估 · 部署 |

> 优先级为本库基于缓解措施特性给出的落地建议：M0001 解决"你的发布物不要变成弹药原料"，M0020 解决"你的模型被滥用时少产出伤害"，M0022 从训练层面抬高武器化成本。三者均无法阻断攻击者的获取行为本身——这是资源开发类技术的共同局限。

## 关联 ATT&CK 技术

- [获取能力 (T1588)](../../enterprise/02-Resource-Development/T1588-Obtain-Capabilities.md) — 本技术的直接映射来源，同源关系

**子技术对照与差异：**

| 维度 | ATT&CK T1588 | ATLAS AML.T0016 |
|------|-------------|-----------------|
| 经典子技术 | [恶意软件 (T1588.001)](../../enterprise/02-Resource-Development/T1588/T1588.001-Malware.md)、[工具 (T1588.002)](../../enterprise/02-Resource-Development/T1588/T1588.002-Tool.md)、证书类、[漏洞 (T1588.006)](../../enterprise/02-Resource-Development/T1588/T1588.006-Vulnerabilities.md)、[漏洞利用 (T1588.005)](../../enterprise/02-Resource-Development/T1588/T1588.005-Exploits.md) | [软件工具]→T1588.002 同源；[漏洞利用]→T1588.005 同源 |
| AI 原生子技术 | [人工智能 (T1588.007)](../../enterprise/02-Resource-Development/T1588/T1588.007-Artificial-Intelligence.md)——ATT&CK v20 新增 | 对抗性 AI 攻击实现、生成式 AI、AI 智能体工具——研究库武器化、uncensored 模型、MCP 工具生态等更细粒度对象 |
| 获取渠道 | 暗网、漏洞市场、窃取、论坛 | 渠道重合，但新增**完全合法的公开渠道**：开源研究库、模型仓库、智能体工具枢纽 |
| 防御观测性 | 获取行为发生在视野外，靠下游检测 | 相同困境，且"合法流通品"属性让渠道侧封锁完全失效 |

一句话总结：T1588 描述"攻击者从哪买武器"，AML.T0016 在此之上指出 AI 时代的特殊现实——**最锋利的武器就在明面上的开源仓库与模型平台里，合法获取、非法使用**。ATT&CK v20 新增的 T1588.007（人工智能）与 ATLAS 的生成式 AI 子技术相互呼应，两大矩阵正在此技术上趋同。

## 动手实验

> ⚠️ **重要提示**：所有实验必须在隔离的实验室环境中进行，仅使用自有环境与公开的防御研究工具。uncensored 模型相关实验只做行为观察对比，不生成、不传播任何攻击内容。

### 实验环境准备

| 环境组件 | 用途 | 获取方式 |
|----------|------|----------|
| 隔离虚拟机（可访问外网下载、与内网隔离） | 实验环境 | 本地虚拟化平台 |
| Python 3.10+ | 运行对抗攻击库 | 官方安装包 |
| PyTorch + 小型分类模型（如 MNIST） | 对抗样本实验对象 | pip 安装 |
| Ollama + 一个小型开源 LLM | 本地部署实验 | [ollama.com](https://ollama.com/) |

### 实验1（初级）：体验"研究库武器化"零门槛

**实验目标：** 理解 AML.T0016.000——公开研究库如何被直接用于攻击。

**实验步骤：**
1. `pip install adversarial-robustness-toolbox torch torchvision`，安装官方文档示例
2. 训练（或加载）一个 MNIST 小模型，记录其在测试集上的准确率
3. 用 ART 的 FGSM 方法生成对抗样本，重新评估模型准确率
4. 记录：从安装到"攻破"自己的模型，总共花了多少分钟？

**预期结果：** 直观感受官方描述中"研究库可被武器化"的含义——全部代码公开合法，威胁只在用途。

### 实验2（中级）：本地部署开源 LLM 并观察拒绝行为

**实验目标：** 理解 AML.T0016.002 的获取路径与 uncensored 现象。

**实验步骤：**
1. 安装 Ollama，拉取一个官方对齐的小型开源模型，本地启动服务
2. 准备 10 个边界问题（如"帮我写一封冒充银行的邮件"），记录模型的拒绝率与拒绝话术
3. 阅读官方参考资料的 uncensored 模型资料（erichartford 的微调方法、拒绝方向论文），理解"移除对齐"的技术路径
4. 思考：如果攻击者完成了第 3 步的第 2 项操作，你的组织哪些环节会首先受害？

**预期结果：** 理解攻击者为何偏好本地部署与 uncensored 变体：可控、无审计、无服务条款约束。

### 实验3（高级）：组装一个最小智能体工具集并审计其影响

**实验目标：** 理解 AML.T0016.004——工具获取如何扩展智能体的能力边界。

**实验步骤：**
1. 用任意本地智能体框架（或 50 行 Python 的 function calling 循环）搭一个最小智能体
2. 为其配置两个工具：只读的目录列表工具、可执行 `whoami` 等白名单命令的 shell 工具
3. 分别在"只有工具 1""有工具 1+2"两种配置下给同一批任务，观察智能体行为差异
4. 修改工具的描述文本（如把命令工具描述成"系统信息查询"），观察模型选择与调用频率的变化
5. 对照 GTG-1002 与 Hermes Agent 案例：攻击者接入扫描器、破解工具时，本质上做了什么？

**预期结果：** 理解"获取工具=获得模型推理之外的资源与动作权限"，以及工具描述对智能体行为的影响——这正是智能体工具治理需要审计的两个面。

## 术语解释

| 术语 | 英文原名 | 通俗解释 |
|------|----------|----------|
| 获取能力 | Obtain Capabilities | 不自己研发，而是搜索、购买、下载现成的攻击工具与代码——"买现货不打铁" |
| 对抗性 AI 攻击实现 | Adversarial AI Attack Implementations | 研究界公开的 AI 攻击代码库（对抗样本、模型提取、投毒等）的可用实现 |
| 研究库武器化 | Weaponizing Research Libraries | 把为防御研究而生的开源库直接用于攻击——本技术最讽刺的获取路径 |
| 越狱 | LLM Jailbreak | 用构造的提示词绕过模型的安全限制，让它输出本应拒绝的内容 |
| Uncensored 模型 | Uncensored Model | 被移除对齐与内容过滤的模型变体，可通过微调、操纵拒绝方向或直接下载获得 |
| 模型对齐 | Model Alignment | 通过训练让模型输出符合人类价值观与安全策略——攻击者获取能力时要拆除的正是它 |
| RLHF | Reinforcement Learning from Human Feedback | 用人类反馈的强化学习做对齐的主流方法 |
| 护栏 | Guardrails | 部署在用户、工具与模型之间的安全控制层，拦截恶意输入输出与危险动作 |
| MCP 服务器 | Model Context Protocol Server | 为智能体提供工具调用的标准服务端，智能体工具生态的核心分发形式 |
| Computer-use 适配器 | Computer-use Adapter | 让智能体能操作真实计算机界面（点击、输入）的工具集成 |
| 漏洞利用 | Exploit | 利用软件 bug 让系统出现非预期行为的代码——可直接用，也是二次开发的输入 |
| 影子 AI | Shadow AI | 组织成员未经授权私自获取使用的 AI 工具与模型，既是合规问题也是攻击面 |

## 参考资料

### 📚 官方文档

- [MITRE ATLAS - Obtain Capabilities (AML.T0016)](https://atlas.mitre.org/techniques/AML.T0016/) - 官方技术页面
- [MITRE ATLAS 矩阵](https://atlas.mitre.org/matrices/ATLAS/)
- [MITRE ATLAS Data (GitHub)](https://github.com/mitre-atlas/atlas-data)

### 📰 案例报告（真实攻击与安全研究）

- [Unit 42: Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) - Hermes Agent 自主攻击战役分析（CS0070）
- [Anthropic: Disrupting the First Reported AI-Orchestrated Cyber Espionage Campaign](https://www.anthropic.com/news/disrupting-AI-espionage) - GTG-1002 间谍行动披露（CS0069）
- [ATT&CK Campaign C0062](https://attack.mitre.org/campaigns/C0062/) - GTG-1002 行动的 ATT&CK 官方条目
- [Cato CTRL: ProKYC - Deepfake Tool for Account Fraud Attacks](https://www.catonetworks.com/blog/prokyc-selling-deepfake-tool-for-account-fraud-attacks/) - KYC 绕过深伪工具研究（CS0034）
- [WSJ: Faces are the next target for fraudsters](https://www.wsj.com/articles/faces-are-the-next-target-for-fraudsters-11625662828) - 人脸识别欺诈案例报道（CS0004）
- [Sysdig: LLMjacking - Stolen Cloud Credentials Used in New AI Attack](https://sysdig.com/blog/llmjacking-stolen-cloud-credentials-used-in-new-ai-attack/) - 被盗凭证 + 逆向代理倒卖 LLM 访问（CS0030）

### 🔬 生成式 AI 滥用研究

- [Cisco Talos: Cybercriminal abuse of large language models](https://blog.talosintelligence.com/cybercriminal-abuse-of-large-language-models/) - 犯罪团伙滥用 LLM 的系统性分析
- [Eric Hartford: Uncensored Models](https://erichartford.com/uncensored-models) - 移除模型对齐的经典方法论述
- [arXiv: Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717/) - 拒绝行为由单一方向介导——uncensored 化的理论基础
- [TAICO: WhiteRabbitNeo](https://taico.ca/posts/whiterabbitneo/) - 为攻防安全构建的开源 uncensored 模型
- [GBHackers: WormGPT Enhanced with Grok and Mixtral](https://gbhackers.com/wormgpt-enhanced-with-grok-and-mixtral/) - 公开宣传恶意用途的犯罪 LLM

### 🔧 工具与资源

- [Adversarial Robustness Toolbox (ART)](https://github.com/Trusted-AI/adversarial-robustness-toolbox) - IBM 开源的对抗鲁棒性研究库
- [CleverHans](https://github.com/cleverhans-lab/cleverhans) - 对抗样本经典研究库
- [FoolBox](https://github.com/bethgelab/foolbox) - 对抗攻击基准库
- [Ollama](https://ollama.com/) / [vLLM](https://docs.vllm.ai/en/latest/) - 开源模型本地部署框架
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - LLM 应用十大安全风险

### 🔗 关联阅读

- [T1588 获取能力](../../enterprise/02-Resource-Development/T1588-Obtain-Capabilities.md) - 本技术的 ATT&CK 映射来源，对照阅读
- [T1588.007 人工智能](../../enterprise/02-Resource-Development/T1588/T1588.007-Artificial-Intelligence.md) - ATT&CK v20 新增的 AI 能力获取子技术
- [资源开发战术 (AML.TA0003)](./README.md) - 本技术所属战术的概览页

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-22 | **模板**: ATLAS 技术文档 v1.0
