import moeda

preco=float(input('Digite o preço: R$'))

print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Com um aumento de 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Com uma diminuição de 10%, temos {moeda.diminuir(preco, 10)}')