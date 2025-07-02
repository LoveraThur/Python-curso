#faça um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar, desconsidere-o

soma= 0

for n in range(1, 7):
    num= int(input(f'Digite o {n}º numero: '))
    if num % 2 == 0:
        soma += num
print(soma)
   