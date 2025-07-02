#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo
from math import cos, sin, tan, radians

angulo = float(input('Digite o valor do seu ângulo: '))

radiano= radians(angulo)
tg= tan(radiano)
cos= cos(radiano)
sen= sin(radiano)

print(f'O seu ângulo {angulo}º tem como seno {sen:.2}, cosseno {cos:.2} e tangente {tg:.2}')