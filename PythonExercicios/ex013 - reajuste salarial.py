salario = float(input('Qual o salário do funcionário? R$'))
aumento = 15
final = (1+(aumento/100))*salario

print('O funcionário que recebia R${:.2f}, com 15% de aumento, passou a receber R${:.2f}'.format(salario,final))