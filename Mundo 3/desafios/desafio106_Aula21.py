#Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer quando o usuário digitar a palavra 'FIM, o programa se encerrará. Utilize cores

def pyHELP(ajuda):
    titulo(f'\033[31mManual do {ajuda}\033[m')
    help(ajuda)
    
def titulo(msg, cor= 0):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'   {msg}')
    print('-'*tam)

#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        pyHELP(comando)
titulo('PyHELP Encerrado!')