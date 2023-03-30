pessoa = {}
ficha = []
medidade = 0

while True:
    pessoa['nome']=str(input('Digite o nome da pessoa: '))
    while True:
        pessoa['sexo']=str(input('Digite o sexo[M/F]: '))
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Por favor, digite apenas M ou F!')
    pessoa['idade']=int(input('Digite a idade: '))

    ficha.append(pessoa.copy())
    pessoa.clear()

    resp=str(input('Você deseja cadastrar mais alguém[S/N]? '))
    if resp in 'nN':
        break

print('=-'*20)

print(f'Foram cadastradas {len(ficha)} pessoas.\n')

for p in ficha:
    medidade += p['idade']
print(f'A média de idade das pessoas cadastradas foram {medidade/len(ficha)}.\n')

print('As mulheres cadastradas são: ')
for p in ficha:
    if p['sexo'] in 'fF':
        print('=>', p['nome'])

print()
print('A lista de pessoas com idade acima da média são: ')
for p in ficha:
    if p['idade'] >= medidade/len(ficha):
        print('=>', p['nome'])