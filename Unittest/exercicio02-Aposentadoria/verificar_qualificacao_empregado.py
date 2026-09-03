def verificar_qualificacao_empregado(idade, tempo_servico):
    requerer="Requerer aposentadoria"
    nao_requerer="Não requerer aposentadoria"
    if type(idade) != int and type(tempo_servico) != int:
        raise TypeError
    if idade < 0 or tempo_servico < 0:
        raise ValueError
    if idade >= 65 or tempo_servico >= 30:
        return requerer
    elif idade >= 60 and tempo_servico >= 25:
        return requerer
    else:
        return nao_requerer