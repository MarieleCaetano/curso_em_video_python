def dobro(preço):
     res = preço * 2
     return res

def metade(preço):
    res = preço / 2
    return res


def aumentando(preço, taxa):
    res= preço + (preço * taxa/100)
    return res


def reduzindo(preço, taxa):
    res = preço - (preço * taxa/100)
    return res
