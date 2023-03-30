import random
from time import sleep
num = int(input('Tente adivinhar um número entre 0 e 3: '))
adv = random.randint(0,3)

print('PROCESSANDO...')
sleep(2)

print('ACERTOU!! eu pensei em {}!' if num == adv else 'Tente novamente! eu pensei em {}'.format(adv,adv))