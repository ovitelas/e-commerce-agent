import os
from dotenv import load_dotenv
from crewai import Task, Crew
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from agents.suporte import criar_agente_suporte
from agents.vendas import criar_agente_vendas
from utils.classificador import classificar_intencao_local
from utils.logger import log_interacao

# Carrega variáveis de ambiente
load_dotenv()

# Carrega o conteúdo do arquivo de conhecimento
loader = TextLoader("data/base_conhecimento.md")
documents = loader.load()

# Divide em chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

#  Gera embeddings e banco vetorial
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Cria o vetorstore com persistência usando Chroma
persist_directory = "chroma_db"
vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory=persist_directory
)

vectorstore.persist()  # Persiste os dados no diretório

# Cria o retriever
retriever = vectorstore.as_retriever()

# Configura LLM via OpenRouter
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-3.5-turbo",  
    temperature=0.7
)


pergunta = input("Digite sua pergunta sobre o e-commerce: ")

#  intenção
intencao = classificar_intencao_local(pergunta)
print(f"[DEBUG] Intenção classificada: {intencao}")

# Cria agente conforme a intenção
if intencao == "vendas":
    agente = criar_agente_vendas(llm)
else:
    agente = criar_agente_suporte(llm)

# Cria tarefa e equipe
expected_output = (
    "Resposta persuasiva sobre produtos, preços ou promoções para ajudar a fechar a venda."
    if intencao == "vendas"
    else "Resposta clara, objetiva e útil para o cliente sobre pedidos e logística."
)

tarefa = Task(
    description=f"Responda com clareza a seguinte pergunta do cliente: {pergunta}",
    expected_output=expected_output,
    agent=agente
)

equipe = Crew(agents=[agente], tasks=[tarefa], verbose=True)


resposta = equipe.kickoff()


print("\nResposta Final:\n")
print(resposta)

log_interacao(pergunta, intencao, resposta)
