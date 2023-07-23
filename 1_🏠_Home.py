import streamlit as st
from PIL import Image
import pandas as pd
from openpyxl import Workbook
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import requests
import openai


st.set_page_config(
    page_title="Rio Chamagunga",
    page_icon="📑",
    layout="wide"
)

data = pd.read_csv("riochamagunga.csv", encoding="ISO-8859-1", sep=';')
print(data.head())


# Multi-select checkbox to choose points to display
selected_points = st.sidebar.multiselect(
    'Selecione os Pontos', options=data['PONTOS'].tolist(), default=data['PONTOS'].tolist(), disabled=True)

# SelectBox to choose between parameters
selected_parameter = st.sidebar.selectbox('Selecione o Parametero a ser analisado', options=[
                                          'PH', 'CONDUTIVIDADE', 'TURBIDEZ (NTU)', 'TEMPERATURA'], disabled=True)

st.sidebar.write("---")
st.sidebar.success(
    "Desenvolvido por Vinicius Saraiva para a disciplina: ANÁLISE E MONITORAMENTO DE ECOSSISTEMAS AQUÁTICOS")


with st.container():
    st.title("Rio Chamagunga")
    st.subheader("Análise e Monitoramento da Qualidade da Água")
    st.write("A análise e monitoramento da qualidade da água são importantes para reduzir os efeitos das atividades humanas sobre os recursos hídricos. Neste estudo, o objetivo é avaliar os principais parâmetros físico-químicos e biológicos da qualidade da água do rio Chamagunga, localizado em Porto Seguro - BA.")
    st.write("As amostras foram coletadas em seis pontos diferentes do rio, todos no perímetro urbano. Os parâmetros analisados foram:")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("- Oxigênio Dissolvido")
    st.write("- pH")
    st.write("- Temperatura")
    st.write("- Turbidez")
    st.write("- Condutividade Elétrica")
with col2:
    st.write("- Metais")
    st.write("- Salinidade")
    st.write("- Coliformes Totais")
    st.write("- Nitrato (NO3)")
with col3:
    st.write("- Nitrito (NO2)")
    st.write("- Clorofila-a")
    st.write("- Sólidos Dissolvidos Totais (SDT)")
    st.write("- Demanda Bioquímica de Oxigênio (DBO)")
image = Image.open('mapa.png')
st.image(image, caption='Mapa do Rio Chamagunga - Porto Seguro - Ba')
