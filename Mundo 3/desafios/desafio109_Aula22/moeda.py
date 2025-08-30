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

def moeda(valor):
    return f'R${valor:.0f},00'