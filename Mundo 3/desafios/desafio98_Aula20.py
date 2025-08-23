#Faça um programa que tenha uma função chamada contador(), que receba trÊs parâmetros: inicio, fim e passo e reralize a contagem. Seu programa tem que realizar três contagens através da função criada. a) de 1 até 10, de 1 em 1. b) de 10 até 0, de 2 em 2. c) uma contagem personalizada

def contador(inicio, fim, pula):
    if pula == 0:
        pula = 1
    if pula < 0:
        pula *= -1
    print(f'contagem de {inicio} até {fim} de {pula} em {pula}')
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=' ')
            inicio += pula
        print('FIM!')
    else:
        while inicio >= fim:
            print(inicio, end=' ')
            inicio -= pula
        print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
print('='*30)
inicio = int(input('Valor do inicio: '))
fim= int(input('valor do fim: '))
pula = int(input('valor de pular: '))
contador(inicio, fim, pula)