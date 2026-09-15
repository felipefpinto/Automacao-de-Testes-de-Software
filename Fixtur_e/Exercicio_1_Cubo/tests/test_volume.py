import pytest
from src.volume_cubo import calcular_volume

@pytest.fixture
def calculo():
    volume=calcular_volume(2)
    return volume

def test_passar_lado_devolver_volume_cubo(calculo):
    assert calculo==8