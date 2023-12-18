#nome, idade e sexo de varias pessoas
#lista_de_nomes = []
#lista_de_idade= []
#lista_de_sexo = []
#prosseguir = ''
#idade_maxima = 20
#idade_minima = 0
#mulheres_com_menos_de_20 = 0
#idade_do_hm_mais_velho = 0
#nomevelho = ''
#media = 0



#while True:
#    print('------------------------')
#    nome = str(input('Qual o nome da pessoa: ')).upper().strip()
#    idade = int(input('Qual a idade:  '))
#    sexo = int(input('Qual o sexo [1]feminino [2]Masculino: '))
#    prosseguir = str(input('Quer continuar? [S ou N]: ')).upper().strip()[0]
#
#    if prosseguir == 'S':
#        lista_de_idade.append(idade)
#        lista_de_nomes.append(nome)
#        lista_de_sexo.append(sexo)
#        total_soma_de_idade = sum(lista_de_idade)
#        media = total_soma_de_idade / 2

#        for c in range(0, len(lista_de_sexo)):
#            if lista_de_sexo[c] == 2:
#                if lista_de_idade[c] > idade_do_hm_mais_velho:
#                    idade_do_hm_mais_velho= lista_de_idade[c]
#                    nomevelho += nome

#        for s in range (0, len(lista_de_sexo)):
#            if lista_de_sexo[s] == 1:
#                if lista_de_idade[s] < idade_maxima:
#                    mulheres_com_menos_de_20 += 1

#    elif prosseguir == 'N':
#        print(f'a quantidade de mulheres com menos de 20 anos é {mulheres_com_menos_de_20}')
#        print(f'idade do homem mais velho {idade_do_hm_mais_velho} e seu nome é {nomevelho}')
#        print(f'A média de idade do grupo é {media}')
#        break
#print('Fim do programa')


#outro modo de resolver
tot18 = 0
totdehomens = 0
totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totdehomens += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1



    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Acabou o programa. Total de pessoas com mais de 18 anos { tot18}')
print(f'Ao todo temos {totdehomens} homens cadastrados')
print(f'E o total de mulheres com menos de vinte anos é {totM20}')

