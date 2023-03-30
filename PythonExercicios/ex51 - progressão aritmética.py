a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for n in range(1,11):
    an = a1 + (n-1) * r
    print('{} -> '.format(an), end='')
print('Acabou')