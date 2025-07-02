#desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

a1= int(input('Digite o primeiro termo da sua PA: '))
r= int(input('Digite a razão de sua PA: '))

print('='*30)
print(f'O termo a1 da sua PA é : {a1}')
for c in range(1,10):
    a1 += r
    print(f'O termo a{c+1} da sua PA é: {a1}')
print('='*30)