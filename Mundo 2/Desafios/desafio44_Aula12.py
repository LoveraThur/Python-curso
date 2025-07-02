#elabore um programa que calcule o valor a ser pago por um produto. Considerando seu preço normal e condição de pagamento:
#-à vista dinheiro/cheque: 10% de desconto
#-Á vista no cartão: 5% de desconto
#-Em até 2x no cartão: Preço normal
#-3x ou mais no cartão: 20% de juros
print('=-'*35)

valor= float(input('Valor do produto: R$'))

print('=-'*35)
print('Escolha uma das opções')
print('|1- À vista dinheiro ou cheque >>> 10% desconto   |')
print('|2- À vista no cartão          >>> 5% desconto    |')
print('|3- 2x no Cartão               >>> Preço normal   |')
print('|4- 3x ou mais no cartão       >>> 20% de Juros   |')
print('=-'*35)

opcao= int(input('Qual opção deseja: '))

if opcao == 1:
    tt= valor - (valor*(10/100))
    a= int(input('|1- Dinheiro| 2- Cheque|\n Escolha uma opção: '))
    if a == 1:
        print(f'Você escolheu pagar no Dinheiro, então ficará \033[32mR${tt}\033[m!')
    elif a ==2:
        print(f'Você escolheu pagar em Cheque, então ficará \033[32mR${tt}\033[m!')
    else:
        print('É possivel escolher apenas entre Dinheiro e Cheque!')
    
elif opcao == 2:
    tt= valor - (valor*(5/100))
    print(f'Pagando no cartão vai ficar \033[32mR${tt}\033[m!')

elif opcao == 3:
    tt= valor / 2
    print(f'Você escolheu pagar em 2 vezes no cartão, então você terá que pagar DUAS parcelas de \033[32mR${tt}\033[m!')

elif opcao == 4:
    a= int(input('Em quantas vezes você deseja fazer? '))
    tt= valor / a
    print(f'Você escolheu pagar em \033[34m{a}\033[m parcelas, então ficará \033[32mR${tt}\033[m cada parcela!')

else:
    print('Esta opção não existe!')

print('=-'*35)

