#aula 9 ex. 24
frase = str(input('Qual o nome da sua cidade xuxu: ')).strip()
cid = (frase[0:5].upper() == 'SANTO')

retorno = ''
if cid == 0:
    retorno = 'Sim'
elif cid == -1:
    retorno = 'Não'

print('a palavra Santo tem {} na sua cidade'.format(retorno))