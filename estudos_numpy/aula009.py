import numpy as np

# Gerar um número aleatório entre 0 e 1
numero = np.random.rand()
print(numero)

# Gerar um array de 1 dimensão com 5 números aleatórios
array_id = np.random.rand(5)
print('Array com 5 números aleatórios entre 0 e 1: ', array_id)

# Gerar uma matriz 2x3 de números aleatórios
matriz_id = np.random.rand(2,3)
print('Matriz com 2x3 de números aleatórios entre 0 e 1: \n', matriz_id)

# Gerar números inteiros
numero = np.random.randint(10) # de 0 a 9
print('Número inteiro: ', numero)

array_inteiros = np.random.randint(10, 21, size=10)
print('Array com 3 números inteiros aleatórios: ',array_inteiros)

# Gerar uma matriz 2x2 de inteiros aleatórioes entre 1 e 100
matriz_2x2 = np.random.randint(1,101, size=(2,2))
print(matriz_2x2)

# Escolher elementos aleatoriamente de um array existente
array_frutas = np.array(['Maçã','Banana','Laranja', 'Limão', 'Abacaxi', 'Abacate'])
print('Array de frutas: ',array_frutas)
print('Fruta aleatória escolhida: ',np.random.choice(array_frutas))

frutas = np.random.choice(array_frutas, size=3)
print('Array de 3 frutas aleatórias: ',frutas)# pode haver repetição

array_original = np.array([1, 5, 10, 5, 3, 8, 2, 2, 1, 10, 7, 10])
print('Array original: ',array_original)
array_unico = np.unique(array_original)
print('Array original único: ', array_unico)

#np.any() - verifica se algum é True
array1 = np.array([False, False, True, False])
array2 = np.array([False, False, False])
print(np.any(array1))
print(np.any(array2))

#np.all verifica se todos são true
array3 = np.array([True, True, True])
array4 = np.array([True, False, True])
print(np.all(array3))
print(np.all(array4))

# np.sort retorna copia ordenada do array
array_ordenado = np.sort(array_original)
print(array_ordenado)

#np.argsort() - Retorna os índices que ordenariam
array_numeros = np.array([9,2,7,1,5,3])
array_indices = np.argsort(array_numeros)
print('Array de índices que ordenariam o array números: ',array_indices)

#Ordenação de matrizes (linha ou coluna)
matriz_ordenada = np.array([[3,1,2], [6,5,4]])
print('Matriz não ordenada: \n', matriz_ordenada)
matriz_linha = np.sort(matriz_ordenada, axis=1) 
print('Matriz ordenada por linha: ',matriz_linha)
matriz_coluna = np.sort(matriz_ordenada, axis=0)
print('Matriz ordenada por coluna: ',matriz_coluna)