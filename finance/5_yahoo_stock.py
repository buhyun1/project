import yfinance as yf
import pandas as pd

# 회사별 티커 심볼 정의
tickers = ["005930.KS", "000660.KS", "066570.KS", "035720.KS"]  # 삼성전자, SK하이닉스, LG전자, 카카오
start_date = "2023-10-01"
end_date = "2023-10-31"

all_data = []

for ticker in tickers:
    # Yahoo Finance에서 역사적 데이터 가져오기
    data = yf.download(ticker, start=start_date, end=end_date)
    data['Ticker'] = ticker  # 회사를 식별하기 위해 열 추가
    all_data.append(data)

# 모든 DataFrame을 하나로 결합
all_data_combined = pd.concat(all_data)

# 데이터를 Excel 파일로 저장
all_data_combined.to_excel("stock_data_october_2023.xlsx")
