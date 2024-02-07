from moeda_2 import modulo_moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {modulo_moeda.moeda(p)} é {modulo_moeda.metade(p,formato=True)}  ')
print(f'O dobro de {modulo_moeda.moeda(p)} é {modulo_moeda.dobro(p,formato=True)} ')
print(f'Aumentando 10%, temos {modulo_moeda.aumentando(preço=p, taxa=10,formato=True)}')
print(f'Reduzindo 13%, temos {modulo_moeda.reduzindo(preço=p, taxa=13,formato=True)}')