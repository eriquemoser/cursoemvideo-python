tot = cont = num = 0
num = int(input('Digite um valor: '))

while num != 999:
    tot = tot + num
    cont = cont + 1
    num = int(input('Digite um valor: '))

print('Foram digitados {} números e a soma deles corresponde à {}'.format(cont,tot))