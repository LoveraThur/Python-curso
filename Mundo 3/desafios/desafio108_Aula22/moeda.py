def metade(valor):
    dividido = valor / 2
    return dividido

def dobro(valor):
    duplicado = valor * 2
    return duplicado

def aumentar(valor, taxa):
    aumento = valor + (valor * taxa / 100)
    return aumento

def diminuir(valor, taxa):
    diminuição = valor - (valor * taxa / 100)
    return diminuição

def moeda(valor):
    return f'R${valor:.0f},00'