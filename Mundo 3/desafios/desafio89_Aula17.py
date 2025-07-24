#Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno inidividualmente

turma = []
aluno = []
notas= []

while True:
    aluno.append(str(input('Nome do Aluno: ')).title())
    for nota in range(0,2):
        notas.append(float(input(f'{nota+1}º nota: ')))
    aluno.append(notas[:])
    turma.append(aluno[:])
    notas.clear()
    aluno.clear()
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper() 
    if continuar == 'N':
        break
print(f'{'Nº':^5}| {'Aluno':^15}| {'Nota'}')
for numero, conteudo in enumerate(turma):
    print(f'{numero:^5}| {conteudo[0]:^15}| {sum(conteudo[1])}')
continuar = int
while True:
    continuar = int(input('Deseja mostrar as notas de qual aluno? [999 interrompe]'))
    if continuar <= len(turma):
        print(f'{turma[continuar][0]} teve as notas {turma[continuar][1]}!')
    if continuar == 999:
        print('--->> Volte Sempre <<---')
