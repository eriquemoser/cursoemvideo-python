cidade = str(input('Digite a cidade que você mora: ')).strip()

#cidade = cidade.lower()
#print('A cidade começa com nome Santo: {}'.format('santo' in cidade))

print(cidade[:5].upper() == 'SANTO')