a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 0
cont2 = 10
cont3 = 1
total = cont2

while cont3 !=0:

    while cont != cont2:
        an = a1 + (cont) * r
        print('{} -> '.format(an), end='')
        cont += 1
    print('Pausa')
    a1 = an
    cont = 1
    cont3 = int(input("Quantos termos você quer mostrar a mais? "))
    cont2 = cont3 + 1
    total = total + cont3

print('FIM. Com {} números mostrados.'.format(total))