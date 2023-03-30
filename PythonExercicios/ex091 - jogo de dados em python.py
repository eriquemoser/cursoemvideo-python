import random
from operator import itemgetter
from time import sleep

ranking = []

jogada = {'jogador1': random.randint(1,6),
          'jogador2' : random.randint(1,6),
          'jogador3': random.randint(1,6),
          'jogador4': random.randint(1,6)}

print('=-'*20)

for k,v in jogada.items():
    print(f'O {k} tirou {v}.')
    sleep(1)

#print('=-'*10)
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
#print(ranking)

print()
print('#######RANKING########')
for p,v in enumerate(ranking):
    print(f'{p}º lugar: O {v[0]} tirou {v[1]}')





