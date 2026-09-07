#test_Infantil A
def obter_categoria(idade):
    if idade ==5:
        return 'Infantil A'
    if idade ==6:
        return 'Infantil A'
    if idade ==7:
        return 'Infantil A'

#refatorando o código acima infantil A
def obter_categoria(idade):
    if idade >= 5 and idade <= 7:
        return 'Infantil A'

#test_infantil_A+infantil_B
def obter_categoria(idade):
    if idade >= 5 and idade <= 7:
        return 'Infantil A'
    elif idade >= 8 and idade <= 10:
        return 'Infantil B'

#test_infantil_A+infantil_B+juvenil_A
def obter_categoria(idade):
    if idade >= 5 and idade <= 7:
        return 'Infantil A'

    elif idade >= 8 and idade <= 10:
        return 'Infantil B'

    elif idade >= 11 and idade <= 13:
        return 'Juvenil A'

#test_infantil_A+infantil_B+juvenil_A+juvenil_B
def obter_categoria(idade):
    if idade >= 5 and idade <= 7:
        return 'Infantil A'

    elif idade >= 8 and idade <= 10:
        return 'Infantil B'

    elif idade >= 11 and idade <= 13:
        return 'Juvenil A'
    elif idade >= 14 and idade <= 17:
        return 'Juvenil B'
    
#test_infantil_A+infantil_B+juvenil_A+juvenil_B
def obter_categoria(idade):
    if idade >= 5 and idade <= 7:
        return 'Infantil A'

    elif idade >= 8 and idade <= 10:
        return 'Infantil B'

    elif idade >= 11 and idade <= 13:
        return 'Juvenil A'
    elif idade >= 14 and idade <= 17:
        return 'Juvenil B'
    elif idade >= 18:
        return 'Senior'