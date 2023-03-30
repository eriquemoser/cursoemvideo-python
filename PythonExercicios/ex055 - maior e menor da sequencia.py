
n = 5 #nro pessoas
vetor= [0]*n

for c in range(1,n+1):
    peso = float(input('Digite o peso da pessoa ({}/{}): '.format(c,n)))
    vetor[c-1] = peso

print('O maior peso lido foi: {}kg'.format(max(vetor)))
print('O menor peso lido foi: {}kg'.format(min(vetor)))
