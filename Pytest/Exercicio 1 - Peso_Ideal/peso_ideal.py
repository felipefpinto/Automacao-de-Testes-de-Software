def calcular_peso_ideal(altura, sexo):
    sexo = sexo.upper()
    if altura <= 1.0 or altura > 2.5:
        raise ValueError
    if type(altura) != float or type(sexo) != str:
        raise TypeError
    if sexo!= 'M' and sexo != 'F' :
        raise ValueError    
    if sexo == 'M':
        return 72.7 * altura - 58
    elif sexo == 'F':
        return 62.1 * altura - 44.7

