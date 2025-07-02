#Crie um programa que leia o ano de nascimento de sete pessoas e mostre quantas ainda nao atingiram a maioridade e quantas ja são maiores de idade
from datetime import date
data_atual= date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    nasc= int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade= data_atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('='*25)
print(f'Temos {totmaior} pessoas de maior!\nTemos {totmenor} pessoas de menor!')
print('='*25)