from random import randint

numeros_sorteados_de_cada_jogador = {}
maior_numero = 0
menor_numero = 0

numeros_sorteados_de_cada_jogador['jogador 1'] = randint(0, 6)
numeros_sorteados_de_cada_jogador['jogador 2'] = randint(0, 6)
numeros_sorteados_de_cada_jogador['jogador 3'] = randint(0, 6)
numeros_sorteados_de_cada_jogador['jogador 4'] = randint(0, 6)

print("Valores sorteados:")
for k, v in numeros_sorteados_de_cada_jogador.items():
    print(f"O {k} tirou {v}")

o = sorted(numeros_sorteados_de_cada_jogador.values())
listaDeKeysOrdenadas = sorted(o, reverse=True)

print("Ranking dos jogadores:")


for num, keyOrdenada in enumerate(listaDeKeysOrdenadas):
    print(f'em {num + 1} lugar: jogador  =  com valor {keyOrdenada}')


#jeito q o guanabara fez ---------
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1, 6),
         'Jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
print('valores sorteados')
ranking = []
for c, k in jogo.items():
    print(f'{c} tirou o {k}')
sleep(1)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse= True)
print('== ranking dos jogadores ==')
for e, m in enumerate(ranking):
    print(f'    {e+1} lugar: {m[0]} com {m[1]}')
    sleep(1)