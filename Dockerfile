# Docker容器用于构建Windows EXE
# 使用方法: docker build -t pdf-tool-builder . && docker run -v $(pwd)/dist:/app/dist pdf-tool-builder

FROM python:3.10-slim

WORKDIR /app

# 安装构建工具
RUN apt-get update && apt-get install -y \
    git \
    wget \
    wine \
    wine32 \
    wine64 \
    && rm -rf /var/lib/apt/lists/*

# 设置Wine环境
ENV WINEPREFIX=/wine
ENV WINEARCH=win64

# 安装Python依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pyinstaller

# 复制源代码
COPY . .

# 创建图标
RUN python create_icon.py

# 构建EXE的命令
CMD ["pyinstaller", "--onefile", "--windowed", "--name", "PDF安全工具", "--icon", "icon.ico", "pdf_secure_gui.py"]