#transformar em dolar, considerando R$1,00 = $3,27
d= float(input('Quanto dinheiro você tem na carteira? R$'))
dol= 3.27
t= d*dol
print('Você tem ${:.2f} '.format(t))
