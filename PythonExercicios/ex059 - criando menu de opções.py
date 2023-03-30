print('Essa é uma calculadora versátil. \n Digite o número apropriado para realizar a conta que deseja:')
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
condição= False

while condição != True:

    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))

    valor = int(input('Opção desejada: '))
    if valor == 1:
        resultado= num1 + num2
    elif valor == 2:
        resultado = num1 * num2
    elif valor == 3:
        if num1 > num2:
            resultado = num1
        else:
            resultado = num2
    elif valor ==4:
        print('Tente novamente')
    elif valor == 5:
        condição = True
    if valor != 5 and valor !=4:
        print("O resultado da operação foi: {}".format(resultado))