# ex 29 - aula 10 - mundo 1


km = float(input('O limite da via é 80km/h. Quantos km o carro está? '))
if km > 80:
    multa = (km - 80) * 7
    print(f'Você utrapassou o limite de velocidade, sua multa é de {multa}')
else:
    print('Você está dentro do limite, tenha uma boa viagem')
