#Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No final, mostre na tela, com a formatação correta

matriz = [[0,0,0], [0,0,0], [0,0,0]]

print('=-'*25)
print('Criador de Matriz 3x3')
print('=-'*25)
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]= int(input(f'Digite o número da posição a{linha+1}{coluna+1}: '))

print('=-'*25)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end= '')
    print()
