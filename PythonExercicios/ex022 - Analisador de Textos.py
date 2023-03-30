nome = str(input('Digite o nome completo: ')).strip()

print('O nome em minúsculas é: {}'.format(nome.lower()))
print('O nome em maiúsculas é: {}'.format(nome.upper()))

print('O nome tem {} letras.'.format(len(nome) - nome.count(' ')))

var1 = nome.find(' ')
nome1 = nome[:var1]

print('O primeiro nome é: {}, e tem {} letras.'.format(nome1,len(nome1)))