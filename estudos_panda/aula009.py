import pandas as pd
import numpy as np

dados = {
    'Numero_String': ['1','2','3','4'],
    'Preco_Float': [10.5, 20.0, 15.75, 30.0]
}

df = pd.DataFrame(dados)
print(df)
print(df.info())

#Converter 'Numero_String' para INT
df['Numero_String'] = df['Numero_String'].astype(int)

#Converter 'Preco_Float' para INT
df['Preco_Float'] = df['Preco_Float'].astype(int)

print('----------------------')
print(df)
print(df.info())

print('----------------------')

#Valores ausentes
df2 = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

print(df2)

#isna retorna um DataFrame booleano, verdadeiro para numeros ausentes
print(df2.isna())

#fillna - preenche os valores ausentes com algum valor
df_nulos = df2.fillna({'A': 0})
print(df_nulos)

#fillna - preencher com uma media de valores da coluna
df_media = df2.fillna(df2.mean())
print(df_media)

#Remover as linhas com valores ausentes
df_drop_linhas = df2.dropna()
print(df_drop_linhas)

#Remover as colunas com vlores ausentes
df_drop_cols = df2.dropna(axis=1)
print(df_drop_cols)