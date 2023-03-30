preco = float(input('Qual o preço do produto? R$'))
desconto = 5
final = (1-(desconto/100))*preco

print('O produto que estava R${}, na promoção com 5% de desconto, passou a custar R${:.2f}.'.format(preco,final))