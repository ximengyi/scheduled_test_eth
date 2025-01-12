# 使用官方 Python 3 镜像作为基础镜像
FROM python:3.9-slim

# 安装必要的依赖（例如 Chrome、ChromeDriver、Selenium）
RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    unzip \
    libx11-dev \
    libx264-dev \
    libxrender-dev \
    libfontconfig1 \
    libxext6 \
    chromium \
    && apt-get clean

# 安装 Python 包
RUN pip install --upgrade pip
RUN pip install selenium webdriver-manager

# 复制 Python 脚本到容器内
COPY get_test_eth.py /app/get_test_eth.py

# 设置环境变量，指定无头模式
ENV DISPLAY=:99

# 设置默认的环境变量，钱包地址
ENV WALLET_ADDRESS=

# 运行 Python 脚本
CMD ["python", "/app/get_test_eth.py"]
