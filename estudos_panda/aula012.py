import pandas as pd

df_datas = pd.DataFrame({
    'Data_String': ['2023-01-01', '2023-01-02', '2023-01-03', '2026-10-22', '2021-02-21', '2026-07-07'],
    'Evento': ['Feriado', 'Reunião', 'Manutenção', 'Lançamento', 'Aniversário', 'Cidalia']
})

print(df_datas)

print('-------------')

#Converter 'Data_String' para datetime

df_datas['Data'] = pd.to_datetime(df_datas['Data_String'])
print(df_datas)
print(df_datas.dtypes)

print('-------------')

df_datas_formatos = pd.DataFrame({
    'Data': {'01/01/2027', '02-jan-2027', '20270103'},
    'valor': [10, 20, 30]
})

print(df_datas_formatos)

df_datas_formatos['Data_Convertida'] = pd.to_datetime(df_datas_formatos['Data'], format='mixed')