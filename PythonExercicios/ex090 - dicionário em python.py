aluno = {}
ficha = []

for c in range(0,2):
    aluno['nome'] = str(input('Digite o nome do aluno: '))
    aluno['media'] = int(input('Digite a média do aluno: '))
    if aluno['media'] > 6:
        aluno['situação'] = 'aprovado'
    else:
        aluno['situação'] = 'reprovado'
    ficha.append(aluno.copy())

for c in range(0,2):
    print('=-' * 20)
    for k, v in aluno.items():

        print(f'-{k} é igual a {v}')
    #print(f'-O nome é {ficha[c]["nome"]}.')
    #print(f'-A média é {ficha[c]["media"]}.')
    #print(f'-A situação é {ficha[c]["situação"]}.')