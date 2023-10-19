#primeiro termo: 1  e a razão:2 ate o numero 10 ex 61 e ex 62
#vezes = 0
#continuar = ''
#while continuar != 'S': 
#    continuar = str(input('Você quer continuar? Se sim digite [C] OU [S] para sair: ')).upper()
#    termo = int(input('Digite o seu numero inicial: '))
#    razão = int(input('Digite a sua razão: '))
#    vezes = int(input('Digite até qual numero: '))
#    soma = 0
#    quantoselem = termo + (vezes-1)
#    elem = quantoselem + 1

#    for var in range(termo, elem, razão):
#        print(f'''{var}', end=' -> 
#              ''')
#        soma= soma+var
#        print(soma)

#Resolução do curso
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA: '))
termo = primeiro 
total = 0
cont = 1
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end= '')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termo você quer mostrar a mais? '))
print(f'Fim, progressão finalizada com {total} termos')

