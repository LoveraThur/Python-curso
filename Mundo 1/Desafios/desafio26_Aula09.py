#faça um programa que leia a frase e mostre:
# quantas vezes aparece a letra 'A'
#em que posição ela aparece a primeira e ultima vez

frase= str(input('Digite uma Frase: ')).upper().strip()

print(f'A letra A aparece {frase.count('A')} vezes na frase')
print(f'A primeira letra A apareceu na posição {frase.find('A')+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind('A')+1}')