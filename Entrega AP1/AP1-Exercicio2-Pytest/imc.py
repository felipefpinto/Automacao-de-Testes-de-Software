def calcular_imc(altura: float, peso: float, nome: str) -> tuple[str, str]:
    # Validação dos tipos de dados para altura e peso
    if type(altura) not in (int, float) or type(peso) not in (int, float):
        raise TypeError("Altura e peso devem ser do tipo float ou inteiro.")
    
    if type(nome) != str:
        raise TypeError("O nome deve ser do tipo texto (str).")

    if altura <= 0 or peso <= 0:
        raise ValueError("Altura e peso devem ser valores maiores que zero.")

   
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Peso normal"
    elif imc <= 29.9:
        classificacao = "Sobrepeso"
    elif imc <= 34.9:
        classificacao = "Obesidade grau I"
    elif imc <= 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return nome, classificacao