#crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, o que sera um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    parametro num: numero a ser calculado
    parametro show: (opcional) mostrar ou não a conta
    return: O valor do fatorial do numero num

    Por: Arthur Albara Lovera
    """
    f = 1
    #fatorial
    for n in range(num, 0, -1):
        f *= n
        if show is True:
            #para mostrar "bonito"
            if n == 1:
                print(f'{n}', end=' = ')
                return f
            print(f'{n}', end=' x ')
    return f

print('-'*30)
#True para mostrar, False ou nada para não mostrar
fat = fatorial(6,)
print(f'{fat}')
print('-'*30)
help(fatorial)