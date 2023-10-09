#criar um programa que leia 7 vezes anos de nascimento
from datetime import date
datadehoje = date.today()
Anoatual = datadehoje.year 

lista_de_pessoas_que_sao_menor = []
for c in range(1, 8):
    ano_de_nasc = int(input(f'Digite o ano de nascimento{c}:'))
    idade = Anoatual - ano_de_nasc
    if idade < 18:
      lista_de_pessoas_que_sao_menor.append(ano_de_nasc)

print(f'As pessoas que nasceram {lista_de_pessoas_que_sao_menor} são menores de idade')

