import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([5, 20, 35, 40, 45])

print(f'Array1: {array1}\nArray2: {array2}')

array_igual = array1 == array2
print(f'Array de igualdade: {array_igual}')

array_maior_que = array1 > array2
print(f'Array maior que {array_maior_que}')

array3 = np.array([True, False, True])
array4 = np.array([False, False, True])

array_and = array3 & array4
print(f'Operador and: {array_and}')

print(np.logical_or(array3, array4))

dados = np.array([1, 5, 10, 15, 20, 25])
filter = dados > 10
print(f'Array de filtros: {filter}')
elementos_filtrados = dados[dados > 10]
print(f'Elementos filtrados: {elementos_filtrados}')

