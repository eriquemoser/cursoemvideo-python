count = 0

jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Numero de partidas que jogou: '))
jogador['gols'] = []

for c in range(0,jogador['partidas']):
    nro = int(input(f'Digite o número de gols do jogo {c}: '))
    count += nro
    jogador['gols'].append(nro)

jogador['total'] = count

print('=-'*20)
print(jogador)
print('=-'*20)
for k,v in jogador.items():
    print(f'-O campo {k} tem valor {v}.')
print('=-'*20)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for p,v in enumerate(jogador['gols']):
    print(f'    => Na partida {p+1}, marcou {v} gols.')
print(f'Foram um total de {jogador["total"]} gols.')