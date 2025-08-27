#Faça um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça tambem um programa que importe esse módulo e use algumas dessas funções

import moeda

preço = float(input('Digite o Preço: '))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço, 13)}')