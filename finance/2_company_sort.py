import pandas as pd
import datetime

# 시작 및 종료 날짜 설정
start_date = datetime.date(2023, 10, 1)
end_date = datetime.date(2023, 10, 31)
current_date = start_date

# 검색할 단어 리스트
search_terms = ["SK하이닉스","삼성전자","카카오","LG전자"]
term = ''
# 결과를 저장할 데이터프레임 초기화
filtered_news = pd.DataFrame()

# 각 파일을 순차적으로 불러오기
while current_date <= end_date:
    file_name = f"news/{current_date.strftime('%Y%m%d')}_news.xlsx"
    
    try:
        # 엑셀 파일 불러오기
        df = pd.read_excel(file_name)

        # 각 검색어에 대해 필터링하고 날짜 추가
        for term in search_terms:
            term = term
            temp_df = df[df['Title'].str.contains(term, na=False)]
            temp_df['Date'] = current_date  # 날짜 열 추가

            # 결과를 전체 결과 데이터프레임에 추가
            filtered_news = pd.concat([filtered_news, temp_df])

        print(f"{current_date.strftime('%Y-%m-%d')} 파일 처리 완료.")

    except FileNotFoundError:
        print(f"{file_name} 파일을 찾을 수 없습니다.")

    # 다음 날짜로 이동
    current_date += datetime.timedelta(days=1)

# 결과 출력
print(filtered_news)

# 필요하다면 결과를 새로운 엑셀 파일로 저장
filtered_news.to_excel(f'{term}.xlsx', index=False)
