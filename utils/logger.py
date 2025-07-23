import logging
from datetime import datetime

#  logger
logging.basicConfig(
    filename='logs/interacoes.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def log_interacao(pergunta: str, intencao: str, resposta: str):
    logging.info(f"Pergunta: {pergunta} | Intenção: {intencao} | Resposta: {resposta}")
