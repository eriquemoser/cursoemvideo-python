lista = []


while True:


    while True:
        flag = 0
        num=int(input('Digite um valor para ser adicionado: '))

        for v in lista:
            if v == num:
                print('Erro de número repetido, tente novamente!')
                flag = 1
        if flag == 0:
            break

    lista.append(num)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]

    if resp == 'N':
        break

print(sorted(lista))
