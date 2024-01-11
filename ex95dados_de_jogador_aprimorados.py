#melhoramento do ex 93
from time import sleep
lista_dos_jogadores = []
dicionario_de_valores = {}
numeração = 0
while True:
    dados_do_jogador = {}
    dados_do_jogador['nome'] = str(input('Nome: '))
    numeração += 1
    dados_do_jogador['Numero'] = numeração
    while True:
        partidas = 0
        gols = []
        dados_do_jogador['quantidade de partidas'] = int(input('Quantas partidas? [999 para encerrar] '))
        if dados_do_jogador['quantidade de partidas'] >= 0:
            partidas += dados_do_jogador['quantidade de partidas']
            for c in range(1, partidas + 1):
                gols.append(int(input(f'Quantidade de gols na partida {c}: ')))
                dados_do_jogador['gols'] = gols
            break
        print('Digite um numero inteiro')  
    lista_dos_jogadores.append(dados_do_jogador.copy())
    dicionario_de_valores[''] = lista_dos_jogadores
    while True:
        continuar = str(input('Quer continuar? [S/N]'))
        if continuar in 'Nn' or continuar in 'Ss':
            break
        print('Digite S ou N')
    if continuar in 'nN':
        break

print(lista_dos_jogadores)
print('-'* 30)
print('cod nome', ' '*10, 'gols', ' '*10, 'Total')
print('--'*40)
for m in lista_dos_jogadores:
    print(f' {m["Numero"]}   {m["nome"]}         {m["gols"]}          {sum(m["gols"])}')
print('--'*40) 
ver_informação_especifica = 0
while True:
    ver_informação_especifica = int(input('Mostrar dados de qual jogador? OU Digite [999] para sair: '))
    if ver_informação_especifica == 999:
        break
    elif ver_informação_especifica >= len(lista_dos_jogadores):
        print('Erro, não existe jogador com esse cod')
    else:
        print(f' LEVANTAMENTO DO JOGADOR {lista_dos_jogadores [ver_informação_especifica - 1]["nome"]}')
        for i, g in enumerate(lista_dos_jogadores[ver_informação_especifica - 1]['gols']):
            print(f' No jogo {i + 1} o jogador fez {g}')
    print('-'*40)
print('VOLTE SEMPRE <3')