
#numero = 1
#while numero !=0:
#    numero = int(input('Fatorial de: '))
#    resultado = 1
#    for n in range(1, numero+1):
#        resultado *= n
#        print(resultado)

#print("final do trabalho!!")

#jeito simplificado usando a biblioteca que o guanabara fez
#from math import factorial
#n = int(input('Digite um numero para calcular o seu fatorial:  '))
#f = factorial(n)
#print(f'O fatorial de {n} é {f}')

# modo tradicional
n = int(input('Digite um numero para calcular o seu fatorial:  '))
c = n
f = 1
print(f'Calculando fatorial de {n}! = ', end='')
while c > 0:
    print(f'{c}', end ='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-= 1
print(f'{f}')
