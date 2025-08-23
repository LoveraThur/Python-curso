#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

def voto(nascimento):
    from datetime import date
    data_atual = date.today()
    idade = data_atual.year - nascimento

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    
    elif idade >= 18 and idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'

nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))