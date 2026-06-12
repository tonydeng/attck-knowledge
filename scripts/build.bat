@echo off
chcp 65001 >nul
REM ============================================================
REM ATT&CK 知识库 - 构建脚本 (Windows)
REM ============================================================
REM 用法:
REM   scripts\build.bat              REM 构建
REM   scripts\build.bat serve        REM 本地预览
REM   scripts\build.bat build        REM 仅构建 (默认)
REM ============================================================

setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
pushd "%SCRIPT_DIR%.."

echo ==========================================
echo  ATT^&CK 知识库 - 构建
echo ==========================================

REM 1. 预处理 Markdown
echo [1/3] 预处理 Markdown 文件...
python "%SCRIPT_DIR%preprocess-md.py"
if %ERRORLEVEL% neq 0 (
    echo 预处理失败!
    exit /b 1
)

REM 2. 确定命令
set "CMD=%~1"
if "%CMD%"=="" set "CMD=build"
if not "%CMD%"=="build" if not "%CMD%"=="serve" if not "%CMD%"=="watch" (
    echo 用法: %0 [build^|serve^|watch]
    exit /b 1
)

REM 3. 执行 mdbook
echo [2/3] 执行 mdbook %CMD%...
mdbook %CMD%

echo [3/3] 完成

popd
