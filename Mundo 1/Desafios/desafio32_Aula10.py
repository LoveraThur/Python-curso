#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano= int(input('Digite um Ano: '))

a= ano % 4

if a == 0:
    print(f'O ano {ano} É BISSEXTO!')

else:
    print(f'O ano {ano} NÃO É BISSEXTO!')