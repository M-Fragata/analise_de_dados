import pandas as pd

dados = {
    'Produto': ['A', 'B', 'C', 'D'],
    'Preco_unitario': [10, 20, 15, 25],
    'Quantidade_vendida': [5, 3, 7, 2]
}

df = pd.DataFrame(dados)
print(df)
print('----------------------')

df['Valor_total'] = df['Preco_unitario'] * df['Quantidade_vendida']
print(df)

print('----------------------')
#Coluna com valor fixo
df['Desconto_aplicado'] = 0.10
print(df)

#Renomear a coluna produto
df.rename(columns={'Produto': 'Produto_Loja', 'Quantidade_vendida': 'Quantidade_vendas'}, inplace=True)
print(df)

print('----------------------')
#Remover colunas
df.drop('Desconto_aplicado', axis=1, inplace=True)
print(df)
df.drop(['Preco_unitario','Quantidade_vendas'], axis=1, inplace=True)
print(df)
