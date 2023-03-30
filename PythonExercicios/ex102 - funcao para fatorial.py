def fatorial(num, show = 'False'):
    """
    ->Função que calcula o fatorial de um número
    :param num: O número desejado
    :param show: caso True, retorna os cálculos. para False, não retorna os cálculos
    :return: resultado da operação
    Criado por Érique Moser em 21/02/23
    """
    total = num
    cont = num -1
    if show == True:
        print(f'{num}! = ')
    while cont > 0:
        if show == True:
            print(f'{total} * {cont} = ', end = '')
        total *= cont
        if show == True:
            print(total)
        cont -= 1
    return f'O resultado é {total}'

#Programa principal
num = 8
print(fatorial(num, show = True))