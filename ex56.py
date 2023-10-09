#nome, idade e sexo de 4 pessoas
lista_de_nomes = []
lista_de_idade= []
lista_de_sexo = []
for c in range(1,5):
    nome = str(input('Qual seu nome:'))
    idade = int(input('Qual sua idade: '))
    sexo = int(input('Qual seu sexo [1]feminino [2]Masculino: '))
    lista_de_idade.append(idade)
    lista_de_nomes.append(nome)
    lista_de_sexo.append(sexo)
total_soma_de_idade = sum(lista_de_idade)
media = total_soma_de_idade / 2

print(f'A média de idade do grupo é {media}')

idade_do_hm_mais_velho=0
for c in range(0, len(lista_de_sexo)):
    if lista_de_sexo[c] == 2:
        if lista_de_idade[c] > idade_do_hm_mais_velho:
            idade_do_hm_mais_velho= lista_de_idade[c]

print(f'idade do homem mais velho {idade_do_hm_mais_velho}')

idade_maxima = 20
mulheres_com_menos_de_20 = 0
for c in range (0, len(lista_de_sexo)):
    if lista_de_sexo[c] == 1:
        if lista_de_idade[c] < idade_maxima:
            mulheres_com_menos_de_20 = lista_de_sexo[c]

print(f'a quantidade de mulheres com menos de 20 anos é {mulheres_com_menos_de_20}')


            

   