#faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso

maior = 0
menor = 0

for i in range(1,6):
    peso= float(input(f'Peso da {i}ª pessoa '))

    if peso >= maior:
        maior = peso
    else:
        menor = peso
        
    #segunda opção
    # if i == 1:
    #     maior = peso
    #     menor = peso
    # else:
    #     if peso > maior:
    #         maior = peso
    #     if peso < menor:
    #         menor = peso
print(f'O maior peso é {maior}Kg\nO menor peso é {menor}Kg')
        