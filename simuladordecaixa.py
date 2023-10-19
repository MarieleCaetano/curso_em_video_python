print('--'*30)
print('Bem-vindo ao banco M')
print('--'*30)

quantidade_notas_50 = 0
quantidade_notas_20 = 0
quantidade_notas_10 = 0
quantidade_notas_1 = 0

print('Notas disponiveis 1, 10, 20 e 50')
valor_a_ser_sacado = int(input('Qual valor você quer sacar? R$ '))
while True:
    if valor_a_ser_sacado == 0:
        break

    if valor_a_ser_sacado >= 50:
        quantidade_notas_50 += 1
        valor_a_ser_sacado = valor_a_ser_sacado - 50
    elif valor_a_ser_sacado >= 20:
        quantidade_notas_20 += 1
        valor_a_ser_sacado = valor_a_ser_sacado - 20
    elif valor_a_ser_sacado >= 10:
        quantidade_notas_10 += 1
        valor_a_ser_sacado = valor_a_ser_sacado - 10
    elif valor_a_ser_sacado >= 1:
        quantidade_notas_1 += 1
        valor_a_ser_sacado = valor_a_ser_sacado - 1

print(f'Notas sacadas: notas de 50: {quantidade_notas_50}, notas de 20: {quantidade_notas_20}, notas de 10: {quantidade_notas_10} e notas de 1: {quantidade_notas_1}')
