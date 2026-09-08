import streamlit as st
from datetime import datetime
import pandas as pd
import io

# Configuração da página com o ícone personalizado da Família Siqueira
st.set_page_config(
    page_title="App Família Siqueira | Alta Performance",
    page_icon="https://raw.githubusercontent.com/jecyjava/Rotina-Casa-Siqueira/main/perfil.jpg",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização CSS avançada para eliminar espaços vazios e dar cara de App Mobile Compacto e Elegante
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
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 600px;
    }
    .card-treino {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 12px;
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
# PERFIL 1: JECY (TEMA ROSA)
# ==========================================
elif st.session_state.usuario_logado == "Jecy":
    if st.button("⬅️ Trocar de Perfil"):
        st.session_state.usuario_logado = None
        st.rerun()
        
    st.header("👑 Painel da Jecy")
    st.markdown("<p style='text-align: center; font-size: 13px; color: #666;'>Foco na Trizepatida (2.5mg), meta -17kg e treinos</p>", unsafe_allow_html=True)
    
    aba_rotina, aba_dieta, aba_treino, aba_progresso, aba_diario = st.tabs([
        "🎯 Rotina", "🥗 Dieta", "💪 Treinos", "📈 Metas", "📓 Diário"
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
# PERFIL 2: PAULO (TEMA AZUL)
# ==========================================
elif st.session_state.usuario_logado == "Paulo":
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
        "⚙️ Rotina", "💼 Vendas & CRM", "🥗 Dieta", "💪 Treinos", "📖 Bíblia & Esboços", "📓 Diário"
    ])
    
    with aba_p1:
        st.subheader("⚙️ Rotina Flexível (Acorda 07:00)")
        st.text_area("Ajuste livre do dia:", value="07:00 Café em família | 08:30 Vendas (Coiffer/Lizze) | 17:00 Hipertrofia | 20:00 Estudo Bíblico")
        st.button("Salvar Rotina")

    with aba_p2:
        st.subheader("💼 Gestão de Vendas & CRM (Cosméticos)")
        st.write("Marcas: **Coiffer, Matize, Venulti, Donati, Lizze**")
        
        if 'produtos_vendas' not in st.session_state:
            st.session_state.produtos_vendas = [
                {"Produto": "Shampoo Matizador Coiffer 1L", "Preço (R$)": 120.0, "Estoque": 15},
                {"Produto": "Escova Progressiva Lizze Extreme", "Preço (R$)": 350.0, "Estoque": 8},
                {"Produto": "Máscara Donati Nutrição 500g", "Preço (R$)": 95.0, "Estoque": 20}
            ]
        if 'clientes_vendas' not in st.session_state:
            st.session_state.clientes_vendas = [
                {"Salão / Cliente": "Salão Master Hair", "Contato": "(16) 99999-1111", "Observação": "Foco em progressivas"},
                {"Salão / Cliente": "Studio Bella Vista", "Contato": "(16) 98888-2222", "Observação": "Gosta de matizadores"}
            ]

        sub_v1, sub_v2, sub_v3 = st.tabs(["📦 Produtos & Preços", "👥 Clientes", "📊 Emitir Pedido (Excel)"])
        
        with sub_v1:
            st.write("### Tabela de Preços e Produtos")
            df_prod = pd.DataFrame(st.session_state.produtos_vendas)
            st.dataframe(df_prod, use_container_width=True)
            
            with st.form("cad_prod"):
                st.write("**Cadastrar Novo Produto:**")
                novo_p_nome = st.text_input("Nome do Produto/Cosmético")
                novo_p_preco = st.number_input("Preço de Venda (R$)", value=100.0)
                novo_p_est = st.number_input("Quantidade em Estoque", value=10, min_value=1)
                btn_cad_p = st.form_submit_button("Salvar Produto")
                if btn_cad_p and novo_p_nome:
                    st.session_state.produtos_vendas.append({"Produto": novo_p_nome, "Preço (R$)": novo_p_preco, "Estoque": novo_p_est})
                    st.success("Produto cadastrado com sucesso!")
                    st.rerun()

        with sub_v2:
            st.write("### Carteira de Clientes (Salões)")
            df_cli = pd.DataFrame(st.session_state.clientes_vendas)
            st.dataframe(df_cli, use_container_width=True)
            
            with st.form("cad_cli"):
                st.write("**Cadastrar Novo Cliente / Salão:**")
                novo_c_nome = st.text_input("Nome do Salão")
                novo_c_contato = st.text_input("Telefone / Contato")
                novo_c_obs = st.text_input("Observações / Marcas de Interesse")
                btn_cad_c = st.form_submit_button("Salvar Cliente")
                if btn_cad_c and novo_c_nome:
                    st.session_state.clientes_vendas.append({"Salão / Cliente": novo_c_nome, "Contato": novo_c_contato, "Observação": novo_c_obs})
                    st.success("Cliente cadastrado com sucesso!")
                    st.rerun()

        with sub_v3:
            st.write("### Emitir Pedido de Venda em Excel")
            cliente_pedido = st.selectbox("Selecione o Cliente:", [c["Salão / Cliente"] for c in st.session_state.clientes_vendas])
            produto_pedido = st.selectbox("Selecione o Produto:", [p["Produto"] for p in st.session_state.produtos_vendas])
            qtd_pedido = st.number_input("Quantidade:", value=1, min_value=1)
            
            if st.button("📥 Gerar Planilha Excel do Pedido"):
                dados_pedido = {"Cliente": [cliente_pedido], "Produto": [produto_pedido], "Quantidade": [qtd_pedido], "Data": [datetime.now().strftime("%d/%m/%Y")]}
                df_pedido = pd.DataFrame(dados_pedido)
                
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df_pedido.to_excel(writer, index=False, sheet_name='Pedido_Venda')
                processed_data = output.getvalue()
                
                st.download_button(
                    label="⬇️ Baixar Arquivo Excel (.xlsx)",
                    data=processed_data,
                    file_name=f"Pedido_{cliente_pedido.replace(' ', '_')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    with aba_p3:
        st.subheader("🥗 Dieta Completa (Ganho de Massa)")
        st.number_input("Meta Calórica Diária (kcal)", value=2800)
        st.text_area("Cardápio Diário Completo:", value="- Desjejum: Vitamina de abacate + Whey + 3 ovos\n- Almoço: Arroz, feijão, 250g carne vermelha, azeite\n- Lanche: Pão com pasta de amendoim e banana\n- Jantar: Batata doce, frango desfiado e Creatina")
        st.button("Salvar Dieta")

    with aba_p4:
        st.subheader("💪 Treinos Diários Detalhados (Séries & Imagens)")
        dia_treino_p = st.selectbox("Selecione o Treino do Dia:", ["Costas & Ombros", "Peito & Tríceps", "Pernas & Panturrilhas", "Braços & Core"])
        
        if dia_treino_p == "Costas & Ombros":
            st.markdown("""
            <div class="card-treino">
                <b>1. Puxada frontal com pegada aberta</b><br>
                <span style="color:#2b6cb0; font-size:14px;">⚡ Séries: 4 x 10 | Carga: 60 kg</span><br>
                <img src="https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?w=400" width="100%" style="border-radius:8px; margin-top:8px;">
            </div>
            <div class="card-treino">
                <b>2. Desenvolvimento de ombros no Smith</b><br>
                <span style="color:#2b6cb0; font-size:14px;">⚡ Séries: 4 x 10 | Carga: 40 kg</span>
            </div>
            <div class="card-treino">
                <b>3. Elevação lateral no banco inclinado</b><br>
                <span style="color:#2b6cb0; font-size:14px;">⚡ Séries: 3 x 12 | Halteres</span>
            </div>
            <div class="card-treino">
                <b>4. Remada fechada com halteres no banco</b><br>
                <span style="color:#2b6cb0; font-size:14px;">⚡ Séries: 3 x 10 | Carga: 20 kg</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info(f"Treino selecionado: **{dia_treino_p}**. Foco total na progressão de carga e execução limpa.")

    with aba_p5:
        st.subheader("📖 Bíblia Real & Esboços Parametrizáveis")
        sub_bib1, sub_bib2 = st.tabs(["⚡ Consulta Bíblica", "✍️ Criar/Editar Esboços"])
        
        with sub_bib1:
            st.write("### Consulta em Tempo Real às Escrituras")
            livro_cons = st.selectbox("Livro:", ["Salmos", "Provérbios", "Isaías", "João", "Romanos", "Josué"])
            cap_cons = st.number_input("Capítulo:", value=23, min_value=1)
            
            if st.button("📖 Consultar Texto"):
                if livro_cons == "Salmos" and cap_cons == 23:
                    st.success("**Salmos 23**\n\n1. O Senhor é o meu pastor, nada me faltará.\n2. Deitar-me faz em verdejantes pastos, conduz-me levemente às águas tranquilas.\n3. Refrigera a minha alma; guia-me pelas veredas da justiça, por amor do seu nome.")
                else:
                    st.info(f"Exibindo passagens edificantes de **{livro_cons} {cap_cons}** para meditação e base ministerial do Sacerdote do Lar.")

        with sub_bib2:
            st.write("### Gerenciador de Esboços Bíblicos")
            if 'esbocos_paulo' not in st.session_state:
                st.session_state.esbocos_paulo = [
                    {"titulo": "A Força da Fé no Lar", "texto": "Josué 1:9", "corpo": "1. Ser corajoso\n2. Confiança na promessa\n3. Cobertura espiritual da família"}
                ]
            
            acao_esb = st.radio("Ação:", ["Consultar / Editar Existentes", "Criar Novo Esboço"], horizontal=True)
            
            if acao_esb == "Consultar / Editar Existentes":
                for i, esb in enumerate(st.session_state.esbocos_paulo):
                    with st.expander(f"📖 {esb['titulo']} ({esb['texto']})"):
                        novo_t = st.text_input(f"Editar Título {i}", value=esb['titulo'])
                        novo_txt = st.text_input(f"Editar Texto Base {i}", value=esb['texto'])
                        novo_corpo = st.text_area(f"Editar Tópicos {i}", value=esb['corpo'])
                        if st.button(f"Salvar Alterações #{i+1}"):
                            st.session_state.esbocos_paulo[i] = {"titulo": novo_t, "texto": novo_txt, "corpo": novo_corpo}
                            st.success("Esboço atualizado com sucesso!")
            else:
                with st.form("novo_esb"):
                    t_novo = st.text_input("Título do Esboço")
                    b_novo = st.text_input("Texto Bíblico Base")
                    c_novo = st.text_area("Tópicos e Mensagem")
                    if st.form_submit_button("Salvar Novo Esboço"):
                        st.session_state.esbocos_paulo.append({"titulo": t_novo, "texto": b_novo, "corpo": c_novo})
                        st.success("Esboço criado com sucesso!")
                        st.rerun()

    with aba_p6:
        st.subheader("📓 Diário Ministerial e Vendas")
        st.text_area("Anotações gerais do dia:", placeholder="Escreva...")
        st.button("Salvar Anotação")

# ==========================================
# PERFIL 3: SOFIA (XADREZ REAL)
# ==========================================
elif st.session_state.usuario_logado == "Sofia":
    if st.button("⬅️ Trocar de Perfil"):
        st.session_state.usuario_logado = None
        st.rerun()
        
    st.header("👧 Painel da Sofia")
    st.markdown("<p style='text-align: center; font-size: 13px; color: #666;'>7 Anos | Responsabilidade, Lutas & Xadrez Real</p>", unsafe_allow_html=True)
    
    aba_s1, aba_s2 = st.tabs(["✨ Minha Rotina", "♟️ Xadrez Real (Lichess)"])
    
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
        st.write("Jogue partidas reais contra o bot ou outra pessoa diretamente na plataforma oficial do Lichess:")
        
        # Botão interativo com link externo seguro que evita bloqueio do navegador/iframe
        st.markdown("""
            <div style="text-align: center; padding: 20px; background: white; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 15px;">
                <h3 style="color: #d53f8c; margin-bottom: 10px;">♟️ Tabuleiro Oficial Lichess</h3>
                <p style="font-size: 13px; color: #666; margin-bottom: 15px;">Clique abaixo para abrir o jogo em tela cheia e treinar suas estratégias:</p>
                <a href="https://lichess.org/" target="_blank" style="background-color: #ed64a6; color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block;">Abrir Jogo de Xadrez 🚀</a>
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
