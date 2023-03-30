import random
from time import sleep
conjunto = []
jogo = []

print('-='*20)
print('Criador de palpites para a Mega Sena')

jogos = int(input('Quantos jogos serão criados? '))

for c in range(0,jogos):
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    conjunto.append(jogo[:])
    jogo.clear()

print('PROCESSANDO...')
sleep(2)

print('Os números da sorte escolhidos são: ')

for j in conjunto:
    print(j)
