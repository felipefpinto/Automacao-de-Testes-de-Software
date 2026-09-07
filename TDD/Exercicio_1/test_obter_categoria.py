from obter_categoria import obter_categoria
import pytest
for idade in range(5, 8):
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
    assert obter_categoria(18)=='Senior'