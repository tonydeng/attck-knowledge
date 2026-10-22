# 资源开发 (AML.TA0003)

## 一句话理解

> 攻击者在动手攻击 AI 系统之前，先要备好"粮草"和"弹药"——搜集公开模型与数据集、租 GPU 服务器、发布投毒制品、注册假账号、抢占 LLM 幻觉出来的域名，这就是 ATLAS 语境下的资源开发。

## 战术概述

资源开发（Resource Development）是 MITRE ATLAS 矩阵中攻击准备阶段的战术，编号 AML.TA0003，位于攻击链的第二阶段。

**官方定义（意译）：**
对手试图建立可用于支撑其行动的资源。资源开发包含对手创建、购买或入侵/窃取可用于定向攻击的资源的技术。此类资源包括 AI 制品（模型/数据集等，AI Artifacts）、基础设施（Infrastructure）、账户与能力。这些资源可被用于支撑攻击生命周期的其他阶段，例如 AI 攻击适配（AI Attack Staging）。

**通俗解释：**
想象一支军队在总攻之前要囤积弹药、搭建指挥部、伪造证件。攻击 AI 系统也是一样——在真正接触目标之前，攻击者有一大堆准备工作要做。与传统网络攻击不同的是，AI 时代的"军火库"里多了新货：目标组织公开的模型和数据集本身就是情报与原料，Hugging Face 等平台上的投毒制品就是陷阱，甚至 LLM 的"幻觉"也能被抢注成钓鱼域名。

**在 AI 攻击中的作用：**
资源开发发生在侦察之后、AI 攻击适配与初始访问之前。这个阶段决定了攻击者是否有足够的"弹药"发起后续攻击：获取了目标公开的模型，才能搭建代理模型、构造对抗样本；发布了投毒数据集，下游受害者可能"自愿"把后门装进自己的训练管线。

**与 ATT&CK 企业版的关系：**
本战术与 ATT&CK Enterprise 的资源开发（TA0042）高度同源——获取基础设施、获取/开发能力、建立账户、入侵基础设施等技术与 T1583 / T1584 / T1585 / T1587 / T1588 一一对应（本库中文版可直接互参）。差异在于 ATLAS 新增了 AI 原生技术：获取公开 AI 制品、发布投毒 AI 制品、发布幻觉实体等，均以模型/数据集/智能体为核心对象，这在传统矩阵中没有对应物。

**难度等级说明：**
本战术各技术的难度星级来自 ATLAS 官方成熟度（maturity）映射：⭐⭐⭐ = Realized（已在真实攻击中实现）、⭐⭐ = Demonstrated（已有演示验证）、⭐ = Feasible（仅理论可行）。本战术 9 个技术中 8 个为 Realized，说明资源开发是已在实战中被反复验证的成熟攻击阶段。

**包含的技术类型：**
在这个阶段，攻击者会做以下几类事情：
- **获取公开 AI 制品**（AML.T0002）：在公开渠道搜集目标组织的模型、数据集与 AI 智能体配置
- **获取基础设施**（AML.T0008）：买域名、租服务器和算力，包括 AI 开发工作区与 AI 服务代理
- **获取能力**（AML.T0016）：收集现成的对抗性 AI 攻击实现、软件工具与漏洞利用
- **开发能力**（AML.T0017）：自研对抗样本、投毒数据集，甚至用 AI 智能体自主开发漏洞利用
- **建立账户**（AML.T0021）：注册各类服务账号，为后续攻击与身份冒充铺路
- **发布幻觉实体**（AML.T0060）：抢注 LLM 幻觉出的包名/域名/邮箱，守株待兔
- **暂存能力**（AML.T0079）：把投毒制品、提示词注入内容部署到模型仓库等阵地待命
- **发布投毒 AI 制品**（AML.T0115）：在公开渠道发布带后门的模型/数据集/智能体工具，污染 AI 供应链
- **入侵基础设施**（AML.T0128）：黑掉第三方的 AI 开发平台与制品仓库，借刀杀人

## 战术在攻击链中的位置

### 攻击链全景图

