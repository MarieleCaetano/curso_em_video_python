number = int(input('Numero: '))
numero_e_primo = True

for i in range(2, number):
    if  number % i == 0:
        numero_e_primo = False


if numero_e_primo:
    print('seu numero é primo')
else:
    print('seu numero nao é primo')

#jeito que o guanabara fez
num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end= ' ')