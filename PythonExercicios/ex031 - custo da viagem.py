dist = float(input('Qual é a distância da viagem? '))

if dist <= 200:
    preco = dist * 0.50
    print('O preço da passagem é: R${:.2f}.'.format(preco))
else:
    preco = dist * 0.45
    print('O preço da passagem é: R${:.2f}'.format(preco))