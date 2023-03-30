lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    resp=str(input('Deseja continuar [S/N]? '))
    if resp in 'nN':
        break

print(f'Foram digitados {len(lista)} valores!')
lista.sort(reverse=True)
print(f'A lista em ordem crescente é: {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista')
else:
    print('O valor 5 não foi digitado')
