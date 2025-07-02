#escreva um programa que pergunte o salario d eum funcionario e calcule o valor de seu aumento
#para salarios superiores a R$1250,00 calcule um aumento de 10%
#para os inferiores ou iguais, o aumento é de 15%

v= float(input('Digite o Salário Atual: '))

s= v*(10/100)
i= v*(15/100)

if v > 1250:
    print(f'O salário passará a ser {s+v}')

else:
    print(f'O salário passará a ser {i+v}')