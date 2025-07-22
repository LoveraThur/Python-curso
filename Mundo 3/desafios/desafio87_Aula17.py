#Aprimore o desafio 86(matriz), mostrando no final: a) A soma de todos valores pares digitados. b) A soma dos valores da terceira coluna. c) O maior valor da segunda linha

matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = 0
coluna3 = 0
maior_linha_2 = 0
print('=-'*25)
print('Criador de Matriz 3x3')
print('=-'*25)
#criar a matriz
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o número da posição a{linha+1}{coluna+1}: '))
#a) numeros pares
        if matriz[linha][coluna] % 2 == 0:
            par = par + matriz[linha][coluna] 
#b) soma dos valores da 3º coluna *****CONFERIR*****
        if coluna == 2:
            coluna3 = coluna3 + matriz[linha][coluna]
#c) maior da segunda            
        # if linha == 1:
        #     for num in range(matriz[1]):
        #         if num > maior_linha_2:
        #             maior_linha_2 = num
maior_valor = max(matriz[1])
print('=-'*25)
#escrever a matriz de forma correta 
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()

print('=-'*25)
print(f'A soma dos valores pares desta matriz é: {par}')
print(f'A soma dos valores da 3º coluna é: {coluna3}')
print(maior_valor)