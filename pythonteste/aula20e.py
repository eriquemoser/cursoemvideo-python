def valores(*valores):
    s=0
    for c in valores:
        s+=c
    print(f'A soma dos valores {valores} é: {s}.')


valores(5, 2)
valores(2,9,4)