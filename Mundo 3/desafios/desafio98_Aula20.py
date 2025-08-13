#Faça um programa que tenha uma função chamada contador(), que receba trÊs parâmetros: inicio, fim e passo e reralize a contagem. Seu programa tem que realizar três contagens através da função criada. a) de 1 até 10, de 1 em 1. b) de 10 até 0, de 2 em 2. c) uma contagem personalizada

def contador(inicio, fim, pula):
    if inicio > fim:
        for i in range(inicio, fim, pula):
            print(i, end=' ')
    elif fim > inicio:
        for j in range(fim, inicio, pula):
            print(j, end=' ')
contador(1, 10, 1)
contador(10, 0, 2)