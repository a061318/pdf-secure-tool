#!/bin/bash

echo "🔄 修复GitHub Actions工作流"
echo "========================="

cd ~/.openclaw/workspace/pdf_tool

echo ""
echo "1. 更新工作流文件版本："
echo "---------------------"
echo "已将 actions/upload-artifact@v3 更新为 v4"
echo "已将 actions/checkout@v3 更新为 v4"
echo "已将 actions/setup-python@v4 更新为 v5"

echo ""
echo "2. 提交更改："
echo "-----------"
git add .github/workflows/
git commit -m "修复: 更新GitHub Actions到最新版本"

echo ""
echo "3. 推送到GitHub："
echo "---------------"
echo "执行以下命令："
echo ""
echo "  git push origin main"
echo ""
echo "或者如果需要强制推送："
echo "  git push origin main --force"
echo ""
echo "注意：使用GitHub token作为密码"

echo ""
echo "4. 触发构建："
echo "-----------"
echo "推送后，访问："
echo "  https://github.com/a061318/pdf-secure-tool/actions"
echo ""
echo "应该能看到 'Build PDF Tool EXE' 工作流"
echo "点击 'Run workflow' 按钮"

echo ""
echo "5. 如果仍然有问题："
echo "----------------"
echo "A. 删除现有工作流文件："
echo "   1. 在GitHub网页删除 .github/workflows/ 目录"
echo "   2. 重新推送"
echo ""
echo "B. 使用网页创建新工作流："
echo "   1. 点击 'Add file' → 'Create new file'"
echo "   2. 路径: .github/workflows/build.yml"
echo "   3. 复制以下内容："
echo ""
cat .github/workflows/stable-build.yml
echo ""
echo "   4. 提交文件"
echo "   5. 自动触发构建"

echo ""
echo "✅ 修复完成！"