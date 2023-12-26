print('='*50)
print('BOLETIM DOS ALUNOS')
print('='*50)
continuar = 'S'
nome_notas_inteiras = []
somente_nome = []

while continuar == 'S':
    nome = str(input('Nome: '))
    nome_notas_inteiras.append(nome)
    somente_nome.append(nome)

    nota1 = float(input('Nota 1: '))
    nome_notas_inteiras.append(nota1)

    nota2 = float(input('Nota 2: '))
    nome_notas_inteiras.append(nota2)

    continuar = str(input('Quer continuar? [S-N]')).upper()[0]

print('-'*30)

for pos in range(0, len(nome_notas_inteiras), 3):
    media = (nome_notas_inteiras[pos + 1] + nome_notas_inteiras[pos + 2]) / 2
    print(f'{int(pos / 3)} {nome_notas_inteiras[pos]} {media}')
    print()
print('-'*30)


while True:
    mostrar_notas = int(input('Mostrar notas de qual aluno? [999 para parar o programa] '))
    print(f'{nome_notas_inteiras[mostrar_notas * 3 + 1]} {nome_notas_inteiras[mostrar_notas * 3 + 2]}')
    if mostrar_notas == 999:
        break