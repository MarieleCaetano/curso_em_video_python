valores = []
continuar = 'S'
pares = []
impares = []
while continuar == 'S':
    n = int(input('Digite um valor: '))
    valores.append(n)
    while True:
        continuar = str(input('Quer continuar? ')).strip().upper()[0]
        if continuar == 'S':
            break
        elif continuar == 'N':
            break
        elif continuar != 'S' or continuar != 'N':
            print('Comando invalido tente novamente')
for s in valores:
    if s % 2 == 0:
        pares.append(s)
    elif s % 2 != 0:
        impares.append(s)
    
print(f'Você digitou os numeros {valores}')
print('**' * 30)
print(f'Os valores pares são {pares}')
print('**'* 30)
print(f'Os impares são {impares}')
    


    
