#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e mostre o comprimento da hipotenusa
from math import sqrt
ca = float(input('Qual o valor do Cateto Adjacente de seu triângulo? '))
co = float(input('Qual é o valor do Cateto oposto de seu triângulo? '))

ca2= ca*ca
co2= co*co

#calculo(a²=b²+c²)

h= sqrt(ca2+co2)

print(f'A hipotenusa de seu triângulo retângulo é: {h}')