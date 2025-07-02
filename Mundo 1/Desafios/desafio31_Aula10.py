#Desenvolva um programa que pergunte a distancia de uma viagem em KM e calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas

KM= float(input('Digite a distância da viagem: '))

pass_curta= KM * 0.50
pass_longa= KM * 0.45

if KM <= 200:
    print(f'A viagem custará {pass_curta} pois é uma viagem curta!')
    print('Você está pagando R$0,50 por KM rodado!')

else:
    print(f'A viagem custará {pass_longa} pois é uma viagem longa!')
    print('Você está pagando R$0,45 por KM rodado!')