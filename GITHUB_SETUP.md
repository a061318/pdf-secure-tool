# GitHub自动构建EXE - 完整指南

## 第一步：登录GitHub
1. 打开 https://github.com/login
2. 登录账号：
   - 用户名：`a061318`
   - 密码：`yx061318`

## 第二步：创建仓库
1. 点击右上角 `+` → `New repository`
2. 填写信息：
   - Repository name: `pdf-secure-tool`
   - Description: `PDF安全工具 - Windows 11免安装版`
   - 选择 `Public`
   - **不要勾选** `Add a README file`
   - **不要勾选** `Add .gitignore`
   - **不要勾选** `Choose a license`
3. 点击 `Create repository`

## 第三步：上传代码
创建仓库后，在终端执行以下命令：

```bash
# 1. 进入工具目录
cd ~/.openclaw/workspace/pdf_tool

# 2. 初始化Git
git init

# 3. 添加所有文件
git add .

# 4. 提交更改
git commit -m "初始提交: PDF安全工具"

# 5. 连接到GitHub仓库（复制创建仓库后显示的URL）
git remote add origin https://github.com/a061318/pdf-secure-tool.git

# 6. 推送代码
git branch -M main
git push -u origin main
```

**注意**：执行第5步时，需要输入GitHub用户名和密码：
- 用户名：`a061318`
- 密码：`yx061318`

## 第四步：触发自动构建
1. 进入仓库页面：https://github.com/a061318/pdf-secure-tool
2. 点击顶部的 `Actions` 标签页
3. 在左侧选择 `Build PDF Secure Tool EXE`
4. 点击右侧的 `Run workflow` 按钮
5. 再次点击 `Run workflow` 确认

## 第五步：等待构建完成
1. 构建需要约5-10分钟
2. 可以点击正在运行的工作流查看进度
3. 等待状态变为绿色 `✓`

## 第六步：下载EXE文件
构建完成后：
1. 点击完成的工作流
2. 在页面底部找到 `Artifacts` 部分
3. 点击 `PDF安全工具` 下载ZIP文件
4. 解压得到 `PDF安全工具.exe`

## 文件清单
上传的代码包含以下文件：
- `pdf_secure_gui.py` - 图形界面主程序
- `requirements.txt` - Python依赖
- `build_exe.bat` - Windows打包脚本
- `create_icon.py` - 图标生成
- `.github/workflows/build-exe.yml` - 自动构建配置
- `README.md` - 使用说明
- `push_to_github.sh` - 上传脚本
- `GITHUB_SETUP.md` - 本指南

## 常见问题

### Q1: 推送时要求输入密码
GitHub现在要求使用token代替密码：
1. 访问 https://github.com/settings/tokens
2. 点击 `Generate new token`
3. 选择 `repo` 权限
4. 生成token并复制
5. 推送时使用token作为密码

### Q2: 构建失败
检查构建日志，常见原因：
1. 依赖安装失败 - 重试构建
2. 内存不足 - GitHub Actions有内存限制
3. 超时 - 免费用户有6小时限制

### Q3: 无法下载EXE
1. 确保构建成功（绿色✓）
2. 检查网络连接
3. 尝试重新下载

### Q4: EXE被误报病毒
这是PyInstaller打包的常见问题：
1. 添加杀毒软件信任
2. 上传到VirusTotal检查
3. 源代码公开可审查

## 技术支持
如果遇到问题：
1. 检查GitHub Actions日志
2. 确保所有文件已上传
3. 验证Python版本兼容性

## 仓库链接
- 仓库主页：https://github.com/a061318/pdf-secure-tool
- Actions页面：https://github.com/a061318/pdf-secure-tool/actions
- 直接下载EXE：构建完成后从Artifacts下载

## 完成！
现在您有了一个可以自动构建EXE的GitHub仓库，以后更新代码只需推送即可自动生成新版本。