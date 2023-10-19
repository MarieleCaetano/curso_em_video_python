sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input(f'Digite o seu genero [F] feminino ou [M] masculino: ')).upper().strip()[0]
    print('Voce dititou ' + sexo)
    if sexo != 'F' and sexo != 'M':
        print("Não existe esse sexo, tente novamente")
    else:
        print('obrigada por sua resposta')
