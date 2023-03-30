from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))

idade = date.today().year - ano

print('A idade do atleta é: {} anos'.format(idade))

if idade < 9:
    print('A sua categoria é MIRIM.')
elif 9 <= idade < 14:
    print('A sua categoria é INFANTIL')
elif 14 <= idade < 19:
    print('A sua categoria é JÚNIOR')
elif 19 <= idade < 25:
    print('A sua categoria é SÊNIOR')
elif 25 <= idade:
    print('A sua categoria é MASTER')