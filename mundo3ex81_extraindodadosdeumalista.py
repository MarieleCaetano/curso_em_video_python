lista_de_numeros = []
lista_de_vezes_digitadas = 0
tem_5_na_lista = False
continuar = 'S'

while continuar == 'S':
    lista_de_numeros.append(int(input('Digite um valor: ')))
    lista_de_vezes_digitadas += 1

    while True:
        continuar = str(input('Quer continuar? ')).strip().upper()[0]
        if continuar == 'S':  
            lista_de_numeros.sort(reverse=True)
            break
        elif continuar == 'N':
            break
        elif continuar != 'S' or continuar != 'N':
            print('Comando invalido, tente novamente')

for i in lista_de_numeros:
    if i == 5:
        tem_5_na_lista = True
        break

print('==' *30)
print(f'Você digitou {lista_de_vezes_digitadas} vezes')
print('=='* 30)
print(f'Você digitou os numeros{lista_de_numeros}')
print('=='*30)

if tem_5_na_lista:
    print('Tem o numero cinco na sua lista')
else:
    print('Não tem numero cinco na sua lista')



##### jeito que o guanabara fez

valores = []
while True:
    valores.append(int(input('Digite o valor: ')))
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp == 'N':
        break
print('='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print('A lista em ordem inversa fica {valores}')
if 5 in valores:
    print('O valor cinco faz parte da lista')
else:
    print('O valor cinco não está na lista')


    
