def metade(valor, formatado= False):
    dividido = valor / 2
    if formatado == True:
        dividido= moeda(dividido)
        return dividido
    else:
        return dividido

def dobro(valor, formatado= False):
    duplicado = valor * 2
    if formatado == True:
        duplicado = moeda(duplicado)
        return duplicado
    else:
        return duplicado

def aumentar(valor, taxa, formatado= False):
    aumento = valor + (valor * taxa / 100)
    if formatado == True:
        aumento = moeda(aumento)
        return aumento
    else: 
        return aumento

def diminuir(valor, taxa, formatado= False):
    diminuição = valor - (valor * taxa / 100)
    if formatado == True:
        diminuição = moeda(diminuição)
        return diminuição
    else: 
        return diminuição

def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.',',')

def resumo(valor=0, aumento=10, diminuição=5):
    print('-'*33)
    print('RESUMO DO VALOR'.center(33))
    print('-'*33)
    print(f'Preço Analisado: \t{moeda(valor)}')
    print(f'Dobro do Preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{diminuição}% de redução: \t{diminuir(valor, diminuição, True)}')
    print('-'*33)