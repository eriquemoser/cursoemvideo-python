num = int(input('Digite um número: '))

print('Escolha uma opção para conversão de base: '
      '\n [ 1 ] conversão para binária'
      '\n [ 2 ] conversão para octal'
      '\n [ 3 ] conversão para hexadecimal')

opção = int(input('Sua opção: '))

if opção == 1:
      print('Resultado: {}.'.format(bin(num)[2:]))
elif opção == 2:
      print('Resultado: {}.'.format(oct(num)[2:]))
elif opção == 3:
      print('Resultado: {}'.format(hex(num)[2:]))
else:
      print('Nenhuma opção válida foi digitada. Tente novamente!')