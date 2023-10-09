# ex 34 - mundo 1 - aula 10
sal = float(input('Digite seu salário: '))
if sal <= 1250:
    novo = sal + (sal * 15 /100)
else:
    novo = sal + (sal * 10/100)

print('Seu salário aumentará {}'.format(novo))