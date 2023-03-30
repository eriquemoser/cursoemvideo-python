def leiaDinheiro(string):
    válido = False
    while válido is not True:
        entrada = str(input(string)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[31m ERRO! Digite um valor válido\033[m')
        else:
            válido = True
            return(float(entrada))