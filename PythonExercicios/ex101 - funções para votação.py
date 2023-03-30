import datetime
from time import sleep
anoatual = datetime.date.today().year

def voto(ano):
    idade = anoatual - ano
    if idade < 18:
        return 'Negado'
    elif 18 <= idade < 65:
        return 'Obrigatório'
    elif idade >= 65:
        return 'Opcional'

#Programa principal
print(f'{"SISTEMA ELEITORAL DE VOTAÇÃO":.^40}')
ano = int(input('Digite o ano de nascimento do indivíduo: '))
decisao = voto(ano)
print('Processando...')
sleep(1)
print('Após análise, verificou-se que o voto é: ', end= '')
print(decisao)