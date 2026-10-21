import pandas as pd

# Criando nosso primeiro DataFrame a partir de um dicionário

dados = {
    'Matrícula': [44256, 44171, 44175],
    'Nome': ['Matheus Fragata', 'Daniel Augusto', 'Moisés de Jesus'],
    'Setor': ['Movimentação', 'Movimentação', 'Movimentação'],
    'Bairro': ['Jardim Atlantico Leste', 'Manu Manoela', 'Cajueiros']
}

df = pd.DataFrame(dados)
print(df)
print(df.Nome)

lista_dict = [
    {'nome': 'Rodrigo', 'idade': 25, 'cidade': 'Belém'},
    {'nome': 'Matheus', 'idade': 26, 'cidade': 'Maricá'},
    {'nome': 'André', 'idade': 24, 'cidade': 'Niterói'}
]

print('-------------')
df = pd.DataFrame(lista_dict)
print(df)
print(df.nome)