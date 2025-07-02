#Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo os nomes dos alunos e escrevendo o nome do escolhido
from random import choice

aluno1= str(input('QUal o nome do primeiro aluno? '))
aluno2= str(input('Qual o nome do segundo aluno? '))
aluno3 = str(input('Qual o nome do terceiro aluno? '))
aluno4= str(input('Qual o nome do quarto aluno? '))


list= [aluno1, aluno2, aluno3, aluno4]

sorteio= choice(list)

print(f'O aluno sorteado foi: {sorteio}')