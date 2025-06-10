import requests
from pybliometrics.scopus import ScopusSearch
import os
import re

# 需設定 SERPAPI_KEY 與 SCOPUS_API_KEY 至 .env 或系統環境變數

SERPAPI_KEY = ""
SCOPUS_API_KEY = ""

# Google Scholar (via SerpAPI)
def fetch_google_scholar(keyword, max_results=30):
    results = []
    try:
        for start in range(0, max_results, 10):
            params = {
                "engine": "google_scholar",
                "q": keyword,
                "api_key": SERPAPI_KEY,
                "start": start
            }
            r = requests.get("https://serpapi.com/search", params=params)
            data = r.json()
            
            if "organic_results" not in data:
                print("警告：無法獲取搜尋結果")
                continue
                
            for article in data.get("organic_results", []):
                title = article.get("title", "")
                link = article.get("link", "")
                # 從 publication_info 的 summary 中提取年份
                publication_info = article.get("publication_info", {})
                year = ""
                if "summary" in publication_info:
                    # 嘗試從摘要中提取年份（通常是四位數字）
                    year_match = re.search(r'\b(19|20)\d{2}\b', publication_info["summary"])
                    if year_match:
                        year = year_match.group(0)
                
                if title:  # 只添加有標題的結果
                    results.append({
                        "title": title,
                        "link": link,
                        "year": year
                    })
                    
        print(f"成功獲取 {len(results)} 筆搜尋結果")
        return results
        
    except Exception as e:
        print(f"搜尋時發生錯誤：{str(e)}")
        return []

# Scopus (via pybliometrics)
def fetch_scopus(keyword, max_results=30):
    results = []
    s = ScopusSearch(f"TITLE-ABS-KEY({keyword})")
    for i, e in enumerate(s.results):
        if i >= max_results:
            break
        results.append({
            "title": e.title,
            "link": f"https://www.scopus.com/record/display.uri?eid={e.eid}",
            "year": e.coverDate.split("-")[0] if e.coverDate else ""
        })
    return results 