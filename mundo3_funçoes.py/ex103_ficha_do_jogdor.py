def jogador(a, b):
    if a == '' or a == int:
        a = 'Desconhecido'
        print(f'O jogador {a}', end='')
    else: 
        print(f'O jogador {a}', end='')
    if b.isnumeric():
        b = int(b)
        print(f' fez {b} gols', end= '')
    else:
        b = 0
        print(f' fez {b} gols', end= '')
    




#programa principal
nome = str(input('Qual o nome do jogador? ' ))
gols = str(input('Quantos gols? ' ))
jogador(a=nome, b=gols)
