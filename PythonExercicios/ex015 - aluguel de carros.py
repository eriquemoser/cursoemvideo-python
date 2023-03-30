dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos quilômetros rodados? '))

valor = (60 * dias) + (0.15 * km)

print('O valor a pagar é R${}.'.format(valor))