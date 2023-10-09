#aula 10, condições - mundo 1 - praticas

#nome = str(input('Qual o seu nome? ')).strip() 
#if nome.lower() == 'gustavo':
#    print('Que nome lindo você tem')
#print('Bom dia {}'.format(nome))


n1 = float(input('Digite sua nota: '))
n2 = float(input('digite sua segunda nota: '))
m = (n1 + n2)/2
print('sua média foi: {:.1f}'.format(m))
if m>= 6.0:
    print('Parabéns! Sua média foi boa!')
else:
    print('Sua média foi ruim, estude mais')