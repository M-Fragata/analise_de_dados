import pandas as pd

# Leituras de arquivos CSV

arquivo = './relatorio.csv'

df = pd.read_csv(arquivo, sep=';')
#print(df)

#df2 = pd.read_excel('exemplo.xlsx')

df3 = pd.DataFrame({
    'Frutas': ['Maçã', 'Banana', 'Laranja'],
    'Quantidade': [100, 150, 120]
})

df3.to_csv('frutas.csv', index=False)

df4 = pd.read_csv('frutas.csv')
print(df4)

df5 = pd.DataFrame({
    'País': ['Brasil', 'Argentina', 'Chile'],
    'População': [215, 45, 19]
})

df5.to_excel('paises.xlsx')
df6 = pd.read_excel('paises.xlsx')
print(df6)