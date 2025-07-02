#a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
#-Até 9 anos: MIRIM
#-Até 14 anos: INFANTIL
#-Até 19 anos: JUNIOR
#-Até 20 anos: SÊNIOR
#-Acima: MASTER

print('='*60)
print('Você quer entrar para a Confederação Nacional de Natação?')
ano= int(input('\nInsira o ano que nasceu: '))
print('='*60)

idade= 2025 - ano

if idade <= 9:
    print(f'Você tem {idade}\nEntão você pertence a categoria \033[34mMIRIM\033[m')

elif idade > 9 and idade <= 14:
    print(f'Você tem {idade}\nEntão você pertence a categoria \033[34mINFANTIL\033[m')

elif idade > 14 and idade <= 19:
    print(f'Você tem {idade}\nEntão você pertence a categoria \033[34mJUNIOR\033[m')

else:
    print(f'Você tem {idade}\nEntão você pertence a categoria \033[34mSÊNIOR\033[m')

print('='*60)