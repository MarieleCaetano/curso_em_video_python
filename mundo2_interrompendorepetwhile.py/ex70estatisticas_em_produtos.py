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

#Outro modo de fazer
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa')
print(f'O total da compra for R${total:2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000')
print(f'O produto mais barato foi {barato} que custa R$ {menor:2f}')


        





