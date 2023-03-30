contesq = contdir = 0

print('=-'*20)
print(f'{"VALIDADOR DE EXPRESSÃO MATEMÁTICA":^40}')
print('=-'*20)
exp = str(input("Digite uma expressão matemática: \n"))

for letra in exp:
    if letra == "(":
        contesq +=1
    elif letra == ")":
        contdir +=1

if contesq < contdir:
    print('faltou um parênteses do lado esquerto')

if contesq > contdir:
    print('Faltou um parênteses do aldo direito')

if contesq == contdir:
    print('Parabéns, você digitou corretamente')