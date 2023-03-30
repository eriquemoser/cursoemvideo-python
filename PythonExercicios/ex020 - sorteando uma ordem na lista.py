import random

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

ordem = random.sample([al1,al2,al3,al4], k=4)
#lista = [al1,al2,al3,al4]
#ordem = lista.random.split()


print('A ordem de sorteio é: {}, {}, {} e {}.'.format(ordem[0], ordem[1], ordem[2], ordem[3]))