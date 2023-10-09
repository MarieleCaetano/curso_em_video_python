from datetime import date
dataDeHoje = date.today()
AnoNascimento = int(input('Qual seu ano de nascimento: '))
Anoatual = dataDeHoje.year 
idade = Anoatual - AnoNascimento
if idade <= 9:
    print(f'A idade é {idade}, ela é menor ou igual a nove anos, então a categoria é mirim')
elif idade > 9 and idade <= 14:
    print(f'A idade é {idade}, então sua categoria é infantil')
elif idade > 14 and idade <= 19:
    print(f'a idade é {idade}, então se encaixa na categoria junior')
elif idade > 19 and idade <= 20:
    print(f'Sua idade é{idade}, então se encaixa na categoria sênior')
elif idade > 20:
    print(f'Sua idade é {idade}, então é categoria master')