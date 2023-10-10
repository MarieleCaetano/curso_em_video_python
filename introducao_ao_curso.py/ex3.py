#desafio 1
n1 = int(input('Escreva um numero inteiro:'))
print("O numero antecessor ao que você digitou é: {} ".format(n1 - 1) , end='>>>>')
print(" E o numero que procede ao que você digitou é: {}".format(n1 + 1))

#desafio 2
n3 = int(input("Digite um valor de 3 digitos:"))
print("O dobro do valor que você digitou é: {} , e a raiz quadrada dele é {:.2} ".format(n3 * 2 , n3**(1/3)))

#desafio 3
mat = float(9.5)
hist = float(8.0)
result = mat + hist 
print('Joãozinho recebeu as notas de duas materias, matematica, 9.5 e história 8.0, que somando dá ' , end='')
print('{}, portanto a média de suas notas é {}'.format(result , result / 2))
