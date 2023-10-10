#aula 9 - ex 27 - mundo 1
nome = input('Digite seu nome completo: ').strip()
nome1 = nome.split (' ')[0]
print('O seu primeiro nome é: {}'.format(nome1))
nome2 = nome.split(' ')[-1]
print('O seu ultimo nome é: {}'.format(nome2))

