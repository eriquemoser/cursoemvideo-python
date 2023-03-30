n = int(input('Digite um número para saber se é primo: '))

divisor = 0

print('\ndivisores: ', end = ' ')
for c in range(1,n+1):
    if n % c == 0:
        divisor += 1
        print(c, end = ' ')

print('\n \nResultado: ')
if divisor > 2:
    print('Não é primo')
else:
    print('É primo!')