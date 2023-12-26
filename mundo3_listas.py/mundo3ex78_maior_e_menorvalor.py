valores = []
mini = 0
maxi = 0
for cont in range (1,6):
    valores.append(int(input(f'Digite o {cont}ª valor: ')))
print('=-'*30)
print('Você digitou os valores: ')
for v, w in enumerate (valores):
    print(f'...{w}', end = ' ')

print("")
num = 0
maxi = max(valores)
mini = min(valores)

print(f'O maior valor digitado foi {maxi} na posição {valores.index(maxi) + 1}')
print(f'O menor valor digitado foi {mini} na posição {valores.index(mini) + 1}')


############ jeito que o guanabara fez

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite o {c}º valor: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)

print(f'Você digitou os valores: {listanum}')
print(f'O maior numero é {mai} e o menor é o {men} o maior esta nas posições', end= '')
for i, v in enumerate (listanum):
    if v == mai:
        print(f'{i}...')
for i, v in enumerate (listanum):
    if v == men:
        print(f'o menor nas posições {i}...')
print()