#crie um programa que leia um numero e mostre se ele é par ou impar

n= int(input('Digite um número: '))

#resto da divisão do numero por 2 for = 0 ele é par, caso contrário é impar

resultado= n % 2

if resultado == 0:
    print(f'o numero {n} é par!')

else:
    print(f'O número {n} é impar!')
