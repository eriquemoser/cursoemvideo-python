soma=0
valores=0

for c in range(3,500,3):
    if c%2 !=0:
        soma += c
        valores += 1

print('A soma de todos os {} valores é: {}.'.format(valores, soma))