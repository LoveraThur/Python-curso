#faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#-se ele ainda vai se alistar ao serviço militar
#- se é a hora de se alistar
#-se ja passou do tempo do alistamento
#deve mostrar tambem o tempo que falta ou que passou do prazo

ano= int(input('Você nasceu em qual ano? '))

idade= 2025 - ano

falta= 18 - idade

passou= idade - 18

if idade < 18:
    print(f'Você terá que se alistar para o exercito!\nMas não se preocupe, é apenas daqui {falta} anos')

elif idade == 18:
    print('É hora de se alistar!')

else:
    print(f'Você deveria ter se alistado a {passou} anos atrás!')

