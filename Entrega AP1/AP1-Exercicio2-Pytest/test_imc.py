import pytest
from imc import calcular_imc

def test_tipo_invalido_altura_e_peso():
    
    with pytest.raises(TypeError, match="Altura e peso devem ser do tipo float ou inteiro."):
        calcular_imc("1.75", 70.0, "Carlos")
def test_tipo_invalido_altura_e_peso_2():
    with pytest.raises(TypeError, match="Altura e peso devem ser do tipo float ou inteiro."):
        calcular_imc(1.75, "70.0", "Carlos")
def test_tipo_invalido_altura_e_peso_3():
    with pytest.raises(TypeError, match="Altura e peso devem ser do tipo float ou inteiro."):
        calcular_imc(None, 70.0, "Carlos")

def test_calculo_imc_com_dados_validos():
    nome, classificacao = calcular_imc(1.75, 70.0, "Seu Nome")
    assert nome == "Seu Nome"
    assert classificacao == "Peso normal"
def test_calculo_imc_com_dados_validos_2():
    nome, classificacao = calcular_imc(2, 80, "Lucas")
    assert nome == "Lucas"
    assert classificacao == "Peso normal"


def test_classificacoes_imc():
    assert calcular_imc(1.70, 50.0, "Ana")[1] == "Abaixo do peso"
def test_classificacoes_imc_2():    
    assert calcular_imc(1.70, 65.0, "Bruno")[1] == "Peso normal"
def test_classificacoes_imc_3():
    assert calcular_imc(1.70, 80.0, "Carla")[1] == "Sobrepeso"
def test_classificacoes_imc_4():    
    assert calcular_imc(1.70, 90.0, "Daniel")[1] == "Obesidade grau I"
def test_classificacoes_imc_5():    
    assert calcular_imc(1.70, 105.0, "Eduardo")[1] == "Obesidade grau II"
def test_classificacoes_imc_6():
    assert calcular_imc(1.70, 120.0, "Fernanda")[1] == "Obesidade grau III"