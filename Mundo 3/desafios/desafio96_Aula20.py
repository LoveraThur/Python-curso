#faça um programa que tenha uma função chamada área(), que recema as dimenções de um tereno retangular(largura e comprimento) e mostre a área do terreno


print('\nControle de Terrenos')
print('-'*27)
def área(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area:.2f}')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

área( largura, comprimento)