#50, 20, 10, 1
ced50 = ced20 = ced10 = ced1 = 0

valor = int(input('Qual o valor a ser sacado? '))
resto = valor

while True:
    if resto >= 50:
        resto = resto-50
        ced50 += 1
    print(resto)
    if resto >= 20:
        resto = resto-20
        ced20 += 1
    print(resto)
    if resto >= 10:
        resto = resto-10
        ced10 += 1
    print(resto)
    if resto >= 1:
        resto = resto-1
        ced1 += 1
    print(resto)

    if resto == 0:
        break

print(f'Preparando saque: \n {ced50} notas de R$50 \n {ced20} notas de R$20 \n {ced10} notas de R$10 \n {ced1} notas de R$1')