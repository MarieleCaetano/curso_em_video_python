
valorcasa = float(input('Qual o valor da casa?  '))
salario = float(input('Qual o seu salário?  '))
parc = float(input('Em quantos anos você quer pagar? '))

trintaporcentdosalario = salario / 100 * 30
print(f'trinta porcento do seu salário seria {trintaporcentdosalario}')

anostransfEmMeses =  parc * 12 
valorDacasadistribuidoaolongodosmeses = valorcasa / anostransfEmMeses

print('as parcelas por mês vão ser de {:.2f}'.format(valorDacasadistribuidoaolongodosmeses))

if valorDacasadistribuidoaolongodosmeses > trintaporcentdosalario:
    print('Infelizmente, por ultrapassar os 30% seu emprestimo não foi aprovado')

elif valorDacasadistribuidoaolongodosmeses <= trintaporcentdosalario:
    print('Parabéns, seu emprestimo foi aprovado')