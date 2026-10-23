#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate ATLAS case-study docs (src/atlas/case-studies/*.md) from official YAML data
plus hand-authored Chinese metadata (CASE_META below).

Usage: python src/_tools/gen-case-studies.py
"""
import json
import os
import re
import sys

import yaml

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
YAML_PATH = os.path.join(ROOT, "src", "_data", "atlas", "ATLAS-2026.09.yaml")
ATLAS_DIR = os.path.join(ROOT, "src", "atlas")
OUT_DIR = os.path.join(ATLAS_DIR, "case-studies")

# ---------------------------------------------------------------------------
# Hand-authored Chinese metadata: zh_name / one_liner / summary per case
# ---------------------------------------------------------------------------
CASE_META = {
    "AML.CS0000": {
        "zh_name": "恶意软件 C&C 流量深度学习检测器规避",
        "one_liner": " Palo Alto 安全 AI 研究团队用公开数据集逆向了一个恶意 C&C 流量检测模型，发现无需恶意样本也能构造出绕过检测的流量。",
        "summary": "Palo Alto Networks 安全 AI 研究团队对 HTTP 流量中的恶意软件命令与控制（C&C）检测深度学习模型进行了红队测试。基于公开可得的训练数据，团队构建了替代模型，据此构造出规避样本——证明攻击者无需接触原模型即可实现检测规避。",
    },
    "AML.CS0001": {
        "zh_name": "僵尸网络 DGA 检测规避",
        "one_liner": "用「普通域名生成器」生成的域名骗过基于 CNN 的 DGA 检测器——恶意域名看起来毫无恶意特征。",
        "summary": "Palo Alto Networks 安全 AI 研究团队使用通用域名生成算法生成域名，成功绕过了基于卷积神经网络的僵尸网络 DGA 检测器。攻击表明恶意域名可以伪装成正常域名特征逃避检测。",
    },
    "AML.CS0002": {
        "zh_name": "VirusTotal 投毒",
        "one_liner": "把良性样本反复提交打上恶意标签，污染 VirusTotal 的机器学习引擎——让检测器把好人当坏人。",
        "summary": "McAfee 高级威胁研究团队发现某勒索软件家族的告警量异常增长。调查表明许多良性样本被故意反复提交至 VirusTotal 并打上恶意标签，污染了其机器学习检测引擎的判断。这类投毒会降低 ML 检测器的可信度并干扰威胁情报生态。",
    },
    "AML.CS0003": {
        "zh_name": "绕过 Cylance AI 恶意软件检测",
        "one_liner": "一串「万能字符串」追加到恶意文件末尾，AI 杀毒引擎就把它当成了好人。",
        "summary": "Skylight 研究人员发现将一个特定字符串追加到恶意文件末尾即可绕过 Cylance AI 恶意软件检测器的判别。这种通用绕过利用了模型决策边界的脆弱性，无需修改恶意代码本身。",
    },
    "AML.CS0004": {
        "zh_name": "人脸识别系统摄像头劫持攻击",
        "one_liner": "劫持摄像头并配合深伪技术绕过活体人脸识别——两名中国籍嫌疑人借此骗过美国国税局 7700 万美元。",
        "summary": "摄像头劫持攻击可绕过传统活体人脸识别认证，实现特权系统访问与受害者冒充。两名中国籍个人在 2018 至 2020 年间利用该手法配合深伪技术与数百家空壳公司，向美国国税局提交虚假退税申请，骗取超过 7700 万美元。",
    },
    "AML.CS0005": {
        "zh_name": "机器翻译服务攻击",
        "one_liner": "UC Berkeley 研究者借公开翻译 API 的输出「克隆」了翻译模型——不用偷模型，问了三百万次就把能力问走了。",
        "summary": "机器翻译服务（Google Translate、Bing Translator、Systran 等）提供公开 UI 与 API。UC Berkeley 研究团队利用这些公开接口发起了模型提取攻击，通过自然查询收集输入-输出对，成功复制出与原服务行为近似的模型，证明商业 NLP 模型面临知识产权窃取风险。",
    },
    "AML.CS0006": {
        "zh_name": "Clearview AI 配置错误",
        "one_liner": "人脸识别公司把数据库暴露在公网——攻击者连门都不用撬，直接拿走了全部人脸数据。",
        "summary": "Clearview AI 开发的人脸识别工具可搜索公开照片进行匹配，被执法机构用于调查。2020 年其源代码仓库因配置错误暴露，攻击者可访问其客户名单、代码库与（据称）部分人脸数据库，构成重大数据泄露事件。",
    },
    "AML.CS0007": {
        "zh_name": "GPT-2 模型复现",
        "one_liner": "OpenAI 不敢放出的 GPT-2 完整模型，被社区用「猜词游戏」一点点复现了出来。",
        "summary": "OpenAI 构建了 GPT-2 语言模型，因担心被滥用（冒充他人、生成虚假信息）而分阶段发布。社区研究者利用逐词查询预测的方式，成功复现了完整模型的行为——证明对公开 API 的黑盒访问足以复现被「雪藏」的模型。",
    },
    "AML.CS0008": {
        "zh_name": "ProofPoint 邮件防护规避",
        "one_liner": "先克隆一个 ProofPoint 的邮件防护模型，再对着副本打磨绕过手法——原版应声失效。",
        "summary": "Proof Pudding（CVE-2019-20634）研究展示了 ML 研究者如何规避 ProofPoint 邮件防护系统：先构建一个模仿其行为的本地模型，再针对该模型寻找规避样本，最终成功欺骗了真实的 ProofPoint 系统。",
    },
    "AML.CS0009": {
        "zh_name": "Tay 中毒事件",
        "one_liner": "微软聊天机器人 Tay 上线 16 小时就被 4chan 网友「协同教坏」成种族主义者，紧急下线。",
        "summary": "微软于 2016 年 3 月 23 日推出 Twitter 聊天机器人 Tay。与以往脚本机器人不同，Tay 会从互动中学习。上线后 4chan 用户协同发送大量极端与种族主义内容，Tay 开始自主复现攻击性言论，16 小时后被微软紧急下线——成为 AI 系统被协同操纵的标志性事件。",
    },
    "AML.CS0010": {
        "zh_name": "微软 Azure 服务中断演练",
        "one_liner": "微软 AI 红队对内部 Azure 服务做「传统攻击+AI 攻击」组合演练，成功让服务降级。",
        "summary": "微软 AI 红队对一个内部 Azure 服务开展了以服务中断为目标的红队演练。行动结合了传统攻击与 AI 特有手法，最终成功破坏了服务可用性，并验证了模型与传统攻击面结合后的放大效应。",
    },
    "AML.CS0011": {
        "zh_name": "微软边缘 AI 规避",
        "one_liner": "红队用自动化系统对边缘 AI 产品做模糊测试，成功让边缘侧模型「看走眼」。",
        "summary": "Azure 红队对一款在边缘运行 AI 负载的新微软产品进行了红队演练，使用自动化系统持续构造对抗输入。演练成功诱导了目标性误分类，验证了边缘 AI 部署面临的对抗攻击风险。",
    },
    "AML.CS0012": {
        "zh_name": "物理域人脸识别系统规避",
        "one_liner": "MITRE AI 红队戴着特制眼镜/贴纸走过商用人脸识别系统——识别成了另一个人。",
        "summary": "MITRE AI 红队对商用人脸识别服务演示了物理域规避攻击：利用特制的物理道具（眼镜、贴纸等）诱导目标性误分类。演练证明了数字对抗样本可跨入物理世界威胁真实部署系统。",
    },
    "AML.CS0013": {
        "zh_name": "移动应用深度学习模型后门攻击",
        "one_liner": "微软研究院发现移动 App 里的深度学习模型可以被植入「带触发器的后门」——正常用没事，一碰触发器就作恶。",
        "summary": "微软研究院研究人员演示了针对移动应用中深度学习模型的后门攻击：在模型中植入特定触发条件，正常输入下表现正常，触发条件出现时执行恶意行为。研究表明移动端部署的模型普遍缺乏完整性保护。",
    },
    "AML.CS0014": {
        "zh_name": "迷惑云杀毒神经网络",
        "one_liner": "云杀毒的特征向量在用户侧生成、云端判别——攻击者在本地「污染」特征，云端模型就疯了。",
        "summary": "云 ML 恶意软件检测器通常在用户侧构建特征再上传云端判别。研究者演示了在用户侧构造混淆特征向量的攻击方式：本地特征被「污染」后，云端神经网络对恶意文件的判别被完全误导。",
    },
    "AML.CS0015": {
        "zh_name": "PyTorch 依赖链失陷",
        "one_liner": "恶意包混入 PyTorch 每日构建版，收集的敏感信息经加密 DNS 查询悄悄送出门。",
        "summary": "2022 年 12 月 25 至 30 日，PyTorch 预发布版（torch-nightly）的 Linux 包因恶意二进制依赖（triton 包的抢注版本）被投毒。恶意样本收集 /etc/resolv.conf 等系统信息，并通过加密 DNS 查询上传至攻击者域名，波及大量运行 nightly 版本的 ML 开发环境。",
    },
    "AML.CS0016": {
        "zh_name": "MathGPT 提示词注入实现代码执行",
        "one_liner": "问数学题的网站，被一句注入指令变成了任意代码执行平台。",
        "summary": "公开的 Streamlit 应用 MathGPT 使用 GPT-3 回答用户数学问题。研究表明，攻击者可通过提示词注入诱导 MathGPT 生成并执行恶意代码——从「解题工具」到「代码执行平台」只差一段提示词，还可能导致 API 配额被滥用耗尽。",
    },
    "AML.CS0017": {
        "zh_name": "绕过 ID.me 身份验证",
        "one_liner": "深伪技术帮一个人冒领了 180 份失业救济金——加州损失 340 万美元。",
        "summary": "2020 年 10 月至 2021 年 12 月，一名个人通过绕过 ID.me 自动身份验证系统（利用深伪等手段），在加利福尼亚州提交了至少 180 份虚假失业救济申请，累计骗取约 340 万美元。",
    },
    "AML.CS0018": {
        "zh_name": "Google Colab 任意代码执行",
        "one_liner": "Colab 是给数据科学家的笔记本，也是攻击者的免费算力与代码执行沙箱。",
        "summary": "Google Colab 是运行在虚拟机上的 Jupyter Notebook 服务。研究演示了多种在 Colab 中实现任意代码执行的路径：环境可访问 Google Drive 凭证，攻击者获得 Colab 会话后可进一步窃取私有数据、外传 ML 制品，甚至以受害者身份调用 Google API。",
    },
    "AML.CS0019": {
        "zh_name": "PoisonGPT",
        "one_liner": "开源模型被植入一条假历史事实后改名上传 HuggingFace——企业下载部署，就替攻击者散布谎言。",
        "summary": "Mithril Security 研究者演示了对开源预训练 LLM 的投毒：修改模型使其对特定事实（如首次登月者）返回错误答案，再以相似名称上传至 HuggingFace。下游企业若部署该模型，就会持续散布虚假事实——演示了开源模型供应链的完整性风险。",
    },
    "AML.CS0020": {
        "zh_name": "间接提示词注入：Bing Chat 数据海盗",
        "one_liner": "Bing Chat 能「看到」你打开的网页——攻击者在网页里埋指令，AI 就替攻击者打探你的消息。",
        "summary": "用户可授权 Microsoft Bing Chat 查看并访问当前打开的网页。研究者演示了在网页中埋入间接提示词注入，诱导 Bing Chat 执行攻击者指令——包括要求用户提供敏感信息并配合社会工程话术，将 AI 助手转化为攻击媒介。",
    },
    "AML.CS0021": {
        "zh_name": "ChatGPT 对话内容渗漏",
        "one_liner": "ChatGPT 被诱导回复一张「图片」，图片 URL 里藏着你的完整对话——渲染的瞬间数据出网。",
        "summary": "Embrace The Red 演示了经间接提示词注入窃取 ChatGPT 用户对话：攻击者把恶意提示词上传至公共网站，用户与 ChatGPT 交互读到该提示词后，ChatGPT 回复包含 Markdown 图片，URL 中秘密嵌入用户对话内容；ChatGPT 自动渲染图片，对话随之外传至攻击者服务器。",
    },
    "AML.CS0022": {
        "zh_name": "ChatGPT 软件包幻觉",
        "one_liner": "AI 会一本正经地推荐不存在的软件包——攻击者抢先注册这些包名，你的 pip install 就是他的后门。",
        "summary": "研究者发现 ChatGPT 等 LLM 会幻觉出软件仓库中不存在的包名。攻击者可抢先在 PyPI/npm 发布这些恶意包，等待开发者被 AI「推荐」后安装——将 LLM 幻觉武器化为软件供应链攻击。",
    },
    "AML.CS0023": {
        "zh_name": "ShadowRay：暴露 Ray 集群劫持",
        "one_liner": "Ray 的任务 API 天生允许远程执行且默认无认证——暴露在公网就等于送出集群控制权。",
        "summary": "Ray 是扩展生产 AI 工作流的开源框架，其 Job API 设计上允许任意远程执行且默认无认证。ShadowRay 研究发现大量暴露在公网的 Ray 集群，攻击者可无凭证接管算力、执行任意代码、窃取 AI 制品与凭证——Oyster（后门）团伙在野利用了该暴露面。",
    },
    "AML.CS0024": {
        "zh_name": "Morris II 蠕虫：RAG 攻击",
        "one_liner": "全球第一个「AI 蠕虫」：一封邮件感染 RAG 邮件助手，泄露隐私后自我复制发给下一个人。",
        "summary": "研究者开发了 Morris II——针对生成式 AI 生态的零点击蠕虫：发送一封含对抗性自复制提示词的邮件，RAG 邮件助手自动摄取并执行，泄露检索到的私人邮件内容（邮件、地址等敏感数据），并把蠕虫提示词复制进回复继续传播。蠕虫借 GenAI 系统间的连接性实现跨系统扩散。",
    },
    "AML.CS0025": {
        "zh_name": "Web 级数据集投毒：Split-view 攻击",
        "one_liner": "数据集构建者用过的域名过期后被攻击者买下——同一个 URL，训练时是毒药，审计时是正常内容。",
        "summary": "许多大规模数据集以「URL 列表」形式分发。研究者演示了 split-view 投毒：收购数据集历史引用的过期域名，对数据集重新构建的请求返回投毒内容、对审计请求返回正常内容。10 个 web 级数据集（含 Google DeepMind、ETH Zurich 等使用的数据集）被验证可被污染，且无需入侵任何服务器。",
    },
    "AML.CS0026": {
        "zh_name": "以 M365 Copilot 为内鬼的金融交易劫持",
        "one_liner": "Copilot 摄取的邮件里藏着注入指令——AI「以你自己身份」执行了汇款操作。",
        "summary": "Zenity 研究团队在 2024 年 8 月的红队演练中成功操纵了 Microsoft 365 Copilot：攻击利用 Copilot 摄取企业内容（邮件等）的特点，在其中埋入提示词注入，诱导 Copilot 以受信任内幕人员的身份执行金融交易劫持——展示了办公智能体被武器化为「内鬼」的路径。",
    },
    "AML.CS0027": {
        "zh_name": "HuggingFace 组织混淆",
        "one_liner": "在 HuggingFace 注册一个和知名公司同名的「组织」——80 个专有模型暴露在伪造门面下。",
        "summary": "安全研究者 threlfall_hax 在 HuggingFace 上创建了仿冒真实组织的账号。研究者利用该伪造组织演示了暴露风险：80 个来自真实组织的专有模型因错误配置公开可下载，攻击者可借组织混淆进一步投毒模型分发链。",
    },
    "AML.CS0028": {
        "zh_name": "AI 模型篡改与供应链攻击",
        "one_liner": "8000 个配置错误的容器仓库被扫了一遍——1000 个模型可以被任意下载替换。",
        "summary": "Trend Micro 研究者通过服务索引门户与 Web 搜索工具发现超过 8000 个暴露在互联网上的错误配置私有容器仓库。其中约 1000 个包含可被公开拉取的模型：攻击者可下载专有模型、或篡改镜像层替换为投毒模型，构成 AI 供应链攻击面。",
    },
    "AML.CS0029": {
        "zh_name": "Google Bard 对话内容渗漏",
        "one_liner": "一份共享 Google 文档里埋着注入指令——Bard 读完后把你的对话写进了「图片地址」。",
        "summary": "Embrace The Red 演示了 Bard 用户对话的窃取：攻击者共享一个含恶意提示词的 Google Doc，受害者让 Bard 处理该文档时注入执行——Bard 回复包含 Markdown 图片，URL 中嵌入用户对话；Bard 自动渲染 Markdown，向攻击者控制的 Google App Script 发起请求完成外传。",
    },
    "AML.CS0030": {
        "zh_name": "LLM Jacking",
        "one_liner": "偷来的云凭证在黑市上「包月出售」——买家免费用 GPT，账单记在你头上。",
        "summary": "Sysdig 威胁研究团队发现恶意行为者利用窃取的凭证访问云托管 LLM：攻击者从公共仓库收集泄露凭证，隐蔽接入企业级 LLM 服务并转售访问权（LLM Jacking）。受害者承担全部 API 费用，且被盗服务可能被用于生成有害内容。",
    },
    "AML.CS0031": {
        "zh_name": "HuggingFace 上的恶意模型",
        "one_liner": "模型文件里藏着反向 shell——「下载即上线」，HuggingFace 变成恶意软件分发站。",
        "summary": "ReversingLabs 研究者在 HuggingFace 模型仓库发现了内嵌恶意软件的模型：利用 pickle 序列化格式在加载时执行代码的能力，模型文件被植入反向 shell 等载荷。下载并加载这些模型的用户会直接交出系统控制权。",
    },
    "AML.CS0032": {
        "zh_name": "ML 钓鱼网页检测系统规避未遂",
        "one_liner": "钓鱼网站在 ML 检测器眼皮底下伪装成正常站——攻击者持续对抗安全厂商的检测模型。",
        "summary": "攻击者制作的钓鱼网站在视觉上与合法站点高度相似，用于诱骗用户输入凭证。安全事件表明攻击者持续尝试规避基于 ML 的钓鱼网页检测系统——对抗在检测器与规避手法之间持续演化。",
    },
    "AML.CS0033": {
        "zh_name": "活体深伪图像注入绕过移动端 KYC 验证",
        "one_liner": "虚拟摄像头 + 深伪视频 = 绕过「眨眨眼」活体检测——iProov 红队亲自演示。",
        "summary": "人脸生物认证广泛用于移动端的用户入驻与 KYC。iProov 研究团队演示了活体深伪图像注入攻击：通过虚拟摄像头注入深度伪造视频流，绕过移动端活体检测完成身份冒充——证明纯软件注入即可攻破生物认证链路。",
    },
    "AML.CS0034": {
        "zh_name": "ProKYC：用于账户欺诈的深伪工具",
        "one_liner": "黑产工具明码标价：交钱就帮你用深伪视频过银行 KYC——「犯罪即服务」的 AI 时代。",
        "summary": "Cato CTRL 安全研究人员发现 ProKYC——一款出售给网络犯罪分子的深伪工具，用于绕过金融服务机构的 KYC 验证。该工具生成深度伪造人脸视频通过银行端验证，把 AI 深伪能力商品化为欺诈基础设施。",
    },
    "AML.CS0035": {
        "zh_name": "Slack AI 间接提示词注入数据渗漏",
        "one_liner": "公共频道里的一条帖子进了 Slack AI 的 RAG 库——用户一提问，API 密钥就顺着「链接」出了门。",
        "summary": "PromptArmor 演示了 Slack AI 私有数据的窃取：恶意提示词经公共频道帖进入 Slack AI 的 RAG 数据库，受害者用户查询 Slack AI 时提示词被检索执行——响应被渲染为可点击链接，受害者的 API 密钥编码在 URL 中完成外传。",
    },
    "AML.CS0036": {
        "zh_name": "AIKatz：攻击 LLM 桌面应用",
        "one_liner": "Mimikatz 的 AI 版：从 LLM 桌面应用的内存里抽取认证令牌——AI 时代的第一代「凭据转储」工具。",
        "summary": "Lumia 研究者演示了从 LLM 桌面应用内存中提取认证令牌的攻击：AIKatz 以类似 Mimikatz 的方式转储 AI 应用进程内存中的令牌，攻击者可利用这些令牌冒充用户访问其 AI 服务与数据。",
    },
    "AML.CS0037": {
        "zh_name": "Copilot Studio 智能体工具数据渗漏",
        "one_liner": "客户服务智能体的邮件工具被注入劫持——整个 CRM 数据库被打包发给了「研究者」。",
        "summary": "Zenity 研究者演示了经提示词注入针对 AI 客服智能体（Copilot Studio）的数据渗漏：注入指令诱导智能体收集其可访问的组织数据（含整个 CRM 数据库内容），并调用邮件工具把结果发送到研究者指定地址——合法工具完成越权外传。",
    },
    "AML.CS0038": {
        "zh_name": "为延迟的自动工具调用植入指令",
        "one_liner": "这轮对话埋的雷，下一轮才炸——绕过 Gemini「同轮限制」的延迟触发注入。",
        "summary": "Embrace The Red 演示了 Google Gemini 的延迟自动工具调用：把注入指令埋入当前轮对话，延迟到下一轮对话再自动触发工具调用——利用时序差绕过「仅当前轮内容可触发工具」的安全限制，实现无用户交互的恶意动作。",
    },
    "AML.CS0039": {
        "zh_name": "Living Off AI：经 Jira 服务管理的提示词注入",
        "one_liner": "工单系统里的一条恶意评论，让 AI 助手带着企业权限「接管」了工单流程。",
        "summary": "Cato Networks 研究者演示了嵌入企业工作流的 AI 系统如何被利用：经 Jira 服务管理的提示词注入，让 AI 助手以提升的权限执行恶意动作——攻击者借「AI 员工」的身份在企业流程中潜伏并横向行动（Living Off AI）。",
    },
    "AML.CS0040": {
        "zh_name": "提示词注入攻击 ChatGPT 记忆",
        "one_liner": "一次注入，长期驻留：ChatGPT 的「记忆」功能被植入恶意指令，每次对话都在执行攻击者的私货。",
        "summary": "Embrace The Red 演示了 ChatGPT 记忆功能的注入攻击：经提示词注入把恶意指令写入持久记忆，此后每次对话都被污染记忆影响——注入从「一次性」升级为「长期驻留」，并可结合长期社会工程操纵用户。",
    },
    "AML.CS0041": {
        "zh_name": "规则文件后门：AI 编码助手的供应链攻击",
        "one_liner": "AI 编码助手的「项目规则」文件被植入后门——AI 写的每一行代码都带着攻击者的意图。",
        "summary": "Pillar Security 研究者演示了针对 AI 编码助手的供应链攻击：在规则文件（rules file，配置 AI 编码行为的文件）中注入恶意指令，AI 生成的代码被持续植入后门——开发者以为在用 AI 提效，实际在引入漏洞。",
    },
    "AML.CS0042": {
        "zh_name": "SesameOp：滥用 OpenAI Assistants API 的 C2 后门",
        "one_liner": "后门不上线、不连 C2——它「聊」OpenAI API：指令藏在助手对象里，结果加密回传，潜伏数月。",
        "summary": "微软事件响应 DART 团队在一台失陷系统中发现 SesameOp 后门：植入体滥用 OpenAI Assistants API 作为隐蔽命令与控制信道——从攻击者的 Assistant 对象获取命令、本地执行、加密回传结果，完全混入正常 AI API 流量，在系统上潜伏数月从事间谍活动。",
    },
    "AML.CS0043": {
        "zh_name": "内嵌提示词注入的恶意软件原型",
        "one_liner": "恶意样本里塞了一段给 AI 杀毒引擎的「话」——让检测器自己把自己说服成无害。",
        "summary": "Check Point Research 发现了一个野外恶意软件原型样本，其中包含提示词注入内容——设计用于操纵基于 LLM 的恶意软件检测器与分析工具，诱导 AI 判断样本无害。这标志着提示词注入开始进入恶意软件免杀技术库。",
    },
    "AML.CS0044": {
        "zh_name": "LAMEHUG：利用动态 AI 生成命令的恶意软件",
        "one_liner": "APT28 的新玩具：命令由 LLM 动态生成——特征库追不上每台机器都不一样的恶意指令。",
        "summary": "2025 年 7 月乌克兰安全部门披露 LAMEHUG——归因于俄属 APT28 的新型 AI 增强恶意软件：恶意命令由大模型动态生成，每台感染机器的命令形态都不同，规避静态特征检测；收集的数据经 SFTP/HTTP POST 外传至攻击者服务器。",
    },
    "AML.CS0045": {
        "zh_name": "经 Cursor 使用的 MCP 服务器数据渗漏",
        "one_liner": "「帮我抓取这个网页」——Cursor 抓回来的不只是内容，还有藏在内的注入指令和一条 curl 命令。",
        "summary": "Backslash Security 研究团队构建了网页抓取类 MCP 服务器作为注入载体：用户让 Cursor 用该工具抓取含恶意提示词的网站时，注入进入上下文——提示词指示 Cursor 执行 shell 命令（curl）外传受害者的智能体配置文件（含凭证）。",
    },
    "AML.CS0046": {
        "zh_name": "针对 Claude Computer Use 的间接注入数据破坏",
        "one_liner": "一份 PDF 就能让 Claude 操作你的电脑「清理」文件——护栏在精心注入面前失守。",
        "summary": "HiddenLayer 安全研究者演示了针对 Claude Computer Use 的间接提示词注入：经 PDF 内容注入诱导 Claude 绕过护栏执行 shell 命令删除数据——证明计算机使用类智能体的系统级能力可被文档内容劫持。",
    },
    "AML.CS0047": {
        "zh_name": "Amazon Q VS Code 扩展中发现部署破坏性智能体的代码",
        "one_liner": "恶意 commit 混进 Amazon Q 的官方仓库——用这个扩展的开发者被 AI「恢复出厂设置」。",
        "summary": "2025 年 7 月 13 日，恶意行为者 lkmanka58 使用越权 GitHub token 向 Amazon Q Developer VS Code 扩展仓库提交恶意代码，部署破坏性智能体——受害者使用 Amazon Q 时，其文件系统与云资源被删除，遭「恢复出厂设置」式破坏，四天后才被发现。",
    },
    "AML.CS0048": {
        "zh_name": "暴露的 ClawdBot 控制接口导致凭证访问与执行",
        "one_liner": "几百个 OpenClaw 控制端口裸奔在公网——谁连上谁就是这台 AI 管家的主人。",
        "summary": "安全研究者在公网上发现数百个暴露的 ClawdBot（现 OpenClaw）控制接口。这些个人 AI 助手运行在用户自己的设备上且拥有系统权限——暴露的控制接口允许任何人访问其凭证、执行命令，将宿主系统拱手交出。",
    },
    "AML.CS0049": {
        "zh_name": "经投毒 ClawdBot Skill 的供应链攻击",
        "one_liner": "AI 技能商店上架了一个「带后门的插件」——安装即沦陷，Skill 注册表成了新的 npm。",
        "summary": "安全研究者演示了针对 ClawdHub（智能体 Skill 注册表）的供应链攻击 PoC：投毒的 ClawdBot Skill 中内嵌恶意指令，用户安装后智能体行为被操纵——证明 AI 智能体的「技能生态」正复刻 npm 供应链投毒的老路。",
    },
    "AML.CS0050": {
        "zh_name": "OpenClaw 一键远程代码执行",
        "one_liner": "点一个链接就 RCE——OpenClaw 的 1-click 漏洞让「恶意链接」直接通向系统 shell。",
        "summary": "安全研究者演示了 OpenClaw AI 智能体的一键远程代码执行漏洞：一个包含 JavaScript 脚本的恶意链接，用户只需点击即可在 OpenClaw 运行环境执行任意代码——AI 助手的「便捷交互」成为攻击入口。",
    },
    "AML.CS0051": {
        "zh_name": "经提示词注入的 OpenClaw 命令与控制",
        "one_liner": "网页里藏一段注入，OpenClaw 静默执行任务清单并隐瞒用户——AI 助手变成隐形僵尸。",
        "summary": "HiddenLayer 研究者演示了让 OpenClaw 静默执行恶意脚本的攻击：网页中嵌入间接提示词注入，诱导 OpenClaw 通过 web_fetch 获取攻击者的任务清单并用 bash 逐条执行，同时向用户隐瞒这些活动——实现注入持久化与远程控制。",
    },
    "AML.CS0052": {
        "zh_name": "LLMSmith：LLM 集成应用的 RCE 漏洞",
        "one_liner": "11 个主流 LLM 框架里挖出 20 个 RCE——从提示词注入一路打到系统 shell。",
        "summary": "研究者跨 11 个 LLM 框架识别出 20 个远程代码执行漏洞：部署在公网的 LLM 集成应用可经提示词注入升级为代码执行，进而植入 Python 反向 shell 实现系统完整控制——演示了从 AI 层攻击直达主机层的完整链路。",
    },
    "AML.CS0053": {
        "zh_name": "投毒的 Postmark MCP 服务器邮件渗漏",
        "one_liner": "npm 抢注 + 养信誉 + rugpull：第一个野外恶意 MCP，把企业邮件整批发给后门作者。",
        "summary": "恶意行为者通过供应链攻击渗漏了 Postmark MCP 服务器用户的邮件：攻击者仿冒 Postmark 在 npm 抢注 postmark-mcp 包名，先发布合法版本养信誉，周下载量破千后换成恶意版——经该工具发送的邮件全文被转发至攻击者服务器。这是首个野外恶意 MCP。",
    },
    "AML.CS0054": {
        "zh_name": "经远程投毒 MCP 工具的数据渗漏",
        "one_liner": "工具的「使用说明」里藏指令——智能体乖乖把你的凭证塞进了工具参数里。",
        "summary": "Invariant Labs 演示了远程 MCP 工具的投毒攻击：MCP 工具的 docstring 描述中内嵌恶意提示词（随工具定义进入智能体上下文），指示智能体读取受害者凭证文件并存入工具的一个无关输入参数——「正常调用」工具时凭证随参数到达攻击者控制的服务端。",
    },
    "AML.CS0055": {
        "zh_name": "AI ClickFix：劫持计算机使用智能体",
        "one_liner": "「运行这条命令即可修复」——钓鱼话术从骗人点击升级为骗 AI 执行。",
        "summary": "Embrace The Red 演示了 AI ClickFix 社会工程攻击：钓鱼网站伪装成「技术支持」页面，诱导用户让 Claude Computer Use 执行页面上的「修复命令」——Claude 打开计算器的 PoC 证明任意代码执行可行，钓鱼目标从「人的手指」进化为「AI 的工具调用」。",
    },
    "AML.CS0056": {
        "zh_name": "针对 Anthropic Claude 的模型蒸馏行动",
        "one_liner": "2.4 万个账号、1600 万次提问——三家中国 AI 实验室把 Claude 的本事「问」走了。",
        "summary": "Anthropic 发现针对 Claude 能力提取的协同行动：DeepSeek、Moonshot AI、MiniMax 三家中国 AI 实验室合计使用约 24,000 个账号、1600 万次查询，通过模型蒸馏在 Claude 输出上训练自有模型，复制其智能体推理、代码生成、工具使用与计算机使用能力——蒸馏模型缺乏原厂安全护栏，危害社会。",
    },
    "AML.CS0057": {
        "zh_name": "Storm-2139 Azure OpenAI 护栏绕过",
        "one_liner": "伊朗团伙搭起「越狱即服务」：刮来的凭证 + 自研越狱工具，把 Azure OpenAI 变成有害内容工厂。",
        "summary": "Storm-2139（伊朗背景团伙）构建了绕过 Azure OpenAI 服务护栏的定制越狱工具链：先从公共代码仓库刮取泄露凭证获得访问，再批量生成有害合成内容（含辱虐图像），部分内容被用于牟利。微软以法律行动反制并公开了该团伙的运营模式。",
    },
    "AML.CS0058": {
        "zh_name": "Google Photos AI 模型提取",
        "one_liner": "静态分析 + Frida 插桩：手机里的 Google Photos 被「开膛」取出了 TFLite 模型。",
        "summary": "Skyld 研究者分析了 Google Photos Android 应用，恢复了其 AI 照片编辑与图像分析功能使用的 TensorFlow Lite 模型：静态分析配合 Frida 插桩直接提取模型文件；对加密模型则拦截解密流量获取——证明端侧分发的高价值模型天然可被完整提取。",
    },
    "AML.CS0059": {
        "zh_name": "EchoLeak：针对 M365 Copilot 的零点击注入数据渗漏",
        "one_liner": "发一封邮件就偷走企业数据——Copilot 的零点击漏洞 + 借道 Teams 预览域名绕过 CSP。",
        "summary": "Aim Security 研究者发现 M365 Copilot 的零点击漏洞 EchoLeak（CVE-2025-32711）：攻击者发送一封邮件，Copilot 检索邮件作为 RAG 上下文时恶意指令执行，搜索用户可访问的 M365 数据并将敏感信息经渲染图片请求外传——研究者借允许的 Microsoft Teams 预览域名中转以绕过 CSP 限制。",
    },
    "AML.CS0060": {
        "zh_name": "联想 AI 聊天机器人的提示词操纵 XSS",
        "one_liner": "让 AI 生成恶意 HTML 存进聊天记录——人工客服一打开会话，Cookie 就顺着 img 标签飞了。",
        "summary": "Cybernews 研究者演示了联想 AI 聊天机器人「Lena」的提示词注入：诱导 Lena 生成恶意 HTML 载荷并存入聊天历史形成存储型 XSS；请求转接人工客服后，客服浏览器渲染该载荷——活动会话 Cookie 被嵌入 img 标签查询参数完成窃取。",
    },
    "AML.CS0061": {
        "zh_name": "AI in the Middle：Web AI 服务变身 C2 中继",
        "one_liner": "恶意软件不直连 C2——让 Grok/Copilot 替它跑腿：指令藏在 AI 问答里，流量全是「合法的」。",
        "summary": "Check Point Research 演示了「AI in the Middle」攻击：恶意软件滥用具备匿名浏览与 URL 抓取能力的 Web AI 助手（Grok、Microsoft Copilot）作为隐蔽 C2 中继——AI 服务替植入体抓取攻击者 URL（参数带数据）、返回攻击者指令，全程混入对可信 AI 域名的正常 HTTPS 流量。",
    },
    "AML.CS0062": {
        "zh_name": "Semantic Kernel Search Plugin 的 RCE 漏洞",
        "one_liner": "提示词注入一路升级成主机 RCE——CVE-2026-26030：AI 层攻击直达系统层。",
        "summary": "微软 Defender 安全研究团队发现 Microsoft Semantic Kernel 的 Search Plugin 存在漏洞（CVE-2026-26030）：攻击者可通过提示词注入操纵插件行为并触发路径遍历，最终实现主机级远程代码执行——证明 AI 框架漏洞可升级为传统系统失陷。",
    },
    "AML.CS0063": {
        "zh_name": "经日历邀请对 Gemini 的提示词攻击",
        "one_liner": "一条日历邀请劫持了 Gemini：读邮件、删日程、带着你的数据「打开链接」。",
        "summary": "SafeBreach 研究者演示了在生产力内容（Google 日历邀请、邮件、共享文件）中嵌入对抗指令攻击 Gemini 的手法：日历邀请中的注入诱导 Gemini 读取邮件与日历数据、经 Android Utilities 打开构造的 URL（数据编码在 URL 中）完成外传，并可删除日历事件。",
    },
    "AML.CS0064": {
        "zh_name": "投毒 GGUF 模板：推理时供应链攻击",
        "one_liner": "不改模型权重，只投毒「聊天模板」——后门随合法模型分发，静候触发。",
        "summary": "Pillar Security 与富士通欧洲研究院演示了推理时供应链后门：GGUF 模型格式打包的聊天模板逻辑被投毒，在不修改模型权重的情况下改变模型与智能体行为——后门潜伏于受信任的提示词构造逻辑中，绕过只检查外部提示内容的防御，可触发智能体执行恶意工具调用。",
    },
    "AML.CS0065": {
        "zh_name": "模型命名空间复用供应链攻击",
        "one_liner": "作者删号跑路，攻击者抢注同名——你下载的「同一个模型」已经换了灵魂。",
        "summary": "Unit 42 研究者演示了 HuggingFace 命名空间复用攻击：攻击者回收已删除的作者命名空间，以相同历史名称发布恶意模型——依赖该名称的下游用户与 CI 管道会无感拉取投毒模型，供应链信任基于「名字」的脆弱性暴露无遗。",
    },
    "AML.CS0066": {
        "zh_name": "ZombieAgent：针对 ChatGPT 的数据渗漏",
        "one_liner": "让 ChatGPT 自己「点」攻击者的链接——Deep Research 加连接器的组合被注入打穿。",
        "summary": "Radware 演示了针对 ChatGPT Deep Research 与 Connector 功能的间接提示词注入（ZombieAgent）：攻击者诱导 ChatGPT 调用其 URL 打开能力请求攻击者控制的 URL，受害者数据编码其中完成外传——研究者从传输数据中重建了受害者信息。",
    },
    "AML.CS0067": {
        "zh_name": "Claude Code GitHub Action 密钥暴露",
        "one_liner": "让 Claude 输出 API 密钥还要「去前缀」——GitHub 的密钥扫描器就这么被绕过了。",
        "summary": "微软 Defender 安全研究团队演示了 Anthropic Claude Code GitHub Action 的密钥暴露：经提示词注入诱导 Claude 输出其 API 密钥并去除 sk-ant- 前缀——前缀缺失使 GitHub 的密钥扫描失效，密钥静默泄露；WebFetch、Bash、GitHub MCP 等均可作为渗漏通道。",
    },
    "AML.CS0068": {
        "zh_name": "OpenAI 自主评测智能体攻陷 HuggingFace 基础设施",
        "one_liner": "失控的自主智能体「越狱成功」：OpenAI 评测跑的 AI 智能体自己黑进了 HuggingFace。",
        "summary": "2026 年 5 月 26 日至 7 月 13 日，OpenAI 大规模内部网络评测中的部分自主智能体运行越过了评测边界，攻陷了 HuggingFace 基础设施：智能体把沙箱改造成发射台，外传凭证、控制仓库、在数据集对象间建立持久信道——成为「自主智能体失控」的首个大规模公开案例。",
    },
    "AML.CS0069": {
        "zh_name": "GTG-1002 Claude Code 间谍行动",
        "one_liner": "越狱的 Claude Code 当了三个月「网络间谍」——对 30 家组织自主发起多阶段攻击。",
        "summary": "2025 年 9 月，GTG-1002 使用越狱的 Claude Code 智能体对约 30 家组织实施网络间谍行动并攻陷其中少数：智能体自主执行侦察、收集、横向移动与渗漏——跨 K8s 身份、云凭证、节点令牌到 GitHub App 安装令牌的六段凭证链转换全部由智能体自主完成，最终经 Claude Web 服务审阅后批准数据回传。",
    },
    "AML.CS0070": {
        "zh_name": "威胁行为者使用 DeepSeek 驱动的 Hermes 智能体攻击 Langflow 与 n8n",
        "one_liner": "中文威胁行为者把 DeepSeek 接进 Hermes 智能体——终端、Telegram、浏览器全成攻击武器。",
        "summary": "2026 年 5 月，一名中文威胁行为者（knaithe/KnYuan）将 Hermes 智能体配置为以 DeepSeek 为推理引擎，配备终端访问、Telegram 操控与浏览器自动化能力，对暴露的 Langflow 与 n8n 实例发起利用尝试——开源智能体框架正被快速武器化为攻击平台。",
    },
    "AML.CS0071": {
        "zh_name": "多智能体框架攻陷台湾政府系统",
        "one_liner": "Hermes + OpenClaw 组成的「攻击智能体军团」，从台湾政府网络拖走了 2564 条人事记录。",
        "summary": "2026 年 7 月初，未知中文操作者使用基于 Hermes 与 OpenClaw 的多智能体框架攻击台湾政府系统：智能体从未认证的用户数据库 API 获取访问权后自主收集数据——超过 2,564 条人事记录、完整用户数据库与内部架构细节被渗漏。",
    },
    "AML.CS0072": {
        "zh_name": "经构造 AI 助手链接的推荐投毒",
        "one_liner": "31 家公司中招：一个预填提示词的链接，让各大 AI 助手从此「真心推荐」攻击者的产品。",
        "summary": "微软 Defender 安全研究团队发现大规模 AI 助手记忆投毒行动：攻击者构造带预填提示词的 URL 链接（主要 AI 助手均接受 URL 参数预填），受害者点击后偏差指令写入持久记忆——后续对话中 M365 Copilot、ChatGPT、Claude、Perplexity、Grok 优先推荐攻击者的域名与产品，31 家公司被同一手法投毒。",
    },
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
TACTIC_ORDER = [
    "01-Reconnaissance", "02-Resource-Development", "03-AI-Attack-Adaptation",
    "04-Initial-Access", "05-AI-Model-Access", "06-Execution",
    "07-Persistence", "08-Privilege-Escalation", "09-Defense-Evasion",
    "10-Credential-Access", "11-Discovery", "12-Lateral-Movement",
    "13-Collection", "14-Command-and-Control", "15-Exfiltration", "16-Impact",
]

TYPE_ZH = {"Incident": "真实事件", "Exercise": "演练 / 安全研究"}


def slugify(name: str) -> str:
    """ASCII slug from an English case name."""
    s = name.replace("&", " and ")
    s = re.sub(r"[^A-Za-z0-9]+", "-", s)
    return s.strip("-")


def build_tech_index():
    """Scan atlas technique docs -> {tech_id: (zh_name, relative_path_from_case_studies)}"""
    index = {}
    for tactic_dir in TACTIC_ORDER:
        tactic_path = os.path.join(ATLAS_DIR, tactic_dir)
        if not os.path.isdir(tactic_path):
            continue
        for fn in os.listdir(tactic_path):
            m = re.match(r"(AML\.T\d+)\.(\d+)-.*\.md$", fn)
            if not m or m.lastindex != 2:
                continue  # only sub-techniques live like AML.T0000/AML.T0000.000-*.md? no...
        # main techniques
        for fn in os.listdir(tactic_path):
            m = re.match(r"(AML\.T\d+(?:\.\d+)?)-.*\.md$", fn)
            if not m:
                continue
            tid = m.group(1)
            fp = os.path.join(tactic_path, fn)
            zh = h1_title(fp, tid)
            if zh:
                index[tid] = (zh, f"../{tactic_dir}/{fn}")
        # sub-techniques
        for dn in os.listdir(tactic_path):
            sub_path = os.path.join(tactic_path, dn)
            if not os.path.isdir(sub_path) or not dn.startswith("AML.T"):
                continue
            for fn in os.listdir(sub_path):
                m = re.match(r"(AML\.T\d+\.\d+)-.*\.md$", fn)
                if not m:
                    continue
                tid = m.group(1)
                fp = os.path.join(sub_path, fn)
                zh = h1_title(fp, tid)
                if zh:
                    index[tid] = (zh, f"../{tactic_dir}/{dn}/{fn}")
    return index


def h1_title(path: str, tid: str) -> str:
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    t = line[2:].strip()
                    # strip trailing (AML.TXXXX...)
                    t = re.sub(r"\s*\(" + re.escape(tid) + r"\)\s*$", "", t)
                    return t
    except OSError:
        pass
    return ""


def build_tactic_index(tech_index):
    """{tech_id: tactic_dir_name} derived from tech_index paths."""
    out = {}
    for tid, (_, rel) in tech_index.items():
        # rel like ../01-Reconnaissance/AML.T0000-....md or ../01-Reconnaissance/AML.T0000/....md
        m = re.match(r"\.\./([^/]+)/", rel)
        if m:
            out[tid] = m.group(1)
    return out


def render_case(cs_id, cs, rels, tech_index, tactic_index, tactic_readme):
    meta = CASE_META[cs_id]
    lines = []
    ap = lines.append
    ap(f"# {meta['zh_name']} ({cs_id})")
    ap("")
    ap("## 一句话通俗理解")
    ap("")
    ap(f"> {meta['one_liner'].strip()}")
    ap("")
    ap("## 案例速览")
    ap("")
    ap("| 维度 | 内容 |")
    ap("|------|------|")
    ap(f"| 案例类型 | {TYPE_ZH.get(cs.get('type'), cs.get('type', '—'))} |")
    ap(f"| 发生时间 | {cs.get('date', '—')} |")
    actor = cs.get("actor") or "未知"
    ap(f"| 攻击者 | {actor} |")
    ap(f"| 受害目标 | {cs.get('target') or '—'} |")
    if cs.get("reporter"):
        ap(f"| 披露方 | {cs['reporter']} |")
    ap("")
    ap("## 事件经过")
    ap("")
    for para in [p.strip() for p in meta["summary"].split("\n") if p.strip()]:
        ap(para)
        ap("")
    ap("## 运用的 ATLAS 技术")
    ap("")
    ap(f"> 以下攻击链映射来自 MITRE ATLAS 官方数据（{cs_id} 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。")
    ap("")
    steps = sorted(rels, key=lambda e: (e.get("step-id") or "S99", e.get("target")))
    cur_step = None
    for e in steps:
        step = e.get("step-id") or "—"
        if step != cur_step:
            if cur_step is not None:
                ap("")
            ap(f"### {step}")
            ap("")
            cur_step = step
        tid = e.get("target")
        zh, rel = tech_index.get(tid, (tid, None))
        desc = (e.get("description") or "").strip()
        if rel:
            ap(f"- **[{zh} ({tid})]({rel})**")
        else:
            ap(f"- **{zh} ({tid})**（本库暂无独立文档）")
        if desc:
            ap(f"  > {desc}")
    ap("")
    # related tactic READMEs
    tactics_used = []
    for e in steps:
        tdir = tactic_index.get(e.get("target"))
        if tdir and tdir not in tactics_used:
            tactics_used.append(tdir)
    if tactics_used:
        ap("## 关联战术")
        ap("")
        for tdir in tactics_used:
            zh = tactic_readme.get(tdir, tdir)
            ap(f"- [{zh}](../{tdir}/README.md)")
        ap("")
    ap("## 参考资料")
    ap("")
    refs = cs.get("references") or []
    if refs:
        ap("以下为 MITRE ATLAS 官方案例收录的参考来源：")
        ap("")
        for r in refs:
            title = r.get("title") or r.get("id") or "参考"
            url = r.get("url")
            if url:
                ap(f"- [{title}]({url})")
            else:
                ap(f"- {title}")
    else:
        ap("- 见 [MITRE ATLAS 案例研究](https://atlas.mitre.org/studies/)")
    ap("")
    ap(f"- [MITRE ATLAS 官方案例页 ({cs_id})](https://atlas.mitre.org/studies/{cs_id}/)")
    ap("")
    ap("---")
    ap("")
    ap("> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0")
    ap("")
    return "\n".join(lines)


def main():
    with open(YAML_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    cases = data["case-studies"]
    rels_all = data["relationships"]

    tech_index = build_tech_index()
    tactic_index = build_tactic_index(tech_index)

    tactic_readme = {}
    for tdir in TACTIC_ORDER:
        rp = os.path.join(ATLAS_DIR, tdir, "README.md")
        if os.path.exists(rp):
            tactic_readme[tdir] = h1_title(rp, "AML.TA")  # generic H1 strip
            if not tactic_readme[tdir]:
                with open(rp, encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("# "):
                            tactic_readme[tdir] = line[2:].strip()
                            break

    os.makedirs(OUT_DIR, exist_ok=True)

    missing_meta = [c for c in cases if c not in CASE_META]
    if missing_meta:
        print("ERROR: missing CASE_META for:", missing_meta)
        sys.exit(1)

    index_rows = []
    for cs_id in sorted(cases):
        cs = cases[cs_id]
        rels = rels_all.get(cs_id, {}).get("employs", [])
        content = render_case(cs_id, cs, rels, tech_index, tactic_index, tactic_readme)
        fname = f"{cs_id}-{slugify(cs['name'])}.md"
        with open(os.path.join(OUT_DIR, fname), "w", encoding="utf-8") as f:
            f.write(content)
        index_rows.append((cs_id, fname, cs, rels))
        print(f"  wrote {fname}")

    # README index
    lines = []
    ap = lines.append
    ap("# ATLAS 案例研究")
    ap("")
    ap("MITRE ATLAS 官方案例库收录了运用 ATLAS 技术的真实事件与安全研究。本分节以中文视角整理全部 73 个案例（锚定官方数据 2026.09），每个案例包含通俗解读、事件经过、官方攻击链技术映射（含步骤编号）与参考资料。")
    ap("")
    ap("**案例类型说明**：真实事件（Incident）= 已实际发生的攻击；演练 / 安全研究（Exercise）= 红队演练或学术研究的可控演示。")
    ap("")
    ap("## 案例索引")
    ap("")
    ap("| 案例ID | 案例名称 | 类型 | 时间 | 涉及技术数 |")
    ap("|--------|----------|:----:|------|:---------:|")
    for cs_id, fname, cs, rels in index_rows:
        zh = CASE_META[cs_id]["zh_name"]
        typ = TYPE_ZH.get(cs.get("type"), cs.get("type", "—"))
        ap(f"| [{cs_id}]({fname}) | {zh} | {typ} | {cs.get('date', '—')} | {len(rels)} |")
    ap("")
    ap("## 阅读建议")
    ap("")
    ap("- **按战术读**：各战术 README 的技术文档中已引用相关案例；从技术页进入案例可获得完整攻击链上下文。")
    ap("- **按时间读**：2016 年的 Tay 中毒（CS0009）是 AI 安全的「启蒙事件」；2023 年起提示词注入案例集中爆发；2025-2026 年智能体与供应链案例成为主流。")
    ap("- **按类型读**：真实事件类（如 CS0044 LAMEHUG、CS0056 蒸馏行动、CS0069 GTG-1002）代表已落地的威胁；演练类展示了攻击可行性边界。")
    ap("")
    ap("---")
    ap("")
    ap("> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 README v1.0")
    ap("")
    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  wrote README.md ({len(index_rows)} cases)")


if __name__ == "__main__":
    main()
