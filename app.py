import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="App Família Siqueira | Rotina & Performance",
    page_icon="🌸",
    layout="wide"
)

# Estilização visual em tons de rosa claro e clean
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
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎀 Painel Integrado da Família Siqueira")
st.write("Gerenciamento de rotina, alta performance, negócios e desenvolvimento infantil.")

# --- SELETOR DE PERFIL (MÚLTIPLOS USUÁRIOS) ---
perfil_selecionado = st.sidebar.selectbox(
    "👤 Escolha o Perfil:",
    ["Jecy (Minha Rotina & Trizepatida)", "Paulo (Negócios, Treino & Ministério)", "Sofia (Painel Infantil & Xadrez)"]
)

dia_semana = datetime.now().weekday()

# ==========================================
# PERFIL 1: JECY
# ==========================================
if perfil_selecionado == "Jecy (Minha Rotina & Trizepatida)":
    st.header("👑 Painel da Jecy")
    st.write("Home office, maternidade sem rede de apoio, treinos e foco na Trizepatida.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎯 Sua Programação de Hoje")
        treinos_jecy = {
            0: "Segunda: Musculação + Bicicleta 05:00 | Jiu-Jitsu da Sofia 18:30",
            1: "Terça: Musculação + Bicicleta 05:00 | Seu Muay Thai 19:00",
            2: "Quarta: Musculação + Bicicleta 05:00 | Noite em família",
            3: "Quinta: Musculação + Bicicleta 05:00 | Seu Muay Thai 19:00",
            4: "Sexta: Musculação + Bicicleta 05:00 | Culto à noite",
            5: "Sábado: Descanso e família",
            6: "Domingo: Culto e preparação da semana"
        }
        st.info(treinos_jecy.get(dia_semana, "Dia de descanso."))
        
        st.subheader("💡 Dicas do Nutri (Trizepatida)")
        st.success("Mantenha a água constante e priorize proteínas logo cedo para proteger sua massa magra nos treinos das 5h!")

    with col2:
        st.subheader("💧 Monitor de Hidratação")
        if 'agua_jecy' not in st.session_state:
            st.session_state.agua_jecy = 0
            
        meta_agua = 3000
        c1, c2 = st.columns(2)
        with c1:
            if st.button("+ 300ml (Jecy)"): st.session_state.agua_jecy += 300
        with c2:
            if st.button("Resetar Água"): st.session_state.agua_jecy = 0
            
        progresso = min(st.session_state.agua_jecy / meta_agua, 1.0)
        st.progress(progresso)
        st.write(f"Total: **{st.session_state.agua_jecy}ml** / {meta_agua}ml")

