#!/bin/bash
# ============================================================
# ATT&CK 知识库 - 构建脚本
# ============================================================
# 用法:
#   bash scripts/build.sh              # 构建
#   bash scripts/build.sh serve        # 本地预览 (含自动重建)
#   bash scripts/build.sh build        # 仅构建 (默认)
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "=========================================="
echo " ATT&CK 知识库 - 构建"
echo "=========================================="

# 预处理由 book.toml 中配置的 preprocessor.attck-preprocess 自动执行:
#   - gen-summary.py  → 自动生成 SUMMARY.md
#   - preprocess-md.py → 修正 README.md 链接

# 1. 确定命令
CMD="${1:-build}"
if [ "$CMD" != "build" ] && [ "$CMD" != "serve" ] && [ "$CMD" != "watch" ]; then
    echo "用法: $0 [build|serve|watch]"
    exit 1
fi

# 2. 执行 mdbook（自动触发预处理器）
echo "[1/2] 执行 mdbook $CMD..."
mdbook "$CMD"

echo "[2/2] 完成"
