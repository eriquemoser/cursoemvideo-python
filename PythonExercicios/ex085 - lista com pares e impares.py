lista =[[], []]

for c in range(0,7):
    n = int(input('Digite um valor: '))
    #lista.append(int(input('Digite um valor: ')))

    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(f'Os valores da lista são {lista}')

print(f'Os valores pares são: {sorted(lista[0])}')
print(f'Os valores impares são: {sorted(lista[1])}')
