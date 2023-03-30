dados = []
galera = []
totmai = totmen = 0

for c in range(0,3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Foram contabilizadas {totmai} pessoas de maior e {totmen} pessoas de menor')