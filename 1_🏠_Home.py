import streamlit as st
from PIL import Image
import pandas as pd
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

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

data = pd.read_csv("riochamagunga.csv", encoding="ISO-8859-1", sep=';')
print(data.head())


st.set_option('deprecation.showPyplotGlobalUse', False)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0.5rem;
                    padding-right: 0rem;
    
                }
                
                
        </style>
        """, unsafe_allow_html=True)

imagem = Image.open('banner.png')
st.image (imagem, caption='')

st.sidebar.write("---")
st.sidebar.info(
    "A plataforma que monitora a qualidade da água do rio que nos abastece não é apenas um recurso técnico, é a sentinela silenciosa que guarda a pureza da vida que flui através de nossas torneiras, garantindo a saúde e a segurança de nossa comunidade a cada gota consumida.")

# Multi-select checkbox to choose points to display
#selected_points = st.sidebar.multiselect(
 #   'Selecione os Pontos', options=data['PONTOS'].tolist(), default=data['PONTOS'].tolist(), disabled=True)

# SelectBox to choose between parameters
#selected_parameter = st.sidebar.selectbox('Selecione o Parametero a ser analisado', options=[
     #                                     'PH', 'CONDUTIVIDADE', 'TURBIDEZ (NTU)', 'TEMPERATURA'], disabled=True)

st.sidebar.write("---")
st.sidebar.success(
    "Desenvolvido por Vinicius Saraiva junto ao Grupo de Pesquisa NuPEcoTropic")


with st.container():
    st.subheader("Contexto")
    st.write("A análise e monitoramento da qualidade da água são importantes para reduzir os efeitos das atividades humanas sobre os recursos hídricos. Neste estudo, o objetivo é analisar os principais parâmetros físico-químicos da qualidade da água. Os dados são coletados por populares treinados para utilizacao correta de uma sonda multiparamêtros e transmissão dos dados coletados.")
    st.write("Atualmente monitoramos os rios: Rio dos Mangues, Rio Utinga e Rio Buranhém, todos no perímetro urbano. Os parâmetros analisados foram:")

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
image = Image.open('buranhem.jpeg')
st.image(image, caption='Vista aérea do Rio Buranhém - Porto Seguro - Ba')
