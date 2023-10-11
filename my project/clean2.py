import pandas as pd

df = pd.read_csv('survey.csv')

df.dropna(inplace = True)

print(df.to_string())