#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
s= float(input('Qual é o salário do funcionário? '))

#calculo
p= s*15
tt= p/100

#total
tt2= s+tt

print('Seu funcionário irá receber R${} com o aumento de 15%'.format(tt2))