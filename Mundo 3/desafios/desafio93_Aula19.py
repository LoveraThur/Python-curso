#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário. incluindo o total de gols feitos durante o campeonato.

temporada = {}
gol_partida = []


temporada['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {temporada['nome']} jogou? '))

for partida in range(partidas):
    gol_partida.append(int(input(f'Quantos gols na {partida + 1}º partida? '))) 
temporada['gols'] = gol_partida
temporada['gols temp'] = sum(gol_partida)

print('=-'*30)
print(temporada)
print('=-'*30)

for k, v in temporada.items():
    print(f'O campo {k} tem valor {v}')

print('=-'*30)
print(f'O jogador {temporada["nome"]} jogou {partidas} partidas na temporada')

for partida, gols in enumerate(gol_partida):
    print(f'   => Na partida {partida +1}, fez {gols} gols')
print(f'Marcando um total de {temporada["gols temp"]} gols na temporada')