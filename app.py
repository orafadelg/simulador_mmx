import streamlit as st
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
    st.markdown(f"### **Satisfação**\n\n## {satisfacao:.1f}")

with col3:
    st.metric("Recompra", f"{recompra:.1f}")
    st.metric("Intenção de Pagar Mais", f"{intencao_pagar:.1f}")
    st.metric("Intenção de Recomendar", f"{intencao_recomendar:.1f}")
    st.metric("Força de Marca", f"{forca_marca:.1f}")
