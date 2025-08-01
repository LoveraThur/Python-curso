#crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario se por acaso a CTPS(carteira de trabalho) for diferente de 0 o dicionario receberá também o ano de contratação e o salário. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar(35 anos de contribuição).

from datetime import datetime

data_atual = datetime.now().year
dicionario = {}

dicionario['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dicionario['idade'] = data_atual - nascimento
dicionario['ctps'] = int(input('carteira de trabalho(0 não tem): '))
contratado = int(input('Ano de contratação: '))
dicionario['ano contratado'] = contratado
dicionario['salario'] = int(input('Salário: R$ '))
dicionario['aposentadoria'] = -((data_atual - contratado) - 35)+dicionario['idade']

print('-='*25)
for k,v in dicionario.items():
    if k == 'nome':
        print(f'Seu {k} é {v}')
    elif k == 'idade':
        print(f'Você tem {v} anos de {k}')
    elif k == 'ctps':
        print(f'seu {k} é {v}')
    elif k == 'ano contratado':
        print(f'você foi contratado em {v}')
    elif k == 'salario':
        print(f'seu {k} é R$ {v}')
    else:
        print(f'você vai ter sua {k} com {v} anos')