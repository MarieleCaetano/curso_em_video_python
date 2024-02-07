
#import random
#nomes = input("Digite os nomes, sugiro que seja quatro: ")

#nome1 = nomes.split(',')[0]
#nome2 = nomes.split(',')[1]
#nome3 = nomes.split(',')[2]
#nome4 = nomes.split(',')[3]

#sorteio = nomes.split(',')[random.randint(0,3)]

#print('Dos alunos 0 - {}, 1 - {}, 2 - {}, 3 - {} quem irá apagar a lousa para o professor é o aluno numero {}'.format(nome1, nome2, nome3, nome4, sorteio))


import random
nome1 = str(input("Primeiro nome: "))
nome2 = str(input("segundo nome: "))
nome3 = str(input("terceiro nome: "))
nome4 = str(input("quarto nome: "))
lista = [nome1, nome2, nome3, nome4]
ordem= random.shuffle(lista)

print(' A ordem de alunos é')
print(lista)