import pytest
from calcular_dosagem import calcular_dosagem

def test_idade_menor():
   with pytest.raises(ValueError): calcular_dosagem(-1, 5)

def test_idade_maior():   
    with pytest.raises(ValueError): calcular_dosagem(250, 5)

def test_peso_menor():
    with pytest.raises(ValueError): calcular_dosagem(1, -1)

def test_peso_maior():
    with pytest.raises(ValueError): calcular_dosagem(1, 250)

def test_calcular_dosagem_20_60():
    assert calcular_dosagem(20, 60) == 1000

def test_calcular_dosagem_12_60():
    assert calcular_dosagem(12, 60) == 1000

def test_calcular_dosagem_20_59():
    assert calcular_dosagem(20, 59) == 875

def test_calcular_dosagem_12_59():
    assert calcular_dosagem(12, 59) == 875

def test_calcular_dosagem_1_5():
    assert calcular_dosagem(1, 5) == 125

def test_calcular_dosagem_12_59():
    assert calcular_dosagem(1, 9) == 125

def test_calcular_dosagem_2_91():
    assert calcular_dosagem(2, 9.1) == 250

def test_calcular_dosagem_2_16():
    assert calcular_dosagem(2, 16) == 250

def test_calcular_dosagem_3_161():
    assert calcular_dosagem(3, 16.1) == 375

def test_calcular_dosagem_3_24():
    assert calcular_dosagem(3, 24) == 375

def test_calcular_dosagem_4_241():
    assert calcular_dosagem(4, 24.1) == 500

def test_calcular_dosagem_5_30():
    assert calcular_dosagem(5, 30) == 500

def test_calcular_dosagem_6_301():
    assert calcular_dosagem(6, 30.1) == 750