#escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem
#-o primeiro valor é maior
#-o segundo valor é maior
#-não existe valor maior, os dois são iguais

print('='*25)
print('Irei comparar dois números!')
print('='*25)

x= int(input('Digite um número: '))
y= int(input('Digite outro número: '))

print('='*25)

if x > y:
    print(f'O primeiro número é maior! \n{x} é maior que {y}')

elif x < y:
    print(f'O segundo número é maior! \n{y} é maior que {x}')

else:
    print('Não existe valor maior, os dois são iguais!')