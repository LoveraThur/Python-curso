#Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuario. O programa será interrompido quando o valor solicitado for negativo

n = 0

tabuada= 'TABUADA'
print(' ')
print('\033[1;31m-\033[m'*45)
print(f'\033[1;31m{tabuada:^45}\033[m')
print('\033[1;31m-\033[m'*45)

while True:
    n = int(input('Você deseja ver a tabuada de qual número? '))
    if n >= 0:
        print('-'*45)
        for i in range(0,11):
            print(f'{n} x {i} = {n*i}')
        print('-'*45)
    if n < 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre')
print('-'*45)