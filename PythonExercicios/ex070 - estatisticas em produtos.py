print('---'*15)
print('CADASTRO DE PRODUTOS')
print('---'*15)

tot = contP = baratoP = cont = 0
baratoN = ' '

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))

    if cont == 0 or preco < baratoP:
        baratoP = preco
        baratoN = produto
    cont += 1

    tot += preco
    if preco > 1000:
        contP += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O valor total gasto foi de R${tot}')
print(f'{contP} produtos custaram mais de MIL Reais')
print(f'O produto mais barato foi {baratoN} e custou {baratoP}')