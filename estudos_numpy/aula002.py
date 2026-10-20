import numpy as np

array1 = np.array([1,2,3,4,5,6])
print(array1)
print(type(array1))

## duas dimensões
array2 = np.array([[1,2,3],[4,5,6]])
print(array2)
print(type(array2))

## três dimensões
array3 = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(array3)
print(type(array3))

## Array de N dimensões
array4 = np.array([1,2,3,4], ndmin=7)
print(array4)

## Verificando o número de dimensões de um array
print(array1.ndim)
print(array2.ndim)
print(array3.ndim)
print(array4.ndim)

## NP Arange - criar um aray de 0 a 20
array5 = np.arange(20)
print(array5)
print(type(array5))

## NP arange com passo
array6 = np.arange(2,11,2)
print(array6)
print(type(array6))

# np.linspace espaçamento uniforme entre o inicial e o final

array7 = np.linspace(0,100,5)
print(array7)
print(type(array7))

array8 = np.linspace(1,2,10)
print(array8)
print(type(array8))

# criar um array contendo 5 zeros
arrays_zeros = np.zeros(5)
print(arrays_zeros)

# Criar uma matriz de 0 contendo 3 linhas e 4 colunas
matriz_zeros = np.zeros((3,4))
print(matriz_zeros)
print(type(matriz_zeros))

# criando um array contendo 4 uns
array_uns = np.ones(4)
print(array_uns)
print(type(array_uns))

# criando uma matriz de 1 contendo 3 linhas e 4 colunas
matriz_uns = np.ones((3,4))
print(matriz_uns)
print(type(matriz_uns))