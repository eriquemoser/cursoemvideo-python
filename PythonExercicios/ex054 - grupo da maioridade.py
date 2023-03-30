from datetime import date
n = 7 #nro pessoas
cont = 0 #contador

atual = date.today().year

for c in range(1,n +1):
    ano = int(input('Digite o ano de nascimento ({}/{}): '.format(c,n)))
    if atual-ano >= 18:
        cont += 1

print('O número de pessoas que atingiram a maioridade é: {}'.format(cont))