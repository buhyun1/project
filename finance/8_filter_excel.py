import pandas as pd

# Paths to the Excel files
samsung_file_path = 'finance/company/4_SK하이닉스.xlsx'

stock_file_path = 'finance/stock_data/stock_2023.xlsx'

# Read the Excel files
samsung_df = pd.read_excel(samsung_file_path)
stock_df = pd.read_excel(stock_file_path)

# Convert the date columns to datetime
# Assuming the date column is named 'Date' in both files
samsung_df['Date'] = pd.to_datetime(samsung_df['Date'])
stock_df['Date'] = pd.to_datetime(stock_df['Date'])

# Filter the '삼성전자' DataFrame to include only the dates present in 'stock_2023'
filtered_samsung_df = samsung_df[samsung_df['Date'].isin(stock_df['Date'])]

# Save the filtered DataFrame to a new Excel file
filtered_samsung_file_path = '5_SK하이닉스.xlsx'
filtered_samsung_df.to_excel(filtered_samsung_file_path, index=False)
