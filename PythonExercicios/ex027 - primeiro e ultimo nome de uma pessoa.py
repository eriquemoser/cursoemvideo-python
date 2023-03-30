nome = input('Digite seu nome: ').strip()

nome = nome.split()

print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)-1]))