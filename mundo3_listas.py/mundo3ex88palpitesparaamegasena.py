print('=-'*30)
print('JOGO NA MEGA SENA')
print('=-'*30)
import random
num = int(input('Quantos jogos você quer? '))
for i in range(0, num):
    print(f'Bet number {i+1}:', end=" ")
    bet = random.sample(range(1, 61), 6)
    print(sorted(bet))
