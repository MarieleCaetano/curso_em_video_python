inicio = float(input('escreva um numero: '))
inicio2 = float(input('escreva outro numero: '))
if inicio == inicio2 and inicio2 == inicio:
    print('Os dois numeros são iguais')
elif inicio > inicio2:
    print('O primeiro numero é maior que o segundo')
elif inicio2 > inicio:
    print(' O primeiro numero é menor que o segundo')