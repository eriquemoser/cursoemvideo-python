while True:
    print('-*'*10, end='')
    print('TABUADA', end='')
    print('-*'*10)
    n = int(input('Digite um número para saber sua tabuada: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{c}x{n}={c*n}')
