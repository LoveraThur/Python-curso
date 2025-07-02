#crie um programa que leia varios numeros inteiros pelo teclado. No final mostre a média entre eles, o maior e o menor dos valores lidos. O programa deve perguntar se o usuario deseja continuar a digitar valores ou nao
print('='*25)
print('Média, maior e menor')
print('='*25)

continuar = 'S'
m = 0
maior = 0
menor = 9999999999999999999999999999999
total = 0
while continuar == 'S':
    n = int(input('Digite um Valor: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    print('~'*25)
    m += 1
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    total += n

media = total / m
print(f'A média é: {media}\nO valor menor é: {menor}\nO valor maior é: {maior}')
print('='*25)
