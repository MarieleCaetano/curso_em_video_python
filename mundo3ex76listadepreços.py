produtos = ('Notebook', 2500, 'Microondas', 340, 'Tablet', 870, 'Tv', 1500, 'Sofá', 890, 'Cama', 990, 'Iphone', 2970)
print('='*20, 'LISTAGEM DE PREÇOS', '='*20)
tamanho_da_linha = 48
for c in range (0,len(produtos),2):
    quantidade_dos_pontos = (tamanho_da_linha - len(f'{produtos[c+1]}')) - len(produtos[c])
    print(f'produto: {produtos[c]}', '.' * quantidade_dos_pontos ,f'R${produtos[c+1]}')


    #outro modo de fazer
listagem = ('Lapis', 1.75, 
            'Borracha', 2.84,
            'Caderno', 15,
            'estojo', 25,
            'mochila', 120.95,
            'Canetas', 22.50,
            'livro', 34,10)
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='  ')
    else:
        print(f'{listagem[pos]:.>7.2f}')