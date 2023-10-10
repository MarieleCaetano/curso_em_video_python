#aula 9 ex 26 mundo 1
frase = str(input('Digite uma frase :) : ')).strip()
frase0 = frase.lower()
frase1 = (frase0.count('a'))
print('A letra A aparece {} vezes'.format(frase1))
frase2 = (frase0.find('a'))
print('A letra A na frase aparece pela primeira vez na posição {}'.format(frase2))
frase3 = (frase0.rfind('a'))
print('A letra A na frase aparece pela ultima vez na posição {}'.format(frase3))