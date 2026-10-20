import numpy as np

array1 = np.array([1,2,3,4,5])
soma = array1.sum()
print(f'A soma do array {array1} é de {soma}')

matriz = np.array([[10,20,30], [5,10,15]])
soma2 = matriz.sum()
print(f'A soma da matriz {matriz} é de {soma2}')

soma_col = matriz.sum(axis=0)
print(f'A soma por coluna: {soma_col}')

soma_row = matriz.sum(axis=1)
print(f'A soma por linha: {soma_row}')

media = array1.mean()
print(f'A média do {array1} é: {media}')

media_col = matriz.mean(axis=0)
media_row = matriz.mean(axis=1)
print(f'A média por coluna: {media_col}\nA média por Linha: {media_row}')

desvio_padrao = array1.std()
print(f'Desvio padrão: {desvio_padrao:.2f}')

array2 = np.array([9, 2, 7, 1, 5])
min = array2.min()
max = array2.max()
print(f'Valor mínimo: {min}\nValor máximo: {max}')

min_col = matriz.min(axis=0)
max_col = matriz.max(axis=0)

min_row = matriz.min(axis=1)
max_row = matriz.max(axis=1)

print(f'Coluna mínima {min_col} e máxima: {max_col}')
print(f'Linha mínima {min_row} e máxima: {max_row}')

array3 = np.array([9, 2, 7, 1, 5])
ind_maior = array3.argmax() ## Índice do maior valor, neste caso maior valor é 9 indice 0
print('Índice do maior valor: ',ind_maior)
ind_menor = array3.argmin()
print('Índice de menor valor: ',ind_menor)

ind_maior_col = matriz.argmax(axis=0)
ind_maior_row = matriz.argmax(axis=1)
print(f'Índice de maior da coluna: {ind_maior_col}\nÍndice de maior da linha: {ind_maior_row}')