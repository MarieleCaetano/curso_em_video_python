teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste[:])
print(galera)

# desta forma acima quando dou o print ele replica duas veses o maria 20, pois vira tudo a mesma estrutura
# para dar certo precisa usar o [:] na frente do teste, como esta ag, que ai mostra gustavo 40 e maria 20 logo em seguida

pessoal = [['João', 19], ['Ana', 33], ['joaquim', 13], ['maria', 45]]
print(pessoal[2][1])
for p in pessoal:
    print(f'{p[0]} tem {p[1]} de idade') # vai girar em torno dos dados da variavel pessoal, o p 0 vai ser
    #os nomes e o p 1 vai ser a idade cada dado de sua estrutura propria ex estrut 1: joao[0] 19[1]


#criando uma lista temporaria para outros dados de outra lista 
grupo = []
dados = []
totaldemaioridade = totaldemenoridade = 0
for c in range(0,3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))   #adicionei os dados de nome e idade na lista dados e depois
    grupo.append(dados[:])                         # transferi para uma lista definitiva grupo e apaguei a lista dados
    dados.clear()
print(grupo)


for p in grupo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totaldemaioridade += 1            # aqui neste for estou verificando que é maior de idade e quem é menor
    else:
        print(f'{p[1]} é menor de idade')
        totaldemenoridade += 1
print(f' temos {totaldemaioridade} maiores de idade e {totaldemenoridade} menores de idade')
