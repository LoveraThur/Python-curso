#prgrama que leia o comprimento de 3 retas e diga ao usuario se elas podem ou não formar um triangulo
#r2= em baixo
#r1=esquerda
#r3= direita

print('='*20)
print('Analisador de Triângulos')
print('='*20)

r1= float(input('Primeiro Segmento: '))

r2= float(input('Segundo Segmento: '))

r3= float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos PODEM formar um Triângulo!')

else:
    print('Os segmentos NÃO PODEM formar um Triângulo!')

print('='*20)