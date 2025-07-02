#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a nome "SANTO"

cidade= str(input('Digite o nome de uma cidade: '))

nome= cidade.split()

achar= 'Santo' in nome[0]

print(achar)