num = [2,5,9,3]
print(num)

#alterar um numero de uma posição da lista
num[2]= 8

#inserir
num.append(7)
print(num)

num.insert(1,8)
print(num)

#ordem crescente
num.sort()
print(num)

#ordem decrescente
num.sort(reverse=True)
print(num)

#quantidade de elementos da lista
print(f'essa lista tem {len(num)} elementos')


#deletar numeros
num.pop()
print(num)

del num[2]
print(num)