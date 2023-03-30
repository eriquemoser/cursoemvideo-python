def dobro(valor):
    return valor * 2

def metade(valor):
    return valor / 2

def aumentar(valor,quant):
    tot = valor * (1+(quant/100))
    return tot

def diminuir(valor,porcent):
    tot = valor * (1-(porcent/100))
    return tot

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor}'.replace('.',',')