```mermaid
graph LR
    A["侦察"] --> B["资源开发<br/>AML.TA0003"]
    B --> C["AI攻击适配"]
    C --> D["初始访问"]
    D --> E["AI模型访问"]
    E --> F["执行"]
    F --> G["持久化"]
    G --> H["权限提升"]
    H --> I["防御规避"]
    I --> J["凭证访问"]
    J --> K["发现"]
    K --> L["横向移动"]
    L --> M["收集"]
    M --> N["命令与控制"]
    N --> O["数据渗漏"]
    O --> P["影响"]

    style B fill:#ff6b6b,stroke:#333,stroke-width:2px
```

### 当前战术的角色

资源开发是 ATLAS 攻击链的**第二阶段**，位于侦察之后、AI 攻击适配之前。攻击者在侦察阶段识别出目标的 AI 资产（公开模型、数据集、AI 服务）后，在本阶段围绕这些资产准备攻击资源。

与传统 ATT&CK 的资源开发（TA0042）相比，本战术的核心差异在于 **AI 制品成为一种新型攻击资源**：它既是情报（用于搭建代理模型）、也是武器载体（投毒制品直接进入受害者供应链）。

若蓝队能在此阶段发现异常（如公开仓库中出现与公司项目高度相似的可疑制品），就能将攻击扼杀在摇篮里——此时攻击者尚未接触目标系统，处置成本最低。

### 前置战术

- **侦察**：攻击者先通过侦察识别目标的 AI 攻击面——组织在 Hugging Face 等平台发布了哪些模型和数据集、AI 服务的技术栈是什么，才能确定需要准备哪些资源。

### 后续战术

- **AI攻击适配**：资源就绪后，攻击者利用获取的模型和数据集构造对抗数据、搭建代理模型，把"原料"加工成"武器"。
- **初始访问 / AI模型访问**：利用投毒制品、钓鱼域名、幻觉实体等资源，攻击者获得对目标系统的初始立足点或直接接触 AI 模型。

## 技术索引表

| 技术ID | 中文名称 | 难度 | 子技术数 | 一句话理解 | 关联ATT&CK | 文档状态 |
|--------|----------|:----:|:--------:|------------|:-----------:|:--------:|
| [AML.T0002](AML.T0002-Acquire-Public-AI-Artifacts.md) | 获取公开 AI 制品 | ⭐⭐⭐ | 3 | 搜刮目标组织公开的模型、数据集和智能体配置，摸清对方 AI 底牌 | — | ✅ 已完成 |
| [AML.T0008](AML.T0008-Acquire-Infrastructure.md) | 获取基础设施 | ⭐⭐⭐ | 6 | 买域名、租算力服务器，为攻击 AI 系统搭建"阵地" | [T1583](../../enterprise/02-Resource-Development/T1583-Acquire-Infrastructure.md) | ✅ 已完成 |
| [AML.T0016](AML.T0016-Obtain-Capabilities.md) | 获取能力 | ⭐⭐⭐ | 5 | 收集现成的对抗性 AI 攻击工具、通用软件与漏洞利用代码 | [T1588](../../enterprise/02-Resource-Development/T1588-Obtain-Capabilities.md) | ✅ 已完成 |
| [AML.T0017](AML.T0017-Develop-Capabilities.md) | 开发能力 | ⭐⭐⭐ | 3 | 自研对抗样本与投毒制品，甚至让 AI 智能体自主开发漏洞利用 | [T1587](../../enterprise/02-Resource-Development/T1587-Develop-Capabilities.md) | ✅ 已完成 |
| [AML.T0021](AML.T0021-Establish-Accounts.md) | 建立账户 | ⭐⭐⭐ | 0 | 注册各类服务账号，为后续攻击、获取受限制品和身份冒充铺路 | [T1585](../../enterprise/02-Resource-Development/T1585-Establish-Accounts.md) | ✅ 已完成 |
| [AML.T0060](AML.T0060-Publish-Hallucinated-Entities.md) | 发布幻觉实体 | ⭐⭐ | 0 | 抢注 LLM"幻觉"出的包名/域名，等开发者照着 AI 答案自己踩坑 | — | ✅ 已完成 |
| [AML.T0079](AML.T0079-Stage-Capabilities.md) | 暂存能力 | ⭐⭐⭐ | 0 | 把投毒制品和提示词注入内容部署到模型仓库，静待受害者上钩 | [T1608](../../enterprise/02-Resource-Development/T1608-Stage-Capabilities.md) | ✅ 已完成 |
| [AML.T0115](AML.T0115-Publish-Poisoned-AI-Artifacts.md) | 发布投毒 AI 制品 | ⭐⭐⭐ | 3 | 在公开平台发布带后门的模型/数据集/智能体工具，污染 AI 供应链 | — | ✅ 已完成 |
| [AML.T0128](AML.T0128-Compromise-Infrastructure.md) | 入侵基础设施 | ⭐⭐⭐ | 0 | 黑掉第三方的 AI 开发平台、模型仓库与算力服务，借刀杀人 | [T1584](../../enterprise/02-Resource-Development/T1584-Compromise-Infrastructure.md) | ✅ 已完成 |

