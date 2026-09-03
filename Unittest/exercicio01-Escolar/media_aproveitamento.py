def media_aproveitamento(n1,n2,n3,media_exercicios):
    if n1 <0 or n1>10:
        raise ValueError("Nota 1 inválida. Deve estar entre 0 e 10.")
    if n2 <0 or n2>10:
        raise ValueError("Nota 2 inválida. Deve estar entre 0 e 10.")
    if n3 <0 or n3>10:
        raise ValueError("Nota 3 inválida. Deve estar entre 0 e 10.")
    if media_exercicios <0 or media_exercicios>10:
        raise ValueError("Média dos exercícios inválida. Deve estar entre 0 e 10.")

    media_aproveitamento = (n1 + n2 * 2 + n3 * 3 + media_exercicios) / 7

    if media_aproveitamento >= 9:
        conceito = 'A'
    elif media_aproveitamento >= 7.5:
        conceito = 'B'
    elif media_aproveitamento >= 6:
        conceito = 'C'
    else:
        conceito = 'D'

    return conceito