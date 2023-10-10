#Neste programa eu fiz um jogo de pedra papel e tesoura onde o computador joga com o usuario.
#import random
#jogue = input('Escolha entre pedra, papel, tesoura: ')

#opções = 'pedra papel tesoura'
#opções = ['pedra','papel', 'tesoura']

#escolhaDoComputador = opções[random.randint(0, 2)]

#if jogue == escolhaDoComputador:
#    print(f'o computador escolheu {escolhaDoComputador} Deu empate')

#elif escolhaDoComputador == 'pedra' and jogue == 'tesoura':
#    print(f'Você perdeu haha o computador jogou {escolhaDoComputador}')

#elif escolhaDoComputador == 'papel' and jogue == 'tesoura':
#    print(f'Parabens vc ganhou né o computador jogou {escolhaDoComputador}')

#elif escolhaDoComputador == 'tesoura' and jogue == 'papel':
#    print(f'Você perdeu haha o comp escolheu {escolhaDoComputador}')

#elif escolhaDoComputador == 'tesoura' and jogue == 'pedra':
#    print(f'você ganhou, o comp escolheu {escolhaDoComputador}')

#elif escolhaDoComputador == 'pedra' and jogue == 'papel':
#    print(f'Você ganhou, o comp escolheu {escolhaDoComputador}')

#elif escolhaDoComputador == 'papel' and jogue == 'pedra':
#    print(f'Voce perdeu, o comp escolheu {escolhaDoComputador}')


# Da pra fazer assim tmb (Jeito que o guanabara fez)
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print(""""" Suas opções:
[0] pedra
[1] papel
[2] tesoura""")
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOOO!!!!!')
sleep(1)
print('computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('jogada invalida!')

elif computador == 1: #Papel
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada invalida')

elif computador == 2: #Tesoura
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida')



