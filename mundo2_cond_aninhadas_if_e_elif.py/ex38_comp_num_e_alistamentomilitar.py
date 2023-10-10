#ex 38 mundo 2
#numero1 = float(input('Digite um numero: '))
#numero2 = float(input('Digite outro numero: '))

#if numero1 == numero2:
#    print('Os dois numeros são iguais')
#elif numero1 > numero2:
#    print('O primeiro numero é maior que o segundo')
#elif numero1 < numero2:
#    print('O segundo numero é maior que o primeiro')


#ex 39 mundo 2
from datetime import date
current_date = date.today()
anoDeNascimento = int(input('Qual o seu ano de nascimento: '))
anoAtual = current_date.year
idade = anoAtual - anoDeNascimento
sexo = str.upper(input('Qual o seu sexo? Para feminino digite (F), ou para masculino digite (M):  '))


if sexo == "M" :
    idade > 18
    TempoQuePassouParaAlistamento = idade - 18
    print(f'Você tem {idade} e já se passaram {TempoQuePassouParaAlistamento} anos para ter se alistado')
    anoparaament = anoAtual - TempoQuePassouParaAlistamento
    print(f'O ano que você deveria ter se alistado foi em {anoparaament}')

elif sexo == "M":
    idade < 18
    tempoQueFaltaParaAlistamento = 18 - idade
    print(f'Sua idade é {idade} anos e faltam {tempoQueFaltaParaAlistamento} anos para você se alistar')
    anosquefaltapparaalistamento = anoAtual + tempoQueFaltaParaAlistamento
    print(f'Você vai se alistar no ano de {anosquefaltapparaalistamento}')
    

elif sexo == "M":
    idade == 18
    print(f'Você tem {idade} anos e pode se alistar no exercito neste ano de {anoAtual}')

elif sexo == "F":
    print('Você não pode se alistar, pois é mulher')

#Neste código calculamos a idade e se a pessoa pode ou não se alistar no exercito (18 anos)
#e quanto tempo falta ou passou do alistamento em questão
