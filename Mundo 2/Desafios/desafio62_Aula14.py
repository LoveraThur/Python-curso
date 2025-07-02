#melhore o exercicio 61, perguntando ao usuario se ele quer mais alguns termos. O programa se encerra quando ele digitar 0

print('-'*26)
print('GERADOR DE PA')
print('=-'*26)
a1= int(input('Digite o Primeiro termo de sua PA: '))
r= int(input('Digite a razão de sua PA: '))
c = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while c < total:
        print(f'{a1} -> ', end='')
        a1 += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos você quer mostrar a mais: '))
print('=-'*26)
print(f'A progressão foi finalizada com {total} termos mostrados\nO ultimo termo sendo {a1-r}')
print('=-'*26)

