#validação de entrada para valores menores a 0
"""def calculadora(valor_total):
    if valor_total <0:
        raise(ValueError)
    """
#validação de entrada para valores menores a 0
"""def calculadora(valor_total):
    if valor_total <0:
        raise(ValueError)
    if valor_total ==0:
        raise(ValueError)
    """

#valores até 100 reais não recebem desconto
'''
def calculadora(valor_total):
    if valor_total <0:
        raise(ValueError)
    if valor_total ==0:
        raise(ValueError)
    if valor_total<100:
        valor_final=valor_total
        return valor_final
'''
#valores de 100 reais não recebem desconto
'''
def calculadora(valor_total):
    if valor_total <0:
        raise(ValueError)
    if valor_total ==0:
        raise(ValueError)
    if valor_total<100:
        valor_final=valor_total
        return valor_final
    elif valor_total == 100:
        valor_final=valor_total
        return valor_final
'''
#valores até 500 recebe 10% de desconto
'''def calculadora(valor_total):
    if valor_total <0:
        raise(ValueError)
    if valor_total ==0:
        raise(ValueError)
    if valor_total<100:
        valor_final=valor_total
        return valor_final
    elif valor_total == 100:
        valor_final=valor_total
        return valor_final
    elif valor_total<500:
        valor_final=valor_total-(valor_total*0.10)
        return valor_final
'''
#valores acima de 500 recebe 20% de desconto
"""def calculadora(valor_total):
    if valor_total <0:
        raise(ValueError)
    if valor_total ==0:
        raise(ValueError)
    if valor_total<100:
        valor_final=valor_total
        return valor_final
    elif valor_total == 100:
        valor_final=valor_total
        return valor_final
    elif valor_total<=500 :
        valor_final=valor_total-(valor_total*0.10)
        return valor_final
    elif valor_total>500:
        valor_final=valor_total-(valor_total*0.20)
        return valor_final

print(calculadora(100))"""