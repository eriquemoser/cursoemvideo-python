r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if abs(r2 - r3) < r1 < r2+r3:
    print('Pode formar triangulo.')
else:
    print('Não pode formar triangulo.')