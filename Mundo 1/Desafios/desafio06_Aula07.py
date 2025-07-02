n= int(input('Digite um número: '))

d= n*2
t= n*3
r= int(n**(1/2))

print('O dobro é: \033[33m{}\033[m \n o triplo é: \033[34m{}\033[m \n e a raiz quadrada é: \033[35m{}\033[m'.format(d, t, r))