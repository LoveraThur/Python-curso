#faça um programa que leia um numero e diga se ele é ou não primo
n= int(input('Digite um número: '))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f'{n} não é primo')
            break
    else:
        print(f'{n} é primo')
elif n == 0:
    print(f'{n} é zero')
elif n == 1:
    print(f'{n} é um')
else:
    print(f'{n} é negativo')


