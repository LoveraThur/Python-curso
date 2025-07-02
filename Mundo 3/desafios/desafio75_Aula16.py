#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. Nofinal mostre: a) Quantas vezes apareceu o valor 9. b) em que posição foi digitado o primeiro valor 3. c) quais foram os numeros pares

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
v4 = int(input('Digite o ultimo valor: '))

print('=-'*20)
tupla = (v1, v2, v3, v4)
tupla:int
print(f'a tupla ficou: {tupla}')
print('=-'*20)

#a)
if 9 in tupla:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')
else:
    print('Não há o numero 9 na tupla')
print('=-'*20)

#b)
if 3 in tupla:
    print(f'O número 3 foi digitado na posição {tupla.index(3) +1 }')
else:
    print('O número 3 não está presente na tupla')

print('=-'*20)
#c)
pares = 0
for c in tupla:
    if c % 2 == 0:
        pares += 1
print(f'na tupla há {pares} numeros pares')
print('=-'*20)
