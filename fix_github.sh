#!/bin/bash

echo "🔧 GitHub仓库修复脚本"
echo "===================="

echo ""
echo "1. 检查当前Git状态："
echo "------------------"
cd ~/.openclaw/workspace/pdf_tool
git status

echo ""
echo "2. 确保工作流文件存在："
echo "---------------------"
ls -la .github/workflows/

echo ""
echo "3. 重新提交所有文件："
echo "-------------------"
git add .
git commit -m "修复: 添加GitHub Actions工作流"

echo ""
echo "4. 推送到GitHub："
echo "---------------"
echo "执行以下命令："
echo ""
echo "  git push origin main"
echo ""
echo "如果需要强制推送："
echo "  git push origin main --force"
echo ""
echo "注意：可能需要输入GitHub token作为密码"

echo ""
echo "5. 检查GitHub页面："
echo "-----------------"
echo "访问：https://github.com/a061318/pdf-secure-tool"
echo "点击 'Actions' 标签页"
echo ""
echo "如果仍然没有 'Run workflow' 按钮："
echo "1. 点击 'Add file' → 'Create new file'"
echo "2. 路径输入: .github/workflows/build.yml"
echo "3. 复制以下内容："
echo ""
cat .github/workflows/simple-build.yml
echo ""
echo "4. 提交文件"
echo "5. 自动触发构建"

echo ""
echo "✅ 完成修复！"