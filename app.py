import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Simulador de Satisfação - MMX Okiar")

st.markdown("### Ajuste os Atributos de Experiência")

# Valores iniciais de referência para comparação
ref_values = {
    "seguranca": 6.0,
    "responsividade": 6.0,
    "tangivel": 6.0,
    "confiabilidade": 6.0,
    "empatia": 6.0
}

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div style='display: flex; flex-direction: column; align-items: center;'>", unsafe_allow_html=True)
    seguranca = st.slider("Segurança", 0.0, 10.0, ref_values["seguranca"], 0.1)
    st.markdown(f"{((seguranca - ref_values['seguranca']) / ref_values['seguranca'] * 100):+.1f}%")

    responsividade = st.slider("Responsividade", 0.0, 10.0, ref_values["responsividade"], 0.1)
    st.markdown(f"{((responsividade - ref_values['responsividade']) / ref_values['responsividade'] * 100):+.1f}%")

    tangivel = st.slider("Tangível", 0.0, 10.0, ref_values["tangivel"], 0.1)
    st.markdown(f"{((tangivel - ref_values['tangivel']) / ref_values['tangivel'] * 100):+.1f}%")

    confiabilidade = st.slider("Confiabilidade", 0.0, 10.0, ref_values["confiabilidade"], 0.1)
    st.markdown(f"{((confiabilidade - ref_values['confiabilidade']) / ref_values['confiabilidade'] * 100):+.1f}%")

    empatia = st.slider("Empatia", 0.0, 10.0, ref_values["empatia"], 0.1)
    st.markdown(f"{((empatia - ref_values['empatia']) / ref_values['empatia'] * 100):+.1f}%")
    st.markdown("</div>", unsafe_allow_html=True)

# Cálculos
satisfacao = 0.25 * seguranca + 0.2 * responsividade + 0.15 * tangivel + 0.3 * confiabilidade + 0.1 * empatia
ref_satisfacao = 0.25 * ref_values['seguranca'] + 0.2 * ref_values['responsividade'] + 0.15 * ref_values['tangivel'] + 0.3 * ref_values['confiabilidade'] + 0.1 * ref_values['empatia']
satisfacao_change = (satisfacao - ref_satisfacao) / ref_satisfacao * 100

recompra = satisfacao * 0.35 + 6.0
intencao_pagar = satisfacao * 0.2 + 6.0
intencao_recomendar = satisfacao * 0.3 + 6.0
forca_marca = satisfacao * 0.15 + 6.0

ref_recompra = ref_satisfacao * 0.35 + 6.0
ref_intencao_pagar = ref_satisfacao * 0.2 + 6.0
ref_intencao_recomendar = ref_satisfacao * 0.3 + 6.0
ref_forca_marca = ref_satisfacao * 0.15 + 6.0

with col2:
    st.markdown("<div style='display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;'>", unsafe_allow_html=True)
    st.markdown(f"### **Satisfação**\n\n## {satisfacao:.1f}")
    st.markdown(f"{satisfacao_change:+.1f}%")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div style='display: flex; flex-direction: column; align-items: center;'>", unsafe_allow_html=True)
    st.metric("Recompra", f"{recompra:.1f}", f"{(recompra - ref_recompra)/ref_recompra*100:+.1f}%")
    st.metric("Intenção de Pagar Mais", f"{intencao_pagar:.1f}", f"{(intencao_pagar - ref_intencao_pagar)/ref_intencao_pagar*100:+.1f}%")
    st.metric("Intenção de Recomendar", f"{intencao_recomendar:.1f}", f"{(intencao_recomendar - ref_intencao_recomendar)/ref_intencao_recomendar*100:+.1f}%")
    st.metric("Força de Marca", f"{forca_marca:.1f}", f"{(forca_marca - ref_forca_marca)/ref_forca_marca*100:+.1f}%")
    st.markdown("</div>", unsafe_allow_html=True)
