#Faça um programa que leia 5 valores numericos e guarde em uma lista. no final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista = []

for v in range(1,6):
    lista.append(int(input(f'Digite um valor para a posição {v}: ')))
    
maior = max(lista)
menor = min(lista)

print('=-'*30)
print(f'A lista é: {lista}')

print(f'O maior valor da listá é {maior}, nas posições ', end=' ')
for i, c in enumerate(lista):
    if c == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor da listá é {menor}, nas posições ', end=' ')
for k, j in enumerate(lista):
    if j == menor:
        print(f'{k}...', end=' ')