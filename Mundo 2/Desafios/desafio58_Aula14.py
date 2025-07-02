#melhore o jogo do desafio 28 onde o computador vai pensar em um numero de 0 a 10, só que agora o jogador vai tentar até acertar, mostrando o total de palpites no final
from random import randint


numero = randint(0,11)
palpite = 0
tentativas = 0

while palpite != numero:
    palpite = int(input('Qual seu palpite? '))
    tentativas += 1

print(f'Você acertou em {tentativas} tentativas! o numero era {palpite}')