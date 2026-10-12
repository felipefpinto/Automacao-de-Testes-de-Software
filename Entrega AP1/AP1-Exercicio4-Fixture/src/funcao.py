def aplicar_desconto(preco: float, percentual: float) -> float:
    if preco < 0 or percentual < 0:
        raise ValueError("O preço e o percentual devem ser maiores ou iguais a zero.")
    return preco - (preco * (percentual / 100))