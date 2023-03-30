nome = str(input('Qual é seu nome? '))
if nome == 'Érique':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'José':
    print('Seu nome é comum no Brasil.')
elif nome in 'Ana Paula Silvia Roberta Camila':
    print('Seu nome é feminino')
else:
    print('Seu nome é bem normal.')

print('Prazer em te conhecer, {}!'.format(nome))