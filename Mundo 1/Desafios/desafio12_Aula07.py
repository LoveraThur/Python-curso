#Faça um algoritmo que leia um produto e mostre seu novo preço com 5% de desconto
v= float(input('Digite o valor: '))

p= v*5

tt= p/100

tt2= v-tt

print('O seu produto valerá {}'.format(tt2))