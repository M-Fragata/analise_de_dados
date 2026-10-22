import pandas as pd

dados = {
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Rio de Janeiro', 'São Paulo'],
    'Vendas': [1000, 1500, 2000, 1200, 1800, 2500],
    'Produto': ['A', 'B', 'A', 'C', 'B', 'A']
    }

df = pd.DataFrame(dados)
print(df)

print('----------------------')

#Agrupar por cidade e calcular soma das vendas
vendas_por_cidades = df.groupby('Cidade')['Vendas'].sum()
print(vendas_por_cidades)

print('----------------------')

media_vendas = df.groupby(['Cidade', 'Produto'])['Vendas'].mean()
print(media_vendas)