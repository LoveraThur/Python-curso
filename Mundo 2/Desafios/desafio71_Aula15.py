#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será o valor sacado(nº inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
#Obs: considere que o caixa possui cedulas de R$50, R$20, R$ 10 e R$1

print('-'*15, end='')
print('CAIXA ELETRÔNICO', end='')
print('-'*15)

retirar= int(input('Quanto você deseja retirar? R$'))
total = retirar
retirado = 0
cédula= 50
print('-'*46)
while True:
    if total >= cédula:
        total-= cédula
        retirado +=1
    else:
        print(f'Foram retiradas {retirado} cédulas de {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula= 1
        retirado = 0
        if total == 0:
            break
print('-'*46)
print('{:^46}'.format('PROGRAMA FINALIZADO'))
print('-'*46)