# 🤖 e-commerce-agent

[![LangChain](https://img.shields.io/badge/langchain-%23000000.svg?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![ChromaDB](https://img.shields.io/badge/chromadb-%23323330.svg?style=for-the-badge&logo=Databricks&logoColor=white)](https://www.trychroma.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-%237A1FA2?style=for-the-badge&logo=openai&logoColor=white)](https://openrouter.ai)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![LLM](https://img.shields.io/badge/LLM-powered-lightblue?style=for-the-badge)](#)
[![RAG](https://img.shields.io/badge/RAG-Enabled-green?style=for-the-badge)](#)
[![NLP](https://img.shields.io/badge/NLP-Transformers-%23ff9800?style=for-the-badge)](#)

> Sistema inteligente de atendimento ao cliente para e-commerce do nicho **piscinas**, com classificação automática de intenção e respostas com base em um **RAG (Retrieval-Augmented Generation)** sobre base de conhecimento local.

---

## 📦 Estrutura do Projeto


e-commerce-agent/
├── main.py                         # Execução principal do agente
├── agents/
│   ├── suporte.py                  # Agente para dúvidas de suporte
│   └── vendas.py                  # Agente para recomendações de venda
├── utils/
│   ├── classificador.py           # Classificação da intenção usando LLM
│   ├── logger.py                  # Logger customizado em arquivo
├── data/
│   └── base_conhecimento.md       # Fonte de conhecimento do negócio (FAQ)
├── chroma_db/                     # Banco vetorial persistente (Chroma)
├── logs/
│   └── interacoes.log             # Log de interações com timestamp
├── .env                           # Variáveis de ambiente (NÃO subir!)
└── README.md                      # Este arquivo :)

---

## Tecnologias e Conceitos

    🔗 LangChain para integração entre LLM, vetores e agentes

    🧠 LLMs via OpenRouter com gpt-3.5-turbo (compatível com OpenAI ou outros modelos)

    🧩 RAG: Geração com recuperação de conhecimento usando ChromaDB

    📚 ChromaDB como vectorstore persistente para consultas locais

    🔍 HuggingFace Embeddings (all-MiniLM-L6-v2)

    📄 Text Chunking com RecursiveCharacterTextSplitter

    🤝 CrewAI para orquestrar tarefas e agentes

    🧪 pytest-ready (facilmente testável)

    📊 Logging estruturado com arquivo .log dedicado

    🔎 Classificação de intenção (suporte vs vendas) usando LLMs

---

## Como Rodar o Projeto

1. Clone o repositório

git clone https://github.com/seu-usuario/e-commerce-agent.git
cd e-commerce-agent

2. Instale as dependências

python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

pip install -r requirements.txt

3. Configure o .env

Crie um arquivo .env com sua chave do OpenRouter:

OPENROUTER_API_KEY=sua_chave_aqui

4. Execute

python main.py

---

## Exemplo de uso

    Usuário: Como posso rastrear meu pedido?
    Resposta (agente): Assim que o pedido for enviado, você receberá um e-mail com o código de rastreio e o link para acompanhamento.

---

## Fontes de Conhecimento

A base usada é um .md com perguntas frequentes e respostas de um e-commerce de piscinas, incluindo:

    Cuidados com cloro e água

    Tipos de piscinas

    Métodos de entrega

    Garantias e trocas

    Suporte e pagamento

---

## Testes

Este projeto está preparado para receber testes com pytest. Basta criar o diretório tests/ e escrever funções com test_....

---

##  Roadmap futuro

Deploy via Streamlit ou Gradio

Suporte a múltiplas bases por categoria

Interface via WhatsApp (Twilio)

Classificador baseado em embeddings

## Contribuições

Este projeto foi criado como prova de conceito para uso de LLMs em e-commerce com agentes inteligentes e recuperação de conhecimento.
License

---

# English

## Intelligent customer support agent for an e-commerce platform focused on pool products, powered by RAG (Retrieval-Augmented Generation) and LLMs.

Key Features

    LangChain + CrewAI: Agent orchestration and task coordination

    RAG Architecture: Answers are generated with local knowledge retrieval

    ChromaDB: Local vector store with persistent embeddings

    HuggingFace Embeddings: Using all-MiniLM-L6-v2 for semantic search

    Text Chunking: Efficient document splitting with RecursiveCharacterTextSplitter

    Intention Classifier: Classifies user intent (sales or support) via LLM

    Structured Logging: Stores all interactions with timestamps

    Test-ready: Easily testable with pytest

---

## 📁 Project Structure

e-commerce-agent/
├── main.py                 # Entry point
├── agents/                 # Support and sales agent definitions
├── utils/                  # Classifier, logger
├── data/                   # Local markdown knowledge base
├── chroma_db/              # Vector store (Chroma)
├── logs/                   # Interaction logs
├── .env                    # API keys (do NOT commit)
└── README.md

---

## Getting Started

git clone https://github.com/your-username/e-commerce-agent.git
cd e-commerce-agent

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

Create a .env file and add:

OPENROUTER_API_KEY=your_key_here

Then run:

python main.py

---

## Example

User: How can I track my order?
Agent: Once your order is shipped, you will receive a tracking code via email.

---

## Knowledge Base

The knowledge base (base_conhecimento.md) includes structured FAQs on:

    Pool maintenance

    Payment and shipping

    Product types and warranties

    Customer support

---

## Future Improvements

    Streamlit/Gradio frontend

    WhatsApp integration (Twilio)

    Multi-domain support

    Embedding-based classification

---

✍️ Autor | Author
 
Victor Hugo B. Soares
📧 [E-mail - contatovictorhugosoares@gmail.com](contatovictorhugosoares@gmail.com)
🌐 [LinkedIn](https://linkedin.com/in/ovitelas)
📞 [Telefone(WhatsApp) +55 11 964628356](https://wa.me/+5511964628356)

© 2025 — ovitelas
