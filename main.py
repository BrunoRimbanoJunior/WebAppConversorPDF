import streamlit as st
from pdf_carteira_tabula import converter_carteira
from pdf_estoque_tabula import converter_estoque_tabula
from datetime import datetime



def converter_pdf(file, tipo):
    if tipo=='Estoque':
        st.warning('Convertendo Estoque.....')
        converter_estoque_tabula(file)
        
    else:
        st.warning('Convertendo Carteira.....')
        converter_carteira(file)
        



st.title('CONVERSOR DE ARQUIVOS PDF')

arquivo = st.file_uploader('Selecione um arquivo', type=['pdf'],accept_multiple_files=False, )

#tipo = st.checkbox('Tipo Estoque', key='tipo')
tipo = st.selectbox('Tipo de Arquivo', ['Estoque', 'Carteira'])
st.write(f'Tipo de pdf Selecionado: {tipo}')
data = datetime.now().strftime('%d%m%Y_%H%M')

if tipo == 'Estoque':
    filename = 'ESTOQUE_METAGAL_'+data+'.xlsx'
else:
    filename = 'CARTEIRA_METAGAL_'+data+'.xlsx'


if arquivo:
    result = st.button(f'Converter {tipo}', type='primary', on_click=converter_pdf, args=(arquivo, tipo))

    if result:
        st.success('Arquivo Convertido.....')
        with open('temp.xlsx', 'rb') as file:
            st.download_button('Download', file_name=filename, data=file, mime='text/plain/xlsx')
            
else:
    st.warning('Selecione um arquivo')