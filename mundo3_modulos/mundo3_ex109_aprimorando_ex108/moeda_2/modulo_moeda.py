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


def reduzindo(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa/100)
    return res if not formato else moeda(res) # - e esse fazem a mesma coisa


def moeda(preço=0, moeda= 'R$'):
    return f'{moeda} {preço:>8.2f}'.replace('.',',') #replace- onde tiver ponto(.) eu vou substituir por virgula(,)
