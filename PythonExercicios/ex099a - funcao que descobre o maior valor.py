def maior(*num):
    print('Recebi os valores: ', end='')
    cont = 0
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        cont += 1
    print()
    tamanho = len(num)
    print(f'Ao todo são {tamanho} numeros e o maior valor é {maior} .')
    print('-=' * 20)


# programa principal
print('-=' * 20)
maior(2, 4, 6, 7, 8, 1, 4)
maior(1, 5, 2, 7, 4)
maior(2, 4, 1)
maior(0)
