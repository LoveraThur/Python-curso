#faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor

n1= int(input('Digite um número: '))
n2= int(input('Digite outro número: '))
n3= int(input('Digite outro número: '))

menor= n1

if n2<n1 and n2<n3:
    menor= n2
if n3<n1 and n3<n2:
    menor= n3

print(f'O menor valor é {menor}')

maior= n1

if n2>n1 and n2>n3:
    maior= n2
if n3>n1 and n3>n2:
    maior=n3

print(f'O maior valor é {maior}')