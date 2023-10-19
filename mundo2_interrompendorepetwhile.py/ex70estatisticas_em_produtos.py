import sys

print('~' *70)
print('-' *30, 'Loja online', '-' * 27)
print('~' * 70)
nomedoproduto = []
lista_de_valor = 0
menor_num = sys.maxsize
maior_num = 0
produtos_com_mais_de_mil_reais = 0
nome_do_produto_maisbarat = ''
while True:
    nomedoproduto = str(input('Digite o nome do produto: ')).upper().strip()
    valor = float(input('Preço: R$ '))
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    lista_de_valor += valor
    
    if valor > 1000:
        produtos_com_mais_de_mil_reais += 1
    if valor > maior_num:
        maior_num = valor
    if valor < menor_num:
        menor_num = valor
        nome_do_produto_maisbarat = nomedoproduto

    if continuar == 'N':
         break
    
print(f'A soma do valor dos produtos que você digitou é {lista_de_valor}')
print(f'A quantidade de produtos com mais de mil reais é {produtos_com_mais_de_mil_reais}')
print(f'E o produto mais barato é o {nome_do_produto_maisbarat} e seu valor é {menor_num}')
        





