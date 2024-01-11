from time import sleep
Dados_pessoa_fisica = {}

Dados_pessoa_fisica['nome'] = str(input('Nome: '))
anoDeNascimento = int(input('Ano de nascimento: ' ))
Dados_pessoa_fisica['Idade'] = 2023 - anoDeNascimento
Dados_pessoa_fisica['carteira de trabalho']= int(input('Carteira de trabalho |0 não tem|: '))

if Dados_pessoa_fisica['carteira de trabalho'] > 0:
    Dados_pessoa_fisica['ano de contratação'] = int(input('Ano de contratação: '))
    Dados_pessoa_fisica['Salário'] = float(input('Salário: '))
    calculandoAposentadoria = 35 - (2023 - Dados_pessoa_fisica['ano de contratação']) 
    Dados_pessoa_fisica['Idade de aposentadoria'] = Dados_pessoa_fisica['Idade'] + calculandoAposentadoria
    print('processando...')
    sleep(2)
    print('-'*30)
    for k, c in Dados_pessoa_fisica.items():
        print(f'{k} {c}')
else:
    print('processando...')
    sleep(2)
    print('-'*30)
    for c, k in Dados_pessoa_fisica.items():
        print(f'{c} é {k}')