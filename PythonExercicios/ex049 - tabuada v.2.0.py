v = int(input('Digite um número para ver sua tabuada: '))

print('='*20)
for c in range(1,11):
    print('{:2} * {:>2} = {:<3}'.format(c,v,c*v))
print('='*20)