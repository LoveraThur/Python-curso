#crie um programa que tenha uma tupla totalmente preenchida com contagem por extenso, de zero até vinte. seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

print('-='*20)
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'\nO número que você digitou foi: \033[32m{numeros[numero]}\033[m')
        break

    print('-='*20)
    print('DIGITE UM NÚMERO VÁLIDO!')
    print('-='*20)
print('-='*20)
