salario = float(input('Digite o valor do seu salário: R$'))

if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print('O salário com aumento passou a ser de: R${}'.format(aumento))