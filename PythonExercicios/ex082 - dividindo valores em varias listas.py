lista = []
listapar = []
listaimpar = []

while True:
    lista.append(int(input('Digite um valor para a lista: ')))

    resp = str(input('Continuar [S/N]? '))
    if resp in 'nN':
        break

for element in lista:
    if element % 2 == 0:
        listapar.append(element)
    else:
        listaimpar.append(element)

print(f'A lista normal é: {lista}')
print(f'A lista de pares é: {listapar}')
print(f'A lista de impares é: {listaimpar}')