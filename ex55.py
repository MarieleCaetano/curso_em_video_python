#programa que leia o peso  de cinco pessoas
lista_de_peso_das_pessoas= []

for c in range(1,6):
    peso = float(input(f'Digite o peso {c}: '))
    lista_de_peso_das_pessoas.append(peso)
    valor_max = max(lista_de_peso_das_pessoas)
    valor_min = min(lista_de_peso_das_pessoas)
print(f'O menor peso na lista é: {valor_min}')
print(f'O maior peso na lista é:{valor_max}')

   
