#crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. caso o numero ja exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores unicos digitados, em ordem crescente

print('=-'*30)
print('LISTA DE VALORES UNICOS')
print('=-'*30)

lista = []
continuar = 's'
while continuar != 'N':
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Ops, este valor ja está na lista')
        
    else:
        print('Valor adicionado na lista com \033[32msucesso\033[m')
        lista.append(valor)
    continuar = str(input('Você deseja continuar? ')).upper()

    if continuar == 'N':
        break
    while continuar != 'S':
        continuar = str(input('Você deseja continuar? ')).upper()
        
    print('=-'*30)
    
            
print('=-'*30)
valores_unicos = sorted(lista)        
print(f'Os valores unicos digitados foram: {valores_unicos}')