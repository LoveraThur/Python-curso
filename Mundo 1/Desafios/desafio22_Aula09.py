#Analisador de Nome completo
#nome com letras maiusculas
#nome com letras minusculas
#Quantas letras tem ao todo, sem considerar espaços
#quantas letras tem o primeiro nome

nome= str(input('Digite seu nome completo: '))

maiuscula= nome.upper()
minuscula= nome.lower()


nome_dividido= nome.split()

nome1= len(nome_dividido[0])
sobrenome= len(nome_dividido[1])
sobrenome2= len(nome_dividido[2])
letrastt= nome1+ sobrenome+ sobrenome2
letrasnome= len(nome_dividido[0])

print(f'Seu nome maiusculo: {maiuscula}\n Seu nome minúscula: {minuscula}\n Seu nome completo tem {letrastt} letras\n Seu primeiro nome tem {letrasnome} letras')