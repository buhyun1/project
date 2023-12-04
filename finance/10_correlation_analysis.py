import pandas as pd
from scipy.stats import pearsonr

file_path = './finance/company/긍정비율데이터.xlsx'
df = pd.read_excel(file_path)

# Define the list of company names and their corresponding stock prefixes
company_stock_pairs = [
    ('Samsung', 'ss'),
    ('SK하이닉스', 'sk'),
    ('LG전자', 'lg'),
    ('카카오', 'kk')
]

# Define the list of stock column suffixes
stock_column_suffixes = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

# Perform Pearson correlation analysis for each company and its corresponding stock columns
for company, prefix in company_stock_pairs:
    print(f"{company} Correlation Results:")
    
    positive_ratio_column = df[f'Positive Ratio {company}']
    
    for suffix in stock_column_suffixes:
        stock_column = df[f'{prefix}{suffix}']
        
        # Create a variable name dynamically
        variable_name = f'{company.lower()}_{prefix.lower()}{suffix.replace(" ", "")}'
        
        # Calculate Pearson correlation and p-value
        correlation, p_value = pearsonr(positive_ratio_column, stock_column)
        
        print(f"- {prefix}{suffix}:")
        print(f"  Pearson Correlation: {correlation:.3f}")
        print(f"  P-value: {p_value:.3f}")
