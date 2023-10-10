#ex 28 - aula 10 mundo 1

import random
num1 = int(input('Qual o numero entre 1 a 5 que o computador escolheu? r: '))
num = (random.randint(1 , 5))
if num1 == num:
    print('Parabéns você acertou!!!!! o num q ele escolheu é {}'.format(num))
else:
    print('Você errou, ta sem sorte o numero certo é {}'.format(num))
