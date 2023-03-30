def dobro(valor, formato=False):
    tot = valor * 2
    return tot if formato is False else moeda(tot)


def metade(valor,formato=False):
    tot = valor / 2
    if formato:
        return f'R${tot:.2f}'.replace('.', ',')
    else:
        return tot


def aumentar(valor, quant,formato=False):
    tot = valor * (1 + (quant / 100))
    if formato:
        return f'R${tot:.2f}'.replace('.', ',')
    else:
        return tot


def diminuir(valor, porcent, formato=False):
    tot = valor * (1 - (porcent / 100))
    if formato:
        return f'R${tot:.2f}'.replace('.', ',')
    else:
        return tot


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
