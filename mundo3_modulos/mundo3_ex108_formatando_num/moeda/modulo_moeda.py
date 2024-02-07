def dobro(preço = 0):
     res = preço * 2
     return res

def metade(preço= 0):
    res = preço / 2
    return res


def aumentando(preço = 0, taxa= 0):
    res= preço + (preço * taxa/100)
    return res


def reduzindo(preço = 0, taxa = 0):
    res = preço - (preço * taxa/100)
    return res


def moeda(preço=0, moeda= 'R$'):
    return f'{moeda} {preço:>8.2f}'.replace('.',',') #replace- onde tiver ponto(.) eu vou substituir por virgula(,)
