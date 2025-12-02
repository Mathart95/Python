import pandas as pd

dados = {
    'cargos': ["assistente","analista","gerente","diretor"],
    'salários': [10000,20000,30000,40000]
}
dados_bi = pd.DataFrame(dados)
print(dados_bi)