numeros_digitados = 0
soma_total = 0
while True:
    escolhadojogador = int(input('Digite um valor (digite 999 para sair): '))
    if escolhadojogador == 999:
        break
    numeros_digitados += 1
    soma_total += escolhadojogador

print(f'Você digitou {numeros_digitados} e a soma dos numeros que você digitou é {soma_total}')


