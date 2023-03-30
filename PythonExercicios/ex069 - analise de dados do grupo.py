print('___DADOS CADASTRAIS___')
cont_idade = cont_sexo = cont_mul = 0

while True:
    idade = int(input('Qual é a idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o sexo(M/F)? ')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar(S/N)? ')).strip().upper()[0]
    if idade > 20:
        cont_idade += 1
    if sexo == 'M':
        cont_sexo += 1
    if sexo == 'F' and idade < 20:
        cont_mul += 1
    if resp == 'N':
        break
print('*-*'*20)
print(f'Número de pessoas > 18: {cont_idade}')
print(f'Número de homens: {cont_sexo}')
print(f'Número de mulheres < 20: {cont_mul}')
print('*-*'*20)


