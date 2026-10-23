# PyTorch 依赖链失陷 (AML.CS0015)

## 一句话通俗理解

> 恶意包混入 PyTorch 每日构建版，收集的敏感信息经加密 DNS 查询悄悄送出门。

## 案例速览

| 维度 | 内容 |
|------|------|
| 案例类型 | 真实事件 |
| 发生时间 | 2022-12-25 |
| 攻击者 | Unknown |
| 受害目标 | PyTorch |
| 披露方 | PyTorch |

## 事件经过

2022 年 12 月 25 至 30 日，PyTorch 预发布版（torch-nightly）的 Linux 包因恶意二进制依赖（triton 包的抢注版本）被投毒。恶意样本收集 /etc/resolv.conf 等系统信息，并通过加密 DNS 查询上传至攻击者域名，波及大量运行 nightly 版本的 ML 开发环境。

## 运用的 ATLAS 技术

> 以下攻击链映射来自 MITRE ATLAS 官方数据（AML.CS0015 的 `employs` 关系），按官方步骤编号排序；技术名称链接至本库对应技术文档，引用文字为官方对本次运用的描述。

### S00

- **[AI 软件 (AML.T0010.001)](../04-Initial-Access/AML.T0010/AML.T0010.001-AI-Software.md)**
  > A malicious dependency package named `torchtriton` was uploaded to the PyPI code repository with the same package name as a package shipped with the PyTorch-nightly build. This malicious package contained additional code that uploads sensitive data from the machine.
The malicious `torchtriton` package was installed instead of the legitimate one because PyPI is prioritized over other sources. See more details at [this GitHub issue](https://github.com/pypa/pip/issues/8606).

### S01

- **[来自本地系统的数据 (AML.T0037)](../13-Collection/AML.T0037-Data-from-Local-System.md)**
  > The malicious package surveys the affected system for basic fingerprinting info (such as IP address, username, and current working directory), and steals further sensitive data, including:
- nameservers from `/etc/resolv.conf`
- hostname from `gethostname()`
- current username from `getlogin()`
- current working directory name from `getcwd()`
- environment variables
- `/etc/hosts`
- `/etc/passwd`
- the first 1000 files in the user's `$HOME` directory
- `$HOME/.gitconfig`
- `$HOME/.ssh/*.`

### S02

- **[通过网络手段渗漏 (AML.T0025)](../15-Exfiltration/AML.T0025-Exfiltration-via-Cyber-Means.md)**
  > All gathered information, including file contents, is uploaded via encrypted DNS queries to the domain `*[dot]h4ck[dot]cfd`, using the DNS server `wheezy[dot]io`.

## 关联战术

- [初始访问 (AML.TA0004)](../04-Initial-Access/README.md)
- [收集 (AML.TA0009)](../13-Collection/README.md)
- [数据渗漏 (AML.TA0010)](../15-Exfiltration/README.md)

## 参考资料

以下为 MITRE ATLAS 官方案例收录的参考来源：

- [PyTorch statement on compromised dependency](https://pytorch.org/blog/compromised-nightly-dependency/)
- [Analysis by BleepingComputer](https://www.bleepingcomputer.com/news/security/pytorch-discloses-malicious-dependency-chain-compromise-over-holidays/)

- [MITRE ATLAS 官方案例页 (AML.CS0015)](https://atlas.mitre.org/studies/AML.CS0015/)

---

> **版本**: ATLAS 2026.09 | **更新**: 2026-10-24 | **模板**: ATLAS 案例研究 v1.0
