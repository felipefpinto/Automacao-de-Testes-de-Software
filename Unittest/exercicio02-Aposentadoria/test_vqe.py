import unittest
from verificar_qualificacao_empregado import verificar_qualificacao_empregado

class TestVerificarQualificacaoEmpregado(unittest.TestCase):
    def test_entrada_invalida_idade(self):
        self.assertRaises(ValueError, verificar_qualificacao_empregado, -1, 20)

    def test_entrada_tipo_invalida_idade(self):
        self.assertRaises(TypeError, verificar_qualificacao_empregado, "65", 20)

    def test_entrada_tipo_invalida_tempo_de_servico(self):
        self.assertRaises(TypeError, verificar_qualificacao_empregado, 65, "20")

    def test_entrada_invalida_tempo_de_servico(self):
        self.assertRaises(ValueError, verificar_qualificacao_empregado, 65, -1)
    

    def test_requerer_aposentadoria_idade_maior_igual_65(self):
        assert verificar_qualificacao_empregado(65, 20) == "Requerer aposentadoria"

    def test_requerer_aposentadoria_tempo_servico_maior_igual_30(self):
        assert verificar_qualificacao_empregado(59, 30) == "Requerer aposentadoria"

    def test_requerer_aposentadoria_idade_maior_igual_60_tempo_servico_maior_igual_25(self):
        assert verificar_qualificacao_empregado(60, 25) == "Requerer aposentadoria"

    def test_nao_requerer_aposentadoria(self):
        assert verificar_qualificacao_empregado(59, 24) == "Não requerer aposentadoria"
    

if __name__ == "__main__":
    unittest.main()
    