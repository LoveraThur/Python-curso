#crie um programa que faça o computador jogar JOKENPÔ (pedra, papel e tesoura) com você

from random import randint
from emoji import emojize

CPU= randint(1,3)

print('='*35)
print('1- Pedra| 2- Papel| 3- Tesoura|')
player1= int(input('Escolha um entre PEDRA🪨, PAPEL📃 ou TESOURA✂️  :'))
print('='*35)


pedra= 1
papel= 2
tesoura= 3

if player1 == pedra and CPU == tesoura:
    print('Player 1 Jogou PEDRA🪨 e a CPU jogou TESOURA✂️')
    print(' \033[34mPlayer 1 \033[1;32mWINS!\033[m')

elif player1 == tesoura and CPU == papel:
    print(f'Player 1 jogou TESOURA✂️  e a CPU jogou PAPEL📃')
    print(' \033[34mPlayer 1 \033[1;32mWINS!\033[m')

elif player1 == papel and CPU == pedra:
    print(f'Player 1 jogou PAPEL📃 e a CPU jogou PEDRA🪨')
    print(' \033[34mPlayer 1 \033[1;32mWINS!\033[m')

elif CPU == pedra and player1 == tesoura  or CPU == papel and player1 == pedra:
    print('Player 1 jogou TESOURA✂️  e a CPU jogou PEDRA🪨')
    print(' \033[34mCPU \033[1;31mWINS!\033[m')

elif CPU == tesoura and player1 == papel:
    print('Player 1 jogou PAPEL📃 e a CPU jogou TESOURA✂️')
    print(' \033[34mCPU \033[1;31mWINS!\033[m')

elif CPU == papel and player1 == pedra:
    print('Player 1 jogou PEDRA🪨 e a CPU jogou PAPEL📃')
    print(' \033[34mCPU \033[1;31mWINS!\033[m')

elif player1 == CPU:
    print('UAU! os dois jogaram a mesma coisa!')
    print(' \033[34mO jogo \033[1;33mEMPATOU!\033[m')

else:
    print(f'\033[4;31mNão é possivel jogar com o número {player1}\033[m')

print('='*35)