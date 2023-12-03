import pandas as pd

# 처리할 파일 목록
files = ['2_LG전자.xlsx', '2_SK하이닉스.xlsx', '2_삼성전자.xlsx', '2_카카오.xlsx']

# 각 파일을 순차적으로 처리
for file in files:
    # Excel 파일 읽기
    df = pd.read_excel(file)

    # 비어 있는 행 제거
    df_cleaned = df.dropna()

    # 처리된 데이터를 새 파일로 저장
    cleaned_file_name = '3_' + file
    df_cleaned.to_excel(cleaned_file_name, index=False)
