lista = []
for c in range(0,3):
    for i in range(0,3):
        lista.append(int(input(f'Digite um valor para [{c}, {i}]: ')))

print('=-'*20)
for p,v in enumerate(lista):
    print(f'[{v:^5}]', end ='')
    if p == 2 or p == 5:
        print()
