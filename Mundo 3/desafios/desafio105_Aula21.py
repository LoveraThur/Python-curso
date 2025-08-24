#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas. A maior nota. A menor nota. A média da turma. A situação(opcional). Adicione também as docstrings da função.
def notas(*nota, sit=False ):
    """
    -> função que calcula notas de um aluno
    parametro nota: mostra a nota do aluno
    parametro sit:(opcional) mostra a situação do aluno[BOA, RUIM, RAZOÁVEL]
    return: dicionário com informações sobre a situação da turma
    """
    qtd = len(nota)
    soma = sum(nota)
    maior = max(nota)
    menor = min(nota)
    media = soma / qtd
    dicionario = {'total': qtd,
                  'maior': maior,
                  'menor': menor,
                  'media': media}
    if sit == True:
        if media < 6:
            dicionario.update({'situação': 'RUIM'})
        elif media >= 6 and media < 7:
            dicionario.update({'situação': 'RAZOÁVEL'})
        else:
            dicionario.update({'situação': 'BOA!'})
    return dicionario
resposta = notas(5,10,0,5,6,5,7,1, sit=True)
print(resposta)