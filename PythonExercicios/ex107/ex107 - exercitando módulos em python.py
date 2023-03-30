from ex107.moeda import multiplicacao, variacao

preco=float(input('Digite o preço: R$'))

print(f'O dobro de {preco} é {multiplicacao.dobro(preco)}')
print(f'A metade de {preco} é {multiplicacao.metade(preco)}')
print(f'Com um aumento de 10%, temos {variacao.aumentar(preco, 10)}')
print(f'Com uma diminuição de 10%, temos {variacao.diminuir(preco, 10)}')