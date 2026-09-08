import streamlit as st
from datetime import datetime

# Configuração inicial da página com o ícone personalizado da Família Siqueira (Foto 2)
st.set_page_config(
    page_title="App Família Siqueira | Alta Performance",
    page_icon="https://raw.githubusercontent.com/jecyjava/Rotina-Casa-Siqueira/main/perfil.jpg", # Se preferir, o ícone oficial da aba
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização CSS avançada para dar cara de App Mobile Compacto e Elegante
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f5;
    }
    h1, h2, h3 {
        color: #d53f8c !important;
        text-align: center;
    }
    .stButton>button {
        background-color: #ed64a6;
        color: white;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        width: 100%;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #b83280;
        color: white;
    }
    /* Reduzindo espaços verticais vazios para parecer um App real */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        max-width: 600px;
    }
    .card-perfil {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
        text-align: center;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Gerenciamento de Estado para a Tela de Autenticação/Seleção
if 'usuario_logado' not in st.session_state:
    st.session_state.usuario_logado = None

dia_semana = datetime.now().weekday()

# ==========================================
# TELA DE LOGIN / SELEÇÃO DE PERFIL (Capa do App)
# ==========================================
if st.session_state.usuario_logado is None:
    st.markdown("<h1 style='color: #d53f8c;'>🎀 Família Siqueira</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Selecione o seu perfil para entrar no painel:</p>", unsafe_allow_html=True)
    
    col_l1, col_l2, col_l3 = st.columns(3)
    
    with col_l1:
        if st.button("👑 Jecy\n(Rosa)"):
            st.session_state.usuario_logado = "Jecy"
            st.rerun()
            
    with col_l2:
        if st.button("👔 Paulo\n(Azul)"):
            st.session_state.usuario_logado = "Paulo"
            st.rerun()
            
    with col_l3:
        if st.button("👧 Sofia\n(Xadrez)"):
            st.session_state.usuario_logado = "Sofia"
            st.rerun()
            
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 12px; color: #b83280;'>Desenvolvido por: Jecy Java</p>", unsafe_allow_html=True)

# ==========================================
# PERFIL 1: JECY (TEMA ROSA - COMPACTO)
# ==========================================
elif st.session_state.usuario_logado == "Jecy":
    if st.button("⬅️ Trocar de Perfil"):
        st.session_state.usuario_logado = None
        st.rerun()
        
    st.header("👑 Painel da Jecy")
    st.markdown("<p style='text-align: center; font-size: 13px; color: #666;'>Foco na Trizepatida (2.5mg), meta -17kg e treinos</p>", unsafe_allow_html=True)
    
    aba_rotina, aba_dieta, aba_treino, aba_progresso, aba_diario = st.tabs([
        "🎯 Rotina", "🥗 Dieta", "💪 Treino", "📈 Metas", "📓 Diário"
    ])
    
    with aba_rotina:
        st.subheader("⚙️ Rotina Flexível de Hoje")
        rotina_j = st.text_area("Ajuste livre dos horários:", value="04:50 Acordar | 05:10 Musculação + Bicicleta | 06:40 Casa | 09:00 Home Office | 18:30 Lutas")
        if st.button("Salvar Rotina"):
            st.success("Atualizado!")

        st.subheader("💧 Água (Meta: 3L)")
        if 'agua_j' not in st.session_state: st.session_state.agua_j = 0
        c1, c2 = st.columns(2)
        with c1:
            if st.button("+ 300ml"): st.session_state.agua_j += 300
        with c2:
            if st.button("Zerar"): st.session_state.agua_j = 0
        st.progress(min(st.session_state.agua_j / 3000, 1.0))
        st.write(f"Total: **{st.session_state.agua_j}ml** / 3000ml")

    with aba_dieta:
        st.subheader("🥗 Cardápio & Calorias")
        st.number_input("Meta Calorias (kcal)", value=1400)
        st.text_area("Cardápio Diário:", value="- Desjejum: Café + Trizepatida\n- Almoço: Frango + Salada\n- Jantar: Omelete proteica")
        st.button("Salvar Cardápio")

    with aba_treino:
        st.subheader("💪 Treinos da Semana")
        st.info("Seg a Sex: Musculação + Cardio às 05:00 | Noites de Luta (Seg/Ter/Qui)")

    with aba_progresso:
        st.subheader("📈 Acompanhamento (-17kg)")
        st.number_input("Peso Atual (kg):", value=83.0, step=0.1)
        st.file_uploader("Enviar Foto de Evolução", type=["png", "jpg", "jpeg"])

    with aba_diario:
        st.subheader("📓 Diário Pessoal")
        st.text_area("Notas e reflexões:", placeholder="Escreva aqui...")
        st.button("Salvar Nota")

# ==========================================
# PERFIL 2: PAULO (TEMA AZUL - COMPACTO)
# ==========================================
elif st.session_state.usuario_logado == "Paulo":
    # Estilização dinâmica para o Azul do Paulo
    st.markdown("""
        <style>
        h1, h2, h3 { color: #2b6cb0 !important; }
        .stButton>button { background-color: #3182ce; color: white; }
        .stButton>button:hover { background-color: #2b6cb0; color: white; }
        </style>
    """, unsafe_allow_html=True)
    
    if st.button("⬅️ Trocar de Perfil"):
        st.session_state.usuario_logado = None
        st.rerun()
        
    st.header("👔 Painel do Paulo")
    st.markdown("<p style='text-align: center; font-size: 13px; color: #666;'>Acorda às 07:00 | Negócios, Dieta & Ministério</p>", unsafe_allow_html=True)
    
    aba_p1, aba_p2, aba_p3, aba_p4, aba_p5, aba_p6 = st.tabs([
        "⚙️ Rotina", "💼 CRM", "🥗 Dieta", "💪 Treino", "📖 Bíblia", "📓 Diário"
    ])
    
    with aba_p1:
        st.subheader("⚙️ Rotina Flexível (Acorda 07:00)")
        st.text_area("Ajuste livre do dia:", value="07:00 Café em família | 08:30 Vendas (Coiffer/Lizze) | 17:00 Hipertrofia | 20:00 Estudo Bíblico")
        st.button("Salvar Rotina")

    with aba_p2:
        st.subheader("📊 CRM de Cosméticos")
        st.write("Marcas: **Coiffer, Matize, Venulti, Donati, Lizze**")
        if 'cli_p' not in st.session_state: st.session_state.cli_p = ["Salão Master Hair"]
        novo_c = st.text_input("Novo Salão / Cliente:")
        if st.button("Cadastrar"):
            st.session_state.cli_p.append(novo_c)
            st.success("Salva!")
        st.write("Clientes:", st.session_state.cli_p)

    with aba_p3:
        st.subheader("🥗 Dieta (Ganho de Massa)")
        st.number_input("Meta Calórica (kcal)", value=2800)
        st.text_area("Dieta Diária:", value="- Vitamina de abacate + Whey + Ovos\n- Almoço: Arroz, feijão, 250g carne\n- Jantar: Batata doce e frango")
        st.button("Salvar Dieta")

    with aba_p4:
        st.subheader("💪 Treinos de Hipertrofia")
        st.text_area("Foco Diário:", value="Treino A: Membros Superiores com progressão de carga.")
        st.button("Salvar Treino")

    with aba_p5:
        st.subheader("📖 Bíblia & Esboços")
        st.text_input("Pesquisar Passagem (ex: Salmos 23)")
        st.text_area("Criar/Editar Esboço de Mensagem:", placeholder="Escreva o esboço do sermão...")
        st.button("Salvar Esboço")

    with aba_p6:
        st.subheader("📓 Diário Ministerial e Vendas")
        st.text_area("Anotações gerais:", placeholder="Escreva...")
        st.button("Salvar Anotação")

# ==========================================
# PERFIL 3: SOFIA (XADREZ REAL & JOGOS)
# ==========================================
elif st.session_state.usuario_logado == "Sofia":
    if st.button("⬅️ Trocar de Perfil"):
        st.session_state.usuario_logado = None
        st.rerun()
        
    st.header("👧 Painel da Sofia")
    st.markdown("<p style='text-align: center; font-size: 13px; color: #666;'>7 Anos | Responsabilidade, Lutas & Xadrez Real</p>", unsafe_allow_html=True)
    
    aba_s1, aba_s2 = st.tabs(["✨ Minha Rotina", "♟️ Xadrez Real (2 Pessoas / Bot)"])
    
    with aba_s1:
        st.subheader("📋 Meu Checklist")
        st.checkbox("Arrumar a cama sozinha")
        st.checkbox("Colocar meu cereal de manhã")
        st.checkbox("Lição da escola")
        st.checkbox("Banho tomado")
        st.checkbox("Tempo de tela (1-2h)")
        
        if dia_semana == 0:
            st.warning("🥋 Hoje tem **Jiu-Jitsu** às 18:30!")
        elif dia_semana in [1, 3]:
            st.warning("🥋 Hoje tem **Muay Thai** às 18:00!")
        else:
            st.success("✨ Descanso das lutas hoje!")

    with aba_s2:
        st.subheader("♟️ Partida Real de Xadrez")
        st.write("Para jogar partidas reais de xadrez (contra outra pessoa no mesmo aparelho ou contra um robô inteligente), integremos diretamente o motor oficial embutido:")
        
        # Incorporação limpa e responsiva de um tabuleiro de xadrez real via widget web otimizado para mobile
        st.markdown("""
            <div style="text-align: center;">
                <iframe src="https://lichess.org/paX28x4t?theme=auto&bg=auto" width="100%" height="400px" style="border:none; border-radius: 12px;"></iframe>
                <p style="font-size: 11px; color: #666; margin-top: 5px;">Tabuleiro interativo online (Jogue livremente ou treine posições).</p>
            </div>
        """, unsafe_allow_html=True)
        
        if 'pontos_sofia' not in st.session_state: st.session_state.pontos_sofia = 50
        st.metric(label="🏆 Seus Pontos de Xadrez", value=st.session_state.pontos_sofia)
        if st.button("Ganhei uma Partida de Xadrez! (+20 pts)"):
            st.session_state.pontos_sofia += 20
            st.balloons()
            st.success("Parabéns pela vitória no tabuleiro!")

# Rodapé minimalista do app
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 11px; color: #d53f8c;'>Jecy Java | Família Siqueira</p>", unsafe_allow_html=True)
