n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s= n1+n2
m= n1*n2
d= n1/n2
din= n1//n2
res= n1%n2
pot= n1**n2

print('Resultado matemático: \n ->a soma é {}; \n ->a multiplicação é {}; \n ->a divisão é {};'.format(s,m,d), end='')
print('\n ->a div inteira é {}; \n ->o resto é {};e \n ->a potencia é {}'.format(din,res,pot))
