dados_do_aluno = {}
dados = []
aprovado = 'parabens, voce passou de ano'
recuperacao = 'Voce está de recuperação'
reprovado = 'Sua nota foi abaixo do esperado, então esta reprovado'

for c in range(0, 1):
    dados_do_aluno['nome'] = str(input('Nome do aluno: '))
    dados_do_aluno['media'] = float(input(f'Digite a media de {dados_do_aluno["nome"]}: '))
    dados.append(dados_do_aluno.copy())

for i, k in dados_do_aluno.items():
    print(f'{i} é igual a {k}')

if dados_do_aluno["media"] >= 7:
    print(aprovado)
if dados_do_aluno["media"] >= 5 and dados_do_aluno["media"] < 7:
    print(recuperacao)
if dados_do_aluno["media"] < 5:
    print(reprovado)