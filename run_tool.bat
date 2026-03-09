@echo off
chcp 65001 >nul
echo ========================================
echo PDF安全工具 - Windows 11
echo ========================================
echo.

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到Python
    echo 请安装Python 3.8+ 并确保已添加到PATH
    pause
    exit /b 1
)

REM 检查依赖
python -c "import PyPDF2, reportlab" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  正在安装依赖库...
    pip install PyPDF2 reportlab --quiet
)

echo ✅ 环境检查完成
echo.

REM 运行工具
python pdf_secure_tool.py %*

if errorlevel 1 (
    echo.
    echo ❌ 工具执行失败
    pause
) else (
    echo.
    echo ✅ 操作完成
)