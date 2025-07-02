#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
nome= str(input('Qual é seu nome? ')).strip()

cortado= nome.split()

print(f'Seu primeiro nome é {cortado [0]}')
print(f'Seu ultimo nome é {cortado [len(cortado)-1]}')