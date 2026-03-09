#!/bin/bash
# Docker构建脚本 - 在任何有Docker的系统上生成EXE

echo "PDF安全工具 - EXE构建脚本"
echo "=========================="

# 检查Docker
if ! command -v docker &> /dev/null; then
    echo "❌ 未安装Docker，请先安装Docker"
    echo "安装指南: https://docs.docker.com/get-docker/"
    exit 1
fi

echo "✅ Docker已安装"

# 创建dist目录
mkdir -p dist

echo "正在构建Docker镜像..."
docker build -t pdf-tool-builder .

if [ $? -ne 0 ]; then
    echo "❌ Docker构建失败"
    exit 1
fi

echo "✅ Docker镜像构建成功"

echo "正在生成EXE文件..."
docker run --rm -v $(pwd)/dist:/app/dist pdf-tool-builder

if [ $? -ne 0 ]; then
    echo "❌ EXE生成失败"
    exit 1
fi

echo "✅ EXE文件生成成功！"
echo ""
echo "生成的EXE文件:"
echo "  dist/PDF安全工具.exe"
echo ""
echo "文件信息:"
ls -lh dist/PDF安全工具.exe
echo ""
echo "使用方法:"
echo "  1. 将 'PDF安全工具.exe' 复制到Windows电脑"
echo "  2. 双击运行即可"
echo "  3. 无需安装任何依赖"
echo ""
echo "注意:"
echo "  • 文件大小约20-30MB"
echo "  • 需要Windows 7或更高版本"
echo "  • 杀毒软件可能误报，请添加信任"