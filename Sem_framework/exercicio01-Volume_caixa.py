def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura

# ct01
try:
    resultado = calcula_volume(1, 1, 1)
    assert resultado == 1
    print ('Volume Correto!')

except AssertionError:
    print('Volume Errado!')

# ct02
try:
    resultado = calcula_volume(2, 4, 3)
    assert resultado == 24
    print ('Volume Correto!')

except AssertionError:
    print('Volume Errado!')

# ct03
try:
    resultado = calcula_volume(5, 5, 2)
    assert resultado == 100
    print ('Volume Correto!')

except AssertionError:
    print('Volume Errado!')