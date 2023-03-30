print('='*25)
print('DETECTOR DE PALÍNDROMO')
print('='*25)

frase2 = ''
frase = str(input('Digite sua frase: ')).strip()
palavras = frase.split()
junto = ''.join(palavras)

#print(junto)
#print(len(frase))
#print(frase[2])

for c in range(len(junto),0,-1):
    #print('', frase[c-1], end = '')
    frase2 = frase2 + junto[c-1]

'''ou então fazer: inverso = junto[::-1}'''

print('A frase invertida é: {}'.format(frase2))

print('É palíndromo?')

if junto == frase2:
    print("SIM")
else:
    print('NÃO')