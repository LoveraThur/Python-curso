# brasil = []

# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}

# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[1]['uf'])

estado = {}
brasil = []

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #Copy faz fatiamento, não da para utilizar [:]

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')