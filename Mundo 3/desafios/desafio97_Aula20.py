#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptavel

def escreva(texto):
    tam = len(texto)
    print('-'*tam)
    print(texto)
    print('-'*tam)



escreva('  Atlético de Madrid  ')
escreva('  Barça  ')