from libb.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um Erro na criação do arquivo!')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso\033[m')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
        
def cadastrar(arq, nome, idade =0):
    if nome == ' ':
        nome = 'desconhecido'
    try:
        a = open(arq, 'at')
    except:
        print('Houve umm ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} Adicionado')
            a.close()