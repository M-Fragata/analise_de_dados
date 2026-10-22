import pandas as pd

dados = {
    'Nome': ['Alice', 'Robert', 'Carla'],
    'Idade': [25, 30, 35],
    'Status': ['Ativo', 'Inativo', 'Ativo']
}

df = pd.DataFrame(dados)
print(df)
print('-------------------')

#apply()
def categoria_idade(idade):
    if idade < 30:
        return 'Jovem'
    else:
        return 'Adulto'

df['Categoria_idade'] = df['Idade'].apply(categoria_idade)
print(df)

df['Idade_dobrada'] = df['Idade'].apply(lambda x : x * 2)
print(df)

print('-------------------')
#map()
mapeamento_status = {'Ativo': 'ativo', 'Inativo': 'inativo'}
df['Status_formatado'] = df['Status'].map(mapeamento_status)
print(df)