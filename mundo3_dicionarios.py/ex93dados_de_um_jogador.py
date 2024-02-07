dados_do_jogador = {}
partidas = 0
gols = []

dados_do_jogador['nome'] = str(input('Nome: '))
dados_do_jogador[f'quantidade de partidas do {dados_do_jogador["nome"]}'] = int(input('Quantas partidas? [0 para encerrar] '))
partidas += dados_do_jogador['quantidade de partidas']

if dados_do_jogador['quantidade de partidas'] > 0:
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantidade de gols na partida {c}: ')))
        dados_do_jogador['gols'] = gols
    print(dados_do_jogador)
    print('-'* 30)
    for n, k in dados_do_jogador.items():
        print(f'{n} tem o valor {k}')
    print('-'*30)
    for c, i in enumerate(gols):
        print(f'>>>>>> Na partida {c + 1} o jogador fez {i}<<<<<<<,')