import pandas as pd

# Function to read and process each file
def process_file(file_path, company_name):
    df = pd.read_excel(file_path)
    df = df[['Date', 'Positive_ratio']]
    grouped_data = df.groupby('Date')['Positive_ratio'].mean()
    return grouped_data.rename(company_name)

# Paths to the Excel files for each company
file_path1 = 'finance/company/5_삼성전자.xlsx'
file_path2 = 'finance/company/5_SK하이닉스.xlsx'
file_path3 = 'finance/company/5_LG전자.xlsx'
file_path4 = 'finance/company/5_카카오.xlsx'

# Process each file
grouped_data_samsung = process_file(file_path1, 'Positive Ratio Samsung')
grouped_data_sk = process_file(file_path2, 'Positive Ratio SK하이닉스')
grouped_data_lg = process_file(file_path3, 'Positive Ratio LG전자')
grouped_data_kakao = process_file(file_path4, 'Positive Ratio 카카오')

# Combine the data from all companies
combined_data = pd.concat([grouped_data_samsung, grouped_data_sk, grouped_data_lg, grouped_data_kakao], axis=1)

# Save the combined data to a new Excel file
output_file_path = 'positive_ratio_data.xlsx'
combined_data.to_excel(output_file_path, index=True)

print(f"Combined data saved to {output_file_path}")
