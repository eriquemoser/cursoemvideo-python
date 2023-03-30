def notas(*n, sit=False):
    """
    Função que calcula informações sobre um número indefinido de notas de um aluno
    :param n: recebe notas
    :param sit: recebe informaçao se é para printar a situação do aluno
    :return: retorna um dicionário com as informações
    Criado por Érique Moser
    """
    ficha = {}
    ficha['total']= len(n)
    ficha['maior']= max(n)
    ficha['menor']= min(n)
    ficha['media']= sum(n)/len(n)
    if sit:
        if ficha['media'] >= 7:
            ficha['situação'] = 'APROVADO'
        elif ficha['media'] >= 5:
            ficha['situação'] = 'RECUPERAÇÃO'
        else:
            ficha['situação'] = 'REPROVADO'

    return ficha


#Programa principal
resp = notas(10, 5, 4, 10, 1, sit=True)
print(resp)