import pandas as pd

dados1 = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
}

index1 = [0, 1, 2, 3]

dados2 = {
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7'],
}

index2 = [4, 5, 6, 7]

df1 = pd.DataFrame(dados1, index1)
df2 = pd.DataFrame(dados2, index2)

print(df1)
print(df2)

print('--------------')

concat_linhas = pd.concat([df1, df2])
print(concat_linhas)

dados3 = {
    'E': ['C0', 'C1', 'C2', 'C3']
}

index3 = [0, 1, 2, 3]

df3 = pd.DataFrame(dados3,index3)
print(df3)

print('--------------')
concat_col = pd.concat([df1, df3], axis=1)
print(concat_col)