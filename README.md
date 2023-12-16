# 匯率轉換API文檔

## 如何執行

### Python 本地執行

#### 建立虛擬環境
```
python -m venv venv
source venv/bin/activate
```
#### 安裝 python 依賴

```
pip install -r requirements.txt
```

#### 啟動伺服器

```
uvicorn app:app
```

### Docker 執行

```
docker compose up -d
```

## 如何使用

建立好伺服器以後，訪問 [API頁面](http://localhost:8000/docs) 測試 API
