print('Este programa irá gerar o fatorial do número que você digitou.')
print('Vamos lá')
num = int(input('Digite um número: '))
cont = num
fatorial = num

while cont != 1:
    cont -= 1
    fatorial *= cont

print('O fatorial de {} é {}'.format(num,fatorial))