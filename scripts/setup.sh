#!/bin/bash
# ============================================================
# ATT&CK 知识库 - mdBook 本地开发环境设置脚本
# ============================================================
# 用法: bash scripts/setup.sh
# ============================================================
set -euo pipefail

echo "=========================================="
echo " ATT&CK 知识库 - 本地环境设置"
echo "=========================================="
echo ""

# --- 1. 安装依赖 ---
echo "[1/4] 检查 Rust 工具链..."
if ! command -v cargo &> /dev/null; then
    echo "错误: 未找到 Rust/Cargo。请先安装 Rust: https://rustup.rs/"
    exit 1
fi

# --- 2. 安装 mdbook 及插件 ---
echo "[2/4] 安装 mdbook 及插件..."
cargo install mdbook 2>/dev/null || echo "  mdbook 已安装"
cargo install mdbook-mermaid 2>/dev/null || echo "  mdbook-mermaid 已安装"

# --- 3. 配置 Catppuccin 主题 ---
echo "[3/4] 配置 Catppuccin 主题..."
mkdir -p theme

# 下载 Catppuccin CSS
if [ ! -f theme/catppuccin.css ]; then
    echo "  -> 下载 catppuccin.css..."
    curl -sL https://github.com/catppuccin/mdBook/releases/latest/download/catppuccin.css \
        -o theme/catppuccin.css
    chmod 644 theme/catppuccin.css
    echo "  ✓ catppuccin.css 已下载"
else
    echo "  ✓ catppuccin.css 已存在"
fi

# 初始化默认主题（获取 index.hbs）
if [ -f book.toml ] && [ ! -f theme/index.hbs ]; then
    echo "  -> 初始化默认主题模板..."
    mdbook init --theme --force 2>/dev/null || echo "  (主题目录已存在)"
fi

# 修改 index.hbs 以支持 Catppuccin 主题切换
if [ -f theme/index.hbs ]; then
    if grep -q 'id="latte"' theme/index.hbs 2>/dev/null; then
        echo "  ✓ index.hbs 已配置 Catppuccin 主题"
    else
        echo "  -> 修改 index.hbs 添加 Catppuccin 主题按钮..."
        cp theme/index.hbs theme/index.hbs.bak
        
        # 替换标准主题按钮为 Catppuccin 主题
        sed -i 's/id="light"/id="latte"/g' theme/index.hbs
        sed -i 's/>Light</>Latte</g' theme/index.hbs
        sed -i 's/id="rust"/id="frappe"/g' theme/index.hbs
        sed -i 's/>Rust</>Frappé</g' theme/index.hbs
        sed -i 's/id="coal"/id="macchiato"/g' theme/index.hbs
        sed -i 's/>Coal</>Macchiato</g' theme/index.hbs
        sed -i 's/id="navy"/id="mocha"/g' theme/index.hbs
        sed -i 's/>Navy</>Mocha</g' theme/index.hbs
        sed -i '/id="ayu"/d' theme/index.hbs
        echo "  ✓ index.hbs 已更新 (备份: theme/index.hbs.bak)"
    fi
fi

# --- 4. 安装 Mermaid ---
echo "[4/4] 安装 Mermaid 插件资源..."
mdbook-mermaid install . 2>/dev/null || true

# 将 mermaid 文件移到 theme 目录
for f in mermaid.min.js mermaid-init.js; do
    if [ -f "$f" ]; then
        mv "$f" theme/
        echo "  ✓ $f 已移动到 theme/"
    fi
done

echo ""
echo "=========================================="
echo " 设置完成!"
echo "=========================================="
echo ""
echo "可用的命令:"
echo "  bash scripts/build.sh              # 预处理 + 构建 (推荐)"
echo "  bash scripts/build.sh serve        # 预处理 + 本地预览"
echo "  mdbook serve                       # 直接预览 (不预处理)"
echo "  mdbook build                       # 直接构建 (不预处理)"
echo ""
echo "注意: 修改 README.md 后，务必先运行 scripts/preprocess-md.py"
echo "推荐使用 scripts/build.sh 替代直接 mdbook 命令"
echo ""
