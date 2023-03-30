from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p ==0:
        p = 1
    print(f'Essa é a contagem de {i} a {f} com passo {p}.')
    cont=i
    if i<f:
        while cont <= f:
            print(cont, end = ' ')
            sleep(0.3)
            cont +=p
        print('FIM')
    if i>f:
        while cont >=f:
            print(cont,end = ' ')
            sleep(0.3)
            cont -=p
        print('FIM')
    print('-='*20)

print(f'{"CONTADOR":.^30}')
contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez: ')
inicio=int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio,fim,passo)







