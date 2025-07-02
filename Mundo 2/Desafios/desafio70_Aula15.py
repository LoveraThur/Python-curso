#crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#Total gasto na compra
#quantos produtos custam mais de R$1000
#Qual o nome do produto mais barato

gasto= 0
maior1k= 0
barato = 9999999999999999999999
prodbarato= ' '
caixa= 'CAIXA DE GASTOS'

print('=-'*17)
print(f'{caixa:^34}')

while True:
    print('=-'*17)
    prod= str(input('Digite o nome do produto: ')).capitalize()
    valor= float(input('O valor do produto é R$'))
    print('=-'*17)

    gasto += valor

    if valor > 1000:
        maior1k += 1
    
    if valor < barato:
        barato = valor
        prodbarato = prod

    continuar = ' '
    while continuar not in 'SN':
        continuar= str(input('Você deseja continuar [S/N]? ')).upper()
          
    if continuar == 'N':
        break
    
print('=-'*17)
print(f'O total \033[1;31mgasto\033[m em suas compras foi \033[1;31mR${gasto:.2f}\033[m\nProdutos que custam \033[1;32mmais de R$1000: {maior1k}\033[m\nO Produto mais \033[1;34mbarato\033[m é \033[1;34m{prodbarato}\033[m')
print('=-'*17)