## 子技术索引

| 子技术ID | 名称 | 难度 | 一句话理解 | 文档状态 |
|----------|------|:----:|-----------|:--------:|
| [AML.T0002.000](AML.T0002/AML.T0002.000-Datasets.md) | 数据集 | ⭐⭐ | 下载目标组织公开的训练/测试数据集，分析其 AI 任务与数据分布 | ✅ 已完成 |
| [AML.T0002.001](AML.T0002/AML.T0002.001-Models.md) | 模型 | ⭐⭐ | 获取目标公开的模型与参数，用于搭建代理模型或直接构造对抗样本 | ✅ 已完成 |
| [AML.T0002.002](AML.T0002/AML.T0002.002-AI-Agent-Configurations.md) | AI 智能体配置 | ⭐⭐ | 搜集目标智能体的系统提示词、工具列表等配置信息 | ✅ 已完成 |
| [AML.T0008.000](AML.T0008/AML.T0008.000-AI-Development-Workspaces.md) | AI 开发工作区 | ⭐⭐ | 租用云 Notebook、开发平台等 AI 工作环境作为攻击阵地 | ✅ 已完成 |
| [AML.T0008.001](AML.T0008/AML.T0008.001-Consumer-Hardware.md) | 消费级硬件 | ⭐⭐⭐ | 采购手机、摄像头等普通设备，作为攻击基础设施的组成部分 | ✅ 已完成 |
| [AML.T0008.002](AML.T0008/AML.T0008.002-Domains.md) | 域名 | ⭐⭐ | 注册相似域名，用于钓鱼、托管恶意内容或伪装成正规 AI 服务 | ✅ 已完成 |
| [AML.T0008.003](AML.T0008/AML.T0008.003-Physical-Countermeasures.md) | 物理对抗措施 | ⭐⭐ | 准备打印图案、可穿戴设备、伪装物等干扰 AI 传感器/组件的实物 | ✅ 已完成 |
| [AML.T0008.004](AML.T0008/AML.T0008.004-Serverless.md) | 无服务器 | ⭐ | 利用云函数快速搭建可随时销毁、难以溯源的攻击基础设施 | ✅ 已完成 |
| [AML.T0008.005](AML.T0008/AML.T0008.005-AI-Service-Proxy.md) | AI 服务代理 | ⭐⭐⭐ | 部署中转代理访问 AI 服务，混入正常流量并隐藏真实来源 | ✅ 已完成 |
| [AML.T0016.000](AML.T0016/AML.T0016.000-Adversarial-AI-Attack-Implementations.md) | 对抗性 AI 攻击实现 | ⭐⭐⭐ | 获取现成的对抗样本生成、模型提取、投毒等攻击代码库 | ✅ 已完成 |
| [AML.T0016.001](AML.T0016/AML.T0016.001-Software-Tools.md) | 软件工具 | ⭐⭐⭐ | 获取可改造用于攻击 AI 系统的通用软件工具 | ✅ 已完成 |
| [AML.T0016.002](AML.T0016/AML.T0016.002-Generative-AI.md) | 生成式 AI | ⭐⭐⭐ | 获取 LLM 等生成式 AI 的访问能力，辅助生成攻击素材 | ✅ 已完成 |
| [AML.T0016.003](AML.T0016/AML.T0016.003-Exploits.md) | 漏洞利用 | ⭐⭐⭐ | 获取针对 AI 相关软件栈（框架、推理服务）的漏洞利用代码 | ✅ 已完成 |
| [AML.T0016.004](AML.T0016/AML.T0016.004-AI-Agent-Tools.md) | AI 智能体工具 | ⭐⭐⭐ | 获取可滥用或改造的智能体框架、插件与工具集 | ✅ 已完成 |
| [AML.T0017.000](AML.T0017/AML.T0017.000-Adversarial-AI-Attacks.md) | 对抗性 AI 攻击 | ⭐⭐ | 自研投毒、对抗扰动、模型提取等针对 AI 系统的攻击方法 | ✅ 已完成 |
| [AML.T0017.001](AML.T0017/AML.T0017.001-Autonomous-Exploit-Development.md) | 自主漏洞利用开发 | ⭐⭐⭐ | 用 AI 智能体迭代挖掘并开发已知/未知漏洞的利用代码 | ✅ 已完成 |
| [AML.T0017.002](AML.T0017/AML.T0017.002-AI-Agent-Tools.md) | AI 智能体工具 | ⭐⭐⭐ | 开发含恶意指令的网站或工具，诱导目标智能体执行恶意行为 | ✅ 已完成 |
| [AML.T0115.000](AML.T0115/AML.T0115.000-Datasets.md) | 数据集 | ⭐⭐ | 发布掺入后门样本或恶意数据的投毒数据集，等受害者拿来训练 | ✅ 已完成 |
| [AML.T0115.001](AML.T0115/AML.T0115.001-Models.md) | 模型 | ⭐⭐⭐ | 发布带后门或恶意行为的模型文件，等受害者下载部署 | ✅ 已完成 |
| [AML.T0115.002](AML.T0115/AML.T0115.002-AI-Agent-Tools.md) | AI 智能体工具 | ⭐⭐⭐ | 发布含恶意代码、恶意配置的智能体插件与工具 | ✅ 已完成 |

