#Escreva um programa que faça o computador pensar em um numero interio entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador. O commputador devera escrever na tela se o usuario venceu ou perdeu
from random import randint

numero= randint(1,5)

tentativa= int(input('\nPensei em um número de 1 a 5, tente adivinhar: '))

if tentativa == numero:
    print('\nUau, você é muito bom nisso! você acertou o numero!\n')

else:
    print(f'Você é fraco! Eu pensei no numero {numero}\n')