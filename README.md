---
status: 【已完成】
---

# ATT&CK 知识库

基于 MITRE ATT&CK® v19 Enterprise 矩阵的知识库，覆盖全部 15 个战术（Tactics）和 254 个技术（Techniques），提供技术原理、真实案例和检测建议。

## 战术索引

| 序号  | 战术名称  | TA ID  | 技术数 | 目录                                                             |
| :-: | ----- | :----: | :-: | -------------------------------------------------------------- |
| 01  | 侦察    | TA0043 | 14  | [01-Reconnaissance](./src/01-Reconnaissance/README.md)         |
| 02  | 资源开发  | TA0042 |  9  | [02-Resource-Development](./src/02-Resource-Development/README.md) |
| 03  | 初始访问  | TA0001 | 11  | [03-Initial-Access](./src/03-Initial-Access/README.md)         |
| 04  | 执行    | TA0002 | 16  | [04-Execution](./src/04-Execution/README.md)                   |
| 05  | 持久化   | TA0003 | 25  | [05-Persistence](./src/05-Persistence/README.md)               |
| 06  | 权限提升  | TA0004 | 14  | [06-Privilege-Escalation](./src/06-Privilege-Escalation/README.md) |
| 07  | 隐蔽    | TA0005 | 25  | [07-Stealth](./src/07-Stealth/README.md)                       |
| 08  | 防御削弱  | TA0112 | 25  | [08-Defense-Impairment](./src/08-Defense-Impairment/README.md) |
| 09  | 凭证访问  | TA0006 | 17  | [09-Credential-Access](./src/09-Credential-Access/README.md)   |
| 10  | 发现    | TA0007 | 35  | [10-Discovery](./src/10-Discovery/README.md)                   |
| 11  | 横向移动  | TA0008 | 11  | [11-Lateral-Movement](./src/11-Lateral-Movement/README.md)     |
| 12  | 收集    | TA0009 | 17  | [12-Collection](./src/12-Collection/README.md)                 |
| 13  | 命令与控制 | TA0011 | 18  | [13-Command-and-Control](./src/13-Command-and-Control/README.md) |
| 14  | 渗漏    | TA0010 |  9  | [14-Exfiltration](./src/14-Exfiltration/README.md)             |
| 15  | 影响    | TA0040 | 11  | [15-Impact](./src/15-Impact/README.md)                         |

## 文章结构规范

每篇技术文章遵循以下结构：

```markdown
# [技术名称] (T####)

## 技术描述
ATT&CK 官方描述 + 技术原理解析

## 子技术（如有）
- T####.001 - [名称]
- T####.002 - [名称]

## 真实案例
### 案例1：[APT组织/攻击活动名称]
- **时间**: 20XX年
- **目标**: [行业/地区]
- **手法**: [具体操作描述]
- **链接**: [外部参考资料URL]

### 案例2：[APT组织/攻击活动名称]
...

## 检测建议
- [检测方法1]
- [检测方法2]

## 缓解措施
- [缓解措施1]
- [缓解措施2]

## 参考资料
- [MITRE ATT&CK 官方](https://attack.mitre.org/techniques/T####/)
- [外部参考1](URL)
- [外部参考2](URL)
```

## 数据来源

- [MITRE ATT&CK® Enterprise Matrix v19](https://attack.mitre.org/matrices/enterprise/)
- [MITRE ATT&CK STIX Data](https://github.com/mitre-attack/attack-stix-data)
- 互联网公开威胁情报、安全研究报告、APT 分析报告

---
