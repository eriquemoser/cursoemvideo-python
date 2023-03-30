print('-=-' * 25)
print('Este programa irá determinar se o número que você pensou é par ou ímpar.')
print('-=-' * 25)

num = int(input('\nDigite um número: '))

resto = num % 2

if resto == 0:
    print('O número é PAR!')
else:
    print('O número é IMPAR!')