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
    


# PARTE PARTICA DA AULA 

pessoas = {'nome': 'gustavo', 'sexo': 'm', 'idade': 22}
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')