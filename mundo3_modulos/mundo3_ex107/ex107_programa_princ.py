import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}  ')
print(f'O dobro de {p} {moeda.dobro(p)} ')
print(f'Aumentando 10%, temos {moeda.aumentando(preço=p, taxa=10)}')
print(f'Reduzindo 13%, temos {moeda.reduzindo(preço=p, taxa=13)}')