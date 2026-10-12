import pytest
from funcao import aplicar_desconto

@pytest.fixture
def preco_base():
    return 100.0

def test_aplicar_desconto_dez_porcento(preco_base):
    resultado = aplicar_desconto(preco_base, 10)
    assert resultado == 90.0

def test_aplicar_desconto_total(preco_base):
    resultado = aplicar_desconto(preco_base, 100)
    assert resultado == 0.0

def test_aplicar_desconto_zero(preco_base):
    resultado = aplicar_desconto(preco_base, 0)
    assert resultado == 100.0
