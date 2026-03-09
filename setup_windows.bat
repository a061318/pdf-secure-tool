@echo off
echo ========================================
echo PDF安全工具 - Windows 11 安装脚本
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到Python，请先安装Python 3.8+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ 检测到Python
python --version

echo.
echo 正在安装依赖库...
echo.

REM 安装依赖
pip install PyPDF2 reportlab

REM 可选安装高级功能
echo.
set /p install_advanced=是否安装高级功能(pikepdf)? (y/n): 
if /i "%install_advanced%"=="y" (
    pip install pikepdf
)

echo.
echo 创建桌面快捷方式...
echo.

REM 创建批处理文件
echo @echo off > "%~dp0pdf_tool.bat"
echo python "%~dp0pdf_secure_tool.py" %%* >> "%~dp0pdf_tool.bat"

REM 创建使用说明
echo.
echo ========================================
echo ✅ 安装完成！
echo ========================================
echo.
echo 使用方法:
echo 1. 打开命令提示符或PowerShell
echo 2. 切换到工具目录: cd "%~dp0"
echo 3. 运行工具: python pdf_secure_tool.py --help
echo.
echo 或者直接运行: pdf_tool.bat --help
echo.
echo 示例:
echo   pdf_tool.bat watermark input.pdf output.pdf "机密文件"
echo   pdf_tool.bat encrypt input.pdf output.pdf mypassword
echo.
pause