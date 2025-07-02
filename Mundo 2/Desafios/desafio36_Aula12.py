#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa
#o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print('='*35)
print('Irei aprovar o emprestimo bancario\n para a compra de uma casa')
print('='*35)

casa= float(input('Insira o valor da casa: R$'))
salario= float(input('Insira quanto você recebe de salário: R$'))
anos=float(input('Insira a quantidade de anos que você pretende pagar a casa: R$'))


prest_mensal= casa/(anos*12)
porcentagem_30_salario= (salario*30)/100

if prest_mensal <= porcentagem_30_salario:
    print(f'\033[1;32mEMPRÉSTIMO CONCEDIDO!\033[m')
    print(f'Para pagar uma casa de \033[34mR${casa:.2f}\033[m em \033[34m{anos:.0f}\033[m anos você terá que pagar prestações de \033[34mR${prest_mensal:.2f}\033[m por mês')

else:
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m')
    print(f'Você não pode pagar o empréstimo de \033[34mR${casa:.2f}\033[m da casa em \033[34m{anos} anos\033[m com seu salário de \033[34mR${salario:.2f}\033[m')

print('-='*47)
    