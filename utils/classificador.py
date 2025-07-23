import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage


# Usa a chave de API
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"), 
    base_url="https://openrouter.ai/api/v1",
    model="gpt-3.5-turbo",
    temperature=0.7
)

def classificar_intencao_local(pergunta: str) -> str:
    prompt = (
        f"Classifique a intenção da pergunta a seguir como 'suporte' ou 'vendas'. "
        f"Responda apenas com uma dessas palavras, sem explicações. Pergunta: {pergunta}"
    )

    resposta = llm([HumanMessage(content=prompt)]).content.strip().lower()

    print("[DEBUG] Prompt usado:", prompt)
    print("[DEBUG] Resposta bruta:", resposta)

    if "suporte" in resposta:
        return "suporte"
    elif "vendas" in resposta:
        return "vendas"
    else:
        return "suporte"  # fallback 
