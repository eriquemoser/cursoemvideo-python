tupla = ('jose', 'maria', 'casa', 'pato', 'gato', 'olho', 'mesa')

print('*'*30)
print(f'{"Impressão de Vogais":^30}')
print('*'*30)

for palavra in tupla:
    print(palavra, '= ', end = '')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end = ' ')
    print('\n', end = '')