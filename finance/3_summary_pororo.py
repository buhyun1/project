from pororo import Pororo
import pandas as pd
import requests
from bs4 import BeautifulSoup
from collections import Counter
from datetime import datetime

# 작업 시작 시간 기록
start_time = datetime.now()
print(f"작업 시작 시간: {start_time}")

# 엑셀 파일 읽기
df = pd.read_excel("삼성전자.xlsx")

# Pororo 모델 초기화
summarizer = Pororo(task="summary", lang="ko")
sentiment_analyzer = Pororo(task="sentiment", lang="ko")

# 텍스트 분할 함수
def split_text(text, max_length=512):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

# 뉴스 링크 순회 및 크롤링
for index, row in df.iterrows():
    link = row['Link']
    print(f"링크 처리 중: {link}")
    
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_paragraphs = soup.select("div.article_view section p")
    article_text = '\n'.join([para.text for para in article_paragraphs]).strip()

    # 기사 본문을 데이터프레임에 저장
    df.at[index, 'Body'] = article_text

    # 요약 및 감성 분석
    if article_text:
        print(f"기사 요약 및 감성 분석 중...")
        summary = summarizer(article_text)

        # 나누어진 각 부분에 대해 감성 분석 수행
        sentiments = []
        for part in split_text(article_text):
            sentiment = sentiment_analyzer(part)
            sentiments.append(sentiment)

        # 결과 처리 (예: 가장 흔한 감성 선택)
        most_common_sentiment = Counter(sentiments).most_common(1)[0][0]

        # 결과 저장
        df.at[index, 'Summary'] = summary
        df.at[index, 'Sentiment'] = most_common_sentiment

        print(f"요약 내용: {summary}")
        print(f"기사 감성: {most_common_sentiment}")
        print(f"기사 요약 및 감성 분석 완료: {index+1}/{len(df)}")

# 변경된 데이터프레임을 새 엑셀 파일로 저장
df.to_excel("updated_news_data.xlsx")

# 작업 종료 시간 기록 및 출력
end_time = datetime.now()
print(f"엑셀 파일 저장 완료")
print(f"작업 종료 시간: {end_time}")

# 전체 작업 시간 계산 및 출력
total_time = end_time - start_time
print(f"총 작업 시간: {total_time}")
