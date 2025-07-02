#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio indo do 10 até o 0 com pausa de 1 segundo entre eles

from time import sleep
from emoji import emojize

print('='*35)
print('Vamos de contagem para o ano novo?')
print('='*35)

for c in range(10, 0,-1):
    sleep(0.5)
    print(c)
    sleep(0.5)

print('IFUUUU. Feliz ano novo!🎆🎆')
print('='*35)
