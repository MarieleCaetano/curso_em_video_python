matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = soma_da_coluna = maior_valor = 0
for l in range(0, 3):
    for c in range(0, 3): #esses primeiros fors sáo os de alimentacao são os q eu vou add a matriz
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
print('-='* 30)
for l in range(0, 3):
    for c in range(0, 3):
         # já esses dois sáo para mostrar a estrutura na tela
        print(f'[{l}{c:ˆ5}]', end='') #:ˆ5 centraliza em 5 espacos os textos
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print() # sem esse print o print da linha acima sairia todo um do lado do outro, com esse fica um embaixo do outro
print('-='* 30)
print(f'A soma dos valores pares é {pares}')
for l in range(0,3):
    soma_da_coluna += matriz[l][2]
print(f'A soma da terceira coluna é {soma_da_coluna}')
for c in range(0,3):
    if c == 0:
        maior_valor = matriz[1][c]
    elif matriz[1][c] > maior_valor:
        maior_valor = matriz[1][c]
print(f'O maior valor da coluna é {maior_valor}')