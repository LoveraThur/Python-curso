#crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separado os valores pares e impares. No final mostre os valores pares e impares em forma crescente

numeros= [[], []]
print('=-'*25)
print('Lista Par e lista Ímpar')
print('=-'*25)
for num in range (1,8):
    numero = int(input(f'Digite o {num}º número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print('=-'*25)
print(f'Lista Par: {sorted(numeros[0])}')
print(f'Lista Ímpar: {sorted(numeros[1])}')