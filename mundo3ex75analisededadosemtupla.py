num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
num4 = int(input('Digite o quarto numero: '))
numdigitados = (num1,num2, num3, num4)

print(f'Você digitou os numeros {numdigitados}')

if numdigitados.count(9) == 0:
    print('Você não digitou nenhum numero 9')
else:
    print(f'O numero nove aparece {numdigitados.count(9)} vezes')
if 3 in numdigitados:
    print(f'O numero 3 aparece na posição {numdigitados.index(3) + 1}')
else:
    print('Você não digitou o numero 3')

numeros_pares = ()
for num in numdigitados:
    if num % 2 == 0:
        numeros_pares = numeros_pares + (num,)

print(f"Numero par: {numeros_pares}")

#no caso de numeros pares da pra fazer assim tmb:
print('Os valores pares digitados foram: ', end= ' ')
for n in numdigitados:
    if n % 2 == 0:
        print(n, end=' ')
