from flask import Flask, render_template, request, jsonify
from data_sources import fetch_google_scholar
import pandas as pd
import os
from dotenv import load_dotenv

app = Flask(__name__)

# 載入環境變數
load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword', 'semiconductor supply chain resilience')
    max_results = int(request.form.get('max_results', 30))
    
    # 執行搜尋
    results = fetch_google_scholar(keyword, max_results)
    df = pd.DataFrame(results)
    
    # 準備圖表數據
    year_counts = df['year'].value_counts().sort_index()
    chart_data = {
        'years': year_counts.index.tolist(),
        'counts': year_counts.values.tolist()
    }
    
    # 準備表格數據
    table_data = df[['title', 'year', 'link']].to_dict('records')
    
    return jsonify({
        'table_data': table_data,
        'chart_data': chart_data
    })

if __name__ == '__main__':
    app.run(debug=True) 