#crie um programa que vai ler varios numeros e colocar em uma lista. Depois mostre: a) quantos numeros foram digitados. b) A lista de valores ordenada de forma decrescente. c) se o valor 5 foi digitado ou não na lista

lista = []

while True:
    num = int(input('\ndigite um número: '))
    lista.append(num)
    continuar = 's'
    while continuar != 'S':
        continuar = str(input('quer continuar?[S/N]: ')).upper()
        if continuar == 'N':
            break
    if continuar == 'N':
        break
reverse = sorted(lista, reverse=True)
print(f'\nEssa lista tem {len(lista)} números!')
print(f'A lista em ordem decrescente fica: {reverse}')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')