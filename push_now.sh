#!/bin/bash

echo "🚀 立即推送到GitHub仓库"
echo "======================"

cd ~/.openclaw/workspace/pdf_tool

echo ""
echo "1. 初始化Git仓库："
echo "----------------"
rm -rf .git
git init
git add .
git commit -m "PDF安全工具 v1.0 - 包含GitHub Actions"

echo ""
echo "2. 连接到您的GitHub仓库："
echo "----------------------"
git remote add origin https://github.com/a061318/pdf-secure-tool.git

echo ""
echo "3. 强制推送（覆盖现有内容）："
echo "--------------------------"
echo "执行以下命令："
echo ""
echo "  git push -u origin main --force"
echo ""
echo "注意：需要输入GitHub用户名和密码"
echo "用户名: a061318"
echo "密码: yx061318"
echo ""
echo "如果要求token，请访问："
echo "  https://github.com/settings/tokens"
echo "生成token并用作密码"

echo ""
echo "4. 触发构建："
echo "-----------"
echo "推送成功后，访问："
echo "  https://github.com/a061318/pdf-secure-tool/actions"
echo ""
echo "点击 'Build PDF Tool EXE' 工作流"
echo "点击 'Run workflow' 按钮"
echo "等待5-10分钟构建完成"

echo ""
echo "5. 下载EXE："
echo "----------"
echo "构建完成后，在Artifacts部分下载 'PDF-Tool-EXE'"

echo ""
echo "✅ 完成！"