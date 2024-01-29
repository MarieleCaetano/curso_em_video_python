def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        a = str(input(msg))
        if a.isnumeric():
            valor = int(a)
            ok = True
        else:
            print('\033[0;31mErro, sua resposta não é um numero inteiro\033[m')
        if ok:
            break
    return valor




#programa principal
a = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {a}')