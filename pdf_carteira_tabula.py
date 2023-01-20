import tabula
import pandas as pd
import numpy as np
import os



def converter_carteira(file):

   temp = 'temp.csv'
   carteira = 'temp.xlsx'
   tabula.convert_into(file, temp, output_format='csv', pages='all', lattice=True)
   
   df = pd.read_csv(temp, names=['IT','PRODUTO','DESCRICAO','PRECO LIQ','QTD','SALDO','VALOR TOTAL SALDO',
                                          'QTD SEP','VALOR TOTAL SEP'], encoding='latin-1')
   
   df2 = df[df['PRODUTO'].str.contains('R', na=False)]
   df2.dropna()                                     
   df2 = df.sort_values(by=['IT'])
   df2 = df2.drop(columns=['IT', 'DESCRICAO', 'PRECO LIQ', 'QTD','VALOR TOTAL SALDO', 'VALOR TOTAL SEP'])
   df2['SALDO'] = df2['SALDO'].replace(',','.', regex=True)
   df2['QTD SEP'] = df2['QTD SEP'].replace(',','.', regex=True)
   df2['SALDO'] = pd.to_numeric(df2['SALDO'], errors='coerce')
   df2['QTD SEP'] = pd.to_numeric(df2['QTD SEP'], errors='coerce')
   
   #somar produtos
   
   df3 =  df2[['PRODUTO','SALDO','QTD SEP']].groupby('PRODUTO').sum()
   df3 = df3.drop(df3.loc[df3.index=='Filtros:'].index)
   df3 = df3.drop(df3.loc[df3.index=='- ZZZZZZZZZZZZZZZZZZZZZZZZZZ'].index)
   df3 = df3.drop(df3.loc[df3.index=='2592'].index)
   df3 = df3.drop(df3.loc[df3.index=='28'].index)
   df3 = df3.drop(df3.loc[df3.index=='30112'].index)
   df3 = df3.drop(df3.loc[df3.index=='34137'].index)
   df3 = df3.drop(df3.loc[df3.index=='4'].index)
   df3 = df3.drop(df3.loc[df3.index=='513'].index)
   df3 = df3.drop(df3.loc[df3.index=='888'].index)
   df3 = df3.drop(df3.loc[df3.index==':040004568'].index)
   df3 = df3.drop(df3.loc[df3.index=='Produto'].index)

   table = pd.ExcelWriter(carteira)
   
   df3.to_excel(table, index=True )
   #saldo_prod.to_excel(table, index=True )
   table.save()
   #excluir arquivo csv
   os.remove(temp)

   return carteira
   









