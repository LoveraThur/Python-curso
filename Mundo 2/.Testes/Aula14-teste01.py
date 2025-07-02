'''for c in range(1,5):
     n= int(input('Digite um valor: '))
 print('Fim!')'''

#parar quando a pessoa nao quiser mais

r = 'S'
soma = 0
while r == 'S':
    n= int(input('Digite um valor: '))
    r= str(input('Você quer continuar (S/N)? ')).upper().strip()
    soma += n
print(f'A soma de seus valores é {soma}!\nFIM!')



