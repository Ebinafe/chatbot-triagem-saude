# Chatbot de Pré-Triagem Médica

Sistema de triagem médica que classifica pacientes por nível de urgência usando o Protocolo Manchester adaptado.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-red.svg)

## Sobre

Chatbot desenvolvido para auxiliar clínicas e hospitais na triagem inicial de pacientes, reduzindo filas e priorizando casos urgentes.

### Classificação por Cores

- 🔴 **VERMELHO** - Emergência (atendimento imediato)
- 🟡 **AMARELO** - Urgente (atendimento prioritário)
- 🟢 **VERDE** - Não urgente (atendimento normal)

## Funcionalidades

- Coleta de dados do paciente
- Seleção de sintomas (12 opções)
- Avaliação de intensidade (escala 1-10)
- Classificação automática de urgência
- Relatório completo com recomendações
- Interface moderna e responsiva

## Instalação

```bash
# Clone o repositório
git clone https://github.com/Ebinafe/chatbot-triagem-saude.git
cd chatbot-triagem-saude

# Instale as dependências
pip install -r requirements.txt

# Execute
streamlit run app.py
```

## Como Usar

1. Preencha seus dados pessoais
2. Selecione os sintomas
3. Informe duração e intensidade
4. Visualize o resultado e recomendações

## Tecnologias

- Python 3.8+
- Streamlit 1.31.0

## Estrutura do Projeto

```
chatbot-triagem-saude/
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências
├── README.md          # Documentação
└── .gitignore         # Arquivos ignorados
```

## Lógica de Classificação

O sistema analisa dois fatores:

**1. Gravidade do Sintoma**
- Nível 3 (Grave): Dor no peito, falta de ar, sangramento
- Nível 2 (Moderado): Febre, náusea, dor abdominal
- Nível 1 (Leve): Dor de cabeça, tosse

**2. Intensidade Reportada**
- 8-10: Alta gravidade → VERMELHO
- 5-7: Moderada → AMARELO
- 1-4: Baixa → VERDE

A classificação final usa o nível mais alto entre os dois fatores.

## Deploy

### Streamlit Cloud (Grátis)

1. Acesse https://chatbot-triagem-saude-prb5euy3gk359yxlylu7vp.streamlit.app/
2. Conecte com GitHub
3. Selecione o repositório
4. Deploy!

## Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request


## Contato

- GitHub: [@Ebinafe](https://github.com/Ebinafe)
- Email: ebina.fe@gmail.com

## Aviso Legal

⚠️ Este sistema NÃO substitui avaliação médica profissional. Em emergências, ligue  (SAMU).

---

Desenvolvido com ❤️ para melhorar o atendimento em saúde
