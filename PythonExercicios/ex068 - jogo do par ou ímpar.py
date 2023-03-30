import random
from time import sleep

pontos = soma = 0

print('O jogo do par ou ímpar vai começar, se prepare...')
sleep(1)

while True:
    print('---'*10)
    resp = str(input('Par ou Ímpar (P/I)? ')).strip()[0].upper()
    if resp == 'P':
        print(f'A máquina escolheu I')
    if resp == 'I':
        print(f'A máquina escolheu P')
    num = int(input('Escolha um número(0~5): '))
    maq = random.randint(0, 5)
    print('1')
    sleep(1)
    print('2')
    sleep(1)
    print('3')
    sleep(1)
    print('JÁ')
    soma = num + maq
    if soma % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
    print(f'{num} e {maq}, {resultado}')
    if resultado[0] == resp:
        print('Parabéns, vamos para a próxima rodada!')
        pontos += 1
    else:
        break

print(f'Você perdeu. Sua pontuação foi de {pontos} pontos.')
