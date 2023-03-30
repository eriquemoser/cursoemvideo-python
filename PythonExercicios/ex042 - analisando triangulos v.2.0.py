r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if abs(r2 - r3) < r1 < r2+r3:
    print('Pode formar triangulo.')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO')
    elif r1 == r2 != r3 or r1 != r2 == r3 or r1 == r3 != r2:
        print('O triângulo é ISÓSCELES')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é ESCALENO')

else:
    print('Não pode formar triangulo.')

