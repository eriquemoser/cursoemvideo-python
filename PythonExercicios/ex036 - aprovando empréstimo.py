casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Em quantos anos você deseja pagar: '))

prestação = casa / (anos*12)
margem = salario * 0.3

print('Valor da prestação atual: R${}'.format(prestação))
print('Valor máximo permitido da prestação: R${}'.format(margem))

if prestação < margem:
    print('Sua prestação foi aprovada!')
else:
    print('Sua prestação foi negada.')