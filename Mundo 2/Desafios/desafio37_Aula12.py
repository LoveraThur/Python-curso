#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão
#1 para binário | 2 para octal| 3 para hexadecimal
print('='*25)

n= int(input('Digite um número: '))

print('='*25)
print('Você quer transformar esse numero em:')
print('|Binário- 1 | Octal-2 | Hexadecimal- 3|')

a= int(input('Digite Aqui: '))

binario= bin(n)

octal= oct(n)

hexadecimal= hex(n)

if a == 1:
    print(f'Você decidiu transformar o numero {n} em \033[1;31mBinário\033[m e ele ficou assim: {binario.lstrip('0b')}')

elif a == 2:
    print(f'Você decidiu transformar o numero {n} em \033[1;32mOctal\033[m e ele ficou assim: {octal.lstrip('0o')}')

elif a == 3:
    print(f'Você decidiu transformar o numero {n} em \033[1;34mHexadecimal\033[m e ele ficou assim: {hexadecimal.lstrip('0x')}')

else:
    print(f'Não há o número {a} nas transformações')
print('='*25)