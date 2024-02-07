matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0, 3):
    for c in range(0, 3): #esses primeiros fors sáo os de alimentacao são os q eu vou add a matriz
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
print('-='* 30)
for l in range(0, 3):
    for c in range(0, 3): # já esses dois sáo para mostrar a estrutura na tela
        print(f'[{l}{c:ˆ5}]', end='') #:ˆ5 centraliza em 5 espacos os textos
    print() # sem esse print o print da linha acima sairia todo um do lado do outro, com esse fica um embaixo do outro
    

