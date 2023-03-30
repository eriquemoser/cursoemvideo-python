lista = []
totpar = tot3c = mai2l = 0
for c in range(0, 3):
    for i in range(0, 3):
        lista.append(int(input(f'Digite um valor para [{c}, {i}]: ')))

print('=-' * 20)
for p, v in enumerate(lista):
    print(f'[{v:^5}]', end='')
    if p == 2 or p == 5:
        print()
    if v % 2 == 0:
        totpar += v
    if p == 2 or p == 5 or p == 8:
        tot3c += v
    if p == 3:
        mai2l = v
    if 2 < p < 6:
        if v > mai2l:
            mai2l = v

print()
print('--' * 20)

print(f'A soma dos números pares é: {totpar}')
print(f'A soma dos números da terceira coluna é: {tot3c}')
print(f'O maior número da segunda linha é: {mai2l}')
