#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. no final mostre: a)Quantas pessoas foram cadastradas. b)Listagem com as pessoas mais pesadas. c) listagem com as pessoas mais leves

lista = []
lista_temp = []
pesado = leve = 0
while True:
    lista_temp.append(str(input('Nome: ')))
    lista_temp.append(int(input('Peso: ')))
    if len(lista) == 0:
        pesado = leve = lista_temp[1] 
    else:
        if lista_temp[1] > pesado:
            pesado = lista_temp[1]
        if lista_temp[1] < leve:
            leve = lista_temp[1]
    lista.append(lista_temp[:])
    lista_temp.clear()
    continuar = ' '
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]:  ')).upper()    
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(lista)} pessoas')
print(f'o maior peso é {pesado}.',end=' ')
for p in lista:
    if p[1] == pesado:
        print(f'A pessoa é: {p[0]}')
print(f'O menor peso é {leve}.',end=' ')
for l in lista:
    if l[1] == leve:
        print(f'A pessoa é: {l[0]}')