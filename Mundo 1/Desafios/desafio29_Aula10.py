#Escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada KM acima do limite

vel= float(input('Seu carro atingiu qual velocidade? '))

multa= (vel-80)*7

if vel >= 80.00:
    print('Vish! Parece que o limite de velocidade era 80Km/h')
    print(f'Você terá que pagar uma multa de R${multa}')

else:
    print('Ufa! O limite era 80Km/h, você se safou')
