escola = []
aluno = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    aluno.append(nome)
    n1 = float(input('Digite a nota 1: '))
    aluno.append(n1)
    n2 = float(input('Digite a nota 2: '))
    aluno.append(n2)
    media = (n1 + n2) / 2
    aluno.append(media)

    escola.append(aluno[:])
    aluno.clear()

    resp = str(input('Você deseja continuar [S/N]? '))
    if resp in 'nN':
        break

print('-='*30)
print('BOLETIM ESCOLAR')
print('-='*30)
print('Nro     Aluno      Media')

for p,v in enumerate(escola):
    print(f'{p:^3}','|', f'{v[0]:^10}','|', f'{v[3]:^6}')

print('=-'*10)
print('CONSULTA ALUNO:')
while True:
    num = int(input('Digite o número correspondente do aluno \npara saber sua nota, ou 999 para sair: '))
    for p,v in enumerate(escola):
        if num == p:
            print(f'As notas de {v[0]} são {v[1]} e {v[2]}.')

    if num == 999:
        break