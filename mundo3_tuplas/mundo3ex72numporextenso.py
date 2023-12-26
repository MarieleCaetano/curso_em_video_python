numeros =('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez')
numpart2 = ('onze', 'doze', 'treze', 'catorze','quinze','dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')
total = numeros + numpart2
while True:
    escolhadojogador = int(input('Digite um numero entre 0 e 20: '))
    cont = str(input('Quer continuar? [S-N]: ')).upper()[0]
    if cont == 'S' and 0 >= escolhadojogador <= 20:
        print(f'Você digitou o numero {total[escolhadojogador]}')
    elif 0 < escolhadojogador > 20 and cont == 'S':
        print('Numero invalido tente novamente')
    else:
        break 
  