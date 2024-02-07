lista_de_pessoas = []
continuar = 'Nn'
while True:
    dic_de_pessoa = {}
    dic_de_pessoa['nome'] = str(input('Nome: '))

    dic_de_pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
    while dic_de_pessoa['sexo'] not in 'mMfF':
        print('Opção invalida')
        dic_de_pessoa['sexo'] = str(input('Sexo: '))

    dic_de_pessoa['idade'] = int(input('Idade: '))

    lista_de_pessoas.append(dic_de_pessoa)
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar in 'Nn':
        break

lista_de_idades = []
soma_das_idades = 0

for pessoa in lista_de_pessoas:
    idade_da_pessoa = pessoa['idade']

    soma_das_idades = soma_das_idades + idade_da_pessoa
    lista_de_idades.append(idade_da_pessoa)

media = soma_das_idades / len(lista_de_idades)
print('='*30)
print(f'A média das pessoas é {media :.4}')


print(f'Pessoas que estão em cima da média:')
for pessoa in lista_de_pessoas:
    idade_da_pessoa = pessoa['idade']
    nome_da_pessoa = pessoa['nome']
    sexo_da_pessoa = pessoa['sexo']
    print(pessoa)
    if idade_da_pessoa > media:
        print(f'{nome_da_pessoa} está acima da média, pois tem {idade_da_pessoa}')
    if sexo_da_pessoa in 'Ff':
        print(f'{nome_da_pessoa} é do sexo feminino ')


#modo que o guanabara fez
galera = []
pessoal = {}
ssoma = mediacao = 0
while True:
    pessoal.clear()
    pessoal['Nome'] = str(input('Digite o nome: '))
    while True:
        pessoal['Sexo'] = str(input('Qual o sexo? [M ou F]: ')).upper()[0]
        if pessoal['Sexo'] in 'MF':
            break
        print('Erro! por favor, digite M ou F')
    pessoal['idade'] = int(input('Digite a idade: '))
    ssoma += pessoal['idade']
    galera.append(pessoal.copy())
    respo = ''
    while True:
        respo = str(input('quer continuar? S ou N: ')).upper()[0]
        if respo in 'SN':
            break
        print('Erro! responda apenas S ou N')
    if respo == 'N':
        break
print('-'* 30)
print(galera)
mediacao = ssoma / len(galera)
print(f'Cadastramos um total de {len(galera)}')
print(f'A media das idades é de {mediacao:5.2f} anos')
print('O nome das mulheres cadastradas foram ', end= '')
for u in galera:
    if u['Sexo'] in 'Ff':
        print(f'{u["Nome"]}', end= '')
print()
print('Lista de pessoas que estão com idade acima da média: ')
for t in galera:
    if t['idade'] >= mediacao:
        print('     ')
        for k, q in t.items():
            print(f'{k} == {q} ', end= '')
        print('     ')
print('>> encerrado <<<')

