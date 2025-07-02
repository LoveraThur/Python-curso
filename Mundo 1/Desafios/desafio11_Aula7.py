#faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, considerando que cada lata de tinta pinta 2m²
l= float(input('Largura da parede: '))
a= float(input('Altura da parede: '))

a2= l*a

lt= 2

tt= a2 / lt
print('Sua parede tem {} metros quadrados!'.format(a2))
print('Você precisará de {} latas de tinta para pintar a sua parede!'.format(tt))