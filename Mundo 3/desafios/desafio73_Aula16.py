#Crie uma tupla preencihida com os 20 primeiros times do Brasileirao, da ordem de colocação. depois mostre: a) os 5 primeiros colocados. b) Os ultimos 4 colocados. c) Uma lista com os times em ordem alfabética. d) em que posição da tabela está o time do vasco.

classificação = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético Mineiro', 'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará', 'Vasco', 'São Paulo', 'Santos', 'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')

#a)
print('-='*20)
print('Os 5 primeiros colocados são: ', end='')
print(classificação[0:6])

#b)
print('-='*20)
print('Os que estão na zona do rebaiamento são:', end='')
print(classificação[16:21])


#c)
print('-='*20)
print('Os times em ordem alfabética:', end='')
print(sorted(classificação))

#D)
print('-='*20)
print('O Vasco está na: ', end='')
vasco = classificação.index('Vasco')
print(vasco + 1,'º Colocação')
print('-='*20)