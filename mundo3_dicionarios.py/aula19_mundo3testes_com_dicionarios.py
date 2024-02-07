#dicionario

dados = {'nome': 'paulo', 'idade': 25} # a diferença é que quando for printar náo vou usar indices numericos
# e sim o nome do indice. ex abaixo
print(dados['nome'])
#no caso do dicionario o append nao funciona, ao inves disso se usa o comando abaixo
dados['sexo'] = 'm' # assim eu adiciono um dado
del dados['idade'] #assim eu removo o dado ídade'

filme = {'nome': 'Star wars', 
         'ano': 1977,
         'diretor': 'george lucas'
}
print(filme.values()) #o comando values me retorna somente os valores do meu dicionario, somente a parte de cima
# que são os 'star wars' '1977' 'george lucas'
print(filme.keys()) # me retorna a parte de baixo, os indices do meu dicionario, que nesse caso sáo:
#nome, ano e diretor, sem os valores.
print(filme.items())# vai pegar todos os dados da lista e printar, tanto o de baixo quanto o de cima, ou seja:
# nome: star wars - ano: 1977 - diretor: george lucas
for chavi, valores in filme.items(): # esse for passa pelas chaves(nome,ano etc) e os valores(star wars, 1977 etc)
    # pois eu coloquei .items() na frente do filme, então ele vai passar por todos os valores do dicionario
    print(f'o {chavi} é {valores}')
# ****** mais algumas explicaçoes no caderno *****
    


# PARTE PraTICA DA AULA 

pessoas = {'nome': 'gustavo', 'sexo': 'm', 'idade': 22}
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}') #mosta itens especificos do meu dicionario, neste caso
# gustavo tem 22 
print(pessoas.keys()) # mostra as chaves, neste caso nome, sexo e idade
print(pessoas.values()) # mostra os valores, gustavo, 'm' e 22
print(pessoas.itens()) #mostra todos os dados ((nome: gustavo)(sexo: m) (idade: 22))
pessoas['peso'] = 98.5 #adiciona o item a lista
for c in pessoas.keys():
    print(c) #vai mostrar somente as chaves 
for k in pessoas.values():
    print(k) #vai monstrar somente os valores
for k, c in pessoas.items(): #para usar o itens é necessario colocar o c em frente ao k
    print(f'{k}{c}')        #para rodar todos os dados do dicionario

# ----------------------------------------

brazil = []
estado1 = {'uf': 'sao paulo', 'sigla': 'sp'}
estado2 = {'uf': 'rio de janeiro', 'sigla': 'rj'}
brazil.append(estado1)
brazil.append(estado2)
print(brazil[1]['sigla']) #vai printar rj

# ------------------------------------------
from random import randint
from operator import itemgetter # função que coloca em ordem 
#exemplo
#jeito q o guanabara usou esse operator ---------
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1, 6),
         'Jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
print('valores sorteados')

for c, k in jogo.items():
    print(f'{c} tirou {k}')
sleep(1)
#logo abaixo ele deu ao ranking a funcionalidade de ordenar a chave, por isso o key = itemgetter(1)
#este (1) é para dizer a funçao para pegar a posição 1 da chave, então sera os valores sorteados ex:
#jogador1 - posicao 0 e o randint(1,6) - posicao 1 / reverse = true é para ir do maior para o menor
#para ir do menor para o maior é só apagar esse comando
ranking = sorted(jogo.items(), key = itemgetter(1), reverse= True) 



estados = {}
usa = []
for c in range(0, 3):
    estados['uf'] = str(input('Unidade federativa: '))
    estados['sigla'] = str(input('Digite a sigla do estado: '))
    usa.append(estados.copy()) #assim copia os dados para a lista sem dar erro e da pra fazer fatiamento
    #sem problemas
for e in usa:
    for k, v in e.items:
        print(f'o campo {k} tem valor {v}')
for c in usa:

    for v in e.values():
        print(f'{v}')