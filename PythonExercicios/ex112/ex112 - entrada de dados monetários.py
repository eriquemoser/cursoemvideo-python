from ex112.utilidadesCeV import moeda, dado

#Programa principal
#preco=float(input('Digite o preço: R$'))
preco = dado.leiaDinheiro('Digite um valor: ')
moeda.resumo(preco, 20, 15)