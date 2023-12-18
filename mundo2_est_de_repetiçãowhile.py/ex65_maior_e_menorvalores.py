
escolha_de_num_do_jogador = 0
quantidade_de_vezes_digitada = 0
escolha_de_sair = ''
total = 0
media = 0
while True:
    escolha_de_num_do_jogador = int(input('Digite um numero: '))
    escolha_de_sair = str(input('Quer continuar? Digite [Sair] ou [F] para continuar: ')).upper()
    total = total + escolha_de_num_do_jogador
    quantidade_de_vezes_digitada = quantidade_de_vezes_digitada + 1

    if escolha_de_sair  == 'SAIR':
        break

    media = total / quantidade_de_vezes_digitada
print(f'A soma total dos numeros digitados é {total}, você digitou {quantidade_de_vezes_digitada} vezes e a média da soma é {media}')

#####Outro modo de fazer

resp = 'S'
soma = quant = medida = maior = menor = 0
while resp in 'Ss':
    num= int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
medida = soma / quant
print(f'Você digitou {quant} numeros e a  média foi {medida}')
print(f'O maior numero foi {maior} e o menor digitado foi {menor}')
    



