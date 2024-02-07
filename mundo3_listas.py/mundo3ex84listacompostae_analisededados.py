grupo = []
continuar = 'S'
while continuar == 'S':
    grupo.append(str(input('Nome: ')))
    grupo.append(int(input('Peso: ')))
    continuar = str(input('Quer continuar? [s/n] ')).upper().split()[0]



print(grupo)
print(f'Você cadastrou {len(grupo) / 2} pessoas')

pesos = []
for c in range(1, len(grupo),2):
    pesos.append(grupo[c])

# pegar o menor valor da lista, ex. 64
menor_peso = min(pesos)
# pega a posição do peso na lista, ex. numa lista [10, 40, 30], ele retornará 0
posicao_do_menor_peso = pesos.index(menor_peso) 

pessoa_mais_leve = grupo[posicao_do_menor_peso * 2]
peso_da_pessoa_mais_leve = grupo[posicao_do_menor_peso * 2 + 1]

print(f'A pessoa mais magra é a {pessoa_mais_leve} e seu peso é {peso_da_pessoa_mais_leve}')

maior_peso = max(pesos)

posicao_do_maior_peso = pesos.index(maior_peso)

pessoa_mais_pesada = grupo[posicao_do_maior_peso * 2]
peso_da_pessoa_mais_pesada = grupo[posicao_do_maior_peso * 2 + 1]

print(f'A pessoa mais gorda é a(o) {pessoa_mais_pesada} e seu peso é {peso_da_pessoa_mais_pesada}')

# jeito que o guanabara fez

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S-N]'))
    if resp in 'Nn':
        break
print(f'Os dados foram{princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai} kg peso de ', end= '')
for a in princ:
    if a[1] == mai:
        print(f'[{a[0]}]',end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end = '')
for a in princ:
    if a[1] == men:
        print(f'[{a[0]}]',end= '')
print()
