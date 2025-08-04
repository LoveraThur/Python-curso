#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário. incluindo o total de gols feitos durante o campeonato. melhorar para varios jogadores

temporada = []
jogador = {}
gol_partida = []
continuar = ' '


while True:
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for partida in range(partidas):
        gol_partida.append(int(input(f'quantos gols {jogador['nome']} fez na {partida +1}º partida? ')))
    jogador['gols'] = gol_partida[:]
    jogador['gols temp'] = sum(gol_partida[:])
    temporada.append(jogador.copy())
    continuar = ' '
    gol_partida.clear()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    print('-='*30)
    if continuar == 'N':
        break
print('Estatísticas da Temporada\n')
print(f'{'id ':^7}', end='')
print(f'{'nome':^15}', end='')
print(f'{'gols':^7}')
for i, player in enumerate(temporada):
    print(f'{i:^7}', end ='')
    for k, v in player.items():
        if k == 'nome':
            print(f'{v:^15}', end='')
        elif k == 'gols temp':
            print(f'{v:^7}')
print(temporada)



