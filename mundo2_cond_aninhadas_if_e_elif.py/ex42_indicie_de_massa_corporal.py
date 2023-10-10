altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))

imc = peso / altura**2
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Seu Imc está abaixo de 18.5, portanto você está abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Seu peso está entre 18.5 e 25, portanto está com o peso ideal')
elif imc > 25.00 and imc <= 30.00:
    print('Seu imc está entre 25 e 30, então você está com sobrepeso')
elif imc > 30 and imc <= 40:
    print('Seu peso está entre entre 30 e 40, você está obeso(a) I')
elif imc > 40:
    print('Seu IMC está maior que 40, você está com obesidade mórbida')