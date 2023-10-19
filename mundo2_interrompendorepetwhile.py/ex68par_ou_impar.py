import random
from time import sleep
totaldejogadas = 0
print('=' * 30)
print ('Vamos jogar impar ou par')
print('=' * 30)
while True:
    escolhaDoComputador = random.randint(0, 30)
    valor = int(input('Digite o valor: '))
    par_ou_impar = str(input('Par ou impar [P\I]: ')).upper().strip()[0]
    totaldasoma = escolhaDoComputador + valor
    if totaldasoma % 2 == 0 and par_ou_impar == 'P':
            totaldejogadas  += 1
            print('E o resultado foi...')
            sleep(2)
            print(f'''         PARABÉNS! Você ganhou! sua jogada foi {valor} 
                  e a do computador foi {escolhaDoComputador} 
                  totalizando {totaldasoma} que é par''')
    elif totaldasoma % 2 != 0 and par_ou_impar == 'I':
            totaldejogadas  += 1
            print('E o resultado foi...')
            sleep(2)
            print(f'''         PARABÉNS! Você ganhou! sua jogada foi {valor} 
                  e a do computador foi {escolhaDoComputador} 
                  totalizando {totaldasoma} que é impar''')
    else:
           break
print('~' * 30)
print(f'GAME OVER, Você perdeu. Total de vezes ganha {totaldejogadas}')
print ('~' *30)
    