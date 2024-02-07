dados_do_aluno = {}

aprovado = 'parabens, voce passou de ano'
recuperacao = 'Voce está de recuperação'
reprovado = 'Sua nota foi abaixo do esperado, então esta reprovado'

dados_do_aluno['nome'] = str(input('Nome do aluno: '))
dados_do_aluno['media'] = float(input(f'Digite a media de {dados_do_aluno["nome"]}: '))

for i, k in dados_do_aluno.items():
    print(f'{i} é igual a {k}')

if dados_do_aluno["media"] >= 7:
    print(aprovado)
if dados_do_aluno["media"] >= 5 and dados_do_aluno["media"] < 7:
    print(recuperacao)
if dados_do_aluno["media"] < 5:
    print(reprovado)


#Jeito que o gunabara fez

aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Digite a media de {aluno["Nome"]}'))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
