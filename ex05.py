import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

# Somente as 5 primeiras linhas
#print(df.head())
# Somente as 5 últimas linhas
#print(df.tail())

#print(df.shape) #imprime a quantidade de linhas e colunas

#print(df.columns) #mostrar colunas detalhadas
for i, coluna in enumerate(df.columns, start=1):
    #print("Coluna: ", coluna)
    print(f"{i}° coluna: {coluna}")