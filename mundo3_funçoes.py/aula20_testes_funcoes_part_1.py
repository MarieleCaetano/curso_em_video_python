#funções aula 20 testes
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s) 
# desta forma acima o programa se torna repetitivo, então podemos fazer da seguinte forma
def soma(a, b):
    print(f'A = {a} + B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
#aqui sempre tem q pular duas linhas após uma def
    
soma(4, 8) # vai printar a soma dos numeros
soma(2, 8)
#logo abaixo mostra um outro exemplo, onde deixo explicito qual é o a e qual e o B
soma(a=3, b=4)
# ----------------------
# em python existe um sistema chamado empacotador para facilitar a vida de quem coda, e ele funciona da
#seguita forma abaixo
def contador(*num): #assim ele conta quantos numero estiverem entre () não importando a quantidade, o * serve
# para dizer ao programa q tem numeros dentro () e q é para ele desempacotar esses numeros, independente
# da quantidade
    for valor in num:
        print(f'{valor} ', end= '')
    print(' - Fim -')
    tam = len(num) #aqui estou contando quantos numeros tem
    print(f'Recebi os valores {num} e contei que nela tem {tam} numeros')


contador(8,7,3,2,4)
contador(3,2,1)
contador(7,1,3,2,6,9,0)
# ----------------------
#em python consigo trabalhar tambem com listas usando funções, ex:
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [0, 7, 3, 2, 1, 4, 6]
dobra(valores)
print(valores)
# ---------------------
#para somar numeros sem um limite de quantidade é da seguinte forma:
def somando(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores{valores} temos {s}')

somando(4,5)
somando(6,4,1,2,3)