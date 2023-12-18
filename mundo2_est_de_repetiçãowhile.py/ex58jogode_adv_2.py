# ex 58 mundo 2

#import random
#escolhas = 0
#jogadas = []
#num = (random.randint(1 , 10))
#while num != jogadas:
#    jogadas = int(input('Olá. Sou seu computador! Qual o numero entre 1 a 10 que eu escolhi r: '))
#    if jogadas == num:
#        print('Parabéns você acertou!!!!! o numero que o sistema escolheu é {}'.format(num))
#    elif jogadas > 5:
#        print('opção invalida, tente novamente')
#    else:
#        escolhas += 1
#    print('E você errou {} vezes'.format(escolhas))


#jeito que o guanabara fez
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print(f'Parabéns, você acertou! Com {palpites} palpites')