# ==========================================
# PERFIL 2: PAULO
# ==========================================
elif perfil_selecionado == "Paulo (Negócios, Treino & Ministério)":
    st.header("👔 Painel do Paulo")
    st.write("Foco em ganho de massa, dieta, homem de Deus, pregador e CRM de Cosméticos.")
    
    tab1, tab2, tab3 = st.tabs(["🚀 Rotina & Dieta", "💼 CRM de Vendas (Cosméticos)", "📖 Homem de Deus & Ministério"])
    
    with tab1:
        st.subheader("💪 Alta Performance & Ganho de Massa")
        st.markdown("""
        * **04:50 / 05:00:** Despertar, pré-treino e foco na hipertrofia.
        * **Treinos:** Musculação pesada + Cardio estratégico.
        * **Alimentação (Ganho de Massa):** Superávit calórico limpo, alto consumo de proteínas e carboidratos complexos para sustentar o volume muscular.
        """)
        
    with tab2:
        st.subheader("📊 Mini CRM de Vendas - Cosméticos para Salão")
        st.write("Marcas: **Coiffer, Matize, Venulti, Donati, Lizze**, entre outras.")
        
        if 'clientes' not in st.session_state:
            st.session_state.clientes = [{"nome": "Salão Bella Vista", "status": "Prospecção", "marca": "Coiffer"}]
            
        acao_crm = st.selectbox("Ação rápida:", ["Ver Clientes", "Cadastrar Novo Cliente", "Registrar Pedido/Venda", "Cobranças Pendentes"])
        
        if acao_crm == "Ver Clientes":
            st.write("### Sua Carteira de Clientes:")
            for c in st.session_state.clientes:
                st.info(f"Salão/Cliente: **{c['nome']}** | Status: **{c['status']}** | Foco: {c['marca']}")
                
        elif acao_crm == "Cadastrar Novo Cliente":
            nome_cli = st.text_input("Nome do Salão / Cliente")
            marca_cli = st.text_input("Marca de Interesse (ex: Lizze, Donati...)")
            if st.button("Salvar Cliente"):
                st.session_state.clientes.append({"nome": nome_cli, "status": "Ativo", "marca": marca_cli})
                st.success("Cliente cadastrado com sucesso!")
                
        elif acao_crm == "Registrar Pedido/Venda":
            st.text_input("Detalhes do Pedido de Compra / Venda")
            st.button("Salvar Pedido no Histórico")
            
        elif acao_crm == "Cobranças Pendentes":
            st.write("Nenhuma cobrança em atraso registrada hoje. Ótimo fluxo de caixa!")

    with tab3:
        st.subheader("🙏 Ministério & Palavra")
        st.markdown("""
        * **Provedor e Sacerdote do Lar:** Direcionamento espiritual da família Siqueira.
        * **Pregador da Palavra:** Momentos de estudo bíblico, preparação de mensagens e edificação espiritual.
        """)

# ==========================================
# PERFIL 3: SOFIA
# ==========================================
elif perfil_selecionado == "Sofia (Painel Infantil & Xadrez)":
    st.header("👧 Painel da Sofia (7 Anos)")
    st.write("Sua rotina independente, treinos, tempo de tela e jogos de memória/xadrez!")
    
    aba_rotina, aba_jogos = st.tabs(["✨ Minha Rotina & Responsabilidades", "♟️ Xadrez & Desafios de Memória"])
    
    with aba_rotina:
        st.subheader("📋 Meu Checklist do Dia")
        st.checkbox("Acordar e arrumar a cama sozinha")
        st.checkbox("Colocar meu cereal de manhã")
        st.checkbox("Ir para a escola")
        st.checkbox("Almoçar e revisar a lição")
        st.checkbox("Tomar banho e me arrumar sozinha")
        st.checkbox("Tempo de tela (Limite de 1 a 2 horas)")
        
        st.subheader("🥋 Meus Dias de Luta")
        if dia_semana == 0:
            st.warning("Hoje tem **Jiu-Jitsu** às 18:30! Prepare o quimono!")
        elif dia_semana in [1, 3]:
            st.warning("Hoje tem **Muay Thai** às 18:00! Vamos com tudo!")
        else:
            st.success("Hoje é dia de descanso das lutas. Bom divertimento!")

    with aba_jogos:
        st.subheader("🧠 Área de Jogos e Estímulo de Memória")
        st.write("Complete os desafios de xadrez e memória para somar pontos e subir de nível!")
        
        if 'pontos_sofia' not in st.session_state:
            st.session_state.pontos_sofia = 10
            
        st.metric(label="🏆 Seus Pontos Acumulados", value=st.session_state.pontos_sofia)
        
        st.write("### ♟️ Desafio de Xadrez do Dia:")
        st.write("Qual peça se move em L no tabuleiro de xadrez?")
        resposta = st.radio("Escolha a resposta:", ["Torre", "Cavalo", "Bispo"], index=None)
        
        if st.button("Enviar Resposta"):
            if resposta == "Cavalo":
                st.session_state.pontos_sofia += 5
                st.balloons()
                st.success("🎉 Parabéns! Resposta certa! Você ganhou +5 pontos!")
            elif resposta is not None:
                st.error("Ops! Quase lá. Tente de novo!")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #b83280; font-weight: bold;'>Desenvolvido por: Jecy Java | Família Siqueira</p>", unsafe_allow_html=True)
