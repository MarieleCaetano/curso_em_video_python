#AULA 21 PARTE 2 ------ APRENDENDO SOBRE:
#- Interactive help, - Docstrings, - Argumentos opcionais, - exopo de variaveis, - retorno de resultado.
# 1 modo: INTERACTIVE HELP(CMDS: TERMINAL > DIG: HELP() > DIG: EX= PRINT OU ALGUM OUTRO, PRA SAIR > quit)
#2 modo de usar: (Se eu digitar > Help(print) < na linha de comando ele vai me retornar a explicacao tmb )
#help(print)
#3 modo de usar:(usar o __doc__ dentro do print depois do variavel ex:)
print(input.__doc__)
#Interactive help - serve para retornar uma explicação sobre uma determinada função do python (help())
#DOCSTRINGS
def contador(i, f, p):
# isso abaixo gera tipo uma docstring, era pra funcionar quando eu roda-se o help(contador) mas se passar
#o mouse acima do contador ali em cima o texto abaixo aparece ja como doc
    """
    -> faz uma contagem e mostra na tela.
    :param i: ínicio da contagem
    :param f: fim da contagem                
    :param p: passo da contagem             
    :return: sem retorno
    """

    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
        print('fim')


#help(contador)


def somar(a,b,c=0): #colocando o =0 faz com que o programa entenda q se n houver valor, o c (no caso)
                    #tem o valor 0, chamados parametros opcionais
    s = a+b+c
    print(f'A soma vale {s}')


somar(2,4,4)
somar(8,1)

#Escopo de variaveis, o que é? = É o local onde uma variavel vai existir, ou onde uma var n vai existir
#ex:
def teste(b):
    global a # essa funcao serve para o prog nao usar o A la debaixo e sim faz o Acom valor 5 ser global
    a = 5 # Se eu colocar um a aqui dentro def e existir um a no programa principal vao haver duas variaveis
    # A, esta var A é uma var local assim como b e x, o outro A é uma var global
    b += 4
    x= 8
    print(f'Na função teste o n tmb vale {n}')

#mesmo o n estando aqui no programa principal ele ainda func no def ali em cima, isso se chama escopo global
n = 2
print(f'No programa principal n tem o valor de {n}')
teste()
#print(f'No programa principal o x vale {x}') #nao funciona por o x esta no def, tendo um escopo local
a = 3 # esse passa a valer 8 graças ao global a lá de cima
teste(a) #apesar do def ter o valor b, o valor 3 q esta no A é copiado para o b, virando 3. mas como eu
#fiz b += 4 ele vai somar o valor de a q é 3 mais o valor 4, virando 7

# ---------------------------------
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao() # vai me retornar o valor 4, do n1 de dentro da def
print(f'N1 fora vale {n1}') # vai me retornar o valor 2, do n1 aqui de fora

#RETORNO DE VALORES - RETURN ------------------------
def smar(a,b,c):
    w = a+b+c
    return w # faz a soma de smar retornar como o valor de resp

resp1 = smar(3,2,4)
res2 = smar(5,6)
res3 = smar(2)

print(smar(3,4,1))
print(f'Meus calculos deram {resp1}, {res2}, {res3}')

#----------------------------------------------------------------
def fatorial (num= 1):
    f = 1
    for c in range(num, 0, -1):
        f += c                          #usando return em numeros
    return f

n = int(input('Digite '))
print(fatorial(n)) # ou
print(f'O fatorial de {n} é igual a {fatorial(n)} ')
#----------------------------------------------------------------
def par(n=0):
    if n%2==0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))      #retorna usando return true ou false
print(par(num))
if par(num):
    print('É par')
else:
    print('É impar')