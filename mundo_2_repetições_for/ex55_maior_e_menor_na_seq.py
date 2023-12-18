#programa que leia o peso  de cinco pessoas
lista_de_peso_das_pessoas= []

for c in range(1,6):
    peso = float(input(f'Digite o peso {c}: '))
    lista_de_peso_das_pessoas.append(peso)
valor_max = max(lista_de_peso_das_pessoas)
valor_min = min(lista_de_peso_das_pessoas)
print(f'O menor peso na lista é: {valor_min}')
print(f'O maior peso na lista é:{valor_max}')

   
#jeito que o guanabara fez
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
