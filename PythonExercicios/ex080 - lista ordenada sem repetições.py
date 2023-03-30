lista = []

for c in range(1,6):
    n = int(input(f'Digite o valor {c}: '))
    if c == 1 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        for p,v in enumerate(lista):
            if n < v:
                lista.insert(p, n)
                print(f'Adicionado na posição {p} da lista')
                break

print(lista)