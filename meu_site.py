import streamlit as st
import pandas as pd

st.set_page_config(page_title='DEV')

with st.container():
    st.subheader('Meu primeiro site')
    st.title('Dashboard de Contrato')
    st.write('Informações sobre os contratos fechados pela Hash&Co ao longo do mês de Maio')
    st.write('Quer aprender Pyhton? [Clique aqui](https://www.hashtagtreinamentos.com/)')

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('resultados.csv')
    return tabela

with st.container():
    st.write('---')
    qtde_dias = st.selectbox('Selecione o período', ["7D", "15D", "21D","30D"])
    num_dias = int(qtde_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x='Data', y='Contratos')