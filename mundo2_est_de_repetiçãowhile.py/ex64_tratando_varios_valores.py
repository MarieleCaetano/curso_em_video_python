soma_total = 0
quantidade_de_numeros_digitadas = 0
numero_escolhido = 0 
while True:
    numero_escolhido = int(input('Digite um numero: '))  
    if numero_escolhido == 999:
        break

    quantidade_de_numeros_digitadas = quantidade_de_numeros_digitadas + 1
    soma_total = soma_total + numero_escolhido
        
print(f'''O programa foi encerrado, pois você digitou o numero 999 
      você digitou essa quantidade de numeros: {quantidade_de_numeros_digitadas}
      a soma dos numeros que você digitou é {soma_total}''')
