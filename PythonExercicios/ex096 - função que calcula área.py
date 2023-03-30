def area(x,y):
    c = x * y
    print(f'A área calculada para as dimensões {x}m X {y}m é de {c}m²')


a = float(input('Digite a largura do terreno em mts: '))
b = float(input('Digite a profundidade do terreno em mts: '))

area(a,b)
