import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(layout="wide")
st.title("Simulador de Satisfação - MMX Okiar")

st.markdown("### Ajuste os Atributos de Experiência")

col1, col2, col3 = st.columns(3)

with col1:
    seguranca = st.slider("Segurança", 0.0, 10.0, 5.0, 0.1)
    responsividade = st.slider("Responsividade", 0.0, 10.0, 5.0, 0.1)
    tangivel = st.slider("Tangível", 0.0, 10.0, 5.0, 0.1)
    confiabilidade = st.slider("Confiabilidade", 0.0, 10.0, 5.0, 0.1)
    empatia = st.slider("Empatia", 0.0, 10.0, 5.0, 0.1)

satisfacao = 0.25 * seguranca + 0.2 * responsividade + 0.15 * tangivel + 0.3 * confiabilidade + 0.1 * empatia
recompra = satisfacao * 0.35 + 6.0
intencao_pagar = satisfacao * 0.2 + 6.0
intencao_recomendar = satisfacao * 0.3 + 6.0
forca_marca = satisfacao * 0.15 + 6.0

with col2:
    st.metric("Satisfação", f"{satisfacao:.1f}")
    st.metric("Recompra", f"{recompra:.1f}")
    st.metric("Intenção de Pagar Mais", f"{intencao_pagar:.1f}")
    st.metric("Intenção de Recomendar", f"{intencao_recomendar:.1f}")
    st.metric("Força de Marca", f"{forca_marca:.1f}")

# Simulação de dados para séries históricas
tempo = ["Onda 1", "Onda 2", "Onda 3", "Onda 4", "Onda 5"]
cliente = [5, 5.5, 6, 6.5, 7]
concorrente = [5.5, 6, 6, 6.5, 6.8]

fig1, ax1 = plt.subplots()
ax1.plot(tempo, cliente, label="Cliente")
ax1.plot(tempo, concorrente, label="Concorrente")
ax1.set_ylim([0, 10])
ax1.set_title("Satisfação - Série Histórica")
ax1.legend()
st.pyplot(fig1)

# Comparativo na jornada
etapas = ["Descoberta", "Pesquisa", "Cadastro", "Onboarding", "Uso Inicial", "Engajamento", "Monetização", "Retenção"]
cliente_jornada = [7, 7.5, 8, 8.5, 8, 8.5, 8, 7.5]
concorrente_jornada = [6.5, 7, 7.5, 7.5, 7.5, 8, 7.5, 7]

fig2, ax2 = plt.subplots()
x = np.arange(len(etapas))
width = 0.35
ax2.bar(x - width/2, cliente_jornada, width, label='Cliente')
ax2.bar(x + width/2, concorrente_jornada, width, label='Concorrente')
ax2.set_xticks(x)
ax2.set_xticklabels(etapas, rotation=45, ha='right')
ax2.set_ylim([0, 10])
ax2.set_title("Satisfação na Jornada")
ax2.legend()
st.pyplot(fig2)

# Tabela resumo
data = {
    "Indicador": ["Satisfação", "Recompra", "Pagar Mais", "Recomendar", "Força de Marca"],
    "Valor": [satisfacao, recompra, intencao_pagar, intencao_recomendar, forca_marca]
}
df = pd.DataFrame(data)
st.markdown("### Resumo dos Indicadores")
st.dataframe(df.style.format({"Valor": "{:.1f}"}))
