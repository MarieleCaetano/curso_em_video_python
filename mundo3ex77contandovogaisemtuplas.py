palavras: ('Flor', 'Cadeado', 'paz', 'alegria', 'carro', 'moto', 'anel', 'nuvem', 'bolsa', 'viagem')
vogais = ('a', 'e', 'i', 'o', 'u')
e = ''
for p in palavras:
    print(f'Na palavra{p} temos: ', end = ' ')
    for letra in p:
        if letra.lower in 'aeiou':
            print(letra, end =' ')