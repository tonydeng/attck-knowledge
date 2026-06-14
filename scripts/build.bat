@echo off
chcp 65001 >nul
REM ============================================================
REM ATT&CK 知识库 - 构建脚本 (Windows)
REM ============================================================
REM 用法:
REM   scripts\build.bat              REM 构建 (build + CJK 搜索优化)
REM   scripts\build.bat serve        REM 本地预览 (build + CJK 搜索优化 + serve)
REM   scripts\build.bat build        REM 仅构建 (默认)
REM ============================================================

setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
pushd "%SCRIPT_DIR%.."

echo ==========================================
echo  ATT^&CK 知识库 - 构建
echo ==========================================

REM 预处理由 book.toml 中配置的 preprocessor.attck-preprocess 自动执行:
REM   - gen-summary.py  自动生成 SUMMARY.md
REM   - preprocess-md.py 修正 README.md 链接

REM 1. 确定命令
set "CMD=%~1"
if "%CMD%"=="" set "CMD=build"
if not "%CMD%"=="build" if not "%CMD%"=="serve" if not "%CMD%"=="watch" (
    echo 用法: %0 [build^|serve^|watch]
    exit /b 1
)

if "%CMD%"=="build" (
    REM build 模式: mdbook build + CJK 搜索优化
    echo [1/2] 执行 mdbook build...
    mdbook build

    echo [2/2] 优化 CJK 搜索索引...
    node scripts\cjk-search.js
) else (
    REM serve / watch 模式: 仅执行 mdbook（CJK 优化仅适用于完整构建）
    echo [1/1] 执行 mdbook %CMD%（CJK 搜索优化仅在 build 模式下运行）...
    mdbook %CMD%
)

echo [32m完成[0m

popd
