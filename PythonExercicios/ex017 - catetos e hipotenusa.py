import math

catOp = float(input('Informe qual é o cateto oposto: '))
catAd = float(input('Informe qual é o cateto adjacente: '))

hipot= (catOp**2 + catAd**2)**(1/2)
#hipot= math.sqrt(math.pow(catOp,2) + math.pow(catAd,2))
#hipot= math.hypot(catOp,catAd)

print('A hipotenusa é: {:.2f}.'.format(hipot))