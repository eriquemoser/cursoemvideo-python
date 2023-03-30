pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade': 22}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

del pessoas['sexo']
pessoas['nome'] = 'Leandro'

pessoas['peso'] = 98.5

for k,v in pessoas.items():
    print(k,v)