import moeda

preco=float(input('Digite o preço: R$'))

print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'Com um aumento de 10%, temos {moeda.aumentar(preco, 10)}')
print(f'Com uma diminuição de 10%, temos {moeda.diminuir(preco, 10)}')