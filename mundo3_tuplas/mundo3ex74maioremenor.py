from random import randint

while True:
    nume1 = randint(0,500)
    num2 = randint(0,500)
    num3 = randint(0,500)
    num4 = randint(0,500)
    num5 = randint(0,500)
    numeros = (nume1, num2, num3, num4, num5)
    print(f'Os numeros sorteados foram : {numeros}')
    if nume1 > num2  and nume1 > num3 and  nume1 > num4 and nume1 > num5:
        print(f'O numero {nume1} é o maior')
    elif num2 > nume1 and num2 > num3 and num2 > num4  and num2 > num5:
        print(f'O numero {num2} é o maior')
    elif num3 > nume1 and num3 > num2 and num3 > num4 and num3 > num5:
        print(f'O numero {num3} é o maior')
    elif num4 > nume1 and num4 > num2 and num4 > num3 and num4 > num5:
        print(f'O numero {num4} é o maior')
    elif num5 > nume1 and num5 > num2 and num5 > num3 and num5 > num4:
        print(f'O numero {num5} é o maior')
        print('-'*60)
    if nume1 < num2  and nume1 < num3 and  nume1 < num4 and nume1 < num5:
        print(f'O numero {nume1} é o menor')
    elif num2 < nume1 and num2 < num3 and num2 < num4  and num2 < num5:
        print(f'O numero {num2} é o menor')
    elif num3 < nume1 and num3 < num2 and num3 < num4 and num3 < num5:
        print(f'O numero {num3} é o menor')
    elif num4 < nume1 and num4 < num2 and num4 < num3 and num4 < num5:
        print(f'O numero {num4} é o menor')
    elif num5 < nume1 and num5 < num2 and num5 < num3 and num5 < num4:
        print(f'O numero {num5} é o menor')
    break

#jeito que o guanabara fez

s  = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end='')
for n in s:
    print(f'{n} ', end='')  
print(f'O maior valor sorteado foi: {max(n)}')  
print(f'O menor valor sorteado foi: {min(n)}')

