#ex 1 da aula 22
from mundo3_modulos.uteis.funcoesdef import fatorial, dobro #NAO É RECOMENDAVEL FAZER DESSE JEITO pois pode gerar conflito
#caso eu tenha alguma outra funcao dobro, então o certo é so usar o import funcoesdef e ali embaixo nas 
#func usar funcoesdef.fatorial

num=int(input("Digite um valor: "))
fat=fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f'O dobro de {num} E {dobro(num)}')


#PACOTE -É uma pasta que contém modulos que é por ex: defs separados por tratamento de numeros, strings etc
# para importar ele da pra usar no modo tradicional ex: import funcoesdef .e da pra importar a pasta e um 
# modulo especifico ex: from funcoesdef import datas
