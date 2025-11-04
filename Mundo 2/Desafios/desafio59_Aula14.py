#crie um programa que leia 2 valores e mostre na tela um menu: 1- soma, 2- multiplicação, 3-maior, 4- novos numeros, 5- sai

menu = 0

while menu != 5:
    print('='*30)
    n1= int(input('Primeiro Valor: '))
    n2= int(input('Segundo Valor: '))
    print('='*30)
    print('Soma[1]\nMultiplicação[2]\nMaior[3]\nNovos números[4]\nSair[5]')
    menu = int(input('Qual você deseja: '))
    print('='*30)

    if menu == 1:
        print(f'A soma de {n1} e {n2} é igual a {n1+n2}\n\033[1;32m{n1}+{n2}= {n1+n2}\033[m')
    elif menu == 2:
        print(f'{n1} vezes {n2} é igual a {n1*n2}\n\033[1;31m{n1}x{n2}= {n1*n2}\033[m')
    elif menu == 3:
        if n1 > n2:
            print(f'O número maior é o \033[34;1m{n1}\033[m')
        elif n2 > n1:
            print(f'O número maior é o \033[34;1m{n2}\033[m')
        else:
            print('Os dois números são \033[34;1miguais\033[m')
    elif menu == 4:
        print('Ok, escolha os novos números!')
    else:
        print('Não existe este numero no menu!')


