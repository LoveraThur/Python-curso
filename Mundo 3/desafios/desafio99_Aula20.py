#faça um programa que tenha uma função chamada maior()que receba varios parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(numeros):
    print('analisando valores passados...')
    sleep(1)
    print(f'Foram informados {len(numeros)} números. Os números informados foram: ', end=' ')
    for num in numeros:
        print(num, end=' ')
    print()
    maior = max(numeros)
    print(f'O maior número informado é: {maior}')
maior([1, 6, 8, 20, 5, 60 ])