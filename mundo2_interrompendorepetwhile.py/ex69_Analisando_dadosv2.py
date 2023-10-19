#nome, idade e sexo de varias pessoas
lista_de_nomes = []
lista_de_idade= []
lista_de_sexo = []
prosseguir = ''
idade_maxima = 20
idade_minima = 0
mulheres_com_menos_de_20 = 0
idade_do_hm_mais_velho = 0
nomevelho = ''
media = 0



while True:
    print('------------------------')
    nome = str(input('Qual o nome da pessoa: ')).upper().strip()
    idade = int(input('Qual a idade:  '))
    sexo = int(input('Qual o sexo [1]feminino [2]Masculino: '))
    prosseguir = str(input('Quer continuar? [S ou N]: ')).upper().strip()[0]

    if prosseguir == 'S':
        lista_de_idade.append(idade)
        lista_de_nomes.append(nome)
        lista_de_sexo.append(sexo)
        total_soma_de_idade = sum(lista_de_idade)
        media = total_soma_de_idade / 2

        for c in range(0, len(lista_de_sexo)):
            if lista_de_sexo[c] == 2:
                if lista_de_idade[c] > idade_do_hm_mais_velho:
                    idade_do_hm_mais_velho= lista_de_idade[c]
                    nomevelho += nome

        for s in range (0, len(lista_de_sexo)):
            if lista_de_sexo[s] == 1:
                if lista_de_idade[s] < idade_maxima:
                    mulheres_com_menos_de_20 += 1

    elif prosseguir == 'N':
        print(f'a quantidade de mulheres com menos de 20 anos é {mulheres_com_menos_de_20}')
        print(f'idade do homem mais velho {idade_do_hm_mais_velho} e seu nome é {nomevelho}')
        print(f'A média de idade do grupo é {media}')
        break
print('Fim do programa')


