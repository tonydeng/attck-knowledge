#!/bin/bash
# ============================================================
# ATT&CK 知识库 - 构建脚本
# ============================================================
# 用法:
#   bash scripts/build.sh              # 构建 (build + CJK 搜索优化)
#   bash scripts/build.sh serve        # 本地预览 (build + CJK 搜索优化 + serve)
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

# build 模式: 链接检查 + SUMMARY 预生成 + mdbook build + CJK 搜索优化
if [ "$CMD" = "build" ]; then
    echo "[1/4] 检查内部链接..."
    python scripts/check-links.py

    # SUMMARY.md 必须在 mdbook 启动前生成：构建内预处理器只重写磁盘文件，
    # 不修改管道中的 book 结构，新增文档要等下一次构建才会被渲染。
    echo "[2/4] 预生成 SUMMARY.md..."
    python scripts/gen-summary.py

    echo "[3/4] 执行 mdbook build..."
    mdbook build

    echo "[4/4] 优化 CJK 搜索索引..."
    node scripts/cjk-search.js

    echo "✅ 完成"
    exit 0
fi

# serve / watch 模式: 仅执行 mdbook（CJK 优化仅适用于完整构建）
echo "[1/1] 执行 mdbook $CMD（CJK 搜索优化仅在 build 模式下运行）..."
mdbook "$CMD"

echo "✅ 完成"
