import moeda

#preco=float(input('Digite o preço: R$'))
preco = 100

moeda.resumo(p, 10, 10)

print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco,True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco,formato=True)}')
print(f'Com um aumento de 10%, temos {moeda.aumentar(preco, 10,formato=True)}')
print(f'Com uma diminuição de 10%, temos {moeda.diminuir(preco, 10, formato=True)}')