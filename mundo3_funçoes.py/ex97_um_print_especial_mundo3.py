total = {}
frase1 = 'Vivendo com dedicação'
frase2 = 'Fé e dignidade'
frase3 = 'É o estilo de vida que molda o mundo'

def quebralinha(a):
    a = '-'
    print(len(frase1) * a)
  

quebralinha(a= '-')
print(frase1)
quebralinha(a= '-')

def quebra(b):
    b = '-'
    print(len(frase2) * b)

quebra(b= '-')
print(frase2)
quebra(b= '-')

def traço(c):
    c = '-'
    print(len(frase3) * c)

traço(c= '-')
print(frase3)
traço(c= '-')
#-----------------------------
def escreva(msg):   #pra quando for usar str, frases
    tamanho = len(msg) + 4
    print('=' * tamanho)
    print(f'  {msg}')
    print('=' * tamanho)



escreva('Mariele caetano siqueira')
escreva('tenho 23 anos')
escreva('Moro no estado de São paulo')