#Crie um programa que leia um numero real qualquer pelo teclado e mostre sua proporção inteira
from math import trunc

n= float(input('Digite um número real: '))

v= trunc(n)

print(f'A parte inteira de {n} é {v}!')
