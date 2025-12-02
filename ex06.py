import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

# Filtrar músicas lançadas após 1980
print(df[df['Year'] > 1980])
print(df[df['Year'] > 1980][['Year', 'Track']])