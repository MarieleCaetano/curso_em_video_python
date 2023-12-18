numero = 0
lista_numeros_unicos = []
while True:
    numero = int(input('Digite um valor: '))
    quer_continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    
    if numero in lista_numeros_unicos:
        print('Ops, esse numero já foi digitado, tente novamente') 
    else:  
        lista_numeros_unicos.append(numero)
        print('Seu numero foi armazenado com sucesso')
    if quer_continuar == 'N':
        break

print(lista_numeros_unicos)
   