## 统计信息

- **技术总数**：9 个
- **子技术总数**：20 个
- **文档总数**：29 个（9 个主技术 + 20 个子技术）
- **已完成文档**：29 个（全部完成 ✅）
- **难度分布**：⭐⭐⭐ × 8 个、⭐⭐ × 1 个（AML.T0060）
- **平台覆盖**：Predictive AI / Generative AI / Agentic AI / Enterprise
- **关联 ATT&CK 技术**：5 项直接映射（T1583 / T1584 / T1585 / T1587 / T1588）

## 推荐阅读顺序

> 各技术文档均已完成，可按以下顺序系统学习；建议对照阅读 ATT&CK Enterprise 对应文档，理解传统技术在 AI 语境下的延伸。

### 第一阶段：理解 AI 时代的"备战"（入门）

**前置知识：** 了解基本网络概念（域名、云服务、公开代码仓库），知道什么是机器学习模型和数据集。

**推荐阅读：**

1. **AML.T0002 获取公开 AI 制品** - 从这里理解 AI 攻击的第一性原理：公开的模型和数据集本身就是攻击者眼中的情报与原料。可先浏览[企业版资源开发战术概览](../../enterprise/02-Resource-Development/README.md)建立背景。
2. **AML.T0008 获取基础设施** - 对照企业版 [T1583 获取基础设施](../../enterprise/02-Resource-Development/T1583-Acquire-Infrastructure.md)，重点关注"AI 开发工作区""AI 服务代理""物理对抗措施"这些 AI 特有的子技术。
3. **AML.T0021 建立账户** - 对照企业版 [T1585 建立账户](../../enterprise/02-Resource-Development/T1585-Establish-Accounts.md)，理解为何获取某些模型/数据集需要"养号"。

**学习建议：**
- 到 Hugging Face 搜索知名组织的公开模型/数据集，感受"公开 AI 制品"的暴露面有多大
- 思考：组织公开发布的每一个制品，向攻击者泄露了什么信息？

### 第二阶段：AI 供应链攻击（进阶）

**前置知识：** 了解机器学习基础概念（训练、微调、后门），熟悉 pip/conda 或 Docker 依赖管理。

**推荐阅读：**

