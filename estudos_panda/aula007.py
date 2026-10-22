import pandas as pd

dados = {
    'Produto': ['Maçã', 'Banana', 'Laranja', 'Uva', 'Pera'],
    'Preco': [2.50, 1.80, 3.00, 4.20, 2.10],
    'Quantidade': [300, 150, 75, 200, 320]
}

df = pd.DataFrame(dados)
print(df)

print('-------------')

# Ordenar por preço em ordem crescente
df_preco = df.sort_values(by='Preco', ascending=False) # True para crescente, False para decrescente
print(df_preco)

print('----------------')
# Ordenar por múltiplas colunas
df_multi = df.sort_values(by=['Preco', 'Quantidade'], ascending=[True, False])
print(df_multi)