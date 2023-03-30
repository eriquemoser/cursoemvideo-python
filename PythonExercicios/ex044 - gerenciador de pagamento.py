valor = float(input('Qual é o valor do produto? '))

dinheiroecheque = valor - (valor * 10 / 100)
cartao1x = valor * 0.95
cartao2x = valor
cartao3x = valor * 1.2

print('''
Opções de pagamento:
(1) à vista dinheiro/cheque
(2) à vista no cartão
(3) em até 2x no cartão
(4) 3x ou mais no cartão
''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('O valor a ser pago é de R${}.'.format(dinheiroecheque))
elif opção == 2:
    print('O valor a ser pago é de R${}.'.format(cartao1x))
elif opção == 3:
    print('O valor a ser pago é de R${}.'.format(cartao2x))
elif opção == 4:
    print('O valor a ser pago é de R${}.'.format(cartao3x))
else:
    print('Opção incorreta, tente novamente.')