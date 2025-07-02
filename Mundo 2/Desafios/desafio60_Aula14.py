##faça um programa que leia um numero e faça seu fatorial

print('Irei calcular o fatorial de um número!')
n= int(input('Digite um número: '))

f = n
fac = 1

while f > 0:

    fac *= f
    f -= 1
print(f'o fatorial de {n} é {fac}')