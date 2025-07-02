# Escreva um programa que leia um numero n inteiro e mostre na tela os n primeiros elementos de uma sequencia de fibonacci

'''n1= 1
n2= 9
n3= n1+n2 #3 #10
n1= n3+n2 #5 #19
n2= n1+n3 #8 #29'''

print('='*30)
print('SEQUÊNCIA DE FIBONACCI')
print('='*30)
n= int(input('digite uma quantidade de elementos: '))
print('~'*30)
n1 = 0
n2= 1
i= 0
print(f'{n1} -> {n2}', end='')
while i < n:
    n3 = n1+n2
    i+= 1
    print(f' -> {n3}', end='')
    n1 = n2
    n2 = n3

print(' -> FIM')