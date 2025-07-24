turma = []


while True:
    aluno = str(input('Nome do Aluno: ')).title()
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    turma.append([aluno,[nota1, nota2]])
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
        break
