n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media < 5:
    print('Você foi \033[31mReprovado')
elif 5 <= media < 7:
    print('Você está em \033[33mRecuperação')
elif media >= 7:
    print('Você foi \033[32mAprovado')