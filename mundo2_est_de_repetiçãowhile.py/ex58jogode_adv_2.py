# ex 58 mundo 2

import random
escolhas = 0
jogadas = []
num = (random.randint(1 , 5))
while num != jogadas:
    jogadas = int(input('Qual o numero entre 1 a 5 que o computador escolheu? r: '))
    if jogadas == num:
        print('Parabéns você acertou!!!!! o numero que o sistema escolheu é {}'.format(num))
    elif jogadas > 5:
        print('opção invalida, tente novamente')
    else:
        escolhas += 1
    print('Você errou {} vezes'.format(escolhas))
