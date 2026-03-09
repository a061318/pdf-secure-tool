# GitHub自动构建EXE指南

## 步骤1：创建GitHub仓库

1. 访问 https://github.com/new
2. 创建新仓库，名称如 `pdf-secure-tool`
3. 选择公开或私有
4. 不要初始化README（我会提供完整文件）

## 步骤2：上传代码到GitHub

```bash
# 在本地创建Git仓库
git init
git add .
git commit -m "初始提交: PDF安全工具"

# 连接到GitHub仓库
git remote add origin https://github.com/你的用户名/pdf-secure-tool.git
git branch -M main
git push -u origin main
```

## 步骤3：触发自动构建

1. 进入GitHub仓库页面
2. 点击 "Actions" 标签页
3. 选择 "Build PDF Secure Tool EXE" 工作流
4. 点击 "Run workflow" 按钮
5. 等待约5-10分钟构建完成

## 步骤4：下载EXE文件

构建完成后：
1. 在Actions页面找到完成的构建
2. 点击进入构建详情
3. 在 "Artifacts" 部分下载 `PDF安全工具.zip`
4. 解压得到 `PDF安全工具.exe`

## 替代方案：使用在线打包服务

### 方案A：PyInstaller Online
1. 访问 https://pyinstaller-online.github.io/
2. 上传 `pdf_secure_gui.py` 文件
3. 添加依赖：`PyPDF2`, `reportlab`
4. 选择 "One file" 和 "Windowed"
5. 点击打包，下载EXE

### 方案B：使用Replit在线打包
1. 注册 https://replit.com/
2. 创建Python项目
3. 上传所有文件
4. 在Shell中运行：
   ```bash
   pip install pyinstaller PyPDF2 reportlab
   pyinstaller --onefile --windowed pdf_secure_gui.py
   ```
5. 下载生成的EXE

## 手动打包指南（在Windows上）

如果您有Windows电脑，可以直接打包：

```cmd
# 1. 安装Python 3.10+
# 2. 安装依赖
pip install PyPDF2 reportlab pyinstaller

# 3. 运行打包脚本
build_exe.bat

# 4. EXE文件在 dist/ 文件夹中
```

## 文件清单

确保上传以下文件到GitHub：
- `pdf_secure_gui.py` - 主程序
- `requirements.txt` - 依赖列表
- `build_exe.bat` - 打包脚本
- `create_icon.py` - 图标生成
- `.github/workflows/build-exe.yml` - 自动构建配置
- `README.md` - 说明文档

## 注意事项

1. **GitHub Actions有免费额度** - 每月2000分钟
2. **EXE文件大小** - 约20-30MB
3. **杀毒软件** - 可能误报，需要添加信任
4. **Windows版本** - 需要Windows 7或更高版本

## 技术支持

如果遇到问题：
1. 检查GitHub Actions日志
2. 确保所有依赖正确安装
3. 验证Python版本为3.8+
4. 检查磁盘空间是否充足