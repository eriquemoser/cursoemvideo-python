import random

lista = []


def maior(num):
    t = len(num)
    m = max(num)
    print(f'Foram passados {t} valores.')
    print(f'O maior valor é {m}.')

def solicita():
    a = random.randint(1, 6)
    lista.clear()
    for c in range(0, a):
        b = random.randint(1, 10)
        lista.append(b)
    return lista

for y in range(0,5):
    lista1 = solicita()
    print(f'Foram sorteados os valores: {lista1}')
    maior(lista1)
    print('-='*20)
