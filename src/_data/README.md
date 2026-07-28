# ATT&CK 知识库数据目录

> 本目录存放审计工具自动生成的数据文件，**禁止手工编辑**。

## 数据文件说明

### `_local_scan.json`

- **生成命令**：`python _tools/attack_mapping.py scan`
- **内容**：扫描 `知识库/` 下 15 个战术目录的所有 `.md` 文件 frontmatter，提取技术 ID、名称、状态等元数据
- **结构**：
  ```json
  {
    "01-Reconnaissance": {
      "tactic_dir": "01-Reconnaissance",
      "parent_count": 12,
      "subtech_count": 34,
      "parents": [
        {
          "file": "T1595-Active-Scanning.md",
          "path": "01-Reconnaissance/T1595-Active-Scanning.md",
          "attack_id": "T1595",
          "attack_name_en": "Active Scanning",
          "attack_name_cn": "主动扫描",
          "tactic_id": "TA0043",
          "sub_techniques_count": "3",
          "status": "【已完成】"
        }
      ],
      "subtechs": [...]
    }
  }
  ```
- **当前规模**：约 409 KB，256 父技术 / 632 子技术

### `_mitre_official.json`

- **生成命令**：`python _tools/attack_mapping.py fetch`
- **内容**：从 `https://attack.mitre.org/tactics/{TID}/` 抓取 15 个战术页 HTML，解析父技术/子技术清单
- **结构**：
  ```json
  {
    "TA0043": {
      "tactic_id": "TA0043",
      "tactic_name_en": "Reconnaissance",
      "parent_techniques": [
        {
          "id": "T1595",
          "name_en": "Active Scanning",
          "subtechniques": [
            {"id": "T1595.001", "name_en": "Scanning IP Blocks"}
          ]
        }
      ]
    }
  }
  ```
- **当前规模**：约 98 KB，254 父技术 / 618 子技术（MITRE ATT&CK v19.1）

## 数据来源

| 数据 | 来源 | 更新方式 |
|------|------|---------|
| `_local_scan.json` | 本地知识库 frontmatter | 运行 `scan` 子命令 |
| `_mitre_official.json` | attack.mitre.org 官方战术页 | 运行 `fetch` 子命令 |

## 版本信息

- **MITRE ATT&CK 版本**：v19.1
- **v19.1 重要变化**：原 TA0005 (Defense Evasion) 拆分为 TA0005 (Stealth) + TA0112 (Defense Impairment)
- **最后更新**：2026-07-24

## 注意事项

- ❌ **禁止手工编辑**这两个 JSON 文件，它们由工具自动生成
- ✅ 删除后可由 `scan` / `fetch` 重新生成
- ⚠️ MITRE 版本升级后，需重新运行 `fetch` 刷新官方数据
- ⚠️ 本地知识库结构变更（新增/删除/重命名文件）后，需重新运行 `scan` 刷新本地数据
