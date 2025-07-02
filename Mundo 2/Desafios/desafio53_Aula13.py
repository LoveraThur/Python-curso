#crie um programa que leia uma frase e diga se ela é um palindromo

frase= str(input('Digite uma frase: ')).strip().upper()
palavra= frase.split()
junto= ''.join(palavra)
inverso= ''

for letra in range(len(junto) -1, -1, -1 ):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'Temos um Palíndromo')
else:
    print(f'Não temos um palíndromo')