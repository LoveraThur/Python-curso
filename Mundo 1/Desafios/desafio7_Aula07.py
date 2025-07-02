print('Agora irei calcular sua média da escola, garoto!')

n1= float(input('Digite sua primeira nota: '))
n2= float(input('Digite sua segunda nota: '))
n3= float(input('Digite sua terceira nota: '))
n4= float(input('Digite sua quarta nota: '))
n5= float(input('Digite sua quinta nota: '))
n6= float(input('Digite sua sexta e ultima nota: '))
media= (n1 + n2 + n3 + n4 + n5 + n6)/6


print('Nossa, sua média ficou em \033[30m{:.1f}\033[m'.format(media))
