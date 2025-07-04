#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

lista = []

expressão = str(input('Digite uma expressão(sem números. Use parênteses!): '))

for simbolo in expressão:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida')    

print(lista)