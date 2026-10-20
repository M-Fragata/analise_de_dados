import numpy as np

array1 = np.arange(1, 5)
array2 = np.arange(5, 9)

print('Array1: ',array1)
print('Array2: ',array2)

soma = array1 + array2
print('Soma de Array: ',soma)

subtracao = array1 - array2
print('Subtração de Array: ',subtracao)

multi = array1 * array2
print('Multiplicação de Array: ',multi)

divi = array2 / array1
print('Divisão de Array: ',divi)

pot = array1 ** array2
print('Potência: ',pot)