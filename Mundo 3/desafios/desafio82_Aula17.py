#Crie um programa que vai ler varios numeros e colocar em uma lista. depois disso, crie duas listas extra que vao conter apenas os numeros pares e os numeros impares digitados respectivamente. Ao final, mostre o conteudo das 3 listas
 
lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N] ')).upper()
    if continuar == 'N':
        break
lista_par = []
for num in lista:
    if num % 2 == 0:
        lista_par.append(num)
lista_impar = []
for num in lista:
    if num % 2 == 1:
        lista_impar.append(num)
        
print(lista)
print(f'Lista Par: {lista_par}')
print(f'Lista Impar; {lista_impar}')