import streamlit as st
import pandas as pd
import altair as alt

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
df_historico = pd.DataFrame({
    'Onda': ["Onda 1", "Onda 2", "Onda 3", "Onda 4", "Onda 5"] * 2,
    'Valor': [5, 5.5, 6, 6.5, 7, 5.5, 6, 6, 6.5, 6.8],
    'Tipo': ['Cliente']*5 + ['Concorrente']*5
})

chart_historico = alt.Chart(df_historico).mark_line(point=True).encode(
    x='Onda', y='Valor', color='Tipo'
).properties(
    title='Satisfação - Série Histórica', width=700
)
st.altair_chart(chart_historico)

# Comparativo na jornada
df_jornada = pd.DataFrame({
    'Etapa': ["Descoberta", "Pesquisa", "Cadastro", "Onboarding", "Uso Inicial", "Engajamento", "Monetização", "Retenção"] * 2,
    'Nota': [7, 7.5, 8, 8.5, 8, 8.5, 8, 7.5, 6.5, 7, 7.5, 7.5, 7.5, 8, 7.5, 7],
    'Grupo': ['Cliente']*8 + ['Concorrente']*8
})

chart_jornada = alt.Chart(df_jornada).mark_bar().encode(
    x=alt.X('Etapa:N', sort=None),
    y='Nota:Q',
    color='Grupo:N'
).properties(
    title='Satisfação na Jornada', width=700
)
st.altair_chart(chart_jornada)

# Tabela resumo
data = {
    "Indicador": ["Satisfação", "Recompra", "Pagar Mais", "Recomendar", "Força de Marca"],
    "Valor": [satisfacao, recompra, intencao_pagar, intencao_recomendar, forca_marca]
}
df = pd.DataFrame(data)
st.markdown("### Resumo dos Indicadores")
st.dataframe(df.style.format({"Valor": "{:.1f}"}))
