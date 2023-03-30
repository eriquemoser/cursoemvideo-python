idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Você está muito NOVO para se alistar.'
          '\n Ainda faltam {} anos.'.format(18-idade))
elif 18 <= idade <= 25:
    print('Chegou a hora do alistamento!')
else:
    print('Você está muito VELHO para se alistar.'
          '\n Já fazem {} anos que passou do prazo.'.format(idade-25))