1. **AML.T0115 发布投毒 AI 制品** - 本战术的核心威胁：理解"发布即攻击"，投毒制品如何借供应链进入下游训练与推理环境。
2. **AML.T0079 暂存能力** - 对照企业版 [T1608 暂存能力](../../enterprise/02-Resource-Development/T1608-Stage-Capabilities.md)，关注模型仓库、包仓库、容器仓库这些 AI 时代的新"弹药库"。
3. **AML.T0016 获取能力 / AML.T0017 开发能力** - 对照企业版 [T1588 获取能力](../../enterprise/02-Resource-Development/T1588-Obtain-Capabilities.md)与 [T1587 开发能力](../../enterprise/02-Resource-Development/T1587-Develop-Capabilities.md)，理解攻击工具的"自研 vs 现货"之分在 AI 领域的对应物。

**学习建议：**
- 阅读 BadNets 论文（见参考资料），理解模型后门的基本原理
- 检查自己项目的模型/数据集来源，实践哈希与签名校验

### 第三阶段：新攻击范式（高级）

**前置知识：** 了解 LLM 工作原理（提示词、幻觉现象）、AI 开发平台（Notebook 云环境、模型仓库）。

**推荐阅读：**

1. **AML.T0060 发布幻觉实体** - 理解"幻觉武器化"（slopsquatting）：LLM 编造的包名被攻击者抢注后，AI 助手会亲手把恶意依赖推荐给开发者。
2. **AML.T0128 入侵基础设施** - 对照企业版 [T1584 破坏基础设施](../../enterprise/02-Resource-Development/T1584-Compromise-Infrastructure.md)，分析 AI 开发平台、模型仓库为何成为高价值跳板。

**学习建议：**
- 关注 AI 供应链安全事件报告（见参考资料 ATLAS 案例库）
- 思考防御侧：如何监控"与我相关的幻觉实体"和可疑相似域名？

## 参考资料

### 官方文档

- [MITRE ATLAS - Resource Development (AML.TA0003)](https://atlas.mitre.org/tactics/AML.TA0003/)
- [MITRE ATLAS 矩阵总览](https://atlas.mitre.org/matrices/atlas/)
- [MITRE ATLAS 案例研究库](https://atlas.mitre.org/studies/)
- [MITRE ATLAS Data (GitHub)](https://github.com/mitre-atlas/atlas-data)

### AI 安全研究

- [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain (Gu et al., 2017)](https://arxiv.org/abs/1708.06733) - 模型后门/投毒攻击的开创性论文
- [Hugging Face Hub 安全文档](https://huggingface.co/docs/hub/security) - 模型仓库安全机制（pickle 风险、GPG 签名、安全看板）
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - LLM 应用安全风险清单
- [We Have a Package for You! Package Hallucinations Induced by Code Generators (Vollmer et al., 2024)](https://arxiv.org/abs/2411.10906) - LLM"幻觉包名"现象的系统研究，AML.T0060 的理论基础
- [ATT&CK Enterprise 资源开发战术（本库中文版）](../../enterprise/02-Resource-Development/README.md) - 对照阅读传统资源开发

## 速查卡

- **常用技术**：AML.T0002（获取公开 AI 制品——情报与原料）、AML.T0115（发布投毒 AI 制品——供应链陷阱）、AML.T0008（获取基础设施——域名/算力/代理）
- **关键检测信号**：新注册域名/包名与公司名或公司项目名高度相似、公开仓库出现仿冒组织名义的模型/数据集、异常的匿名下载行为、证书透明度日志中的可疑域名
- **防御要点**：清点组织公开 AI 制品的暴露面、对第三方模型/数据集做哈希与签名校验、锁定依赖版本、监控 Hugging Face/PyPI 等平台上的仿冒名称、对 LLM 推荐的依赖保持人工审核
- **蓝队关注点**：资源开发阶段攻击者尚未接触目标系统，是"扼杀在摇篮里"的最佳窗口期；盯住"与我相关的新出现的域名、包名、制品"是性价比最高的监控策略
- **红队视角**：攻击 AI 系统的成本结构与传统入侵不同——"发布"一个投毒制品的边际成本极低，一次发布可被无数下游受害者重复"采购"，这是 AI 供应链攻击最具规模效应的地方

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-22 | **模板**: ATLAS 战术README v1.0
