#para criar lista pode se usar 'valores = []' ou 'valores = list'
valores = []

#valores.append(5)
#valores.append(9)
#valores.append(3)

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c+1} encontrei o valor {v}!')
print('Cheguei ao final da lista')

