lista = [int(input(f'Digite um valor para a posição {c}: ')) for c in range(0,5)]

#print(f'O menor valor é {min(lista)} de posição {lista.index(min(lista))}')
print(f'O menor valor é {min(lista)} de posição: ', end='')

for p,v in enumerate(lista):
    if v == min(lista):
        print(p, '...', end='')

print(f'\nO maior valor é {max(lista)} de posição: ', end='')

for p,v in enumerate(lista):
    if v == max(lista):
        print(p, '...', end='')