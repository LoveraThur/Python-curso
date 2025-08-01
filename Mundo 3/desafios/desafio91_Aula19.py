#crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep

jogadores = {}

print('Valores Sorteados:')

for jogador in range(1,5):
    dado = randint(1,6)
    sleep(0.7)
    print(f'    O jogador {jogador} tirou {dado}')
    jogadores[f'jogador {jogador}'] = dado

sleep(0.7)
print('\nRanking dos Jogadores:')
pos = 1
for j in sorted(jogadores, key = jogadores.get, reverse=True):
    sleep(0.7)
    print(f'    {pos}º lugar: {j} com {jogadores[j]}')
    pos += 1