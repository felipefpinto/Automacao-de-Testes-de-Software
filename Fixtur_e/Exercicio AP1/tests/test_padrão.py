import pytest
from funcao import aplicar_desconto

def test_aplicar_desconto_dez_porcento():
    preco_inicial = 100.0
    resultado = aplicar_desconto(preco_inicial, 10)
    assert resultado == 90.0

def test_aplicar_desconto_total():
    preco_inicial = 100.0
    resultado = aplicar_desconto(preco_inicial, 100)
    assert resultado == 0.0

def test_aplicar_desconto_zero():
    preco_inicial = 100.0
    resultado = aplicar_desconto(preco_inicial, 0)
    assert resultado == 100.0