import random
maquina = random.choice(['Pedra','Papel','Tesoura'])

print('Escolha:'
                    '\n  Pedra'
                    '\n  Papel'
                    '\n  Tesoura \n')

escolha = str(input('Sua opção: '))

print('Seu oponente selecionou {}'.format(maquina))

if escolha == 'Pedra' and maquina == 'Pedra':
    print('Houve empate')
elif escolha == 'Pedra' and maquina == 'Papel':
    print('Você perdeu')
elif escolha == 'Pedra' and maquina == 'Tesoura':
    print('Você ganhou')

elif escolha == 'Papel' and maquina == 'Pedra':
    print('Você ganhou')
elif escolha == 'Papel' and maquina == 'Papel':
    print('Houve empate')
elif escolha == 'Papel' and maquina == 'Tesoura':
    print('Você perdeu')

elif escolha == 'Tesoura' and maquina == 'Pedra':
    print('Você perdeu')
elif escolha == 'Tesoura' and maquina == 'Papel':
    print('Você ganhou')
elif escolha == 'Tesoura' and maquina == 'Tesoura':
    print('Houve empate')

