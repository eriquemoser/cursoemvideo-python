tupla = ('lápis', 1.75, 'borracha', 2, 'caderno', 15.90, 'estojo', 25, 'transferidor', 4.2, 'compasso', 9.99, 'mochila', 120.32, 'caneta', 22.30, 'livro', 34.90)

print(tupla)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for c in range(0,len(tupla)):
    if c % 2 == 0:
        print(f'{tupla[c]:.<30}', 'R$', end = '')
    else:
        print(f'{tupla[c]:>8.2f}')

print('-'*40)