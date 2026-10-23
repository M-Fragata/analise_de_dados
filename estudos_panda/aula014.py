import pandas as pd

df_clientes = pd.DataFrame({
    'ID_Client': [1, 2, 3, 4],
    'Nome': ['João Paulo', 'Maria da Silva', 'Pablo Gomes', 'Irís da Costa']
    })

df_pedidos = pd.DataFrame({
    'ID_Pedido': [101, 102, 103, 104, 105],
    'ID_Client': [2, 1, 3, 2, 1],
    'Produto': ['Livro','Caneta','Caderno','Mochila','Lapís']
})

print(df_clientes)
print(df_pedidos)

print('----------------------------------')

#Inner Merge
merge_inner = pd.merge(df_clientes,df_pedidos,on='ID_Client', how='inner')
print(merge_inner)

print('----------------------------------')

#left merge
merge_left = pd.merge(df_clientes, df_pedidos, on='ID_Client', how='left')
print(merge_left)

print('----------------------------------')

#left merge
merge_right = pd.merge(df_clientes, df_pedidos, on='ID_Client', how='right')
print(merge_right)

print('----------------------------------')

#left merge
merge_outer = pd.merge(df_clientes, df_pedidos, on='ID_Client', how='outer')
print(merge_outer)