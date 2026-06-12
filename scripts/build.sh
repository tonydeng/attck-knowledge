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

# 1. 预处理 Markdown（修正 README.md 链接兼容性问题）
echo "[1/3] 预处理 Markdown 文件..."
python3 "$SCRIPT_DIR/preprocess-md.py"

# 2. 确定命令
CMD="${1:-build}"
if [ "$CMD" != "build" ] && [ "$CMD" != "serve" ] && [ "$CMD" != "watch" ]; then
    echo "用法: $0 [build|serve|watch]"
    exit 1
fi

# 3. 执行 mdbook
echo "[2/3] 执行 mdbook $CMD..."
mdbook "$CMD"

echo "[3/3] 完成"
