# crie um programa que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. no final mostre quantos numeros foram digitados e a soma deles, desconsiderando o 999
n = 0
c = 0
a= 0 
print('='*30)
print('SOMA DE NUMEROS USANDO WHILE')

print('~'*25)
print('Digite 999 para parar!')
print('~'*25)
while a != 999:
    a = int(input('Digite um valor: '))
    c += 1
    n += a

print('~'*46)
print(f'você digitou {c-1} valores e a soma deles é: {n - 999}')
print('~'*46)

