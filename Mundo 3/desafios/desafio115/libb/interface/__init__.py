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

def cadastrar():
    cabecalho('NOVO CADASTRO')
    while True:
        try:    
            nome = str(input('Nome: ')).title()
            if nome.isnumeric():
                print('\033[31mERRO! Digite um nome válido\033[m')
            elif len(nome) >= 8: 
                break
            else:
                print('\033[31mDigite seu nome completo\033[m')
        except:
            print('\n\033[31mERRO! Digite um nome válido\033[m')
    while True:
        try:    
            idade = int(input('idade: '))
        except (KeyboardInterrupt):
            print('\n\033[31mERRO! Não existe esta idade\033[m')
        except:
            print('\033[31mERRO! Não existe esta idade\033[m')
        else:
            print(f'{nome} foi cadastrado(a)')
            break
def risco(tam = 42):
    return '-' * tam

def cadastro():
    risco()
    print('PESSOAS CADASTRADAS'.center(42))
    risco()

def cabecalho(txt):
    print(risco())
    print(txt.center(42))
    print(risco())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c+= 1
    print(risco())
    opc = LeiaInt('\033[33mSua Opção: \033[m')
    return opc
