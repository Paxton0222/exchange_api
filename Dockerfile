# 使用官方 Python 長輩作為基底
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 將本地檔案添加到容器中（當前目錄內的所有檔案）
COPY . /app

# 安裝所需的套件
RUN pip install --no-cache-dir -r requirements.txt

# 開放 FastAPI 運行的端口
EXPOSE 8000

# 啟動 FastAPI 應用程式
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
