#valorDoProduto = float(input('Qual o valor do produto? '))
#ModoDePag = input('Qual a forma de pagamento? ')
#QuantasParcelas = int(input('Quantas parcelas? ex: 2: '))


#if ModoDePag == 'cheque' or ModoDePag == 'dinheiro':
#    comDescontoDe10 = valorDoProduto / 100 * 10
#    totalemcheque = valorDoProduto - comDescontoDe10
#    print(f'O valor avista com 10% desconto sai {totalemcheque}')
#
#elif ModoDePag == 'cartão' and QuantasParcelas == 0:
#    ComDescontoDe5 = valorDoProduto / 100 * 5 
#    totalNoCartão = valorDoProduto - ComDescontoDe5
#    print(f'O valor no cartão avista com 5% de desconto sai {totalNoCartão}')
#
#elif ModoDePag == 'cartão' and  QuantasParcelas >= 0 and QuantasParcelas <= 2:
#    print(f'O valor de sua compra saíra {valorDoProduto}, sem descontos')

#elif ModoDePag == 'cartão' and QuantasParcelas > 3:
#    comjurosde20 = valorDoProduto / 100 * 20
#    totalcjuros = valorDoProduto + comjurosde20
#    print(f'Seu valor terá 20% de juros, então saira {totalcjuros}')

# Forma que o guanabara resolveu esse cód

print('{:=^40}'.format(' Lojas da Mari '))
preço = float(input('Qual o preço das compras?: '))
print(""" formar de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {} sem juros'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra sairá em {} vezes e saira {}  com juros'.format(totalparc, parcela))
else:
    total = 0
    print ('opção invalida')
print('Sua compra de {:.2f} vai custar {} no final'.format(preço, total))
