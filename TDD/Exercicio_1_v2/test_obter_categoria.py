from obter_categoria import obter_categoria
import pytest
'''for idade in range(5, 8):
    def test_obter_categoria_infantil_a(idade=idade):
        print(f'Testando idade {idade}')
        assert obter_categoria(idade)=='Infantil A'
for idade in range(8, 11):
    def test_obter_categoria_infantil_b(idade=idade):
        print(f'Testando idade {idade}')
        assert obter_categoria(idade)=='Infantil B'
for idade in range(11, 14):
    def test_obter_categoria_juvenil_a(idade=idade):
        print(f'Testando idade {idade}')
        assert obter_categoria(idade)=='Juvenil A'
for idade in range(14, 18):
    def test_obter_categoria_juvenil_b(idade=idade):
        print(f'Testando idade {idade}')
        assert obter_categoria(idade)=='Juvenil B'

def test_obter_categoria_18():
    assert obter_categoria(18)=='Senior'''

def test_obter_categoria_infantil_a_5():
    assert obter_categoria(5)=='Infantil A'

def test_obter_categoria_infantil_a_6():
    assert obter_categoria(6)=='Infantil A'

def test_obter_categoria_infantil_a_7():
    assert obter_categoria(7)=='Infantil A'

def test_obter_categoria_infantil_b_8():
    assert obter_categoria(8)=='Infantil B'

def test_obter_categoria_infantil_b_9():
    assert obter_categoria(9)=='Infantil B'

def test_obter_categoria_infantil_b_10():
    assert obter_categoria(10)=='Infantil B'

def test_obter_categoria_juvenil_a_11():
    assert obter_categoria(11)=='Juvenil A'

def test_obter_categoria_juvenil_a_12():
    assert obter_categoria(12)=='Juvenil A'

def test_obter_categoria_juvenil_a_13():
    assert obter_categoria(13)=='Juvenil A'

def test_obter_categoria_juvenil_b_14():
    assert obter_categoria(14)=='Juvenil B'

def test_obter_categoria_juvenil_b_15():
    assert obter_categoria(15)=='Juvenil B'

def test_obter_categoria_juvenil_b_16():
    assert obter_categoria(16)=='Juvenil B'

def test_obter_categoria_juvenil_b_17():
    assert obter_categoria(17)=='Juvenil B'

def test_obter_categoria_senior_18():
    assert obter_categoria(18)=='Senior'

def test_obter_categoria_senior_19():
    assert obter_categoria(19)=='Senior'