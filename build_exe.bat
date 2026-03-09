@echo off
chcp 65001 >nul
echo ========================================
echo PDF安全工具 - EXE打包脚本
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

echo ✅ 检测到Python
python --version

echo.
echo 正在安装打包工具...
echo.

REM 安装PyInstaller
pip install pyinstaller --quiet

echo.
echo 正在安装依赖库...
echo.

REM 安装PDF处理库
pip install PyPDF2 reportlab --quiet

echo.
echo 正在打包EXE文件...
echo.

REM 使用PyInstaller打包
pyinstaller --onefile ^
            --windowed ^
            --name "PDF安全工具" ^
            --icon "icon.ico" ^
            --add-data "icon.ico;." ^
            --hidden-import PyPDF2 ^
            --hidden-import reportlab ^
            --hidden-import reportlab.lib ^
            --hidden-import reportlab.pdfgen ^
            pdf_secure_gui.py

if errorlevel 1 (
    echo.
    echo ❌ 打包失败
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ EXE打包成功！
echo ========================================
echo.
echo 生成的EXE文件位置:
echo   dist\PDF安全工具.exe
echo.
echo 文件大小信息:
dir "dist\PDF安全工具.exe"
echo.
echo 使用方法:
echo   1. 将 "PDF安全工具.exe" 复制到任何位置
echo   2. 双击运行即可
echo   3. 无需安装Python或其他依赖
echo.
echo 功能说明:
echo   • 添加文字水印到PDF
echo   • PDF文件加密
echo   • 批量处理文件夹
echo   • 图形界面操作
echo.
pause