p= 4 #nro pessoas
cont = 0 #contador
lista = [0]*4
mediaidade=0

for c in range(1,p+1):
    nome = str(input('Nome pessoa {}: '.format(c)))
    idade = int(input('Idade pessoa {} '.format(c)))
    sexo = str(input('Sexo pessoa {} (M/F): '.format(c)))

    mediaidade += idade
    if sexo == 'M':
        lista[c-1]=idade

    if sexo == 'F' and idade < 20:
        cont += 1


media = mediaidade/p
print(lista)
print('A média de idade do grupo é: {} anos'.format(media))
print('O homem mais velho tem {} anos'.format(max(lista)))
print('O número de mulheres jovens (<20) é: {}'.format(cont))