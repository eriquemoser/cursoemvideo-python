cond = ''
flag = flag2 = flag3 = False
med = cont = tot = maior = menor = 0

while flag != True:
    num = int(input("Digite um número: "))

    while flag3 != True:
        maior = num
        menor = num
        flag3 = True

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    tot += num
    cont += 1

    flag2 = False
    while flag2 != True:
        cond = str(input('Continua? [S/N] ')).strip().upper()[0]
        #print(cond)
        if cond in 'N':
            flag = True
            flag2 = True
        elif cond in 'S':
            flag2 = True
        else:
            print("Sentença incorreta, digite novamente")
med = tot/cont
print("A média dos números digitados foi {}, o maior valor foi {} e o menor foi {}".format(med,maior,menor))