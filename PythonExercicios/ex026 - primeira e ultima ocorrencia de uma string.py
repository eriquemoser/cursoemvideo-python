frase = str(input('Digite uma frase: ')).lower().strip()

print('quantas vezes aparece A: {}'
      ''.format(frase.count('a')))

print('o primeiro A aparece no caractere: {}'.format(frase.find('a') + 1))
print('o último A aparece no caractere: {}'.format(frase.rfind('a') + 1))