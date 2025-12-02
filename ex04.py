import pandas as pd

df = pd.read_csv('ClassicDisco.csv')
filtro = df['Artist']
print(filtro)
print(df.columns) #mostrar os nomes das colunas