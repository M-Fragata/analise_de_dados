import pandas as pd

dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Matheus', 'Franklin'],
    'Idade': [25, 30, 35, 40, 28, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Recife'],
    'Pontuacao': [85, 90, 78, 92, 88, 95]
}

df = pd.DataFrame(dados)
print(df)

print('----------')

filtro_idade = df[df['Idade'] <= 30]
print(filtro_idade)

print('----------')

filtro_cidade_pontuaca = df[(df['Cidade'] == 'São Paulo') | (df['Cidade'] == 'Rio de Janeiro') & (df['Pontuacao'] > 80)]
filtro_cidade_pontuaca = df[(df['Cidade'].isin(['Belo Horizonte','Curitiba'])) & (df['Pontuacao'] > 80)]
print(filtro_cidade_pontuaca)