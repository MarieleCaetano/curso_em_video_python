from moeda import modulo_moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {modulo_moeda.moeda(p)} é {modulo_moeda.moeda(modulo_moeda.metade(p))}  ')
print(f'O dobro de {modulo_moeda.moeda(p)} {modulo_moeda.moeda(modulo_moeda.dobro(p))} ')
print(f'Aumentando 10%, temos {modulo_moeda.moeda(modulo_moeda.aumentando(preço=p, taxa=10))}')
print(f'Reduzindo 13%, temos {modulo_moeda.moeda(modulo_moeda.reduzindo(preço=p, taxa=13))}')