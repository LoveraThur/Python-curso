#Faça um programa que leia o nome e media de um aluno, guardando tambem a situação em um dicionário. No final, mostre o conteudo da estrutura na tela

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno['nome']}: '))

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
if aluno['Média'] >= 7.5:
    print('A situação é igual a Aprovado')
else:
    print('A situação é igual a Reprovado')