try:
    a = int(input('numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as error:
    print(f'Problema encontrado foi {error}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre')