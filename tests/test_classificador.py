import unittest
from utils.classificador import classificar_intencao_llm

class TestClassificadorLLM(unittest.TestCase):

    def test_classifica_suporte(self):
        pergunta = "Meu pedido está com erro de entrega"
        resultado = classificar_intencao_llm(pergunta)
        self.assertEqual(resultado, "suporte")

    def test_classifica_vendas(self):
        pergunta = "Quero comprar um produto com desconto"
        resultado = classificar_intencao_llm(pergunta)
        self.assertEqual(resultado, "vendas")

if __name__ == '__main__':
    unittest.main()
