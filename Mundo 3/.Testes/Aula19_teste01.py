pessoas = {'Nome':'Arthur','Idade':17, 'sexo':'Masculino'}

# print(f'O {pessoas['Nome']} tem {pessoas['Idade']} anos e é do sexo {pessoas['sexo']}')

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

pessoas['peso'] = 57
for k, v in pessoas.items():
    print(f'{k} = {v}')