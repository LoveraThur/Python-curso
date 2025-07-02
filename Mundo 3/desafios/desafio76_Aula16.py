#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia. No final mostre uma listagem de preços organizando os dados em forma tabular

tupla = ('Mouse', 85, 
        'Gabinete', 380.90, 
        'Monitor', 869,
        'Placa mãe', 850.99,
        'Processador', 999.90)

for item in range(0, len(tupla)):
    if item % 2 == 0:
        print(f'{tupla[item]:.<30}', end='')
    elif item % 2 == 1:
        print(f'R$ {tupla[item]}')