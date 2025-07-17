# teste = []
# teste.append('Arthur')
# teste.append(18)
# galera = []
# galera.append(teste[:])
# teste[0] = 'Lovera'
# teste[1] = 17
# galera.append(teste[:])
# print(galera)


# galera = [['Arthur', 18], ['Lovera', 17], ['João', 25]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade!')


galera = []
dado = []

for c in range(0,3):
    dado.append(str(input('\nNome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')