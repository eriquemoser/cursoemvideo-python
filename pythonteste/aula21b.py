def contador(i, f, p):
    """
    Função utilizada para realizar a contagem de um número até o outro
    :param i: valor inicial
    :param f: valor final
    :param p: valor do passo
    :return: sem retorno
    Criado por Érique Moser
    """
    cont = i
    while cont <= f:
        print(cont, end=' ')
        cont += p
    print('FIM')


contador(0, 100, 10)
help(contador)
