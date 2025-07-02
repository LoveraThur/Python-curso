#refaça o desafio 09, mostrando a tabuada de um numero que o usuario escolher usando o laço for

n= int(input('Digite o numero que deseja: '))
print('='*20)
print(f'A tabuada de {n} é:')
print('='*20)
for c in range(1, 11):
    print(f'{n}x{c}=',n*c)
print('='*20)