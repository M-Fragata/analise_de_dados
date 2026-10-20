import numpy as np

array1 = np.array([5, 17, 32, -50])
print(array1)
print(array1.dtype)

array_float = np.array([2, 1.5, 3.4, -17, -3.2])
print(array_float)
print(array_float.dtype)

array_boolean = np.array([True, False, True])
print(array_boolean)
print(array_boolean.dtype)

array_str = np.array(['Matheus', 'José', 'Cidália'])
print(array_str)
print(array_str.dtype)

array_1_dimensao = np.array([10, 43, 22, 9])
print(array_1_dimensao)
print(array_1_dimensao.shape)

matriz = np.array([[10, 49, 37],[-13, 9, -45]])
print(matriz)
print(matriz.shape) ## 2 linhas e 3 colunas (2, 3)
print(matriz.size)
print(matriz.ndim) ## Tamanho de dimensoes 


array_cast = array_float.astype(int)
print(array_cast)
print(array_cast.dtype)

array_aux = array_cast.astype(float)
print(array_aux)
print(array_aux.dtype)