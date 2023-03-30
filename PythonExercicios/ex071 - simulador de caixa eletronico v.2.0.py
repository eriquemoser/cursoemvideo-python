
valor = int(input('Digite o valor a ser sacado: R$'))
resto = valor
ced = 50
totcel = 0

while True:
    if resto >= ced:
        resto = resto - ced
        totcel += 1
    else:
        if totcel != 0:
            print(f'{totcel} notas de R${ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totcel = 0
        if resto == 0:
            break