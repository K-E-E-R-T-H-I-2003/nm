
import pandas as pd

df = pd.read_csv('survey.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())