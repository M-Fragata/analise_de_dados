import numpy as np

array_original = np.arange(16)
print('Array original: ',array_original)

# Reshape para 4 linhas e 4 colunas

array_modificado = array_original.reshape(4,4)
print('Array reshape: ',array_modificado)

# Divisão vertical (vsplit)
array_dividido = np.vsplit(array_modificado, 2)
print('Array dividido vertical: ',array_dividido)
print('Array dividido 1º parte',array_dividido[0])
print('Array dividido 2º parte',array_dividido[1])

# Divisão horizontal (hsplit)
array_dividido = np.hsplit(array_modificado, 4)
print('Array dividido horizontal', array_dividido)
print('Array dividido horizontal 1º coluna: ', array_dividido[0])
print('Array dividido horizontal 2º coluna: ', array_dividido[1])
print('Array dividido horizontal 3º coluna: ', array_dividido[2])
print('Array dividido horizontal 4º coluna: ', array_dividido[3])

array_original = np.arange(10,90,10)
print('Array original', array_original)

array_dividido = np.split(array_original,4)
print('Array dividido split: ',array_dividido)

matriz_original = np.arange(20)
print('Matriz original', matriz_original)

matriz_2d = matriz_original.reshape(4,5)
print('Matriz reshape: ', matriz_2d)

# Dividir a matriz em 2 partes ao longo do eixo de linhas
matriz_split = np.split(matriz_2d, 2, axis=0)
print('Matriz dividida pelo eixo linha: ', matriz_split)