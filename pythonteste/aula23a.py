try: #o que vai tentar fazer
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))

    r = a/b
except: #o que vai aparecer se der errado
    print('Infelizmente tivemos um problema :(')
else: #o que vai aparecer se der certo
    print(f'O resultado é {r:.2f}')
finally: #acontece sempre
    print('Volte sempre')