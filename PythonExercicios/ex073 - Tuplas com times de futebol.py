print('*'*25)
print('TABELA DO BRASILEIRÃO')
print('*'*25)

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
         'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino',
         'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('\nGrupo G5: ')
print(times[0:5])

print('\nGrupo Z4: ')
print(times[-4:])

print('\nOrdem alfabética')
print(sorted(times))

print('\nPosição Flamengo')
print(f'O flamengo está na {times.index("Flamengo")+1}ª posição')