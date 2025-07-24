#faça um programa que ajuda um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

print('='*30)
print('GERADOR DE PALPITE MEGA SENA')
print('='*30)
mega_senas = int(input('Quantos jogos você quer sortear? '))
lista = []
jogos = []

print('=-'*3, end=' ')
print(f'SORTEANDO {mega_senas} JOGOS', end=' ')
print('=-'*3)
for jogo in range(mega_senas):
    for a in range(6):
        numero = (randint(0,61))
        while numero in lista:
            numero = (randint(0,61))
        lista.append(numero)
        jogos = lista[:]
    lista.clear()
    print(f'Jogo {jogo+1}: {sorted(jogos)}')
    sleep(1.5)
print('=-'*4+'> ', end= '')
print('BOM JOGO!', end=' ')
print(' <'+'=-'*4,)