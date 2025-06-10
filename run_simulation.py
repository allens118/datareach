from data_sources import fetch_google_scholar
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 使用者輸入參數
KEYWORD = os.getenv("SIM_KEYWORD", "semiconductor supply chain resilience")
MAX_RESULTS = int(os.getenv("MAX_RESULTS", 30))


def main():
    print("🔍 正在搜尋 Google Scholar 文章……")
    scholar_results = fetch_google_scholar(KEYWORD, MAX_RESULTS)

    df_scholar = pd.DataFrame(scholar_results)
    df_scholar['source'] = 'Google Scholar'

    print("✅ 搜尋完成，統整中……")
    df_all = df_scholar

    # 顯示分析
    print("📈 顯示前10筆資料：")
    print(df_all[['title', 'year', 'source']].head(10))

    # 圖表顯示年份分布
    plt.figure(figsize=(10, 5))
    df_all['year'] = pd.to_numeric(df_all['year'], errors='coerce')
    df_all.dropna(subset=['year'], inplace=True)
    df_all['year'] = df_all['year'].astype(int)
    df_all['year'].value_counts().sort_index().plot(kind='bar')
    plt.title(f"📊 發表年份分布：{KEYWORD}")
    plt.xlabel("年份")
    plt.ylabel("文章數")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main() 