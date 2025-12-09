from sqlalchemy import create_engine

import pandas as pd

#conexão com o banco de dados MySQL
host = 'localhost'
user = 'root'
password = ''
database = 'aulaPandas'

#criar o caminho para o banco de dados
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
#criando um caminho com o usuário, senha, local e banco de dados

#df = pd.read_sql('select * from odontologia', con=engine)
#df = pd.read_sql('select * from odontologia where nome = "VITTOR WERNECK"', con=engine)
df = pd.DataFrame(
    [{
        'nome': 'Matheus Lemos',
        'titulacao': 'Graduado',
        'registroProfissional': '112-B',
        'uf': 'RJ',
        'municipio': 'Niterói'
    }]
)
print(df)