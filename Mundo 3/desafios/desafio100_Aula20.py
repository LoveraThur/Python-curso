#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e SomaPar(). A primeira vai sortear 5 numeros e colocá-los dentro da lista e a segunda vai mostrar a soma entre todos os valores pares sorteados na função anterior.

from random import randint
lista = []
def sorteia(a, b):
    for i in range(5):
        num = randint(a, b)
        lista.append(num)

def somaPar(numeros):
    pares = 0
    print(f'presentes na lista há os números:', end=' ')
    for num in numeros:
        print(num, end=' ')
        if num % 2 == 0:
            pares += 1
    print(f'\nDestes {len(numeros)} números há {pares} números pares')
sorteia(0, 100)
somaPar(lista)