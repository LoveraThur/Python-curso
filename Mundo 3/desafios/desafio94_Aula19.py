#crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre: A) quantas pessoas foram cadastradas. B) A média de idade do grupo. C) Uma lista com todas as mulheres. D) Uma lista com todas pessoas com idade acima da média

pessoas = []
dicionario = {}
soma_idd = 0
mulheres = []

continuar = ' '
while continuar != 'N':
    dicionario['nome'] = str(input('Nome: ')).title()

    while True:
        dicionario['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dicionario['sexo'] in 'MF':
            if dicionario['sexo'] == 'F':
                mulheres.append(dicionario['nome'])
            break
        print('Erro! Digite um sexo válido')

    dicionario['idade'] = int(input('Idade: '))
    soma_idd += dicionario['idade']
    pessoas.append(dicionario.copy())

    continuar = ' '
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]

print('-='*30)
print(f'O grupo tem {len(pessoas)} pessoas')  
media = soma_idd / len(pessoas)
print(f'A média do grupo é {media:.2f}')
print(f'As mulheres do grupo são: ', end=' ')
for mulher in mulheres:
    print(f'{mulher};', end=' ')
print()
print('Pessoas com idade acima da média:')

for p in pessoas:
    if p['idade'] > media:
        print('')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        