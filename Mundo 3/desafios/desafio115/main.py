#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um aquivo de texto simples. O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar pessoas cadastradas

from libb.interface import *
from libb.arquivo import *
from time import sleep

arquivo = 'pessoas.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)
while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])

    nome = ''
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        while True:
            try:
                while not nome.strip():
                    nome = str(input('Nome: ')).title()
                    if not nome.strip():
                        print('\033[31mDigite um nome válido\033[m')
                    else:
                        continue
            except:
                print('ERRO! Digite um nome válido')
            else:
                break
        idade = LeiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistma. Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')    
    sleep(1)