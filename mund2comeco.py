#aula 12 condições aninhadas
nome = str(input('Qual é o seu nome? '))
if nome.lower() == ('mariele'):
    print('Que nome lindo!')
elif nome.lower() == 'pedro' or nome == 'maria' or nome == 'marco':
    print('Seu nome até que é daorinha')
elif nome.lower() in 'célia marta ana julia':
    print('Seu nome é bem comum')
else:
    print('Seu nome é mto feio tenho pena, mas de qualquer modo')
print('tenha um bom dia {}'.format(nome))