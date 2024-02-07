def dobro(preço = 0, formato=False):
     res = preço * 2
     return res if formato is False else moeda(res)

def metade(preço= 0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res) # -  esse


def aumentando(preço = 0, taxa= 0, formato=False): #formato=false para funcionar preciso colocar 
                                                   #no programa principal a palavra true
    res= preço + (preço * taxa/100)
    return res if not formato else moeda(res)
'''
-> calcula o aumento de um determinado preço
retornando o resultado com ou sem formatação
:param preço: o preço que se quer ajustar
:param taxa: qual é a porcentagem do aumento/redução
:param formato: quer a saida formatada ou nao
: param return: o valor reajustado, com ou sem formato.
'''


def reduzindo(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa/100)
    return res if not formato else moeda(res) # - e esse fazem a mesma coisa


def moeda(preço=0, moeda= 'R$'):
    return f'{moeda} {preço:>8.2f}'.replace('.',',') #replace- onde tiver ponto(.) eu vou substituir por virgula(,)


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(35))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preoço é: \t{dobro(preço, True)}')
    print(f'Metade do preço é: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento fica: \t{aumentando(preço, taxaa, True)}')
    print(f'{taxar}% de redução fica: \t{reduzindo(preço, taxar, True)}')
