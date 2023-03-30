count = 0
pessoa = []
galera = []
mai = men = 0

while True:
    pessoa.append(str(input('Qual o nome da pessoa: ')))
    pessoa.append(int(input('Qual o peso: ')))

    if len(galera) == 0:
        mai = pessoa[1]
        men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        elif pessoa[1] < men:
            men = pessoa[1]

    galera.append(pessoa[:])
    pessoa.clear()


    resp=str(input('Deseja continuar [S/N]? '))
    if resp in 'nN':
        break

print(f'Número de pessoas cadastradas: {len(galera)}')

print(f'Os maiores pesos são: {mai}, de ', end= '')
for p in galera:
    if p[1] == mai:
        print(p[0], end= ', ')

print(f'\nOs menores pesos são: {men} de', end= '')
for p in galera:
    if p[1] == men:
        print(p[0], end= ', ')
