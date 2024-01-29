from time import sleep

def maior(* núm):
    cont = maior = 0
    print(f'\n Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', flush=True, end='')
        sleep(1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\n foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')

#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()