import datetime
year = datetime.date.today().year

trabalhador = {}
#ficha = []

#while True:
trabalhador['nome'] = str(input('Qual o nome do trabalhador? '))
ano = int(input('Qual o ano de nascimento? '))
trabalhador['carteira'] = int(input('Qual o número da carteira[0 - não tem]? '))
trabalhador['idade'] = year - ano

if trabalhador['carteira'] != 0:
    trabalhador['contratacao'] = int(input('Digite o ano de contratação: '))
    trabalhador['salario'] = float(input('Digite o seu salário: '))
    trabalhador['aposentadoria'] = (trabalhador['contratacao'] + 35) - ano

    #ficha.append(trabalhador.copy())
    #trabalhador.clear()

    #resp = str(input('Deseja continuar[S/N]? '))
    #if resp in 'nN':
    #    break

print('-='*20)
print()

for k,v in trabalhador.items():
    print(f'-{k} tem valor {v}')


#print(trabalhador)
#print(ficha)