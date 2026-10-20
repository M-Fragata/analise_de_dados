import numpy as np

array1 = np.arange(10,60,10)
print(f'Primeiro elemento: {array1[0]}')
print(f'Último elemento: {array1[-1]}')

matriz = np.array([np.arange(1,4),np.arange(4,7), np.arange(7,10)])
print(matriz)

## Acessando a matriz [linha, coluna]
print(matriz[0,2]) ## primeira linha terceira coluna

## Fatiamento [inicial, final, passo]
array2 = np.arange(0,21)
print(array2[2:6]) ## Fatiando do índice 2 ao 5
print(array2[5:]) ## do 5 até o final
print(array2[::2]) ## do início ao fim de 2 em 2


matriz2 = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120]
    ])

matriz_fat = matriz2[:,1:3] ## todas as linhas e 2º e 3º colunas
print('Matriz fatiada: ',matriz_fat)
matriz_fat2 = matriz2[:2,:] ## Duas primeiras linhas e todas as colunas
print('Matriz fatiada2: ',matriz_fat2)