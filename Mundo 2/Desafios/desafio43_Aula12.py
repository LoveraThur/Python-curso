#desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
#-Abaixo de 18,5: Abaixo do peso
#-Entre 18,5 e 25: Peso ideal
#-25 até 30: Sobrepeso
#-30 até 40: Obesidade
#-Acima de 40: Obesidade mórbida

print('='*25)
peso= float(input('Digite seu peso: '))
altura= float(input('Digite sua altura(em metros): '))
print('='*25)

cm= altura/100
IMC= peso/(cm*cm)

if IMC <= 18.5:
    print(f'Seu IMC é de {IMC}, então você está \033[31mABAIXO DO PESO\033[m!')

elif IMC > 18.5 and IMC <= 25:
    print(f'Seu IMC é de {IMC}, então você está no \033[34mPESO IDEAL\033[m!')

elif IMC > 25 and IMC <= 30:
    print(f'Seu IMC é de {IMC}, então você está com \033[31mSOBREPESO\033[m!')

elif IMC > 30 and IMC <= 40:
    print(f'Seu IMC é de {IMC}, então você está com \033[31mOBESIDADE\033[m!')

else:
    print(f'Seu IMC é de {IMC}, então você está com \033[31mOBESIDADE MÓRBIDA\033[m]')

print('='*30)