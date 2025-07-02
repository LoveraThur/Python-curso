#Escreva um programa que calcule a quantidade de KM percoridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa  R$60,00 por dia e R$0,15 por KM rodado.
KM= float(input('Quantos KM o carro rodou? '))
Dias= float(input('Você utilizou o carro por quantos dias? '))

ValorKM = KM * 0.15
ValorDias = Dias * 60.00

TT = ValorKM + ValorDias

print(f'você terá que pagar R${TT} por ter usado o carro por {Dias}Dias e ter percorrido {KM}KM')