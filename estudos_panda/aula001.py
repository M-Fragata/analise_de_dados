import pandas as pd

# Criando uma série do pandas a partir de uma lista

numeros = [10, 20, 30, 40, 50]

serie1 = pd.Series(numeros)
print(serie1)

# Acessar um elemento da série
print(serie1[3])

#Criar uma série com índice personalizado
lista_numeros = [100,200,300]
index = ['a', 'b', 'c']

serie_personalizada = pd.Series(lista_numeros, index)
print(serie_personalizada)
print(serie_personalizada['a'])

#Criar uma Series a partir de um dicionário

dados = {'primeiro': 'Mouse', 'segundo': 'Teclado', 'terceiro': 'Monitor'}

serie_dict_dados = pd.Series(dados)
print(serie_dict_dados)
print(serie_dict_dados['segundo'])