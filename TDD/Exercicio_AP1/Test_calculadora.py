import pytest
from Calculadora_Refector import calculadora

def test_compras_ate_100():
    assert calculadora(90)==90

def test_compras_de_100():
    assert calculadora(100)==100

def test_compras_acima_de_100_ate_500():
    assert calculadora(200)==180

def test_compras_de_500():
    assert calculadora(500)==450

def test_compras_acima_500():
    assert calculadora(1000)==800

def test_compra_valor_0():
    with pytest.raises(ValueError):calculadora(0)

def test_compra_valor_negativo():
    with pytest.raises(ValueError):calculadora(-100)
