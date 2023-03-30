count9 = 0
count3 = -1

n = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))

for c in range(0,len(n)):
    if n[c] == 9:
        count9 += 1
    if n[c] == 3 and count3 < 0:
        count3 += 1
        save = c
    if n[c] % 2 == 0:
        print(f'{n[c]} é par')

print(f'Foram digitadas {count9} vezes o número 9')
if count3 != -1:
    print(f'O primeiro 3 foi digitado na posição {save+1}')
else:
    print('Não houve digitação do número 3')

#print(f'O número 9 apareceu {n.count(9)} vezes')
#if 3 in n:
#    print(f'O número 3 aparece primeiramente na posição {n.index(3)+1}')
#else:
#    print('O número 3 não aparece')
#print('Os números pares são: ', end = '')
#for num in n:
#    if num % 2 == 0:
#        print(num, end= ' ')

