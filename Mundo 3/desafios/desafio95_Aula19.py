#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário. incluindo o total de gols feitos durante o campeonato.Aprimore o desafio para que ele funcione cm vários jogadores, incluindo um sistema de visualização detalhada de detalhes do aproveitamento de cada jogador

temporada = []
jogador = {}
gol_partida = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for partida in range(partidas):
        gol_partida.append(int(input(f' -> quantos gols {jogador['nome']} fez na {partida +1}º partida? ')))
    jogador['gols'] = gol_partida[:]
    jogador['gols temp'] = sum(gol_partida[:])
    temporada.append(jogador.copy())
    continuar = ' '
    gol_partida.clear()
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Digite uma resposta válida!')
    print('-='*30)
    if continuar == 'N':
        break
print('Estatísticas da Temporada\n')
print(f'{'ID '}', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for i, player in enumerate(temporada):
    print(f'{i:>2} ', end ='')
    for v in player.values():
        print(f'{str(v):<15}', end='')
    print()
print('-='*30)
while True:
    estatistica = int(input('Deseja mostrar os dados detalhados de qual jogador?[ID](999 p/ parar) '))
        
    if estatistica > len(temporada):
        print('Ops... Não existe esse jogador')
    elif estatistica == 999:
        print('Estatísticas encerradas!')
        break
    print('-'*40)
    print(f'Estatisticas do jogador {temporada[estatistica]['nome']}:')
    for partida, gol in enumerate(temporada[estatistica]['gols']):
        print(f'    -> No {partida + 1}º jogo fez {gol} gols')
