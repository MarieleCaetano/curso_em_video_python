primeiros10col = ('Corintians', 'Santos', 'Botafogo', 'Flamengo', 'Palmeiras', 'Mineirão', 'Chapecoense', 'Fluminense', 'Vasco', 'São Paulo')
ultimosdez = ('Ponte Preta', 'Gremio', 'Cruzeiro', 'Bahia', 'internacional', 'galvez', 'atletico', 'america', 'interporto', 'Sportverde')
total = primeiros10col + ultimosdez
print(f'Temos um total de {len(total)} times nas ultimas colocações')
print(f'Os cinco primeiros colocados da série b são em {primeiros10col[0:6]} na posição ')
print(f'Os ultimos 4 colocados da série b são {ultimosdez[-4: ]}')
print('-'*10,'A lista em ordem alfabetica:', '-'*10)
print(f'{sorted(total)} na posição')
print('-'*50)
print(f' E  chapecoense está na posição {total.index("Chapecoense")}')


#ex do guanabara
lista = ('Corintians', 'Santos', 'Botafogo', 'Flamengo', 'Palmeiras', 'Mineirão', 'Chapecoense', 'Fluminense',
         'Vasco', 'São paulo', 'Ponte Preta', 'Gremio', 'Cruzueiro', 'Bahia','Internacional', 'Galvez', 'Atletico', 'America',
         'Interporto', 'Sportverde')
   
print('-='*30)
print(f'Lista de times do Brasileirão: {lista}')
print('-='*30)
print(f'Osprimeiros 5 primeiros são {lista[0:5]}')
print('=-'*30)
print(f'Os quatro ultimos são: {lista[-4:]}')
print('='*30)
print(f'Alista de times em ordem alfabetica: {sorted(lista)}')
print('-='*30)
print(f'E o chapecoense está na posição {lista.index("Chapecoense")+1}')