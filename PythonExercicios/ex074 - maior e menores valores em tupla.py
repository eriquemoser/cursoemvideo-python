import random
from time import sleep
numeros = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

print(f'Os numeros sorteados foram: {numeros}')
print(f'O maior número foi: {max(numeros)}')
print(f'O menor número foi: {min(numeros)}')
