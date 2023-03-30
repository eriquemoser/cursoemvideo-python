def resumo(v, q, p):
    print('-='*20)
    print(f'RESUMO DO VALOR'.center(40))
    print('-=' * 20)
    print(f'{"Preço analisado":<20}',end='')
    print(f'{moeda(v):>20}')
    print(f'{"Dobro do Preço":<20}', end='')
    print(f'{dobro(valor=v, formato=True):>20}')
    print(f'{"Metade do preço":<20}', end='')
    print(f'{metade(valor=v, formato=True):>20}')
    print(f'{q}{"% de aumento":<18}', end='')
    print(f'{aumentar(valor = v,quant = q, formato=True):>20}')
    print(f'{p}{"% de diminuição":<18}', end='')
    print(f'{diminuir(valor = v, porcent = p, formato=True):>20}')
    print('-=' * 20)


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
