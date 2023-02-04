import pandas as pd
df = pd.read_excel('patterns.xlsx')
df = df.drop_duplicates()
print(df)