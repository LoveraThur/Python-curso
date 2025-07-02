n1= int(input('Insira um valor: '))
n2= int(input('Insira outro valor: '))
s= n1+n2
sub= n1-n2
m= n1*n2
d= n1/n2
di= n1//n2
sd= n1%n2
p= n1**n2
r1= n1**(1/2)
r2= n2**(1/2)

print('A soma vale: {}'.format(s))

print('A subtração vale: {}'.format(sub))

print('A multiplicação vale: {}'.format(m))

print('{} dividido por {} é igual a: {}'.format(n1, n2, d))

print('A divisão inteira é: {}'.format(di))

print('A sobra da divisão é: {}'.format(sd))

print('{} elevado a {} é igual a: {}'.format(n1, n2, p))

print('A raiz quadrada de {} é: {}'.format(n1, r1))

print('Já a raiz quadrada de {} é: {}'.format(n2, r2))