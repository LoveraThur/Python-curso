#Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitção de um número de tipo inválido. Aproveite e crie também a função leiaFloat() com a mesma funcionalidade

def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
            
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não informar o número\033[m')
            return 0
        else:    
            return n

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido\033[m')
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não informar o número\033[m')
            return 0
        else:    
            return n
n = LeiaInt('Digite um número inteiro: ')
f = LeiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n}')
print(f'Você acabou de digitar o número real {f:.2f}')