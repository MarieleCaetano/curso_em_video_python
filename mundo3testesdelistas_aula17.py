#no ex abaixo vemos que ao contrario da tupla, conseguimos mudar o valor de uma determinada posição(nesse caso posição
# 2 virou o numero 3, substituindo o valor 9)
num = [2, 5, 9, 1]
num1 = [3, 9, 5, 4, 6, 8]
num[2] = 3
num1.insert(4, 1) #insere um valor na posição que você quiser, nesse ex. ele inseriu o valor 0 na posição 2
num.append(7)  #add o valor 7 a lista, faz ele ser adicionado no final da lista
num.sort() #coloca os numeros em ordem crescente
num1.sort(reverse=True) #coloca os numeros em ordem decrescente
num.pop()# sem valor dentro ele elimina o ultimo valor, no caso dessa lista é o num 1
num.pop(2) #Ele elimina o elemento na posição dois, no caso o numero 9
num.remove(2) # Elimina o primeiro numero 2 da lista, independente da posição, nesse caso seria o na posição 0
print(num1)
print(f'Essa lista tem {len(num1)} elementos') #mostra quantos valores tem na lista
print(num)
#del lanche[9]  - remove o objeto na posição nove
#lanche.pop(9)  - é só outro modo de eliminar o objeto que esta na posição nove
#lanche.remove('pizza') - remove o objeto indicado entre aspas
#lanche.pop() - vai eliminar o ultimo elemento da lista

#------------------------

valores = list()  #da pra criar uma lista assim tmb
mylist = []
mylist.append(5)
mylist.append(9)
mylist.append(4)
for m in mylist:
    print(f'{m}...\n', end=' ')
for c, w in enumerate(mylist):
    print(f'Na posição {c} encontrei o valor {w}', end=' ') #mostra o valor e a posição
print('Cheguei ao final da lista')
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))#Pega os valores que são digitados e coloca dentro da lista

#------------------------

a = [2, 3, 4, 7]
b = a
b = a[:] # cria uma cópia dos numeros de a no b, então quando eu mudar a posição do b ele vai pegar o numero
#e o modificar, mas sem mexer no num da lista a, o q aconteceria se não tivesse o [:]
b[2] = 8 # Ele muda o numero tanto no a quanto no b
print(a)
print(b)

#===========================
valores = list(range(4,11))