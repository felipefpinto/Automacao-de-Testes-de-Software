import unittest
from tabela_calculo_imc import calcular_imc

class TestCalcularIMC(unittest.TestCase):
    def test_calcular_imc_abaixo_peso(self):
        self.assertEqual(calcular_imc(50, 1.8), "Abaixo do peso")

    def test_calcular_imc_peso_normal(self):
        self.assertEqual(calcular_imc(70.1, 1.8), "Peso normal")

    def test_calcular_imc_sobrepeso(self):
        self.assertEqual(calcular_imc(90, 1.8), "Sobrepeso")

    def test_calcular_imc_obesidade_grau_I(self):
        self.assertEqual(calcular_imc(110.8, 1.8), "Obesidade grau I")

    def test_calcular_imc_obesidade_grau_II(self):
        self.assertEqual(calcular_imc(120, 1.8), "Obesidade grau II")

    def test_calcular_imc_obesidade_grau_III(self):
        self.assertEqual(calcular_imc(130.5, 1.8), "Obesidade grau III")
    
    def test_entrada_invalida_peso(self):
        self.assertRaises(ValueError, calcular_imc, -1, 1.8)

    def test_entrada_invalida_altura(self):
        self.assertRaises(ValueError, calcular_imc, 70, -1.8)
    
    def test_entrada_tipo_invalida_peso(self):
        self.assertRaises(TypeError, calcular_imc, "70", 1.8)
    
    def test_entrada_tipo_invalida_altura(self):
        self.assertRaises(TypeError, calcular_imc, 70, "1.8")
    
    


if __name__ == "__main__":
    unittest.main()