a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1

while cont != 11:
    an = a1 + (cont-1) * r
    print('{} -> '.format(an), end='')
    cont += 1
print('Acabou')