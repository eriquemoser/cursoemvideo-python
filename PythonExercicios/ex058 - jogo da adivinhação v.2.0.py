import random
from time import sleep

num = 11
adv = random.randint(0, 10)
cont = 0

while num != adv:
    print('*'*40)
    num = int(input('Tente adivinhar um número entre 0 e 10: '))

    if num > adv:
        print('Tente novamente! eu pensei em um número MENOR')
    elif num < adv:
        print('Tente novamente! eu pensei em um número MAIOR')

    cont += 1

print('ACERTOU em {} tentativas!! eu pensei em {}!'.format(cont,adv))