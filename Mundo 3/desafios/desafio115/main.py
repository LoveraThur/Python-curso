#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um aquivo de texto simples. O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar pessoas cadastradas

from libb.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])

    if resposta == 1:
        print('opção 1')
    elif resposta == 2:
        cadastrar()
    elif resposta == 3:
        cabecalho('Saindo do sistma. Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')    
    sleep(1)