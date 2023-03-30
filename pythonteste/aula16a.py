lanche = ('hambúrguer', 'suco','pizza', 'pudim', 'batata frita')

print(lanche[-2:])

for comida in lanche:
    print(f'1 - Eu vou comer {comida}')

for cont in range(0,len(lanche)):
    print(f'2 - Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'3 - Eu vou comer {comida} na posição {pos}')

print('Eu comi pra caramba')

print(sorted(lanche))