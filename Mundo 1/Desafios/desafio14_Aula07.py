#Escreva um programa que converte uma temperatura de ºC em ºF

temperatura = float(input('Digite a temperatura em ºC: '))


conversor = ((9*temperatura)/5) + 32

print(f'A temperatura {temperatura}ºC corresponde a {conversor}ºF')