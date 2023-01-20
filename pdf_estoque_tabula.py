import tabula
import pandas as pd
import numpy as np
import os



def converter_estoque_tabula(file):

   
    temp = 'temp.csv'
    tabula.convert_into(file, temp, output_format='csv', pages='all')
    arquivo = 'temp.xlsx'
  
    df = pd.read_csv(temp, names=['CODIGO','DESCRICAO','PGM','PRODUZIDO','SALDO PGM','ESTOQUE','CARTEIRA','SEPARACAO','DISPONIVEL','NECESSIDADE'], encoding='latin-1')    
    
    df2 = df.sort_values(by=['CODIGO'])
    df2['DESCRICAO'].replace('', np.nan, inplace=True)
    df2.dropna(subset=['DESCRICAO'], inplace=True)
    df2['CODIGO'].replace('', np.nan, inplace=True)
    df2['CODIGO'].replace('0', np.nan, inplace=True)
    df2.dropna(subset=['CODIGO'], inplace=True)
    filtro = df2['CODIGO'] != 'Classe'
    df2 = df2[filtro]
    filtro = df2['CODIGO'] != 'PRODUTO'
    df2 = df2[filtro]
    df2 = df2.drop(columns=['DESCRICAO', 'PGM', 'PRODUZIDO','SALDO PGM','ESTOQUE','CARTEIRA','SEPARACAO', 'NECESSIDADE'])
    df2['DISPONIVEL'] = pd.to_numeric(df2['DISPONIVEL'], errors='coerce', downcast='integer')
    
   
    #CASO QUEIRA SALVAR EM UMA TABELA EXCEL JA EXISTENTE, USAR AS LINHAS COMENTADAS, AJUSTANDO A VARIAVEL DIRE PARA A PLANILHA CORRETA
    #table = pd.ExcelWriter(dire)
    
    df2.to_excel(arquivo, sheet_name='ESTOQUE_FABRICA',index=False )
    
    os.remove(temp)


