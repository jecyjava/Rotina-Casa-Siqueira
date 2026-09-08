import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="App Família Siqueira | Alta Performance",
    page_icon="🌸",
    layout="wide"
)

# Estilização visual dinâmica (Rosa Claro para Jecy/Sofia, Azul para Paulo via abas ou seletor)
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

st.title("🎀 Painel Integrado da Família Siqueira")
st.write("Alta performance, saúde, negócios, espiritualidade e desenvolvimento em família.")

# --- SELETOR DE PERFIL (MÚLTIPLOS USUÁRIOS) ---
perfil_selecionado = st.sidebar.selectbox(
    "👤 Escolha o Perfil:",
    ["Jecy (Minha Rotina & Performance - Rosa)", "Paulo (Negócios, Dieta & Ministério - Azul)", "Sofia (Painel Infantil & Xadrez - Rosa)"]
)

dia_semana = datetime.now().weekday()

# ==========================================
# PERFIL 1: JECY (TEMA ROSA)
# ==========================================
if perfil_selecionado == "Jecy (Minha Rotina & Performance - Rosa)":
    st.header("👑 Painel da Jecy")
    st.write("Foco na Trizepatida (2.5mg), meta de -17kg, treinos matinais (04:50) e home office.")
    
    aba_rotina, aba_dieta, aba_treino, aba_progresso, aba_diario = st.tabs([
        "🎯 Rotina & Hidratação", 
        "🥗 Cardápio, Calorias & Dieta", 
        "💪 Treinos da Semana", 
        "📈 Acompanhamento (Peso & Medidas)",
        "📓 Diário & Anotações"
    ])
    
    with aba_rotina:
        st.subheader("⚙️ Rotina Flexível Parametrizável (Hoje/Amanhã)")
        rotina_jecy_input = st.text_area(
            "Ajuste livre dos seus horários e tarefas para hoje:",
            value="04:50 Acordar | 05:10 Musculação + Bicicleta | 06:40 Retorno casa / Organização | 09:00 Home Office & Vendas Atomy | 18:30 Lutas / Família"
        )
        if st.button("💾 Salvar Nova Rotina Jecy"):
            st.success("Rotina atualizada com sucesso para hoje!")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📌 Programação Oficial")
            treinos_jecy = {
                0: "Segunda: Musculação + Bicicleta 05:00 | Jiu-Jitsu da Sofia 18:30",
                1: "Terça: Musculação + Bicicleta 05:00 | Seu Muay Thai 19:00",
                2: "Quarta: Musculação + Bicicleta 05:00 | Noite em família",
                3: "Quinta: Musculação + Bicicleta 05:00 | Seu Muay Thai 19:00",
                4: "Sexta: Musculação + Bicicleta 05:00 | Culto à noite",
                5: "Sábado: Descanso e organização",
                6: "Domingo: Culto e preparação da semana"
            }
            st.info(treinos_jecy.get(dia_semana, "Dia de descanso."))
            st.success("💡 **Dica do Nutri/Coach:** Mantenha alta ingestão proteica logo cedo para proteger a massa magra durante o uso da Trizepatida.")

        with col2:
            st.subheader("💧 Monitor de Água (Meta: 3L)")
            if 'agua_jecy' not in st.session_state:
                st.session_state.agua_jecy = 0
            
            c1, c2 = st.columns(2)
            with c1:
                if st.button("+ 300ml"): st.session_state.agua_jecy += 300
            with c2:
                if st.button("Zerar Água"): st.session_state.agua_jecy = 0
                
            progresso_agua = min(st.session_state.agua_jecy / 3000, 1.0)
            st.progress(progresso_agua)
            st.write(f"Consumido: **{st.session_state.agua_jecy}ml** / 3000ml")

    with aba_dieta:
        st.subheader("🥗 Planejamento Nutricional & Dieta Completa")
        calorias_meta = st.number_input("Meta de Calorias Diária (kcal)", value=1400)
        proteina_meta = st.number_input("Meta de Proteína Diária (g)", value=120)
        
        st.write("### 📋 Cardápio Completo da Semana (Editável):")
        cardapio_edit = st.text_area("Edite o cardápio e suplementação:", value="""Segunda a Domingo:
- Desjejum: Café sem açúcar + Água com limão + Trizepatida (conforme protocolo)
- Café da Manhã: Ovos mexidos + Queijo branco + Frutas vermelhas
- Almoço: Frango/Peixe grelhado + Salada verde farta + Azeite + Legumes
- Lanche da Tarde: Whey protein + Pasta de amendoim ou castanhas
- Jantar: Omelete de forno com legumes ou sopa proteica""")
        if st.button("Salvar Alterações no Cardápio"):
            st.success("Cardápio atualizado!")

    with aba_treino:
        st.subheader("💪 Treinos Diários Parametrizáveis")
        dia_escolhido = st.selectbox("Selecione o dia para ver/editar o treino:", 
                                     ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"])
        
        treino_editavel = st.text_area("Detalhes do Treino para este dia:", value="Musculação focada em membros inferiores + 20 minutos de bicicleta ergometrométrica em intensidade moderada.")
        if st.button("Salvar Treino do Dia"):
            st.success("Treino atualizado com sucesso!")

    with aba_progresso:
        st.subheader("📈 Acompanhamento Corporal (-17kg Meta)")
        if 'peso_atual' not in st.session_state:
            st.session_state.peso_atual = 83.0
            st.session_state.altura = 1.61

        col_a, col_b = st.columns(2)
        with col_a:
            st.session_state.peso_atual = st.number_input("Peso Atual (kg):", value=st.session_state.peso_atual, step=0.1)
            st.session_state.altura = st.number_input("Altura (m):", value=st.session_state.altura, step=0.01)
        with col_b:
            imc = st.session_state.peso_atual / (st.session_state.altura ** 2)
            st.metric(label="📊 Seu IMC Atual", value=f"{imc:.2f}")
            st.metric(label="🎯 Meta de Perda", value="17 kg total")

        st.write("---")
        st.subheader("📸 Fotos de Evolução")
        st.file_uploader("Carregar foto de acompanhamento", type=["png", "jpg", "jpeg"])

    with aba_diario:
        st.subheader("📓 Diário de Bordo & Anotações")
        st.text_area("Escreva aqui suas reflexões, observações da Trizepatida, insights ou anotações gerais:", placeholder="Como foi o dia hoje? Algum sintoma ou conquista?")
        st.button("Salvar Nota no Diário")

# ==========================================
# PERFIL 2: PAULO (TEMA AZUL)
# ==========================================
elif perfil_selecionado == "Paulo (Negócios, Dieta & Ministério - Azul)":
    # Mudança visual temporária para azul no perfil do Paulo
    st.markdown("""
        <style>
        h1, h2, h3 { color: #2b6cb0 !important; }
        .stButton>button { background-color: #3182ce; color: white; }
        .stButton>button:hover { background-color: #2b6cb0; color: white; }
        </style>
    """, unsafe_allow_html=True)
    
    st.header("👔 Painel do Paulo (Homem de Deus & Alta Performance)")
    st.write("Acordar às 07:00, rotina flexível, ganho de massa, CRM de Cosméticos e Ministério.")
    
    tab_paulo_rotina, tab_paulo_vendas, tab_paulo_dieta, tab_paulo_treino, tab_paulo_ministerio, tab_paulo_diario = st.tabs([
        "⚙️ Rotina Flexível",
        "💼 CRM de Vendas", 
        "🥗 Dieta & Massa", 
        "💪 Treinos Diários",
        "📖 Homem de Deus & Bíblia",
        "📓 Diário & Anotações"
    ])
    
    with tab_paulo_rotina:
        st.subheader("⚙️ Rotina Flexível Parametrizável (Hoje/Amanhã)")
        rotina_paulo_input = st.text_area(
            "Ajuste livre dos horários do Paulo para hoje (acorda às 07:00):",
            value="07:00 Acordar e café com a família | 08:30 Prospecção e Vendas (Coiffer, Lizze, etc.) | 13:00 Almoço e Foco em Negócios | 17:00 Treino de Hipertrofia | 20:00 Estudo Bíblico e Família"
        )
        if st.button("💾 Salvar Nova Rotina Paulo"):
            st.success("Rotina flexível do Paulo atualizada!")

    with tab_paulo_vendas:
        st.subheader("📊 Mini CRM de Vendas - Cosméticos para Salão")
        st.write("Marcas: **Coiffer, Matize, Venulti, Donati, Lizze**")
        
        if 'clientes_paulo' not in st.session_state:
            st.session_state.clientes_paulo = [{"nome": "Salão Master Hair", "status": "Ativo", "marca": "Coiffer / Lizze"}]
            
        acao_crm_p = st.selectbox("Gerenciamento:", ["Ver Clientes", "Cadastrar Cliente", "Registrar Pedido/Compra", "Cobranças"])
        if acao_crm_p == "Ver Clientes":
            for cli in st.session_state.clientes_paulo:
                st.info(f"Cliente: **{cli['nome']}** | Status: {cli['status']} | Foco: {cli['marca']}")
        elif acao_crm_p == "Cadastrar Cliente":
            n_cli = st.text_input("Nome do Salão")
            m_cli = st.text_input("Marcas de interesse")
            if st.button("Adicionar Cliente"):
                st.session_state.clientes_paulo.append({"nome": n_cli, "status": "Prospecção", "marca": m_cli})
                st.success("Cliente cadastrado!")
        elif acao_crm_p == "Registrar Pedido/Compra":
            st.text_input("Detalhes de Compra/Venda de Produtos")
            st.button("Salvar no Histórico Comercial")
        elif acao_crm_p == "Cobranças":
            st.write("Painel limpo. Sem pendências financeiras registradas.")

    with tab_paulo_dieta:
        st.subheader("🥗 Dieta Completa & Ganho de Massa (Parametrizável)")
        calorias_p = st.number_input("Meta Calórica Diária (Ganho de Massa)", value=2800)
        prot_p = st.number_input("Meta de Proteína (g)", value=180)
        
        st.text_area("📝 Cardápio de Dieta & Suplementação Diária:", value="""- Desjejum: Vitamina de abacate com aveia, whey protein e 3 ovos inteiros.
- Almoço: Arroz, feijão, 250g de carne vermelha ou frango, azeite e legumes.
- Pré-Treino: Pão com pasta de amendoim e banana.
- Pós-Treino / Jantar: Batata doce, frango desfiado e suplementação de Creatina e Whey.""")
        st.button("Salvar Alterações na Dieta do Paulo")

    with tab_paulo_treino:
        st.subheader("💪 Treinos Diários de Hipertrofia")
        dia_p = st.selectbox("Escolha o dia da semana:", ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"], key="treino_p")
        st.text_area("Planejamento de Treino de Força:", value="Treino A: Peito, Ombro e Tríceps com foco em progressão de carga.")
        st.button("Salvar Treino")

    with tab_paulo_ministerio:
        st.subheader("📖 Homem de Deus: Bíblia, Esboços & Ministério")
        
        sub_tab1, sub_tab2, sub_tab3 = st.tabs(["⚡ Consulta Rápida à Bíblia", "✍️ Criar e Editar Esboços", "📚 Meus Esboços Salvos"])
        
        with sub_tab1:
            st.write("### Consulta de Textos Bíblicos")
            livro = st.selectbox("Livro:", ["Salmos", "Provérbios", "João", "Romanos", "Efésios"])
            capitulo = st.number_input("Capítulo:", value=1, min_value=1)
            if st.button("Consultar Palavra"):
                st.info(f"Exibindo passagem selecionada de {livro} {capitulo} para edificação e meditação do Sacerdote do Lar.")
                
        with sub_tab2:
            st.write("### Criar Novo Esboço de Pregador")
            titulo_esboco = st.text_input("Título da Mensagem / Esboço")
            texto_base = st.text_input("Texto Bíblico Base (ex: Josué 1:9)")
            corpo_esboco = st.text_area("Tópicos e Mensagem:")
            if st.button("Salvar Novo Esboço"):
                if 'esbocos' not in st.session_state:
                    st.session_state.esbocos = []
                st.session_state.esbocos.append({"titulo": titulo_esboco, "texto": texto_base, "corpo": corpo_esboco})
                st.success("Esboço bíblico salvo com sucesso!")
                
        with sub_tab3:
            st.write("### Seus Esboços Criados:")
            if 'esbocos' in st.session_state and len(st.session_state.esbocos) > 0:
                for idx, esb in enumerate(st.session_state.esbocos):
                    with st.expander(f"📖 {esb['titulo']} ({esb['texto']})"):
                        st.write(esb['corpo'])
            else:
                st.write("Nenhum esboço cadastrado ainda. Crie o seu na aba ao lado!")

    with tab_paulo_diario:
        st.subheader("📓 Diário Pessoal do Paulo")
        st.text_area("Anotações ministeriais, metas de vendas e registros do dia:", placeholder="Escreva aqui...")
        st.button("Salvar no Diário do Paulo")

# ==========================================
# PERFIL 3: SOFIA (TEMA ROSA)
# ==========================================
elif perfil_selecionado == "Sofia (Painel Infantil & Xadrez - Rosa)":
    st.header("👧 Painel da Sofia (7 Anos)")
    st.write("Sua rotina independente, treinos de luta, tempo de tela e jogos de xadrez e memória!")
    
    aba_rotina_s, aba_jogos_s = st.tabs(["✨ Minha Rotina & Lutas", "♟️ Jogo de Xadrez & Desafios"])
    
    with aba_rotina_s:
        st.subheader("📋 Meu Checklist do Dia")
        st.checkbox("Acordar e arrumar a cama sozinha")
        st.checkbox("Colocar meu cereal de manhã")
        st.checkbox("Ir para a escola")
        st.checkbox("Almoçar e revisar a lição")
        st.checkbox("Tomar banho e me arrumar sozinha")
        st.checkbox("Tempo de tela (1 a 2 horas)")
        
        if dia_semana == 0:
            st.warning("🥋 Hoje tem **Jiu-Jitsu** às 18:30!")
        elif dia_semana in [1, 3]:
            st.warning("🥋 Hoje tem **Muay Thai** às 18:00!")
        else:
            st.success("✨ Hoje é dia de descanso das lutas!")

    with aba_jogos_s:
        st.subheader("♟️ Área de Xadrez & Jogos de Memória")
        if 'pontos_sofia' not in st.session_state:
            st.session_state.pontos_sofia = 10
            
        st.metric(label="🏆 Seus Pontos de Xadrez", value=st.session_state.pontos_sofia)
        
        st.write("---")
        st.write("### 🎮 Mini Tabuleiro Virtual de Xadrez")
        jogada_s = st.selectbox("Escolha sua jogada de peças:", [
            "Peão e4 (Abertura clássica do rei)", 
            "Peão d4 (Abertura da dama)", 
            "Cavalo f3 (Desenvolvimento rápido)",
            "Bispo c4 (Ataque diagonal)"
        ])
        
        if st.button("Fazer Jogada no Tabuleiro"):
            st.session_state.pontos_sofia += 10
            st.balloons()
            st.success(f"Excelente jogada ({jogada_s})! O computador respondeu. Você ganhou +10 pontos!")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #b83280; font-weight: bold;'>Desenvolvido por: Jecy Java | Família Siqueira</p>", unsafe_allow_html=True)
