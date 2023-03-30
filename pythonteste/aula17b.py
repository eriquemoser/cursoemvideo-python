#lista=[]
lista=list()

lista.append(4)
lista.append(6)
lista.append(3)

for cont in range(0,3):
    lista.append(int(input('Digite um valor no teclado: ')))

for posicao, valor in enumerate(lista):
    print(f'Na posição {posicao}, encontrei o valor {valor}.')
print('Cheguei ao final da lista')