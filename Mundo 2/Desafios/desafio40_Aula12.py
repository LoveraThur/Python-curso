#crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#-média abaixo de 5: REPROVADO
#-Média entre 5 e 6,9: RECUPERAÇÃO
#-Média 7 ou superior: APROVADO

print('='*30)
nota1= float(input('Digite a Primeira nota: '))
nota2= float(input('Digite a Segunda nota: '))
print('='*30)

media= (nota1 + nota2)/2

if media < 5:
    print('\033[31mREPROVADO!\033[m')

elif media >= 5 and media <= 6.9:
    print('\033[34mRECUPERAÇÃO!\033[m')

else:
    print('\033[32mAPROVADO!\033[m')