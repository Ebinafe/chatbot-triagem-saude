"""
Chatbot de Pré-Triagem para Clínicas e Hospitais
Tecnologia: Python + Streamlit
Versão: 2.0 - Interface Premium
Autor: Desenvolvido para auxiliar triagem médica
"""

import streamlit as st
from datetime import datetime
from typing import List, Dict

# Configuração da página
st.set_page_config(
    page_title="Chatbot Pré-Triagem Saúde+",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS premium
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Header estilizado */
    .header-container {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
        text-align: center;
        animation: slideDown 0.5s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .header-title {
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .header-subtitle {
        color: rgba(255,255,255,0.95);
        font-size: 1.3rem;
        margin-top: 0.5rem;
        font-weight: 300;
    }
    
    /* Card estilizado */
    .card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 15px 50px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
        animation: fadeIn 0.6s ease-out;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    /* Botões personalizados */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    /* Checkbox estilizado */
    .stCheckbox {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .stCheckbox:hover {
        border-color: #667eea;
        transform: scale(1.02);
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e0e0e0;
        padding: 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Urgência cards */
    .urgencia-card {
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.02);
        }
    }
    
    .urgencia-vermelho {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
        color: white;
    }
    
    .urgencia-amarelo {
        background: linear-gradient(135deg, #ffd93d 0%, #f9ca24 100%);
        color: #333;
    }
    
    .urgencia-verde {
        background: linear-gradient(135deg, #6bcf7f 0%, #26de81 100%);
        color: white;
    }
    
    .urgencia-titulo {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .urgencia-subtitulo {
        font-size: 1.3rem;
        font-weight: 400;
        opacity: 0.95;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-left: 5px solid #2196f3;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border-left: 5px solid #ff9800;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .success-box {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-left: 5px solid #4caf50;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* Métrica customizada */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
    }
    
    /* Sintoma card */
    .sintoma-card {
        background: white;
        border: 3px solid #e0e0e0;
        border-radius: 15px;
        padding: 1.2rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        font-size: 1.1rem;
    }
    
    .sintoma-card:hover {
        border-color: #667eea;
        transform: translateX(5px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
    }
    
    .sintoma-card-selected {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-color: #667eea;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: white;
        opacity: 0.8;
        margin-top: 3rem;
    }
    
    /* Divisor */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        margin: 2rem 0;
    }
    
    /* Text area */
    .stTextArea > div > div > textarea {
        border-radius: 12px;
        border: 2px solid #e0e0e0;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        margin: 0.3rem;
        font-size: 0.9rem;
    }
    
    .badge-danger {
        background: #ff6b6b;
        color: white;
    }
    
    .badge-warning {
        background: #ffd93d;
        color: #333;
    }
    
    .badge-success {
        background: #6bcf7f;
        color: white;
    }
    
    /* Esconde elementos do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


class SistemaTriagem:
    """Sistema de triagem médica com classificação de urgência"""
    
    SINTOMAS = [
        {"id": "febre", "nome": "🌡️ Febre alta (acima de 38°C)", "gravidade": 2},
        {"id": "dor_peito", "nome": "💔 Dor no peito", "gravidade": 3},
        {"id": "falta_ar", "nome": "😮‍💨 Falta de ar / Dificuldade para respirar", "gravidade": 3},
        {"id": "dor_cabeca", "nome": "🤕 Dor de cabeça", "gravidade": 1},
        {"id": "tosse", "nome": "😷 Tosse persistente", "gravidade": 1},
        {"id": "nausea", "nome": "🤢 Náusea / Vômito", "gravidade": 2},
        {"id": "dor_abdominal", "nome": "🔥 Dor abdominal intensa", "gravidade": 2},
        {"id": "tontura", "nome": "💫 Tontura / Vertigem", "gravidade": 2},
        {"id": "sangramento", "nome": "🩸 Sangramento", "gravidade": 3},
        {"id": "fratura", "nome": "🦴 Suspeita de fratura ou trauma", "gravidade": 3},
        {"id": "desmaio", "nome": "😵 Desmaio ou perda de consciência", "gravidade": 3},
        {"id": "confusao", "nome": "🧠 Confusão mental", "gravidade": 3}
    ]
    
    @staticmethod
    def calcular_urgencia(sintomas_ids: List[str], intensidade: int) -> Dict:
        """Calcula o nível de urgência baseado nos sintomas e intensidade"""
        if not sintomas_ids:
            return {
                "nivel": "VERDE",
                "texto": "NÃO URGENTE",
                "cor": "verde",
                "recomendacao": "✅ Você pode aguardar atendimento normal ou agendar consulta.",
                "emoji": "🟢"
            }
        
        gravidades = [
            s["gravidade"] for s in SistemaTriagem.SINTOMAS 
            if s["id"] in sintomas_ids
        ]
        gravidade_maxima = max(gravidades) if gravidades else 0
        
        if gravidade_maxima == 3 or intensidade >= 8:
            return {
                "nivel": "VERMELHO",
                "texto": "EMERGÊNCIA",
                "subtexto": "Atendimento Imediato Necessário",
                "cor": "vermelho",
                "recomendacao": "🚨 DIRIJA-SE IMEDIATAMENTE ao pronto-socorro ou ligue 192 (SAMU). Esta é uma situação de emergência que requer atenção médica urgente.",
                "emoji": "🔴"
            }
        elif gravidade_maxima == 2 or intensidade >= 5:
            return {
                "nivel": "AMARELO",
                "texto": "URGENTE",
                "subtexto": "Atendimento Prioritário Recomendado",
                "cor": "amarelo",
                "recomendacao": "⚠️ Recomendamos atendimento médico nas próximas horas. Você terá prioridade na fila de atendimento.",
                "emoji": "🟡"
            }
        else:
            return {
                "nivel": "VERDE",
                "texto": "NÃO URGENTE",
                "subtexto": "Atendimento Normal",
                "cor": "verde",
                "recomendacao": "✅ Você pode aguardar na recepção ou agendar uma consulta para os próximos dias. Seus sintomas não indicam urgência imediata.",
                "emoji": "🟢"
            }


def inicializar_sessao():
    """Inicializa as variáveis de sessão"""
    if 'etapa' not in st.session_state:
        st.session_state.etapa = 'inicio'
    if 'dados_paciente' not in st.session_state:
        st.session_state.dados_paciente = {
            'nome': '',
            'idade': '',
            'telefone': '',
            'sintomas': [],
            'duracao': '',
            'intensidade': 5,
            'observacoes': '',
            'data_triagem': datetime.now().strftime("%d/%m/%Y às %H:%M")
        }


def exibir_header():
    """Exibe o cabeçalho premium"""
    st.markdown("""
        <div class="header-container">
            <div class="header-title">🏥 Clínica Saúde+</div>
            <div class="header-subtitle">Assistente Virtual de Pré-Triagem Inteligente</div>
        </div>
    """, unsafe_allow_html=True)


def etapa_inicio():
    """Etapa inicial com design premium"""
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    st.markdown("### 👋 Bem-vindo ao Sistema de Pré-Triagem")
    st.markdown('<div class="info-box">📋 Vamos coletar algumas informações para direcionar seu atendimento de forma adequada e eficiente.</div>', unsafe_allow_html=True)
    
    with st.form("dados_pessoais"):
        st.markdown("#### 📝 Informações Pessoais")
        
        nome = st.text_input(
            "Nome completo:",
            placeholder="Digite seu nome completo",
            help="Informe seu nome completo para identificação"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            idade = st.number_input(
                "Idade:",
                min_value=0,
                max_value=120,
                step=1,
                help="Informe sua idade em anos"
            )
        with col2:
            telefone = st.text_input(
                "Telefone (com DDD):",
                placeholder="(00) 00000-0000",
                help="Telefone para contato"
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Continuar ➡️", use_container_width=True)
        
        if submitted:
            if not nome or not telefone or idade == 0:
                st.error("❌ Por favor, preencha todos os campos para continuar.")
            else:
                st.session_state.dados_paciente['nome'] = nome
                st.session_state.dados_paciente['idade'] = idade
                st.session_state.dados_paciente['telefone'] = telefone
                st.session_state.etapa = 'sintomas'
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)


def etapa_sintomas():
    """Etapa de seleção de sintomas com design premium"""
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    st.markdown(f"### Olá, {st.session_state.dados_paciente['nome']}! 👋")
    st.markdown("### 🩺 Selecione os sintomas que você está sentindo")
    
    st.markdown('<div class="warning-box">⚠️ <strong>Importante:</strong> Selecione TODOS os sintomas que você está apresentando no momento.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    sintomas_selecionados = []
    
    for i, sintoma in enumerate(SistemaTriagem.SINTOMAS):
        with col1 if i % 2 == 0 else col2:
            if st.checkbox(
                sintoma["nome"],
                key=f"sintoma_{sintoma['id']}",
                help=f"Gravidade: {'🔴 Alta' if sintoma['gravidade'] == 3 else '🟡 Média' if sintoma['gravidade'] == 2 else '🟢 Baixa'}"
            ):
                sintomas_selecionados.append(sintoma['id'])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        if st.button("⬅️ Voltar", use_container_width=True):
            st.session_state.etapa = 'inicio'
            st.rerun()
    with col_b:
        if st.button("Continuar ➡️", type="primary", use_container_width=True):
            if not sintomas_selecionados:
                st.error("❌ Por favor, selecione pelo menos um sintoma para continuar.")
            else:
                st.session_state.dados_paciente['sintomas'] = sintomas_selecionados
                st.session_state.etapa = 'detalhes'
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)


def etapa_detalhes():
    """Etapa de detalhes com design premium"""
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    st.markdown(f"### {st.session_state.dados_paciente['nome']}, agora precisamos de mais detalhes 📊")
    
    sintomas_nomes = [
        s["nome"] for s in SistemaTriagem.SINTOMAS 
        if s["id"] in st.session_state.dados_paciente['sintomas']
    ]
    st.markdown(f'<div class="success-box"><strong>✅ Sintomas selecionados:</strong><br>{", ".join(sintomas_nomes)}</div>', unsafe_allow_html=True)
    
    with st.form("detalhes_sintomas"):
        st.markdown("#### ⏰ Duração dos Sintomas")
        duracao = st.text_input(
            "Há quanto tempo você está com esses sintomas?",
            placeholder="Ex: 2 dias, 1 semana, algumas horas",
            help="Seja o mais específico possível"
        )
        
        st.markdown("#### 📈 Intensidade dos Sintomas")
        st.caption("Use a escala abaixo para indicar a intensidade da sua dor ou desconforto:")
        
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.markdown("**1**<br>Muito leve", unsafe_allow_html=True)
        with col2:
            intensidade = st.slider(
                "Intensidade:",
                min_value=1,
                max_value=10,
                value=5,
                label_visibility="collapsed"
            )
        with col3:
            st.markdown("**10**<br>Insuportável", unsafe_allow_html=True)
        
        # Feedback visual da intensidade
        if intensidade <= 3:
            st.markdown(f'<div class="success-box">🟢 <strong>Intensidade Atual: {intensidade}/10</strong><br>Sintomas de intensidade leve</div>', unsafe_allow_html=True)
        elif intensidade <= 7:
            st.markdown(f'<div class="warning-box">🟡 <strong>Intensidade Atual: {intensidade}/10</strong><br>Sintomas de intensidade moderada</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); color: white; padding: 1.5rem; border-radius: 12px; margin: 1rem 0;">🔴 <strong>Intensidade Atual: {intensidade}/10</strong><br>Sintomas de alta intensidade</div>', unsafe_allow_html=True)
        
        st.markdown("#### 💬 Informações Adicionais")
        observacoes = st.text_area(
            "Há algo mais que gostaria de compartilhar?",
            placeholder="Medicamentos em uso, alergias, histórico médico relevante, etc.",
            height=120,
            help="Informações opcionais que podem ajudar no atendimento"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])
        with col1:
            voltar = st.form_submit_button("⬅️ Voltar", use_container_width=True)
        with col2:
            finalizar = st.form_submit_button("Finalizar Triagem ✅", type="primary", use_container_width=True)
        
        if voltar:
            st.session_state.etapa = 'sintomas'
            st.rerun()
            
        if finalizar:
            if not duracao:
                st.error("❌ Por favor, informe há quanto tempo está com os sintomas.")
            else:
                st.session_state.dados_paciente['duracao'] = duracao
                st.session_state.dados_paciente['intensidade'] = intensidade
                st.session_state.dados_paciente['observacoes'] = observacoes
                st.session_state.etapa = 'resultado'
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)


def etapa_resultado():
    """Exibe o resultado com design premium"""
    dados = st.session_state.dados_paciente
    urgencia = SistemaTriagem.calcular_urgencia(dados['sintomas'], dados['intensidade'])
    
    # Card de urgência
    st.markdown(f"""
        <div class="urgencia-card urgencia-{urgencia['cor']}">
            <div style="font-size: 4rem; margin-bottom: 1rem;">{urgencia['emoji']}</div>
            <div class="urgencia-titulo">{urgencia['nivel']}</div>
            <div class="urgencia-subtitulo">{urgencia['subtexto']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Cabeçalho do relatório
    st.markdown("# 📋 Relatório Completo de Pré-Triagem")
    st.markdown(f"**🕐 Realizado em:** {dados['data_triagem']}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Dados do paciente em cards
    st.markdown("### 👤 Dados do Paciente")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">NOME</div>
                <div class="metric-value" style="font-size: 1.3rem;">{dados['nome']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">IDADE</div>
                <div class="metric-value">{dados['idade']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">TELEFONE</div>
                <div class="metric-value" style="font-size: 1.3rem;">{dados['telefone']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Sintomas
    st.markdown("### 🩺 Sintomas Reportados")
    sintomas_nomes = [
        s["nome"] for s in SistemaTriagem.SINTOMAS 
        if s["id"] in dados['sintomas']
    ]
    
    cols = st.columns(2)
    for i, sintoma in enumerate(sintomas_nomes):
        with cols[i % 2]:
            gravidade = next((s["gravidade"] for s in SistemaTriagem.SINTOMAS if s["nome"] == sintoma), 1)
            badge_class = "badge-danger" if gravidade == 3 else "badge-warning" if gravidade == 2 else "badge-success"
            st.markdown(f'<span class="badge {badge_class}">{sintoma}</span>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Detalhes
    st.markdown("### 📊 Informações Clínicas")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="info-box"><strong>⏰ Duração:</strong><br>{dados["duracao"]}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="info-box"><strong>📈 Intensidade:</strong><br>{dados["intensidade"]}/10</div>', unsafe_allow_html=True)
    
    if dados['observacoes']:
        st.markdown("### 💬 Observações Adicionais")
        st.markdown(f'<div class="info-box">{dados["observacoes"]}</div>', unsafe_allow_html=True)
    
    # Recomendação
    st.markdown("### 🎯 Recomendação Médica")
    if urgencia["cor"] == "vermelho":
        st.markdown(f'<div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); color: white; padding: 2rem; border-radius: 15px; font-size: 1.2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">{urgencia["recomendacao"]}</div>', unsafe_allow_html=True)
    elif urgencia["cor"] == "amarelo":
        st.markdown(f'<div style="background: linear-gradient(135deg, #ffd93d 0%, #f9ca24 100%); color: #333; padding: 2rem; border-radius: 15px; font-size: 1.2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">{urgencia["recomendacao"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background: linear-gradient(135deg, #6bcf7f 0%, #26de81 100%); color: white; padding: 2rem; border-radius: 15px; font-size: 1.2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">{urgencia["recomendacao"]}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Botões de ação
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🖨️ Imprimir Relatório", use_container_width=True):
            st.info("📄 Use Ctrl+P ou o menu do navegador para imprimir este relatório.")
    with col2:
        if st.button("🔄 Nova Triagem", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)


def main():
    """Função principal da aplicação"""
    inicializar_sessao()
    exibir_header()
    
    # Roteamento de etapas
    if st.session_state.etapa == 'inicio':
        etapa_inicio()
    elif st.session_state.etapa == 'sintomas':
        etapa_sintomas()
    elif st.session_state.etapa == 'detalhes':
        etapa_detalhes()
    elif st.session_state.etapa == 'resultado':
        etapa_resultado()
    
    # Footer premium
    st.markdown("""
        <div class="footer">
            <p style="font-size: 1.1rem; margin-bottom: 0.5rem;">🏥 <strong>Clínica Saúde+</strong> | Sistema de Pré-Triagem Virtual</p>
            <p style="font-size: 0.9rem; opacity: 0.8;">© 2025 Todos os direitos reservados</p>
            <p style="font-size: 0.85rem; opacity: 0.7; margin-top: 1rem;">⚠️ Este sistema não substitui avaliação médica profissional</p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()