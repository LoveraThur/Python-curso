#Faça um programa que calcule a soma entre todos numeros impares que são multiplos de 3 e se encontram no intervalo de 1 até 50

soma= 0
cont= 0

for i in range(1, 500, 2):
    if i % 3 ==0:
        cont= cont + 1
        soma= soma + i
print(f'A soma dos primeiros {cont} numeros impares divisiveis por três {soma}')
