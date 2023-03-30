count = 0

jogador = {}
ficha = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input('Numero de partidas que jogou: '))
    jogador['gols'] = []

    for c in range(0,jogador['partidas']):
        nro = int(input(f'Digite o número de gols do jogo {c}: '))
        count += nro
        jogador['gols'].append(nro)
    jogador['total'] = count

    ficha.append(jogador.copy())


    resp = str(input('Deseja continuar[S/N]: '))
    if resp in 'nN':
        break

print()
#print('=-'*20)
print(f'{"DADOS DOS JOGADORES:":.^40}')

print(f'{"Cod":^4}',f'{"Nome":<15}',f'{"Partidas":^15}', f'{"Gols":^15}', f'{"Total":^15}')
for p,v in enumerate(ficha):
    print(f'{p:^4}', f'{v["nome"]:<15}', f'{v["partidas"]:^15}', f'{str(v["gols"]):^15}', f'{v["total"]:^15}')
print(f'{"":.^40}')

print('cod ', end = '')
for i in jogador.keys():
    print(f'{i:<15}', end = '')
print()
for k,v in enumerate(ficha):
    print(f'{k:<4}', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()

while True:
    dados=int(input('Mostrar dados de qual jogador[999 para sair]? '))
    print()
    for p,v in enumerate(ficha):
        if p == dados:
            print(f'O jogador {v["nome"]} jogou {v["partidas"]} partidas')
            for r,t in enumerate(v['gols']):
                print(f'    => Na partida {r+1}, marcou {t} gols.')
            print(f'Foram um total de {v["total"]} gols.')


    if dados == 999:
        print('FINALIZANDO...')
        break
    print('-=' * 15)

