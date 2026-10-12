def calcular_imc(peso,altura):
    if type(peso) == float and type(peso)==int or type(altura) != float:
        raise TypeError
    if peso <= 0 or altura <= 0:
        raise ValueError  
    
    imc = peso / (altura ** 2)
    
    if imc<18.5:
        return "Abaixo do peso"
    elif imc>=18.5 and imc<25:
        return "Peso normal"
    elif imc>=25 and imc<30:
        return "Sobrepeso"
    elif imc>=30 and imc<35:
        return "Obesidade grau I"
    elif imc>=35 and imc<40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"
