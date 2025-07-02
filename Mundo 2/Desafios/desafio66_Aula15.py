#crie um programa que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuario digital o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles(Desconsiderando o flag(999))

n = s = q = 0

while True:
    n= int(input('Digite um número (digite 999 para parar): '))
    if n == 999:
        break
    s += n
    q += 1
print(f'Você somou {q} números e a soma deles foi de {s}')
