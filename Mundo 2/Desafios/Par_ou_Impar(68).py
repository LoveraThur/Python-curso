#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitorias consecutivas no final do jogo
from random import randint

win = 0

while True:
    CPU = randint(1,11)
    player = 11
    while player < 0 or player > 10:
        player = int(input('Digite um número[0 a 10]: '))

    PI = ' '
    while PI not in 'PI':
        PI= str(input('Par ou Impar [P/I]? ')).upper()
    
    s = CPU + player

    print('-'*30)
    if s % 2 == 0 and PI == 'P':
        print(f'Você jogou {player} e a CPU {CPU}. Total deu {s}, DEU PAR\nVocê ganhou!')
        win += 1

    elif s % 2 == 1 and PI == 'I':
        print(f'Você jogou {player} e a CPU {CPU}. O Total deu {s}, DEU IMPAR\nVocê ganhou!')
        win+=1

    elif s % 2 == 0 and PI == 'I':
        print(f'A CPU jogou {CPU} e você jogou {player}. O total deu {s}, Deu PAR\nVocê perdeu')
        break

    elif s % 2 == 1 and PI == 'P':
        print(f'A CPU jogou {CPU} e você jogou {player}. O total deu {s}, Deu IMPAR\nVocê perdeu')
        break

    print('-'*30)
    
print('-'*30)
print(f'Você ganhou {win} Rodadas')
print('-'*30)


