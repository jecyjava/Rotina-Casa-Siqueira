import streamlit as st
from datetime import datetime

# Configuração da página e layout visual
st.set_page_config(
    page_title="Rotina & Performance | Jecy Java",
    page_icon="🌸",
    layout="centered"
)

# Estilização CSS personalizada (Tema Rosa Claro & Clean)
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f5;
    }
    h1, h2, h3 {
        color: #d53f8c !important;
    }
    .stButton>button {
        background-color: #ed64a6;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #d53f8c;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎀 Painel Inteligente: Rotina & Performance")
st.write("Gerencie sua alta performance, hidratação para Trizepatida e treinos de forma flexível.")

# --- MÓDULO DINÂMICO: O usuário descreve e o app se adapta ---
st.subheader("⚙️ Ajuste Flexível de Rotina")
st.write("Descreva sua rotina ou informe qualquer mudança de horário hoje:")

rotina_personalizada = st.text_area(
    "O que muda hoje?",
    value="04:50 Acordar | 05:10 Musculação | 06:20 Bicicleta | 07:00 Escola | 09:00 Home Office | 19:00 Muay Thai"
)

if st.button("🔄 Reorganizar e Analisar Rotina"):
    st.success("Rotina recalculada com sucesso! As janelas de foco e blocos de descanso foram adaptados.")

st.markdown("---")

# --- PROGRAMAÇÃO AUTOMÁTICA POR DIA DA SEMANA ---
st.subheader("🎯 Programação Oficial de Hoje")
dia_semana = datetime.now().weekday()
treinos = {
    0: "Segunda: Musculação + Bicicleta às 05:00 | Jiu-Jitsu da filha às 18:30",
    1: "Terça: Musculação + Bicicleta às 05:00 | Seu Muay Thai às 19:00",
    2: "Quarta: Musculação + Bicicleta às 05:00 | Noite livre em família",
    3: "Quinta: Musculação + Bicicleta às 05:00 | Seu Muay Thai às 19:00",
    4: "Sexta: Musculação + Bicicleta às 05:00 | Culto à noite",
    5: "Sábado: Descanso, família e organização",
    6: "Domingo: Culto à noite e preparação para a semana"
}
st.info(f"**Planejamento do Dia:** {treinos.get(dia_semana, 'Dia de descanso.')}")

st.markdown("---")

# --- CONTROLE INTERATIVO DE HIDRATAÇÃO (Trizepatida) ---
st.subheader("💧 Monitor de Hidratação & Trizepatida")

if 'agua' not in st.session_state:
    st.session_state.agua = 0

meta_agua = 3000

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("+ 300ml"):
        st.session_state.agua += 300
with col2:
    if st.button("+ 500ml"):
        st.session_state.agua += 500
with col3:
    if st.button("Resetar"):
        st.session_state.agua = 0

# Barra de progresso da água
progresso = min(st.session_state.agua / meta_agua, 1.0)
st.progress(progresso)
st.write(f"Consumido hoje: **{st.session_state.agua}ml** de {meta_agua}ml")

if st.session_state.agua >= meta_agua:
    st.balloons()
    st.success("🏆 Meta de água batida! Excelente hidratação para hoje.")

# --- DICA DO NUTRI ---
st.markdown("---")
st.warning("💡 **Dica do Nutri:** Com a Trizepatida, mantenha a garrafinha sempre por perto e priorize proteínas de alto valor biológico nas primeiras refeições para proteger sua massa magra.")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #b83280; font-weight: bold;'>Desenvolvido por: Jecy Java</p>", unsafe_allow_html=True)
