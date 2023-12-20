numeros_dig= []
pares = []
impares = []

for n in range(0,7):
    numeros_dig.append(int(input(f'Digite o {n} valor: ')))

    if numeros_dig[n] % 2 == 0:
        pares.append(numeros_dig[n])
        p = pares.sort()

    elif numeros_dig[n] % 2 != 0:
        impares.append(numeros_dig[n])
        i = impares.sort

print(f'Os numeros pares são: {pares}')
print(f'E os numeros impares são: {impares}')

# jeito que o guanabara fez

num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 == 0:
        #abaixo estou adicionando os numeros pares na primeira sublista da lista num, que é a primeira
        num[0].append(valor)
    else:
        num[1].append(valor)
num[1].sort()
num[0].sort()
print(f'Os numeros pares foram: {num[0]}')
print(f'Os numeros impares foram: {num[1]}')
      
