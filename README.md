# 學術文獻搜尋工具

這是一個使用 Python Flask 建立的簡單學術文獻搜尋工具，它整合了 Google Scholar (透過 SerpAPI) 的搜尋功能，並將結果以圖表和表格形式展示在網頁介面上。

## 功能

- 透過關鍵字搜尋 Google Scholar 學術文章。
- 顯示搜尋結果的年份分佈圖。
- 以表格形式展示文章標題、年份和連結。
- 支援自訂最大搜尋結果數量。

## 環境建置

請按照以下步驟來設定和執行專案：

### 1. 建立並啟用虛擬環境

```bash
python -m venv venv
```

在 Windows 上啟用虛擬環境：

```bash
.\venv\Scripts\activate
```

在 macOS/Linux 上啟用虛擬環境：

```bash
source venv/bin/activate
```

### 2. 安裝依賴套件

```bash
pip install -r requirements.txt
```

### 3. 設定 API 金鑰

您需要一個 SerpAPI 金鑰來使用 Google Scholar 搜尋功能。請前往 [SerpAPI](https://serpapi.com/) 註冊並獲取您的 API 金鑰。

創建一個名為 `.env` 的檔案在專案的根目錄中，並加入以下內容：

```
SERPAPI_KEY=你的_serpapi_key
SCOPUS_API_KEY=
SIM_KEYWORD=semiconductor supply chain resilience
MAX_RESULTS=30
```

請將 `你的_serpapi_key` 替換為您實際的 SerpAPI 金鑰。Scopus API 暫時不需要，因此可以留空。

### 4. 執行應用程式

```bash
python app.py
```

應用程式啟動後，您可以在瀏覽器中開啟 `http://127.0.0.1:5000/` 來存取網頁介面。

## 專案結構

```
.
├── app.py              # Flask 應用程式主檔案，處理網頁路由和搜尋邏輯
├── data_sources.py     # 包含 Google Scholar (SerpAPI) 搜尋功能的函式
├── requirements.txt    # 專案所需的 Python 依賴套件列表
├── .env                # 環境變數設定檔案 (需手動建立並填寫 API 金鑰)
└── templates/
    └── index.html      # 網頁前端模板，包含搜尋介面、結果顯示和圖表
``` 