import pandas as pd

df_vendas_loja_a = pd.DataFrame({
    'Item': ['Tv', 'Geladeira', 'Fogão'],
    'Vendas_A': [100, 50, 30]
}, index=['Tv', 'Geladeira', 'Fogão'])

df_vendas_loja_b = pd.DataFrame({
    'Vendas_B': [80, 60, 70],
    'Estoque_B': [10, 5, 2]
}, index=['Tv', 'Geladeira', 'Máquina de Lavar'])

print(df_vendas_loja_a)
print(df_vendas_loja_b)

print('-------------------------------------------------')

#Left Join (Padrão)
left_join = df_vendas_loja_a.join(df_vendas_loja_b)
print(left_join)

print('-------------------------------------------------')

#Inner Join (Padrão)
inner_join = df_vendas_loja_a.join(df_vendas_loja_b, how='inner')
print(inner_join)

print('-------------------------------------------------')

#Outer Join (Padrão)
outer_join = df_vendas_loja_a.join(df_vendas_loja_b, how='outer')
print(outer_join)