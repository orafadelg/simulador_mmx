import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Simulador de Satisfação - MMX Okiar")

st.markdown("""
<style>
.card {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
    text-align: center;
}
.center-card {
    background-color: #c62828;
    border-radius: 10px;
    color: white;
    padding: 40px 20px;
    text-align: center;
    margin: 20px 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("### Ajuste os Atributos de Experiência")

ref_values = {
    "seguranca": 6.0,
    "responsividade": 6.0,
    "tangivel": 6.0,
    "confiabilidade": 6.0,
    "empatia": 6.0
}

col1, col2, col3 = st.columns([1.2, 1, 1.2])

with col1:
    def show_slider(attr, label):
        change = 0
        value = ref_values[attr]
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            value = st.slider(label, 0.0, 10.0, ref_values[attr], 0.1, key=label)
            change = (value - ref_values[attr]) / ref_values[attr] * 100
            color = "green" if change > 0 else ("red" if change < 0 else "black")
            st.markdown(f"<span style='color:{color}; font-weight:bold;'>{change:+.1f}%</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        return value

    seguranca = show_slider("seguranca", "Segurança")
    responsividade = show_slider("responsividade", "Responsividade")
    tangivel = show_slider("tangivel", "Tangível")
    confiabilidade = show_slider("confiabilidade", "Confiabilidade")
    empatia = show_slider("empatia", "Empatia")

satisfacao = 0.25 * seguranca + 0.2 * responsividade + 0.15 * tangivel + 0.3 * confiabilidade + 0.1 * empatia
ref_satisfacao = 0.25 * ref_values['seguranca'] + 0.2 * ref_values['responsividade'] + 0.15 * ref_values['tangivel'] + 0.3 * ref_values['confiabilidade'] + 0.1 * ref_values['empatia']
satisfacao_change = (satisfacao - ref_satisfacao) / ref_satisfacao * 100
color_s = "green" if satisfacao_change > 0 else ("red" if satisfacao_change < 0 else "white")

recompra = satisfacao * 0.35 + 6.0
intencao_pagar = satisfacao * 0.2 + 6.0
intencao_recomendar = satisfacao * 0.3 + 6.0
forca_marca = satisfacao * 0.15 + 6.0

ref_recompra = ref_satisfacao * 0.35 + 6.0
ref_intencao_pagar = ref_satisfacao * 0.2 + 6.0
ref_intencao_recomendar = ref_satisfacao * 0.3 + 6.0
ref_forca_marca = ref_satisfacao * 0.15 + 6.0

with col2:
    with st.container():
        st.markdown("<div class='center-card'>", unsafe_allow_html=True)
        st.markdown(f"<h4><strong>Satisfação</strong></h4><h1 style='margin: 10px 0;'>{satisfacao:.1f}</h1>", unsafe_allow_html=True)
        st.markdown(f"<span style='color:{color_s}; font-size: 18px;'>{satisfacao_change:+.1f}%</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with col3:
    def metric_delta(title, current, reference):
        change = (current - reference) / reference * 100
        color = "green" if change > 0 else ("red" if change < 0 else "black")
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"<strong>{title}</strong><br><h3>{current:.1f}</h3><span style='color:{color}; font-weight:bold;'>{change:+.1f}%</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    metric_delta("Recompra", recompra, ref_recompra)
    metric_delta("Intenção de Pagar Mais", intencao_pagar, ref_intencao_pagar)
    metric_delta("Intenção de Recomendar", intencao_recomendar, ref_intencao_recomendar)
    metric_delta("Força de Marca", forca_marca, ref_forca_marca)
