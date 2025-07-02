#Crie u programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se p usuário quer ou não continuar. No final, mostre:
#Quantas pessoas tem mais de 18 anos
#Quantos homens foram cadastrados
#Quantas mulheres tem MENOS de 20 anos
cadastro = 'CADASTRO CONCLUIDO'
iddtt = homens= mulheres = 0

while True:
    print('-'*35)
    print('    \033[32m    Cadastre uma pessoa\033[m')
    print('-'*35)
    idd= int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo= str(input('Qual seu sexo [M/F]? ')).upper().strip()
        
    if idd >= 18:
        iddtt += 1
        
    if sexo == 'M':
        homens += 1
        
    elif sexo == 'F' and idd < 20:
        mulheres += 1
    continuar = ' '

    print('-'*35)
    while continuar not in 'SN':
        continuar= str(input('Você deseja continuar [S/N]? ')).upper().strip()

    if continuar == 'N':
        break
    


    
print('')
print('')
print('-'*35)
print(f'{cadastro:^35}')
print('-'*35)

print(f'Pessoas maiores de 18: {iddtt}\nHomens cadastrados: {homens}\nMulheres com menos de 20 anos: {mulheres}')
print('-'*35)
