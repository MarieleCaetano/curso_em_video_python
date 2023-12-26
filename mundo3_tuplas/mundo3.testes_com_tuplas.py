#tupla () lista [] dicionario {}
lanche = ('hamburguer','suco', 'pizza', 'pudim')
#para no print não aparecer o () e as virgulas, dá pra fazer assim:
#esse abaixo é caso não precise da posição
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-'*50)
#Esse mostra a posição
for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('-'*50)
#Esse também mostra a posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-'*50)
#da pra mostrar tambem os elementos da lista em ordem
print(sorted(lanche))

print(lanche[1])
print(lanche[-1])
print(lanche[0])
print(lanche [1:3])
print(lanche[:3])
print(lanche[-2:])
#tuplas são imutaveis
#lanche[1] = 'refrigerante' #vai dar erro pois nao dá pra substituir o suco pelo rrefri(um por outro)

#outros tipos de tuplas 
print('-'*50)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #junta a tupla a com a b, colando uma na outra, se for b + a fica 5,8,1,2,2,5,4
print(c.count(5)) # Quantas vezes aparece o numero 5 dentro de c
print(c.index(8))  #Mostra em qual posição está o 8 em c
print(c.index(2, 4)) #mostra qual posição tem o numero 2 apartir da posição 4, como o num 2 aparece mais de uma vez
print('-' * 50)

#No python as tuplas aceitam tanto numero quanto string juntas, elas não precisam ser do mesmo tipo. ex:

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) #Apaga a tupla, mas você só consegue apagar ela por inteira, apagar algum elem dentro dela n é possivel
print(pessoa)

#sorted = (lista) #põe em ordem alfabetica