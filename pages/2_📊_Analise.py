import streamlit as st
from PIL import Image
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import requests
import openai
import json





st.set_page_config(
    page_title="Analise dos Dados Coletados",
    page_icon="📑",
    layout="wide"
)


st.title("Analisando parâmetros físicos da água")
st.write("Rio Chamagunga")

data = pd.read_csv("riochamagunga.csv", encoding="ISO-8859-1", sep=';')


# Multi-select checkbox to choose points to display
selected_points = st.sidebar.multiselect(
    'Selecione os Pontos', options=data['PONTOS'].tolist(), default=data['PONTOS'].tolist())

# SelectBox to choose between parameters
selected_parameter = st.sidebar.selectbox('Selecione o Parametero a ser analisado', options=[
                                          'PH', 'CONDUTIVIDADE', 'TURBIDEZ (NTU)', 'TEMPERATURA'])

st.sidebar.write("---")
st.sidebar.success(
    "Desenvolvido por Vinicius Saraiva para a disciplina: ANÁLISE E MONITORAMENTO DE ECOSSISTEMAS AQUÁTICOS :pencil: ")


# Filter the data based on the selected points
filtered_data = data[data['PONTOS'].isin(selected_points)]

# Define dictionaries with minimum and maximum values for each parameter
parameter_ranges = {
    'PH': (5.9, 9),
    'CONDUTIVIDADE': (115, 300),
    'TURBIDEZ (NTU)': (7.5, 11.2),
    'TEMPERATURA': (23.1, 25.4)
}


# Update the graph based on the selected parameter and points
y_column = selected_parameter
title = f'Valores de {selected_parameter.capitalize()} do(s) ponto(s) selecionado(s)'
yaxis_title = selected_parameter.capitalize()

# Create the bar chart using Plotly Express
fig = px.bar(filtered_data, x='PONTOS', y=y_column, title=title)

# Modify bar properties
fig.update_traces(marker_color='blue', width=0.4)

# Update x-axis and y-axis titles
fig.update_xaxes(title_text='Pontos de Coleta')
fig.update_yaxes(title_text=yaxis_title)

# Add shapes for the ideal range (minimum and maximum values)
min_value, max_value = parameter_ranges[selected_parameter]
fig.add_shape(
    type='line',
    line=dict(color='green', width=2, dash='dash'),
    x0=-0.5,
    y0=min_value,
    x1=5.5,
    y1=min_value,
    xref='x',
    yref='y'
)

fig.add_shape(
    type='line',
    line=dict(color='orange', width=2, dash='dash'),
    x0=-0.5,
    y0=max_value,
    x1=5.5,
    y1=max_value,
    xref='x',
    yref='y'
)

# Add legend next to the graph with the minimum and maximum values according to CONAMA
legend_text = f"Valores segundo o CONAMA:<br>Min: {min_value}<br>Max: {max_value}"
fig.add_trace(
    go.Scatter(
        x=[data['PONTOS'].iloc[0], data['PONTOS'].iloc[-1]],
        y=[max_value, max_value],
        mode='lines',
        line=dict(color='orange', width=4, dash='dash'),
        name=legend_text
    )
)
# Create the histogram using Plotly Express
# hist_fig = px.histogram(filtered_data, x=y_column, nbins=10, title=f'{selected_parameter.capitalize()} Histogram')

# fig1 = ff.create_distplot(
# hist_data, group_labels, bin_size=[.1, .25, .5])

# Show the plot using Streamlit with reduced size
st.plotly_chart(fig, use_container_width=True)

# st.plotly_chart(fig1, use_container_width=True)

# st.plotly_chart(hist_fig, use_container_width=True)
# Código Python

# Get parameter values for analysis using OpenAI GPT-3.5
parameter_values = filtered_data[y_column].tolist()
conama_values = parameter_ranges[selected_parameter]

#pergunta_composta = (
#    "O que é {selected_parameter} <END> ?"
 #   "Qual a importância do {selected_parameter} para as águas de um rio? <END> "
  #  "Qual análise pode ser feita quando um rio tem dois pontos, um com pH de 5.9 e outro com pH de 7, "
   # "quando os índices do CONAMA indicam que para água doce o nível mínimo seria 6.1 e o máximo 8?"
#)
#resposta_composta = openai.Completion.create(engine="gpt-3.5-turbo", prompt=pergunta_composta)

# Make the OpenAI API call for analysis
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
       {"role": "user",
            "content": f'Responda separando por paragrafos, O primeiro paragrafo o titulo é "Você sabe o que é {selected_parameter} ?" e após o titulo  pule uma linha e fale sobre esse parametro de forma curta explicando-o. O segundo paragrafo o titulo é: "Qual a importancia do {selected_parameter} ?", em seguida pule uma linha e fale a importancia desse parametro em um rio. Vale salientar que o segundo paragrafo deve sempre ter a mesma quantidade de linhas do primeiro. No terceiro paragrafo o titulo é "Analise do gráfico", faça uma analise dos dados utilizando as informacoes obtidas com a coleta da agua desse rio, foi coletada agua para analise em 6 pontos diferentes do Rio Chamagunga. O parametro selecionado é {selected_parameter}, o valor encontrado foi {parameter_values}. De acordo com o CONAMA, os valores ideais para esse paramentro, fica entre {conama_values[0]} e {conama_values[1]}. lembrando que deve citar apenas os valores dos pontos selecinados, da seguinte forma: "ponto: valor", com o nome de cada ponto em negrito. A resposta deve vir no formato json, com a seguinte estrutura:a chave se chama respostas e contem id da resposta, titulo da resposta, conteudo da resposta'}
    ]
)


#st.write(completion['choices'][0]['message']['content'])
# Extrair as respostas do objeto 'content'

response = json.loads(completion['choices'][0]['message']['content'])
respondendo = response
meusdados = respondendo['respostas']
st.write (meusdados)


# Configuração de estilo
st.markdown("""
    <style>
    .card {
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.1);
        background-color: #f0f0f0;
    }
    .card-title {
        font-size: 18px;
        font-weight: bold;
    }
    .card-content {
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Crie uma linha com dois cards
col1, col2 = st.columns(2)

# Card 1
col1.markdown(f"""
    <div class="card">
        <div class="card-title">{meusdados[0]['titulo']}</div>
        <div class="card-content">{meusdados[0]['conteudo']}</div>
    </div>
    """, unsafe_allow_html=True)

# Card 2
col2.markdown(f"""
    <div class="card">
        <div class="card-title">{meusdados[1]['titulo']}</div>
        <div class="card-content">{meusdados[1]['conteudo']}</div>
    </div>
    """, unsafe_allow_html=True)

# Crie um espaço vazio
st.empty()
st.write("")
st.write("")

# Crie uma linha com um card
col3 = st.columns(1)

# Card 3
col3[0].markdown(f"""
    <div class="card">
        <div class="card-title">{meusdados[2]['titulo']}</div>
        <div class="card-content">{meusdados[2]['conteudo']}</div>
    </div>
    """, unsafe_allow_html=True)






