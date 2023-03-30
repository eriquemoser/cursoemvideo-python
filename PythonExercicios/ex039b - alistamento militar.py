from datetime import date

ano = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - ano

if idade < 18:
    print('Sua idade é de {} anos e ainda não está na hora do alistamento.'
          '\n Faltam {} anos!'.format(idade,18-idade))
elif idade == 18:
    print('Você tem {} anos e chegou a hora do alistamento. Não perca tempo!'.format(idade))
else:
    print('Sua idade é de {} anos e passou da hora do alistamento.'
          '\n Você deveria ter se alistado fazer {} anos!'.format(idade, idade-18))