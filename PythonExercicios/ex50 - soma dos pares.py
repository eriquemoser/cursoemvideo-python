max = 6
cont = 0
n = 0
soma = 0

for c in range(1,max+1):
    n = int(input('Digite um número inteiro ({}/{}): '.format(c,max)))
    if n%2 == 0:
        cont += 1
        soma += n

print('{} número foram pares e a soma deles é: {}'.format(cont, soma))