import random
lista = []


def sorteia(lista):
    for c in range(0,5):
        n = random.randint(0,10)
        lista.append(n)
    return lista


def somaPar(numeros):
    tot = 0
    for num in numeros:
        if num % 2 == 0:
            tot += num
    return tot


#programa Principal
numeros = sorteia(lista)
valor = somaPar(numeros)

print(f'Os números sorteados foram: {numeros} \n e a soma dos pares é igual a {valor}')