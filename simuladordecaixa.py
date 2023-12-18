print('--'*30)
print('Bem-vindo ao banco M')
print('--'*30)

print('Notas disponiveis 1, 10, 20 e 50')
notade50 = 0
notade20 = 0
notade10 = 0
notadeum = 0

valor_a_ser_sacado = int(input('Qual valor você deseja sacar? R$ '))
while True:
    if valor_a_ser_sacado <= 0:
        break
    if valor_a_ser_sacado >= 50:
        notade50 += 1
        valor_a_ser_sacado -= 50
    elif valor_a_ser_sacado >= 20:
        notade20 += 1
        valor_a_ser_sacado -= 20
    elif valor_a_ser_sacado >= 10:
        notade10 += 1
        valor_a_ser_sacado -= 10
    elif valor_a_ser_sacado >= 1:
        notadeum += 1
        valor_a_ser_sacado = valor_a_ser_sacado - 1

print(f'''Notas a sacadas: nota de R$50 = {notade50}
                         nota de R$20  =  {notade20} 
                         notas de R$10 = {notade10} 
                         e notas de R$1 = {notadeum}''')