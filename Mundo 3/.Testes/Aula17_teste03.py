
a= [2, 3, 4, 7]
#a lista b está unida à lista a
b = a

b[2]= 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('\n')
a= [2, 3, 4, 7]
#a lista b recebe a lista a mas pode fazer alterações apenas nela sem afetar a lista a
b = a[:]

b[2]= 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')