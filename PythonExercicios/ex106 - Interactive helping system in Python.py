resp = ''
while True:

    print(f'\033[31;40m{"":~^40}\033[m')
    print(f"\033[31;40m{'Sistema de Busca de Ajuda':^40}\033[m")
    print(f'\033[31;40m{"":~^40}\033[m')

    resp = str(input('Digite a biblioteca ou função [fim p/ sair]: '))
    if resp == 'fim':
        break
    print(f'\033[40m{"":~^40}\033[m')
    print(f"\033[40m{f'Acessando o manual de {resp}':^40}\033[m")
    print(f'\033[40m{"":~^40}\033[m')
    print(f'\033[32m{help(resp)}\033[m')