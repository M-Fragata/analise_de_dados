import pandas as pd

dados = {
    'Produto': ['A', 'B', 'C', 'D', 'E'],
    'Preco': [10.5, 20.0, 15.75, 25.0, 30.0],
    'Estoque': [100, 50, 75, 30, 20]
}

index = ['item1', 'item2', 'item3', 'item4', 'item5']

df = pd.DataFrame(dados, index)
print(df)

print(df[['Produto', 'Estoque']])
print('-----------')

#Comando loc - Seleção do item3
print(df.loc['item3'])
print(df.loc[['item1', 'item5'],['Preco','Estoque']])
print('-----------')

#comando iloc para buscar o item2
print(df.iloc[2])
print('-----------')

#Comando iloc para linhas e colunas
print(df.iloc[0:2, 1:3]) #fatiando da linha 0 até a linha 1 e da coluna 1 até a 2

