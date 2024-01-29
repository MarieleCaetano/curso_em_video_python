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


def somar(a,b,c):
    s = a+b+c
    print(f'A soma vale {s}')


somar(2,4,4)
somar(8,1)


