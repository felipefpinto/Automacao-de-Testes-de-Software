def calculadora(valor_total):
    if valor_total <=0:
        raise(ValueError)
    if valor_total<=100:
        valor_final=valor_total
        return valor_final
    elif valor_total<=500 :
        valor_final=valor_total-(valor_total*0.10)
        return valor_final
    else:
        valor_final=valor_total-(valor_total*0.20)
        return valor_final
