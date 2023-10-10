#aula 9 - ex 23
#frase = (input('Digite um numero: '))
#num1 = (frase.strip()[0])
#print('milhar: {}'.format(num1))
#num2 = (frase.strip()[1])
#print('centena:{}'.format(num2))
#num3 = (frase.strip()[2])
#print('dezena:{}'.format(num3))
#num4 = (frase.strip()[3])
#print('unidade:{}'.format(num4))


#Exemplo do guanabara muito pika


num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando seu numero: {}...'.format(num))
print('Unidade: {}'.format(u))
print('dezena:  {}'.format(d))
print('centena: {}'.format(c))
print(' milhar: {}'.format(m))