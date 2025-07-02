#Faça um programa que leia o sexo de uma pessoa e só aceite os valores 'M' ou 'F', caso contrario peça novamente
sexo= ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual seu sexo (M/F)? ')).upper().strip()

print(f'você é do sexo {sexo}')