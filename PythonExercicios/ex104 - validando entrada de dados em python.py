def leiaInt(string):
    while string.isnumeric() == False:
        #print(type(string))
        string = input('Digite um número: ')
        if string.isnumeric() == False:
            print('\033[31m ERRO! Digite um número válido\033[m')
        #print(type(string))
    return string

#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')