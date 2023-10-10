#ex 32 - mundo 1 - aula 10
#ano = int(input('Digite um ano: '))
#if(ano%4 == 0 and ano%100!=0) or (ano%400 == 0):
#    print('O ano que você digitou é bissexto')
#else:
#    print('O ano que você digitou não é bissexto')

# ex 33 - mundo 1 - aula 10

a= int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior numero dos que você digitou é {}'.format(maior))
print('O menor numero dos que você digitou é o {}'.format(menor))

