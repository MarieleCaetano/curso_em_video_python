from random import randint
from time import sleep
numsorteados = []

def sorteio(* list):
    soma = 0
    print(f'\n Numeros sorteados: {numsorteados}', flush=True)
    sleep(1)
    for c in numsorteados:
        if c % 2 == 0:
            soma += c

    print(f'Dos numeros {numsorteados}, a soma dos pares da {soma}')


#programa principal
for c in range(0,5):
    sort = randint(0,100)
    numsorteados.append(sort)
sorteio(numsorteados)

#jeito que o guanabara fez
def sorteia(lista):
    print('Sorteando 5 valores da lista')
    for cont in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(1)
    print('PRONTO!')


def somapar(lista):
    som = 0 
    for valor in lista:
        if valor % 2 == 0:
            som += valor
    print(f'Somando os valores pares da {lista} temos {som}')


numeros = []
sorteia(numeros)
somapar(numeros)
