#Crie um programa que tenha uma tupla com várias palavras (Não usar acentos). depois disso, você deve mostrar para cada palavra quais são suas vogais

words = ('Batata', 'Processador', 'Cubo', 'Pica Pau')

for c in words:
    print(f'\nNa palavra {c} tem as vogais: ', end=' ')
    for vogal in c:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')