#crie um programa onde o usuário possa digitar 5 valore numericos e cadastre-os em uma lista, ja na posição correta de inserção(sem usar o sort()). No final mostre a lista ordenada na tela

lista = []

for v in range(0,5):
    num = int(input('Digite um valor: '))
    if v == 0 or num > lista[-1]:
        lista.append(num)
        print(f'O número {num} foi adicionado ao final da lista!')
    else:
        contador = 0
        while contador < len(lista):
            if num <= lista[contador]:
                lista.insert(contador, num)
                print(f'O número {num} foi adicionado na posição {contador}')
                break
            contador += 1

print(lista)