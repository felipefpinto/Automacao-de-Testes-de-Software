import pytest
from peso_ideal import calcular_peso_ideal

def test_peso_ideal_masculino_1():
    assert calcular_peso_ideal(1.5, 'M') == pytest.approx(51.05,0.01)

def test_peso_ideal_feminino_1():
    assert calcular_peso_ideal(1.5, 'F') == pytest.approx(48.45,0.01)

def test_peso_ideal_masculino_2():
    assert calcular_peso_ideal(1.6, 'M') == pytest.approx(58.32,0.01)

def test_peso_ideal_feminino_2():
    assert calcular_peso_ideal(1.6, 'F') == pytest.approx(54.66,0.01)

def test_peso_ideal_masculino_3():
    assert calcular_peso_ideal(1.7, 'M') == pytest.approx(65.59,0.01)

def test_peso_ideal_feminino_3():
    assert calcular_peso_ideal(1.7, 'F') == pytest.approx(60.86,0.01)

def test_peso_ideal_masculino_4():
    assert calcular_peso_ideal(1.8, 'M') == pytest.approx(72.86,0.01)

def test_peso_ideal_feminino_4():
    assert calcular_peso_ideal(1.8, 'F') == pytest.approx(67.08,0.01)

def test_peso_ideal_masculino_5():
    assert calcular_peso_ideal(1.9, 'M') == pytest.approx(80.13,0.01)

def test_peso_ideal_feminino_5():
    assert calcular_peso_ideal(1.9, 'F') == pytest.approx(73.28,0.01)

def test_peso_ideal_masculino_6():
    assert calcular_peso_ideal(2.0, 'M') == pytest.approx(87.4,0.01)

def test_peso_ideal_feminino_6():
    assert calcular_peso_ideal(2.0, 'F') == pytest.approx(79.5,0.01)



#   python -m pytest -v