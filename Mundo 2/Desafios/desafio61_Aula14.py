#refaça o exercicio nunmero 51; lendo o primeiro termo de uma pa e a razao, mostrando os 10 primeiros termos. usando while

a1= int(input('Digite o Primeiro termo de sua PA: '))
r= int(input('Digite a razão de sua PA: '))
c = 1

while c < 10:
    a1 += r
    c += 1
print(f'O 10º termo de sua PA de razão {r} é {a1}')
    