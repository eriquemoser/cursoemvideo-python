def leiaInt(string):
    while True:
        try:
            s = int(input('Digite um número: '))
        except(ValueError, TypeError):
            print('\033[31m Tivemos um problema, digite novamente! \033[m')
            continue
        except (KeyboardInterrupt):
            print('\nO usuário preferiu não informar os dados')
            return 0
        else:
            return s
            break

def leiaFloat(string):
    while True:
        try:
            s = float(input('Digite um número: '))
        except(ValueError, TypeError):
            print('\033[31m Tivemos um problema, digite novamente! \033[m')
            continue
        except (KeyboardInterrupt):
            print('\nO usuário preferiu não informar os dados')
            return 0
        else:
            return s
            break

#Programa principal
n = leiaInt('Digite um inteiro: ')
print(f'Você acabou de digitar o número {n}')
m = leiaFloat('Digite um real: ')
print(f'Você acabou de digitar o número {m}')

