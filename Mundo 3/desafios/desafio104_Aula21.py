#crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. ex: n= leiaint('digite um n')

def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return n   
   


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')