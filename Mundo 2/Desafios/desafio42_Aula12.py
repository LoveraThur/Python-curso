#refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar qual triangulo será formado
#-Equilátero: todos lados iguais
#-Isósceles: dois lados iguais
#-Escaleno: Todos lados diferentes

print('='*25)
print('Analisador de Triângulos')
print('='*25)

r1= float(input('Primeiro Segmento: '))

r2= float(input('Segundo Segmento: '))

r3= float(input('Terceiro Segmento: '))

print('='*40)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos PODEM formar um Triângulo!')

if r1 == r2 == r3:
    print('Este é um \033[32mTriângulo Equilátero\033[m!')

elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Este é um \033[32mTriângulo Isósceles\033[m!')

elif r1 != r2 or r1 != r3 or r2 != r3:
    print('Este é um \033[32mTriângulo Escaleno\033[m!')

else:
    print('Os segmentos NÃO PODEM formar um Triângulo!')

print('='*40)