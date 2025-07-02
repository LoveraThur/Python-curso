#crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla, depois disso mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla

from random import randint

numeros = tuple(randint(i + 1, 10) for i in range(randint(5,5)))
print(f'os números gerados foram: {numeros}')
print(f'o maior numero da tupla gerada é: {max(numeros)}')
print(f'o menor número da tupla gerada é {min(numeros)}')