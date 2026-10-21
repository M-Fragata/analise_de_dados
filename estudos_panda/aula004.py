import pandas as pd

# Criando DataFrames

dados = {
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Fernando', 'Gabriela', 'Hugo', 'Júlio', 'Raiane'],
    'idade': [22, 35, 28, 40, 29, 33, 25, 45, 30, 38],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'São Paulo', 'Rio de Janeiro', 'Fortaleza', 'Belém', 'Goiania'],
    'Salário': [3000, 5500, 4000, 7000, 4200, 6000, 3500, 8000, 4900, 6500]
}

df = pd.DataFrame(dados)
print(df)

#head(n) - retorna as primeiras n linhas do df
print(df.head(3)) # Retorna as 3 primeiras linhas e por padrão, head() retorna as 5 

#tail(n) - Retorna as últimas n linhas do df
print(df.tail(2))

#shape - Retorna quantidade de linhas e colunas
df.shape

#info - Retorna um resumo do DF
df.info()

#describe() - Retorna estatísticas sobre o DF
print(df.describe())