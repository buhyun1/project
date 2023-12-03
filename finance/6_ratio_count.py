import pandas as pd

import os
print(os.getcwd())
# 데이터프레임을 로드합니다. 여기서는 예시로 파일 경로를 지정하였습니다.
df = pd.read_excel('./company/3_SK하이닉스.xlsx')

# 'Date' 열을 datetime 객체로 변환합니다.
df['Date'] = pd.to_datetime(df['Date'])

# 날짜별로 긍정과 부정의 개수를 계산합니다.
sentiment_count = df.groupby(['Date', 'Sentiment']).size().unstack(fill_value=0)

# 각 날짜별로 긍정과 부정의 비율을 계산합니다.
sentiment_count['Positive_ratio'] = sentiment_count['Positive'] / (sentiment_count['Positive'] + sentiment_count['Negative'])
sentiment_count['Negative_ratio'] = sentiment_count['Negative'] / (sentiment_count['Positive'] + sentiment_count['Negative'])

# 결과를 확인합니다.
print(sentiment_count[['Positive_ratio', 'Negative_ratio']])

# 엑셀 파일에 긍정 및 부정 비율을 추가합니다.
df = df.merge(sentiment_count[['Positive_ratio', 'Negative_ratio']], left_on='Date', right_index=True)

# 업데이트된 데이터프레임을 새로운 엑셀 파일로 저장합니다.
df.to_excel('./company/4_SK하이닉스.xlsx', index=False)
