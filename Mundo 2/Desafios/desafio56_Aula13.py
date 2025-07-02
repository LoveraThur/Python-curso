#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre: Média de idade do grupo. Nome do homem mais velho. Quantas mulheres tem menos de 20 anos

mediaidd = 0
homemvelho = ''
iddhomemvelho = 0
mulheres20 = 0

for i in range(1,5):
  nome= str(input(f'Nome pessoa {i}: ')).strip()
  idade= int(input(f'Idade pessoa {i}: '))
  sexo= str(input(f'Sexo (M/F) pessoa {i}: ')).strip() .lower()

  mediaidd += idade

  if sexo == 'm' and idade >= iddhomemvelho:
    homemvelho = nome
    iddhomemvelho = idade

  elif sexo == 'f' and idade <= 20:
    mulheres20 += 1


mediaidd = mediaidd / 4
print('='*35)

print(f'A média de idade das 4 pessoas é {mediaidd}.')
print(f'O homem mais velho é {homemvelho} com a idade de {iddhomemvelho}.')
print(f'A quantidade de mulheres com menos de 20 anos é {mulheres20}.')        

print('='*35)
  